#!/usr/bin/env python3
"""Enforce assessment structure, originality, mapping, and answer-position rules.

Originality checks intentionally remove question identifiers, numeric decoration,
variable names, and known generated suffixes.  They also build a context-masked
signature from each lab's authored facts.  A repeated template therefore remains a
repeat even when a generator swaps a lab name or appends a unique-looking label.
"""

from __future__ import annotations

import argparse
import re
import unicodedata
from collections import Counter, defaultdict
from difflib import SequenceMatcher
from typing import Any, Iterable

from jsonschema import Draft202012Validator, FormatChecker

from az305lib import ROOT, load_model, load_yaml

TOKEN = re.compile(r"[a-z0-9]+")
IDENTIFIER = re.compile(r"(?i)\b(?:LAB[- ]?\d{1,2}(?:-(?:Q|CP|REQ)-?\d+)?|ADR-LAB\d+-\d+)\b")
VARIABLE = re.compile(r"\$[A-Za-z_][A-Za-z0-9_]*")
URL = re.compile(r"https?://\S+")
NUMBER = re.compile(r"\b\d+(?:\.\d+)?\b")
CAMOUFLAGE_SUFFIXES = (
    re.compile(r"(?i)\s*[—-]\s*apply this specifically to\s+lab\s*[- ]?\d+\s+checkpoint\s+\d+\.?\s*$"),
    re.compile(r"(?i)\bdecision case\s+(?:lab)?\d*[- ]?q?\d+\.?"),
    re.compile(r"(?i)\bcheckpoint-specific facts:\s*.*$"),
)
BANNED_GENERATOR_SCAFFOLDS = (
    re.compile(r"(?i)approve .{0,240} immediately,? then use the successful deployment"),
    re.compile(r"(?i)use the outcome from .{0,300} as the only acceptance test"),
    re.compile(r"(?i)search the subscription for names resembling"),
    re.compile(r"(?i)purge recoverable data first,? then reconstruct"),
    re.compile(r"(?i)claim all five pillars are satisfied once"),
    re.compile(r"(?i)switch command surfaces midway because both tools"),
    re.compile(r"(?i)generate a new runid and discard the existing state"),
    re.compile(r"(?i)delete every resource matching the lab name"),
    re.compile(r"(?i)\bcomplete this action\b"),
    re.compile(r"(?i)\bcomplete two checks\b"),
    re.compile(r"(?i)\bfollow with (?:exclude|verify|assume|run|record|store|apply|use)\b"),
    re.compile(r"(?i)\bafter (?:declare|apply|use|record|store|run|verify|select|reject|require|keep|make|investigate)\b"),
    re.compile(r"(?i)\bcomplete (?:store|record|apply|use|run|verify|select|reject|require|keep|make|investigate)\b"),
)
BANNED_META_PHRASES = (
    "the scenario says",
    "one possible record is",
    "proposed disposition",
    "checkpoint-specific facts",
    "apply this specifically",
)

# Keep functional prose visible while masking service- and scenario-specific nouns.
# This turns "In the X review ... Y" and "In the Z review ... W" into the same
# signature without deleting the language that reveals a repeated template.
SCAFFOLD_WORDS = {
    "a", "an", "and", "after", "against", "all", "also", "as", "at", "be", "because", "before", "but", "by",
    "can", "cannot", "case", "choose", "condition", "constraint", "decision", "design", "does", "during", "each",
    "evidence", "every", "fact", "failure", "for", "from", "has", "have", "how", "if", "in", "into", "is", "it",
    "must", "no", "not", "of", "on", "only", "option", "or", "other", "outcome", "record", "requirement", "review",
    "select", "should", "state", "that", "the", "then", "this", "to", "under", "use", "when", "which", "while",
    "with", "without", "would", "acceptance", "action", "apply", "associated", "basis", "claimed", "compare", "conclusive",
    "consider", "decisive", "directly", "disposition", "evaluate", "evaluates", "explicit", "first", "grounds", "identify",
    "independent", "infer", "inspection", "linked", "make", "observation", "pair", "premise", "preserve", "proposal",
    "proposed", "recorded", "records", "relevant", "result", "resulting", "second", "sequence", "separate", "specific",
    "stated", "support", "supporting", "team", "test", "treatment", "trace", "traceable", "two",
}
GENERIC_ASSESSMENT_WORDS = {
    "assertion", "assertions", "checkpoint", "correct", "expected", "negative", "positive", "properties", "property",
    "safe", "safest", "successful", "success", "result", "results", "option", "choice", "answer", "evidence", "requirement",
}


