#!/usr/bin/env python3
"""Render registered AZ-305 visuals to deterministic, self-contained SVG assets."""

from __future__ import annotations

import argparse
import base64
import hashlib
import html
import json
import math
import re
import struct
import textwrap
from pathlib import Path
from typing import Any

import yaml

from az305lib import ROOT, load_model, plan_generated, sha256_text, write_or_check


REGISTRY_PATH = ROOT / "curriculum" / "visuals.yml"
ICONS_PATH = ROOT / "docs" / "site-assets" / "icons" / "icons.yml"
INFOGRAPHIC_FILENAMES = {
    "VIS-LEARNING-LOOP": "learning-loop.svg",
    "VIS-DOMAIN-COVERAGE": "exam-domains.svg",
    "VIS-JOB-READY": "job-ready.svg",
    "VIS-OBJECTIVE-TRACE": "objective-coverage.svg",
    "VIS-STUDY-ROADMAP": "study-roadmap.svg",
    "VIS-ASSESSMENT-FLOW": "assessment-coverage.svg",
    "VIS-ADR-LOOP": "decision-workflow.svg",
    "VIS-WAF-PILLARS": "waf-pillars.svg",
    "VIS-EVIDENCE-CHAIN": "evidence-chain.svg",
    "VIS-COMMAND-LANES": "command-lanes.svg",
    "VIS-CONTINUITY": "continuity-targets.svg",
    "VIS-COST": "cost-levers.svg",
    "VIS-LICENSING": "licensing-boundary.svg",
    "VIS-MIGRATION": "migration-waves.svg",
    "VIS-PERMISSIONS": "permission-boundary.svg",
    "VIS-TROUBLESHOOTING": "troubleshooting-flow.svg",
}


def load_yaml(path: Path) -> dict[str, Any]:
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"Expected a mapping in {path.relative_to(ROOT)}")
    return value


def esc(value: Any) -> str:
    return html.escape(str(value), quote=True)


def lines(value: str, width: int, limit: int = 3) -> list[str]:
    return textwrap.wrap(str(value), width=width, break_long_words=False)[:limit] or [""]


def text_block(x: float, y: float, value: str, *, width: int, size: int,
               fill: str, anchor: str = "start", weight: int = 400,
               limit: int = 3, line_height: int | None = None) -> list[str]:
    wrapped = lines(value, width, limit)
    step = line_height or size + 5
    result = [
        f'  <text x="{x:g}" y="{y:g}" text-anchor="{anchor}" '
        f'font-family="Segoe UI,Arial,sans-serif" font-size="{size}" '
        f'font-weight="{weight}" fill="{esc(fill)}">'
    ]
    for index, line in enumerate(wrapped):
        dy = "0" if index == 0 else str(step)
        result.append(f'    <tspan x="{x:g}" dy="{dy}">{esc(line)}</tspan>')
    result.append("  </text>")
    return result


def svg_open(width: int, height: int, title: str, description: str,
             metadata: str, palette: dict[str, Any]) -> list[str]:
    primary = palette["primary"]
    accent = palette["accent"]
    highlight = palette["highlight"]
    background = palette["background"]
    return [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" aria-labelledby="visual-title visual-desc">',
        f'  <title id="visual-title">{esc(title)}</title>',
        f'  <desc id="visual-desc">{esc(description)}</desc>',
        f'  <metadata>{esc(metadata)}</metadata>',
        "  <defs>",
        f'    <linearGradient id="wash" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{background}"/><stop offset="1" stop-color="#ffffff"/></linearGradient>',
        f'    <linearGradient id="accent" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{accent}"/><stop offset="1" stop-color="{highlight}"/></linearGradient>',
        f'    <filter id="shadow" x="-20%" y="-20%" width="140%" height="150%"><feDropShadow dx="0" dy="8" stdDeviation="9" flood-color="{primary}" flood-opacity=".14"/></filter>',
        f'    <marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="5" orient="auto"><path d="M0 0L10 5L0 10Z" fill="{accent}"/></marker>',
        "  </defs>",
        '  <rect width="100%" height="100%" fill="url(#wash)"/>',
    ]


def svg_finish(parts: list[str]) -> str:
    parts.append("</svg>")
    return "\n".join(parts) + "\n"


