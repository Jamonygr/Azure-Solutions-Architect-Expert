#!/usr/bin/env python3
"""Validate container pins without downloading packages or contacting services."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
LOCK_PATH = ROOT / "tools" / "container-lock.json"
QUALITY_LOCK_PATH = ROOT / "tools" / "quality-tools-lock.json"
POWERSHELL_LOCK_PATH = ROOT / "tools" / "powershell-packages.lock.json"
AZURE_CLI_EXTENSION_LOCK_PATH = ROOT / "tools" / "azure-cli-extensions.lock.json"
REGISTRY_PATH = ROOT / "curriculum" / "tool-versions.yml"
DOCKERFILE_PATH = ROOT / ".devcontainer" / "Dockerfile"
DEVCONTAINER_PATH = ROOT / ".devcontainer" / "devcontainer.json"
PYTHON_LOCK_PATH = ROOT / "requirements-container.lock.txt"
PACKAGE_PATH = ROOT / "package.json"
PACKAGE_LOCK_PATH = ROOT / "package-lock.json"
WORKFLOW_PATHS = (
    ROOT / ".github" / "workflows" / "quality.yml",
    ROOT / ".github" / "workflows" / "pages.yml",
)


def fail(message: str) -> None:
    raise ValueError(message)


def main() -> int:
    lock = json.loads(LOCK_PATH.read_text(encoding="utf-8"))
    quality_lock = json.loads(QUALITY_LOCK_PATH.read_text(encoding="utf-8"))
    powershell_lock = json.loads(POWERSHELL_LOCK_PATH.read_text(encoding="utf-8"))
    azure_cli_extension_lock = json.loads(
        AZURE_CLI_EXTENSION_LOCK_PATH.read_text(encoding="utf-8")
    )
    registry = yaml.safe_load(REGISTRY_PATH.read_text(encoding="utf-8"))
    dockerfile = DOCKERFILE_PATH.read_text(encoding="utf-8")
    devcontainer = json.loads(DEVCONTAINER_PATH.read_text(encoding="utf-8"))
    python_lock = PYTHON_LOCK_PATH.read_text(encoding="utf-8")
    package = json.loads(PACKAGE_PATH.read_text(encoding="utf-8"))
    package_lock = json.loads(PACKAGE_LOCK_PATH.read_text(encoding="utf-8"))
    workflows = {
        path.name: path.read_text(encoding="utf-8") for path in WORKFLOW_PATHS
    }

    if lock.get("schemaVersion") != "1.0.0":
        fail("container-lock.json must use schemaVersion 1.0.0")
    if lock.get("platform") != "linux-amd64":
        fail("the checked direct-artifact hashes are limited to linux-amd64")

    frontend = lock.get("dockerfileFrontend", {})
    expected_frontend = f'# syntax={frontend.get("reference")}@{frontend.get("digest")}'
    if not re.fullmatch(r"sha256:[0-9a-f]{64}", frontend.get("digest", "")):
        fail("Dockerfile frontend must have a lowercase SHA-256 digest")
    if not dockerfile.startswith(expected_frontend + "\n"):
        fail("Dockerfile frontend differs from the digest-pinned container lock")

    base = registry["containerBase"]
    if lock["baseImage"] != {
        "reference": base["image"],
        "digest": base["digest"],
    }:
        fail("base image lock differs from curriculum/tool-versions.yml")
    expected_from = f'{base["image"]}@{base["digest"]}'
    if f"FROM {expected_from}" not in dockerfile:
        fail("Dockerfile does not use the registry's digest-pinned base image")

    apt_lock = lock["apt"]
    if apt_lock.get("snapshot") != "https://snapshot.ubuntu.com/ubuntu/20260902T000000Z":
        fail("Ubuntu packages must come from the frozen 2026-09-02 snapshot")
    if apt_lock.get("checkValidUntil") is not False:
        fail("snapshot metadata validity must be explicitly disabled for future rebuilds")
    for package_name, version in apt_lock["packages"].items():
        if f"{package_name}={version}" not in dockerfile:
            fail(f"Dockerfile does not pin apt prerequisite {package_name}={version}")
    if "snapshot.ubuntu.com/ubuntu/${UBUNTU_SNAPSHOT}" not in dockerfile:
        fail("Dockerfile does not rewrite Ubuntu sources to the immutable snapshot")

    tool_map = {
        "powershell": "powershell",
        "azureCli": "azureCli",
        "bicep": "bicep",
        "azcopy": "azcopy",
        "python": "python",
        "node": "node",
    }
    for lock_name, registry_name in tool_map.items():
        expected = str(registry["tools"][registry_name])
        if str(lock["artifacts"][lock_name]["version"]) != expected:
            fail(f"{lock_name} lock differs from curriculum/tool-versions.yml")
        if expected not in dockerfile:
            fail(f"Dockerfile does not contain the {lock_name} version {expected}")

    if azure_cli_extension_lock.get("schemaVersion") != "1.0.0":
        fail("azure-cli-extensions.lock.json must use schemaVersion 1.0.0")
    if azure_cli_extension_lock.get("platform") != lock["platform"]:
        fail("Azure CLI extension lock platform differs from the container lock")
    if azure_cli_extension_lock.get("azureCliVersion") != lock["artifacts"]["azureCli"]["version"]:
        fail("Azure CLI extension lock targets a different Azure CLI version")
    if azure_cli_extension_lock.get("sourceIndex") != "https://aka.ms/azure-cli-extension-index-v1":
        fail("Azure CLI extensions must be selected from the official extension index")

    expected_extensions = {
        "monitor-control-service": {
            "version": "1.2.0",
            "commandGroups": {
                "az monitor data-collection rule",
                "az monitor data-collection rule association",
            },
        },
        "virtual-wan": {
            "version": "1.0.1",
            "commandGroups": {
                "az network vhub",
                "az network vhub route-table route",
            },
        },
    }
    extension_entries = azure_cli_extension_lock.get("extensions", [])
    if {entry.get("name") for entry in extension_entries} != set(expected_extensions):
        fail("Azure CLI extension lock must contain exactly the two approved GA extensions")
    all_command_groups: list[str] = []
    for entry in extension_entries:
        name = entry["name"]
        expected = expected_extensions[name]
        if entry.get("version") != expected["version"]:
            fail(f"Azure CLI extension {name} must be pinned to {expected['version']}")
        if entry.get("preview") is not False:
            fail(f"Azure CLI extension {name} must be a GA release")
        if set(entry.get("commandGroups", [])) != expected["commandGroups"]:
            fail(f"Azure CLI extension {name} command-group coverage is incomplete")
        if not entry.get("uri", "").startswith(
            "https://azcliprod.blob.core.windows.net/cli-extensions/"
        ):
            fail(f"Azure CLI extension {name} does not use Microsoft's production feed")
        if entry.get("filename") != entry["uri"].rsplit("/", maxsplit=1)[-1]:
            fail(f"Azure CLI extension {name} filename differs from its locked URI")
        if not re.fullmatch(r"[0-9a-f]{64}", entry.get("sha256", "")):
            fail(f"Azure CLI extension {name} has an invalid SHA-256 digest")
        if not isinstance(entry.get("size"), int) or entry["size"] <= 0:
            fail(f"Azure CLI extension {name} has an invalid byte count")
        all_command_groups.extend(entry["commandGroups"])
    if len(all_command_groups) != len(set(all_command_groups)):
        fail("Azure CLI extension command-group coverage contains duplicates")
    if set(azure_cli_extension_lock.get("coreCommandGroups", [])) != {
        "az cosmosdb private-endpoint-connection",
        "az rest",
    }:
        fail("Azure CLI core command-group coverage is incomplete")
    excluded_preview = {
        entry.get("name") for entry in azure_cli_extension_lock.get("excludedPreviewExtensions", [])
    }
    if excluded_preview != {"cdn"}:
        fail("the preview-only cdn extension exclusion must be explicit")
    if "azure-cli-extensions.lock.json" not in dockerfile:
        fail("Dockerfile does not consume the Azure CLI extension lock")
    for required_fragment in (
        "AZURE_EXTENSION_DIR=/opt/az305/azure-cli-extensions",
        "AZURE_EXTENSION_USE_DYNAMIC_INSTALL=no",
        'echo "${expected_hash}  ${package}" | sha256sum --check --strict',
        'PIP_NO_INDEX=1 az extension add --source "${package}"',
    ):
        if required_fragment not in dockerfile:
            fail(f"Dockerfile Azure CLI extension install is missing: {required_fragment}")

    module_versions = {
        "Az": str(registry["tools"]["azModule"]),
        "Pester": str(registry["tools"]["pester"]),
        "PSScriptAnalyzer": str(registry["tools"]["psScriptAnalyzer"]),
    }
    graph_version = str(registry["tools"]["microsoftGraph"])
    for module_name in registry["graphModules"]:
        module_versions[module_name] = graph_version

    if set(lock["powershellModules"]) != set(module_versions):
        fail("PowerShell module lock must contain exactly Az, quality modules, and the approved Graph submodules")
    for name, expected in module_versions.items():
        entry = lock["powershellModules"][name]
        if str(entry["version"]) != expected:
            fail(f"{name} lock differs from curriculum/tool-versions.yml")
        if not re.fullmatch(r"[0-9a-f]{64}", entry["packageSha256"]):
            fail(f"{name} packageSha256 is not a lowercase SHA-256 digest")

    packages = powershell_lock["packages"]
    if powershell_lock.get("packageCount") != len(packages):
        fail("PowerShell packageCount differs from the package array length")
    package_keys = [(entry["name"], str(entry["version"])) for entry in packages]
    if len(package_keys) != len(set(package_keys)):
        fail("PowerShell package lock contains a duplicate name/version")
    closure_roots = {
        entry["name"]: str(entry["version"])
        for entry in powershell_lock["dependencyClosureOf"]
    }
    if closure_roots != module_versions:
        fail("PowerShell dependency-closure roots differ from the approved module set")
    locked_by_name = {entry["name"]: entry for entry in packages}
    for name, expected in module_versions.items():
        entry = locked_by_name.get(name)
        if not entry or str(entry["version"]) != expected or entry.get("topLevel") is not True:
            fail(f"PowerShell closure does not lock approved root {name} {expected}")
        if entry["sha256"] != lock["powershellModules"][name]["packageSha256"]:
            fail(f"PowerShell root digest differs between locks for {name}")
    for entry in packages:
        name = entry["name"]
        if name.startswith("Microsoft.Graph.") and name not in module_versions:
            fail(f"unapproved Graph package is locked: {name}")
        if not entry["uri"].startswith("https://www.powershellgallery.com/api/v2/package/"):
            fail(f"PowerShell package {name} does not use the official package endpoint")
        if not re.fullmatch(r"[0-9a-f]{64}", entry["sha256"]):
            fail(f"PowerShell package {name} has an invalid SHA-256 digest")
        if not isinstance(entry.get("size"), int) or entry["size"] <= 0:
            fail(f"PowerShell package {name} has an invalid byte count")
    if "powershell-packages.lock.json" not in dockerfile:
        fail("Dockerfile does not consume the complete PowerShell package lock")
    if any(command in dockerfile for command in ("Install-Module", "Save-Module", "Install-PSResource")):
        fail("Dockerfile must not re-download modules through a PowerShell package manager")
    if "sha256sum --check --strict" not in dockerfile or 'unzip -q "${package}"' not in dockerfile:
        fail("Dockerfile must verify and extract the same downloaded PowerShell package file")

    for name, entry in lock["artifacts"].items():
        if not entry["uri"].startswith("https://"):
            fail(f"{name} artifact URI must use HTTPS")
        if not re.fullmatch(r"[0-9a-f]{64}", entry["sha256"]):
            fail(f"{name} sha256 is not a lowercase SHA-256 digest")
        if entry["sha256"] not in dockerfile:
            fail(f"Dockerfile does not enforce the locked {name} digest")

    npm_quality_map = {
        "markdownlintCli2": "markdownlint-cli2",
        "cspell": "cspell",
    }
    for lock_name, package_name in npm_quality_map.items():
        expected = str(quality_lock["qualityTools"][lock_name]["version"])
        if package["devDependencies"].get(package_name) != expected:
            fail(f"package.json does not pin {package_name} to {expected}")
        npm_entry = package_lock["packages"].get(f"node_modules/{package_name}", {})
        if str(npm_entry.get("version")) != expected or not str(npm_entry.get("integrity", "")).startswith("sha512-"):
            fail(f"package-lock.json does not integrity-lock {package_name} {expected}")

    for tool_name in ("actionlint", "gitleaks"):
        entry = quality_lock["qualityTools"][tool_name]
        if not entry["uri"].startswith("https://"):
            fail(f"{tool_name} URI must use HTTPS")
        if not re.fullmatch(r"[0-9a-f]{64}", entry["sha256"]):
            fail(f"{tool_name} sha256 is not a lowercase SHA-256 digest")
        for value in (entry["version"], entry["sha256"]):
            if value not in dockerfile:
                fail(f"Dockerfile does not enforce the locked {tool_name} value {value}")

    if devcontainer.get("build", {}).get("dockerfile") != "Dockerfile":
        fail("devcontainer.json must build .devcontainer/Dockerfile")
    if "features" in devcontainer:
        fail("floating dev-container features are forbidden")
    if "--require-hashes" not in dockerfile or "requirements-container.lock.txt" not in dockerfile:
        fail("Dockerfile must install Python dependencies from the hashed container lock")
    for requirement in (ROOT / "requirements-dev.txt", ROOT / "requirements-docs.txt"):
        for line in requirement.read_text(encoding="utf-8").splitlines():
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue
            normalized_name = re.split(r"[<>=!~\[]", stripped, maxsplit=1)[0].lower()
            if not re.search(rf"(?mi)^{re.escape(normalized_name)}==", python_lock):
                fail(f"{requirement.name} entry {normalized_name} is absent from the Python lock")
    if "--hash=sha256:" not in python_lock:
        fail("Python dependency lock does not contain SHA-256 hashes")

    for workflow_name, workflow in workflows.items():
        docker_run_lines = re.findall(r"(?m)^\s*docker run\b.*$", workflow)
        if not docker_run_lines:
            fail(f"{workflow_name} must run validation in the frozen container")
        for line in docker_run_lines:
            if "--network none" not in line:
                fail(f"{workflow_name} has a container run without --network none")

    print(
        "Container lock validated: base/snapshot, runtimes, two GA Azure CLI extensions, "
        "113 PowerShell packages, Python/npm dependencies, and quality binaries are pinned."
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (KeyError, TypeError, ValueError, json.JSONDecodeError, yaml.YAMLError) as error:
        print(f"Container lock validation failed: {error}", file=sys.stderr)
        raise SystemExit(1) from error