def normalized(value: str) -> str:
    return " ".join(TOKEN.findall(value.lower()))


def word_count(value: str) -> int:
    return len(TOKEN.findall(value))


def invalid_control_characters(value: str) -> list[str]:
    """Return Unicode control/private/unassigned code points, excluding tab."""
    invalid_categories = {"Cc", "Cf", "Cs", "Co", "Cn"}
    return sorted(
        {
            f"U+{ord(character):04X}"
            for character in value
            if character != "\t" and unicodedata.category(character) in invalid_categories
        }
    )


def decamouflaged(value: str) -> str:
    """Normalize text after removing common uniqueness camouflage."""
    cleaned = value
    for pattern in CAMOUFLAGE_SUFFIXES:
        cleaned = pattern.sub(" ", cleaned)
    cleaned = URL.sub(" url ", cleaned)
    cleaned = IDENTIFIER.sub(" identifier ", cleaned)
    cleaned = VARIABLE.sub(" variable ", cleaned)
    cleaned = NUMBER.sub(" number ", cleaned)
    return normalized(cleaned)


def strings_in(value: Any) -> Iterable[str]:
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for item in value.values():
            yield from strings_in(item)
    elif isinstance(value, list):
        for item in value:
            yield from strings_in(item)


def context_vocabulary(lab: dict[str, Any], content: dict[str, Any], checkpoint: dict[str, Any]) -> set[str]:
    """Return content words that may not provide scaffold uniqueness."""
    selected = {
        "title": lab.get("title", ""),
        "laneLabel": lab.get("laneLabel", ""),
        "scenario": content.get("scenario", ""),
        "businessOutcome": content.get("businessOutcome", ""),
        "stakeholders": content.get("stakeholders", []),
        "candidates": content.get("candidates", []),
        "selected": content.get("selected", ""),
        "changeRequest": content.get("changeRequest", ""),
        "allCheckpoints": content.get("checkpoints", []),
        "checkpoint": checkpoint,
    }
    words = {word for text in strings_in(selected) for word in TOKEN.findall(text.lower())}
    return {word for word in words if len(word) > 2 and word not in SCAFFOLD_WORDS}


def checkpoint_specific_vocabulary(checkpoint: dict[str, Any]) -> set[str]:
    """Return service/control terms that make a keyed option checkpoint-specific."""
    words = {word for text in strings_in(checkpoint) for word in TOKEN.findall(text.lower())}
    ignored = SCAFFOLD_WORDS | GENERIC_ASSESSMENT_WORDS | {"lab", "req", "runid"}
    return {word for word in words if len(word) > 3 and word not in ignored}


def context_skeleton(value: str, vocabulary: set[str]) -> str:
    """Mask authored nouns so repeated prose frames become comparable."""
    tokens = decamouflaged(value).split()
    masked = ["context" if token in vocabulary else token for token in tokens]
    collapsed: list[str] = []
    for token in masked:
        if token != "context" or not collapsed or collapsed[-1] != "context":
            collapsed.append(token)
    return " ".join(collapsed)


def repeated_frames(values: Iterable[tuple[str, str]], minimum: int) -> dict[str, list[str]]:
    """Return exact normalized frames used by at least ``minimum`` owners."""
    owners: defaultdict[str, list[str]] = defaultdict(list)
    for owner, frame in values:
        if frame:
            owners[frame].append(owner)
    return {frame: ids for frame, ids in owners.items() if len(ids) >= minimum}