def icon_index() -> dict[str, dict[str, Any]]:
    if not ICONS_PATH.is_file():
        return {}
    data = load_yaml(ICONS_PATH)
    sources = data.get("sources", {})
    result: dict[str, dict[str, Any]] = {}
    for authored in data.get("icons", []):
        item = dict(authored)
        source = sources[item["source"]]
        item["sourceUrl"] = source["termsUrl"]
        result[item["key"]] = item
        for alias in item.get("aliases", []):
            result[alias] = item
    return result


def icon_data(key: str, icons: dict[str, dict[str, Any]]) -> str | None:
    item = icons.get(key)
    if not item:
        return None
    path = ROOT / item["path"]
    if not path.is_file():
        return None
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return "data:image/svg+xml;base64," + encoded


def render_banner(lab: dict[str, Any], visual: dict[str, Any], palette: dict[str, Any]) -> str:
    width, height = 1200, 320
    banner = visual["banner"]
    digest = sha256_text(json.dumps(banner, sort_keys=True, ensure_ascii=False))
    parts = svg_open(width, height, f"{lab['id']} summary banner", banner["alt"],
                     f"registry-sha256:{digest}", palette)
    parts.extend([
        f'  <circle cx="1040" cy="86" r="170" fill="{palette["accent"]}" opacity=".10"/>',
        f'  <circle cx="1110" cy="245" r="126" fill="{palette["highlight"]}" opacity=".12"/>',
        f'  <path d="M785 228 C880 112 1000 96 1155 151" fill="none" stroke="{palette["line"]}" stroke-width="4" stroke-linecap="round" opacity=".85"/>',
        f'  <circle cx="802" cy="216" r="15" fill="{palette["accent"]}"/>',
        f'  <circle cx="965" cy="122" r="15" fill="{palette["highlight"]}"/>',
        f'  <circle cx="1146" cy="150" r="15" fill="{palette["primary"]}"/>',
        f'  <rect x="64" y="48" width="170" height="36" rx="18" fill="{palette["primary"]}"/>',
        f'  <text x="149" y="72" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif" font-size="15" font-weight="700" fill="#ffffff">{esc(lab["id"])} · {esc(lab["domainId"])}</text>',
    ])
    parts.extend(text_block(64, 118, banner["title"], width=48, size=32,
                            fill=palette["text"], weight=700, limit=2, line_height=38))
    parts.extend(text_block(64, 206, banner["caption"], width=72, size=17,
                            fill=palette["muted"], limit=3, line_height=23))
    badges = [(lab["implementationMode"], palette["highlight"]),
              (lab["laneLabel"], palette["accent"]),
              (lab["status"], palette["primary"])]
    x = 64
    for label, color in badges:
        badge_width = max(116, min(230, 22 + len(label) * 8))
        parts.append(f'  <rect x="{x}" y="266" width="{badge_width}" height="32" rx="16" fill="{color}" opacity=".13" stroke="{color}"/>')
        parts.append(f'  <text x="{x + badge_width / 2:g}" y="287" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif" font-size="13" font-weight="700" fill="{palette["text"]}">{esc(label)}</text>')
        x += badge_width + 12
    return svg_finish(parts)


def node_positions(count: int) -> list[tuple[float, float]]:
    if count <= 1:
        return [(600, 330)]
    columns = min(4, max(3, math.ceil(count / 2)))
    x_values = [155 + index * (890 / max(1, columns - 1)) for index in range(columns)]
    positions: list[tuple[float, float]] = []
    for index in range(count):
        row = index // columns
        col = index % columns
        y = 220 + row * 330
        if row and count % columns:
            offset = (columns - (count % columns)) * 445 / max(1, columns - 1)
        else:
            offset = 0
        positions.append((x_values[col] + offset, y))
    return positions


