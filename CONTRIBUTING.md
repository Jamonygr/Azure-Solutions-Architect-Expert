# Contributing

Edit authoritative curriculum fragments in `curriculum/content`, assessment inputs, registries, schemas, or generator templates—not generated aggregates or generated regions directly. Then run the pipeline in this order:

```powershell
python tools/merge_lab_content.py
python tools/generate_assessment_banks.py
python tools/generate_labs.py
python tools/render_diagrams.py
python tools/expand_assessments.py
python tools/build_docs_site.py
python tools/build_docs_site.py --check
pwsh ./tools/Invoke-OfflineReleaseGate.ps1
```

The release gate repeats every drift check and is the authoritative quality entrypoint.

Generated files use the exact comments `BEGIN GENERATED AZ305 V1` and `END GENERATED AZ305 V1`. Both must occur once, in that order, and may not be nested. The generator refuses malformed markers and preserves all text outside them byte-for-byte.

Use synthetic identifiers and `.invalid` names in examples. Never commit credentials, tenant data, subscription data, `.state`, learner progress, command transcripts from real environments, screenshots, or live evidence. Every command-bearing change must retain preview behavior, ownership proofs, recovery state, and idempotent cleanup.

Assessment contributions must retain 50 questions per instructional lab, the 15/25/10 difficulty distribution, one primary objective and checkpoint per item, direct Microsoft sources, answer balance, and duplicate protections.