def repeated_ngrams(values: Iterable[tuple[str, str]], width: int = 14, minimum: int = 8) -> dict[str, list[str]]:
    """Find long boilerplate spans repeated across multiple questions."""
    owners: defaultdict[str, set[str]] = defaultdict(set)
    for owner, value in values:
        tokens = decamouflaged(value).split()
        for index in range(len(tokens) - width + 1):
            owners[" ".join(tokens[index:index + width])].add(owner)
    return {gram: sorted(ids) for gram, ids in owners.items() if len(ids) >= minimum}


def repeated_cross_bank_leadins(
    values: Iterable[tuple[str, str, str]], width: int = 20, minimum_words: int = 12, minimum_owners: int = 3
) -> dict[str, list[str]]:
    """Find substantial option openings reused in more than one lab bank."""
    owners: defaultdict[str, set[tuple[str, str]]] = defaultdict(set)
    for lab_id, owner, value in values:
        lead = " ".join(decamouflaged(value).split()[:width])
        if len(lead.split()) >= minimum_words:
            owners[lead].add((lab_id, owner))
    return {
        lead: sorted(owner for _, owner in entries)
        for lead, entries in owners.items()
        if len(entries) >= minimum_owners and len({lab_id for lab_id, _ in entries}) > 1
    }


def token_overlap(left: str, right: str) -> float:
    a, b = set(TOKEN.findall(left.lower())), set(TOKEN.findall(right.lower()))
    return len(a & b) / max(1, min(len(a), len(b)))


def max_run(values: list[str]) -> int:
    longest = current = 1
    for before, after in zip(values, values[1:]):
        current = current + 1 if before == after else 1
        longest = max(longest, current)
    return longest