def render_topology(lab: dict[str, Any], visual: dict[str, Any], palette: dict[str, Any],
                    source: str, icons: dict[str, dict[str, Any]]) -> str:
    topology = visual["topology"]
    nodes = topology["nodes"]
    width, height = 1200, 760
    parts = svg_open(width, height, topology["title"], topology["alt"],
                     f"source-sha256:{sha256_text(source)}", palette)
    positions = {node["id"]: position for node, position in zip(nodes, node_positions(len(nodes)))}
    boundary_nodes: dict[str, list[tuple[float, float]]] = {}
    for node in nodes:
        boundary_nodes.setdefault(node["boundaryId"], []).append(positions[node["id"]])
    boundary_labels = {item["id"]: item["label"] for item in topology["boundaries"]}
    for boundary_id, points in boundary_nodes.items():
        min_x = max(24, min(point[0] for point in points) - 104)
        max_x = min(width - 24, max(point[0] for point in points) + 104)
        min_y = max(105, min(point[1] for point in points) - 104)
        max_y = min(height - 52, max(point[1] for point in points) + 128)
        parts.append(f'  <g role="group" aria-label="Boundary: {esc(boundary_labels[boundary_id])}">')
        parts.append(f'    <rect x="{min_x:g}" y="{min_y:g}" width="{max_x-min_x:g}" height="{max_y-min_y:g}" rx="24" fill="{palette["surface"]}" fill-opacity=".62" stroke="{palette["line"]}" stroke-width="2" stroke-dasharray="8 7"/>')
        parts.append(f'    <text x="{min_x + 16:g}" y="{min_y + 25:g}" font-family="Segoe UI,Arial,sans-serif" font-size="14" font-weight="700" fill="{palette["muted"]}">{esc(boundary_labels[boundary_id])}</text>')
        parts.append("  </g>")
    for edge in topology["edges"]:
        start = positions[edge["from"]]
        end = positions[edge["to"]]
        dx, dy = end[0] - start[0], end[1] - start[1]
        length = math.hypot(dx, dy) or 1
        x1, y1 = start[0] + dx / length * 77, start[1] + dy / length * 77
        x2, y2 = end[0] - dx / length * 77, end[1] - dy / length * 77
        label_x, label_y = (x1 + x2) / 2, (y1 + y2) / 2 - 9
        aria = f"{edge['label']}: {edge['from']} to {edge['to']}"
        parts.append(f'  <g role="group" aria-label="{esc(aria)}">')
        parts.append(f'    <path d="M{x1:g} {y1:g} C{label_x:g} {y1:g} {label_x:g} {y2:g} {x2:g} {y2:g}" fill="none" stroke="{palette["accent"]}" stroke-width="3" marker-end="url(#arrow)"/>')
        label_w = min(210, max(92, len(edge["label"]) * 6.5))
        parts.append(f'    <rect x="{label_x-label_w/2:g}" y="{label_y-16:g}" width="{label_w:g}" height="24" rx="12" fill="#ffffff" stroke="{palette["line"]}"/>')
        parts.append(f'    <text x="{label_x:g}" y="{label_y:g}" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif" font-size="11" fill="{palette["text"]}">{esc(edge["label"])}</text>')
        parts.append("  </g>")
    for node in nodes:
        x, y = positions[node["id"]]
        data = icon_data(node["iconKey"], icons)
        parts.append(f'  <g role="group" aria-label="Service node: {esc(node["label"])}" filter="url(#shadow)">')
        parts.append(f'    <rect x="{x-78:g}" y="{y-72:g}" width="156" height="146" rx="22" fill="{palette["surface"]}" stroke="{palette["primary"]}" stroke-width="2"/>')
        if data:
            parts.append(f'    <image x="{x-28:g}" y="{y-52:g}" width="56" height="56" preserveAspectRatio="xMidYMid meet" href="{data}"/>')
        else:
            parts.append(f'    <circle cx="{x:g}" cy="{y-24:g}" r="27" fill="url(#accent)"/>')
            parts.append(f'    <path d="M{x-13:g} {y-24:g}h26M{x:g} {y-37:g}v26" stroke="#fff" stroke-width="4" stroke-linecap="round"/>')
        wrapped = lines(node["label"], 21, 3)
        parts.append(f'    <text x="{x:g}" y="{y+27:g}" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif" font-size="13" font-weight="600" fill="{palette["text"]}">')
        for index, line in enumerate(wrapped):
            dy = "0" if index == 0 else "17"
            parts.append(f'      <tspan x="{x:g}" dy="{dy}">{esc(line)}</tspan>')
        parts.append("    </text>")
        parts.append("  </g>")
    parts.append(f'  <text x="600" y="730" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif" font-size="14" fill="{palette["muted"]}">{esc(topology["caption"])}</text>')
    return svg_finish(parts)


