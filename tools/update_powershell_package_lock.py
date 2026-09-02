#!/usr/bin/env python3
"""Resolve and checksum the PowerShell module closure from a verified image.

This maintenance command uses the network and is not part of the offline release
gate. The resulting lock is consumed directly by the container build.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import subprocess
import time
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "tools" / "powershell-packages.lock.json"
ROOT_LOCK = ROOT / "tools" / "container-lock.json"


def inventory_modules(image: str) -> list[dict[str, str]]:
    command = (
        '$root="/usr/local/share/powershell/Modules"; '
        "Get-ChildItem -LiteralPath $root -Directory | ForEach-Object { "
        "$name=$_.Name; Get-ChildItem -LiteralPath $_.FullName -Directory | "
        "ForEach-Object { [pscustomobject]@{name=$name;version=$_.Name} } } | "
        "Sort-Object name,version | ConvertTo-Json -Depth 3 -Compress"
    )
    completed = subprocess.run(
        [
            "docker",
            "run",
            "--rm",
            "--network",
            "none",
            image,
            "pwsh",
            "-NoLogo",
            "-NoProfile",
            "-Command",
            command,
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    inventory = json.loads(completed.stdout)
    if not isinstance(inventory, list):
        raise ValueError("PowerShell module inventory must be a JSON array")
    return inventory


def package_record(module: dict[str, str], top_level: set[str]) -> dict[str, Any]:
    name = module["name"]
    version = module["version"]
    escaped_name = urllib.parse.quote(name, safe=".")
    escaped_version = urllib.parse.quote(version, safe=".")
    uri = f"https://www.powershellgallery.com/api/v2/package/{escaped_name}/{escaped_version}"
    request = urllib.request.Request(uri, headers={"User-Agent": "AZ305-package-lock/1.0"})

    last_error: Exception | None = None
    for attempt in range(1, 4):
        try:
            digest = hashlib.sha256()
            size = 0
            with urllib.request.urlopen(request, timeout=180) as response:
                while chunk := response.read(1024 * 1024):
                    digest.update(chunk)
                    size += len(chunk)
            return {
                "name": name,
                "version": version,
                "topLevel": name in top_level,
                "uri": uri,
                "sha256": digest.hexdigest(),
                "size": size,
            }
        except Exception as error:  # noqa: BLE001 - retry reports the final transport error
            last_error = error
            time.sleep(attempt * 2)
    raise RuntimeError(f"Unable to lock {name} {version}: {last_error}") from last_error


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", default="az305-learning:local")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    roots = json.loads(ROOT_LOCK.read_text(encoding="utf-8"))["powershellModules"]
    inventory = inventory_modules(args.image)
    actual = {item["name"]: item["version"] for item in inventory}
    for name, entry in roots.items():
        if actual.get(name) != entry["version"]:
            raise ValueError(
                f"inventory has {name} {actual.get(name)!r}; expected {entry['version']}"
            )

    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
        records = list(
            executor.map(
                lambda item: package_record(item, set(roots)),
                inventory,
            )
        )
    records.sort(key=lambda entry: (entry["name"].casefold(), entry["version"]))

    output = {
        "$schema": "urn:az305:schema:powershell-package-lock:1.0.0",
        "schemaVersion": "1.0.0",
        "verifiedOn": "2026-09-02",
        "source": "https://www.powershellgallery.com/api/v2/package/",
        "dependencyClosureOf": [
            {"name": name, "version": entry["version"]}
            for name, entry in roots.items()
        ],
        "packageCount": len(records),
        "packages": records,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    temporary = args.output.with_suffix(args.output.suffix + ".tmp")
    temporary.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    temporary.replace(args.output)
    print(f"Locked {len(records)} PowerShell packages in {args.output}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