def short_period(values: list[str]) -> int | None:
    for period in range(1, 13):
        if all(values[index] == values[index % period] for index in range(len(values))):
            return period
    return None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()
    _, catalog, content_model, _, _ = load_model()
    content_by_id = {f"LAB-{str(item['number']).zfill(2)}": item for item in content_model["labs"]}
    schema = load_yaml(ROOT / "schemas/questions-schema.json")
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors: list[str] = []
    all_questions: list[tuple[str, dict]] = []
    leadins: defaultdict[str, set[str]] = defaultdict(set)
    option_leadin_texts: list[tuple[str, str, str]] = []
    option_sets: dict[tuple[str, ...], str] = {}
    explanation_texts: dict[str, str] = {}
    option_texts: dict[str, str] = {}
    stem_frames: list[tuple[str, str]] = []
    option_frames: list[tuple[str, str]] = []
    rationale_frames: list[tuple[str, str]] = []
    stem_texts: list[tuple[str, str]] = []
    for lab in catalog["labs"]:
        if not 1 <= int(lab["number"]) <= 25:
            continue
        content = content_by_id[lab["id"]]
        path = ROOT / "labs" / lab["folder"] / "assessment/questions.yml"
        bank = load_yaml(path)
        for issue in validator.iter_errors(bank):
            errors.append(f"{path.relative_to(ROOT)}: schema: {issue.message}")
        questions = bank.get("questions", [])
        ids = [q.get("id") for q in questions]
        expected_ids = [f"LAB{lab['number']}-Q{index:02d}" for index in range(1, 51)]
        if ids != expected_ids:
            errors.append(f"{lab['id']}: question IDs are not the exact Q01-Q50 sequence")
        difficulty = Counter(q.get("difficulty") for q in questions)
        if difficulty != Counter({"foundational": 15, "applied": 25, "advanced": 10}):
            errors.append(f"{lab['id']}: difficulty mix is {dict(difficulty)}")
        answers = [q.get("answer") for q in questions]
        counts = Counter(answers)
        if sorted(counts.values()) != [12, 12, 13, 13]:
            errors.append(f"{lab['id']}: answer balance is {dict(counts)}")
        if max_run(answers) > 3:
            errors.append(f"{lab['id']}: answer run exceeds three")
        period = short_period(answers)
        if period:
            errors.append(f"{lab['id']}: answer sequence repeats with period {period}")
        seen_objectives = Counter()
        seen_checkpoints = Counter()
        for question in questions:
            qid = question.get("id", lab["id"])
            checkpoint_match = re.fullmatch(r"LAB\d{2}-CP0([1-5])", str(question.get("checkpointId", "")))
            checkpoint = content["checkpoints"][int(checkpoint_match.group(1)) - 1] if checkpoint_match else content["checkpoints"][0]
            vocabulary = context_vocabulary(lab, content, checkpoint)
            seen_objectives[question.get("objectiveId")] += 1
            seen_checkpoints[question.get("checkpointId")] += 1
            options = question.get("options", {})
            normalized_options = [decamouflaged(str(value)) for value in options.values()]
            if len(set(normalized_options)) != 4:
                errors.append(f"{qid}: options differ only by identifier, number, variable, or generated suffix")
            option_key = tuple(sorted(normalized_options))
            if option_key in option_sets:
                errors.append(f"{qid}: repeats option set from {option_sets[option_key]}")
            option_sets[option_key] = qid
            for letter, option in options.items():
                option_owner = f"{qid}/{letter}"
                option_text = str(option)
                if word_count(option_text) > 55:
                    errors.append(f"{option_owner}: option has {word_count(option_text)} words; maximum is 55")
                controls = invalid_control_characters(option_text)
                if "\ufffd" in option_text or controls:
                    errors.append(f"{option_owner}: option contains invalid Unicode/control characters {controls or ['U+FFFD']}")
                for phrase in BANNED_META_PHRASES:
                    if phrase in option_text.lower():
                        errors.append(f"{option_owner}: option contains generator-oriented phrase '{phrase}'")
                option_key = decamouflaged(option_text)
                if option_key in option_texts:
                    errors.append(f"{option_owner}: repeats decamouflaged option from {option_texts[option_key]}")
                option_texts[option_key] = option_owner
                option_frames.append((option_owner, context_skeleton(option_text, vocabulary)))
                option_leadin_texts.append((lab["id"], option_owner, option_text))
            if question.get("answer") not in options:
                errors.append(f"{qid}: answer does not select an option")
            else:
                keyed_terms = set(decamouflaged(str(options[question["answer"]])).split())
                if not keyed_terms.intersection(checkpoint_specific_vocabulary(checkpoint)):
                    errors.append(f"{qid}: keyed option lacks a checkpoint-specific service, control, or fact")
            if not str(question.get("source", "")).startswith("https://learn.microsoft.com/"):
                errors.append(f"{qid}: source is not a direct Microsoft Learn URL")
            if len(question.get("objectiveId", "").split()) != 1 or len(question.get("checkpointId", "").split()) != 1:
                errors.append(f"{qid}: objective and checkpoint mappings must be singular")
            stem = str(question.get("stem", ""))
            if word_count(stem) > 70:
                errors.append(f"{qid}: stem has {word_count(stem)} words; maximum is 70")
            controls = invalid_control_characters(stem)
            if "\ufffd" in stem or controls:
                errors.append(f"{qid}: stem contains invalid Unicode/control characters {controls or ['U+FFFD']}")
            for phrase in BANNED_META_PHRASES:
                if phrase in stem.lower():
                    errors.append(f"{qid}: stem contains generator-oriented phrase '{phrase}'")
            checkpoint_title = normalized(checkpoint.get("title", ""))
            if checkpoint_title and normalized(stem).count(checkpoint_title) > 1:
                errors.append(f"{qid}: repeats the checkpoint title in one stem")
            expected_clause = normalized(checkpoint.get("expected", ""))
            if expected_clause and normalized(stem).count(expected_clause) > 1:
                errors.append(f"{qid}: repeats the expected-state clause in one stem")
            for pattern in BANNED_GENERATOR_SCAFFOLDS:
                if pattern.search(stem):
                    errors.append(f"{qid}: contains a banned repeated generator scaffold")
            lead = " ".join(decamouflaged(stem).split()[:12])
            leadins[lead].add(lab["id"])
            stem_texts.append((qid, stem))
            stem_frames.append((qid, context_skeleton(stem, vocabulary)))
            for letter, explanation in question.get("explanations", {}).items():
                key = decamouflaged(explanation)
                if key in explanation_texts:
                    errors.append(f"{qid}/{letter}: repeats decamouflaged rationale from {explanation_texts[key]}")
                explanation_texts[key] = f"{qid}/{letter}"
                rationale_frames.append((f"{qid}/{letter}", context_skeleton(explanation, vocabulary)))
                option_terms = set(decamouflaged(str(options.get(letter, ""))).split()) - SCAFFOLD_WORDS
                explanation_terms = set(key.split()) - SCAFFOLD_WORDS
                if not option_terms.intersection(explanation_terms):
                    errors.append(f"{qid}/{letter}: explanation is not tied to a fact in its option")
                if any(phrase in key for phrase in ("because it is best", "obviously wrong", "all of the above", "not the correct answer")):
                    errors.append(f"{qid}/{letter}: generic rationale scaffold")
            for letter, option in options.items():
                for pattern in BANNED_GENERATOR_SCAFFOLDS:
                    if pattern.search(str(option)):
                        errors.append(f"{qid}/{letter}: contains a banned repeated distractor scaffold")
            all_questions.append((qid, question))
        if set(seen_objectives) != set(lab["primaryObjectiveIds"]):
            errors.append(f"{lab['id']}: primary objective coverage mismatch")
        expected_checkpoints = {f"LAB{lab['number']}-CP0{index}" for index in range(1, 6)}
        if set(seen_checkpoints) != expected_checkpoints or any(seen_checkpoints[item] != 10 for item in expected_checkpoints):
            errors.append(f"{lab['id']}: checkpoint coverage must be ten questions per checkpoint")
    duplicate_leads = [(lead, labs) for lead, labs in leadins.items() if len(labs) > 1]
    for lead, labs in duplicate_leads:
        errors.append(f"Cross-bank lead-in repeated by {sorted(labs)}: {lead}")
    for lead, owners in repeated_cross_bank_leadins(option_leadin_texts).items():
        errors.append(f"Cross-bank option lead-in repeated by {owners[:6]}: {lead}")
    for frame, owners in list(repeated_frames(stem_frames, 3).items())[:50]:
        errors.append(f"Repeated context-masked stem scaffold in {owners[:6]}: {frame}")
    for frame, owners in list(repeated_frames(option_frames, 3).items())[:50]:
        errors.append(f"Repeated context-masked option scaffold in {owners[:6]}: {frame}")
    for frame, owners in list(repeated_frames(rationale_frames, 3).items())[:50]:
        errors.append(f"Repeated context-masked rationale scaffold in {owners[:6]}: {frame}")
    for gram, owners in list(repeated_ngrams(stem_texts).items())[:50]:
        errors.append(f"Boilerplate stem phrase repeated in {owners[:6]}: {gram}")
    normalized_stems: dict[str, str] = {}
    for index, (qid, question) in enumerate(all_questions):
        stem = decamouflaged(question["stem"])
        if stem in normalized_stems:
            errors.append(f"{qid}: decamouflaged duplicate of {normalized_stems[stem]}")
        normalized_stems[stem] = qid
        for other_id, other in all_questions[:index]:
            other_stem = decamouflaged(other["stem"])
            overlap = token_overlap(stem, other_stem)
            if overlap >= 0.82 and SequenceMatcher(None, stem, other_stem).ratio() >= 0.88:
                errors.append(f"{qid}: near duplicate of {other_id} (overlap {overlap:.2f})")
    learner_pages = list(ROOT.glob("labs/*/assessment/QUESTIONS.md"))
    for path in learner_pages:
        text = path.read_text(encoding="utf-8")
        if re.search(r"(?im)^## LAB[0-2][0-9]-Q[0-9]{2} — answer ", text) or "✓" in text:
            errors.append(f"{path.relative_to(ROOT)}: learner page exposes answers")
    if errors:
        print(f"assessment validation failed with {len(errors)} issue(s)")
        for error in errors[:200]:
            print(f"- {error}")
        if len(errors) > 200:
            print(f"- … {len(errors) - 200} more")
        return 1
    print(f"assessment validation passed: {len(all_questions)} questions across 25 banks")
    if args.verbose:
        print("answer balance, period/run rules, decamouflaged exact/near duplicates, context-masked scaffolds, long boilerplate spans, lead-ins, option sets, option-specific rationales, mappings, and learner-page separation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