def render_decision(lab: dict[str, Any], visual: dict[str, Any], palette: dict[str, Any],
                    decision: dict[str, Any]) -> str:
    spec = visual["decisionMatrix"]
    candidates = decision["candidates"]
    width, row_h = 1200, 122
    height = 176 + row_h * len(candidates) + 72
    digest = sha256_text(json.dumps(decision, sort_keys=True, ensure_ascii=False))
    parts = svg_open(width, height, spec["title"], spec["alt"],
                     f"decision-sha256:{digest}", palette)
    parts.extend(text_block(56, 62, spec["title"], width=62, size=28,
                            fill=palette["text"], weight=700, limit=2, line_height=34))
    parts.extend(text_block(56, 113, spec["caption"], width=105, size=15,
                            fill=palette["muted"], limit=2, line_height=20))
    criterion_names = {item["id"]: item["name"] for item in decision["criteria"]}
    criterion_ids = [item["id"] for item in decision["criteria"]]
    start_y = 154
    for index, candidate in enumerate(candidates):
        y = start_y + index * row_h
        selected = candidate["name"] == decision["selectedCandidate"]
        eligible = candidate["eligible"] and not candidate["disqualifiers"]
        status = "selected" if selected else "eligible" if eligible else "disqualified"
        stroke = palette["highlight"] if selected else palette["line"]
        fill = palette["surface"] if eligible else "#F7F8FA"
        parts.append(f'  <g role="group" aria-label="Candidate {esc(candidate["name"])}; {status}; weighted total {candidate["weightedTotal"]:g} out of 100">')
        parts.append(f'    <rect x="48" y="{y}" width="1104" height="106" rx="18" fill="{fill}" stroke="{stroke}" stroke-width="{4 if selected else 2}"/>')
        title_parts = text_block(68, y + 31, candidate["name"], width=43, size=15,
                                 fill=palette["text"], weight=700, limit=2, line_height=19)
        parts.extend("    " + item.strip() for item in title_parts)
        parts.append(f'    <text x="68" y="{y+84}" font-family="Segoe UI,Arial,sans-serif" font-size="12" font-weight="700" fill="{palette["highlight"] if selected else palette["muted"]}">{status.upper()}</text>')
        bar_x, bar_y, bar_w = 462, y + 23, 286
        parts.append(f'    <rect x="{bar_x}" y="{bar_y}" width="{bar_w}" height="22" rx="11" fill="{palette["background"]}"/>')
        parts.append(f'    <rect x="{bar_x}" y="{bar_y}" width="{bar_w * float(candidate["weightedTotal"]) / 100:g}" height="22" rx="11" fill="url(#accent)"/>')
        parts.append(f'    <text x="{bar_x+bar_w+18}" y="{bar_y+17}" font-family="Segoe UI,Arial,sans-serif" font-size="18" font-weight="700" fill="{palette["text"]}">{candidate["weightedTotal"]:g}</text>')
        dot_x = 470
        for criterion in criterion_ids:
            score = candidate["scores"][criterion]
            parts.append(f'    <g role="group" aria-label="{esc(criterion_names[criterion])}: {score} out of 5">')
            parts.append(f'      <text x="{dot_x}" y="{y+78}" font-family="Segoe UI,Arial,sans-serif" font-size="11" font-weight="700" fill="{palette["muted"]}">{criterion}</text>')
            for dot in range(5):
                color = palette["accent"] if dot < score else palette["line"]
                opacity = "1" if dot < score else ".28"
                parts.append(f'      <circle cx="{dot_x+28+dot*13}" cy="{y+74}" r="5" fill="{color}" opacity="{opacity}"/>')
            parts.append("    </g>")
            dot_x += 126
        if candidate["disqualifiers"]:
            parts.append(f'    <title>{esc(" ".join(candidate["disqualifiers"]))}</title>')
        parts.append("  </g>")
    parts.append(f'  <text x="600" y="{height-30}" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif" font-size="13" fill="{palette["muted"]}">Scores: 1–5 · Weighted total = sum(weight × score) / 5 · Disqualifiers override totals</text>')
    return svg_finish(parts)


