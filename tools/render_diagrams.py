#!/usr/bin/env python3
"""Render the repository's constrained Mermaid flowcharts to deterministic SVG."""

from __future__ import annotations

import argparse
import html
import re
import textwrap

from az305lib import ROOT, load_model, sha256_text, write_or_check

NODE = re.compile(r"\b([A-Z][A-Z0-9]*)\[\"([^\"]+)\"\]")


def render(source: str, title: str) -> str:
    nodes: list[tuple[str, str]] = []
    seen = set()
    for node_id, label in NODE.findall(source):
        if node_id not in seen:
            seen.add(node_id)
            nodes.append((node_id, label))
    if len(nodes) < 2:
        raise ValueError("The supported Mermaid subset requires at least two labelled nodes")
    width = 760
    box_x, box_w, box_h, gap, top = 80, 600, 76, 34, 70
    height = top + len(nodes) * (box_h + gap) + 30
    elements = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="diagram-title diagram-desc">',
        f'  <title id="diagram-title">{html.escape(title)}</title>',
        f'  <desc id="diagram-desc">Architecture flow from business requirements through five checkpoints to independent evidence.</desc>',
        f'  <metadata>source-sha256:{sha256_text(source)}</metadata>',
        '  <defs><marker id="arrow" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto"><path d="M0,0 L10,3.5 L0,7 Z" fill="#005a9e"/></marker></defs>',
        '  <rect width="100%" height="100%" fill="#ffffff"/>',
    ]
    for index, (_, label) in enumerate(nodes):
        y = top + index * (box_h + gap)
        if index:
            prior_y = y - gap
            elements.append(f'  <line x1="380" y1="{prior_y}" x2="380" y2="{y}" stroke="#005a9e" stroke-width="3" marker-end="url(#arrow)"/>')
        elements.append(f'  <rect x="{box_x}" y="{y}" width="{box_w}" height="{box_h}" rx="10" fill="#eef5ff" stroke="#005a9e" stroke-width="2"/>')
        wrapped = textwrap.wrap(label, width=76)[:3]
        text_y = y + 27 - (len(wrapped) - 1) * 8
        elements.append(f'  <text x="380" y="{text_y}" text-anchor="middle" font-family="Arial, sans-serif" font-size="15" fill="#111111">')
        for line_index, line in enumerate(wrapped):
            dy = "0" if line_index == 0 else "20"
            elements.append(f'    <tspan x="380" dy="{dy}">{html.escape(line)}</tspan>')
        elements.append("  </text>")
    elements.append("</svg>")
    return "\n".join(elements) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--only", nargs="*", default=[])
    args = parser.parse_args()
    _, catalog, _, _, _ = load_model()
    only = set(args.only)
    drift = []
    for lab in catalog["labs"]:
        if only and lab["id"] not in only:
            continue
        folder = ROOT / "labs" / lab["folder"] / "diagrams"
        source_path = folder / "architecture.mmd"
        if not source_path.exists():
            raise SystemExit(f"Missing Mermaid source: {source_path.relative_to(ROOT)}")
        source = source_path.read_text(encoding="utf-8")
        body = render(source, f"{lab['id']} {lab['title']}")
        svg_path = folder / "architecture.svg"
        if write_or_check(svg_path, body, "xml", args.check):
            drift.append(str(svg_path.relative_to(ROOT)))
    if drift and args.check:
        print("Diagram drift:\n" + "\n".join(f"- {item}" for item in drift))
        return 1
    print(f"{'would update' if args.check else 'updated' if drift else 'verified'} {len(drift)} diagrams")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