def render_infographic(spec: dict[str, Any], palette: dict[str, Any]) -> str:
    stages = spec["stages"]
    width, height = 1200, 520
    digest = sha256_text(json.dumps(spec, sort_keys=True, ensure_ascii=False))
    parts = svg_open(width, height, spec["title"], spec["alt"],
                     f"registry-sha256:{digest}", palette)
    parts.extend(text_block(58, 64, spec["title"], width=62, size=29,
                            fill=palette["text"], weight=700, limit=2, line_height=35))
    parts.extend(text_block(58, 116, spec["caption"], width=108, size=15,
                            fill=palette["muted"], limit=2, line_height=20))
    count = len(stages)
    card_w = min(250, (1080 - (count - 1) * 20) / max(1, count))
    total_w = count * card_w + (count - 1) * 20
    start_x = (width - total_w) / 2
    y = 184
    for index, stage in enumerate(stages):
        x = start_x + index * (card_w + 20)
        if index:
            parts.append(f'  <line x1="{x-20:g}" y1="302" x2="{x-3:g}" y2="302" stroke="{palette["accent"]}" stroke-width="3" marker-end="url(#arrow)"/>')
        parts.append(f'  <g role="group" aria-label="{esc(stage["label"])}: {esc(stage["detail"])}" filter="url(#shadow)">')
        parts.append(f'    <rect x="{x:g}" y="{y}" width="{card_w:g}" height="246" rx="22" fill="{palette["surface"]}" stroke="{palette["line"]}" stroke-width="2"/>')
        parts.append(f'    <circle cx="{x+card_w/2:g}" cy="{y+57}" r="32" fill="url(#accent)"/>')
        parts.append(f'    <text x="{x+card_w/2:g}" y="{y+65}" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif" font-size="22" font-weight="700" fill="#ffffff">{index+1}</text>')
        label_lines = lines(stage["label"], max(13, int(card_w / 9)), 3)
        parts.append(f'    <text x="{x+card_w/2:g}" y="{y+119}" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif" font-size="16" font-weight="700" fill="{palette["text"]}">')
        for line_index, line in enumerate(label_lines):
            dy = "0" if line_index == 0 else "20"
            parts.append(f'      <tspan x="{x+card_w/2:g}" dy="{dy}">{esc(line)}</tspan>')
        parts.append("    </text>")
        detail_lines = lines(stage["detail"], max(18, int(card_w / 8)), 4)
        detail_y = y + 165 + max(0, len(label_lines) - 1) * 12
        parts.append(f'    <text x="{x+card_w/2:g}" y="{detail_y:g}" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif" font-size="12" fill="{palette["muted"]}">')
        for line_index, line in enumerate(detail_lines):
            dy = "0" if line_index == 0 else "17"
            parts.append(f'      <tspan x="{x+card_w/2:g}" dy="{dy}">{esc(line)}</tspan>')
        parts.append("    </text>")
        parts.append("  </g>")
    return svg_finish(parts)


def png_dimensions(payload: bytes) -> tuple[int, int]:
    if len(payload) < 24 or payload[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("not a PNG")
    return struct.unpack(">II", payload[16:24])


def asset_record(path: Path, asset_type: str, alt: str, usage: list[str],
                 origin: str, license_name: str, payload: bytes | None = None,
                 dimensions: tuple[int, int] | None = None) -> dict[str, Any]:
    data = payload if payload is not None else path.read_bytes()
    if dimensions is None:
        if path.suffix.casefold() == ".png":
            dimensions = png_dimensions(data)
        else:
            match = re.search(rb'viewBox="0 0 ([0-9]+) ([0-9]+)"', data)
            dimensions = (int(match.group(1)), int(match.group(2))) if match else (0, 0)
    return {
        "path": path.relative_to(ROOT).as_posix(),
        "type": asset_type,
        "dimensions": {"width": dimensions[0], "height": dimensions[1]},
        "byteSize": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
        "alt": alt,
        "usage": sorted(usage),
        "origin": origin,
        "license": license_name,
    }


def expected_svg_bytes(path: Path, body: str) -> bytes:
    return plan_generated(path, body, "xml").encode("utf-8")


def write_manifest(registry: dict[str, Any], expected_svgs: dict[Path, tuple[bytes, str, list[str], str]],
                   icons: dict[str, dict[str, Any]], check: bool) -> bool:
    assets: list[dict[str, Any]] = []
    for raster in registry["rasterAssets"]:
        path = ROOT / raster["path"]
        if not path.is_file():
            raise FileNotFoundError(f"Missing registered raster: {raster['path']}")
        assets.append(asset_record(path, "raster-illustration", raster["alt"], raster["usage"],
                                   raster["origin"]["generator"], raster["license"]["grant"]))
    for path, (payload, alt, usage, asset_type) in sorted(expected_svgs.items(), key=lambda item: item[0].as_posix()):
        assets.append(asset_record(path, asset_type, alt, usage, "deterministic renderer", "MIT",
                                   payload=payload))
    icon_usage: dict[str, set[str]] = {}
    icon_by_path: dict[str, dict[str, Any]] = {}
    for lab in registry["labs"]:
        for node in lab["topology"]["nodes"]:
            icon = icons.get(node["iconKey"])
            if icon:
                icon_by_path[icon["path"]] = icon
                icon_usage.setdefault(icon["path"], set()).add(lab["id"])
    for icon_path, icon in sorted(icon_by_path.items()):
        path = ROOT / icon["path"]
        assets.append(asset_record(path, "official-service-icon", icon.get("alt", icon_path),
                                   sorted(icon_usage[icon_path]), icon["sourceUrl"], "Microsoft icon terms"))
    document = {
        "schemaVersion": "1.0.0",
        "generatedFrom": "curriculum/visuals.yml",
        "counts": {
            "registeredRasters": len(registry["rasterAssets"]),
            "labSvgs": sum(1 for item in assets if item["type"].startswith("lab-")),
            "siteInfographics": sum(1 for item in assets if item["type"] == "site-infographic"),
            "officialIcons": sum(1 for item in assets if item["type"] == "official-service-icon"),
        },
        "assets": assets,
    }
    payload = (json.dumps(document, indent=2, ensure_ascii=False) + "\n").encode("utf-8")
    path = ROOT / registry["generatedManifestPath"]
    actual = path.read_bytes() if path.exists() else b""
    if actual == payload:
        return False
    if check:
        return True
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(payload)
    return True


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--only", nargs="*", default=[], help="LAB IDs or infographic IDs")
    args = parser.parse_args()
    registry = load_yaml(REGISTRY_PATH)
    palettes = {item["id"]: item for item in registry["palettes"]}
    _, catalog, _, _, _ = load_model()
    catalog_by_id = {item["id"]: item for item in catalog["labs"]}
    icons = icon_index()
    only = set(args.only)
    known = {item["id"] for item in registry["labs"]} | {item["id"] for item in registry["siteInfographics"]}
    unknown = only - known
    if unknown:
        raise SystemExit("Unknown visual scope: " + ", ".join(sorted(unknown)))
    drift: list[str] = []
    expected_svgs: dict[Path, tuple[bytes, str, list[str], str]] = {}
    for visual in registry["labs"]:
        lab_id = visual["id"]
        lab = catalog_by_id[lab_id]
        palette = palettes[visual["paletteId"]]
        folder = ROOT / "labs" / visual["folder"]
        source_path = folder / "diagrams" / "architecture.mmd"
        decision_path = ROOT / visual["decisionMatrix"]["sourcePath"]
        if not source_path.is_file() or not decision_path.is_file():
            raise FileNotFoundError(f"Missing topology source or decision for {lab_id}")
        source = source_path.read_text(encoding="utf-8")
        decision = load_yaml(decision_path)
        outputs = [
            (folder / "diagrams" / "summary.svg", render_banner(lab, visual, palette),
             visual["banner"]["alt"], "lab-summary"),
            (folder / "diagrams" / "architecture.svg", render_topology(lab, visual, palette, source, icons),
             visual["topology"]["alt"], "lab-topology"),
            (folder / "diagrams" / "decision-matrix.svg", render_decision(lab, visual, palette, decision),
             visual["decisionMatrix"]["alt"], "lab-decision"),
        ]
        for path, body, alt, asset_type in outputs:
            expected = expected_svg_bytes(path, body)
            expected_svgs[path] = (expected, alt, [f"labs/{visual['folder']}/README.md"], asset_type)
            if not only or lab_id in only:
                if write_or_check(path, body, "xml", args.check):
                    drift.append(path.relative_to(ROOT).as_posix())
    for spec in registry["siteInfographics"]:
        palette = palettes[spec["paletteId"]]
        path = ROOT / "docs" / "site-assets" / "infographics" / INFOGRAPHIC_FILENAMES[spec["id"]]
        body = render_infographic(spec, palette)
        expected = expected_svg_bytes(path, body)
        expected_svgs[path] = (expected, spec["alt"], spec["usage"], "site-infographic")
        if not only or spec["id"] in only:
            if write_or_check(path, body, "xml", args.check):
                drift.append(path.relative_to(ROOT).as_posix())
    if not only and write_manifest(registry, expected_svgs, icons, args.check):
        drift.append(registry["generatedManifestPath"])
    if drift and args.check:
        print("Visual drift:\n" + "\n".join(f"- {item}" for item in drift))
        return 1
    verb = "would update" if args.check else "updated" if drift else "verified"
    print(f"{verb} {len(drift)} visual artifacts ({len(registry['labs']) * 3} lab SVGs, {len(registry['siteInfographics'])} infographics)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
