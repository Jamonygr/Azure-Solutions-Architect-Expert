#!/usr/bin/env python3
"""Create deterministic, checkpoint-grounded assessment banks for Labs 01-25.

Every checkpoint contributes ten different reasoning tasks. The prose is composed
from authored scenario, requirement, command, evidence, failure, recovery, WAF, and
decision facts; question identifiers are deliberately absent from question text so
they cannot be used to disguise repeated content.
"""

from __future__ import annotations

import argparse
import hashlib
import random
import re
from dataclasses import dataclass
from typing import Any

from az305lib import ROOT, load_model, write_or_check, yaml_text

LETTERS = "ABCD"


def answer_sequence(lab_id: str) -> list[str]:
    """Return a deterministic balanced sequence without a short period or long run."""
    values = list("A" * 13 + "B" * 13 + "C" * 12 + "D" * 12)
    seed = int(hashlib.sha256(lab_id.encode()).hexdigest()[:16], 16)
    randomizer = random.Random(seed)
    for _ in range(10000):
        randomizer.shuffle(values)
        if max_run(values) <= 3 and not has_short_period(values):
            return list(values)
    raise RuntimeError(f"Could not create a balanced answer sequence for {lab_id}")


def max_run(values: list[str]) -> int:
    longest = current = 1
    for before, after in zip(values, values[1:]):
        current = current + 1 if before == after else 1
        longest = max(longest, current)
    return longest


def has_short_period(values: list[str]) -> bool:
    return any(all(values[index] == values[index % period] for index in range(len(values))) for period in range(1, 13))


def sentence(value: str) -> str:
    """Normalize authored prose for interpolation without changing its meaning."""
    return re.sub(r"\s+", " ", value.strip()).rstrip(".?!")


def lower_start(value: str) -> str:
    value = sentence(value)
    return value[:1].lower() + value[1:] if value else value


def upper_start(value: str) -> str:
    value = sentence(value)
    return value[:1].upper() + value[1:] if value else value


CASE_OPENERS = (
    "A review of '{checkpoint}' begins with input from {actor}.",
    "'{checkpoint}' awaits approval from {actor}.",
    "'{checkpoint}' is reopened at the request of {actor}.",
    "A design review of '{checkpoint}' includes {actor}.",
    "The team asks {actor} to assess '{checkpoint}'.",
    "A recommendation on '{checkpoint}' is requested by {actor}.",
    "'{checkpoint}' is assigned to {actor}.",
    "An assurance review of '{checkpoint}' includes {actor}.",
    "Approval of '{checkpoint}' is questioned by {actor}.",
    "The implementation review has reached '{checkpoint}'.",
    "The approach to '{checkpoint}' is challenged by {actor}.",
    "A decision test for '{checkpoint}' includes {actor}.",
    "The architecture board reconsiders '{checkpoint}' with {actor}.",
)

ASK_FORMS = (
    "Which option is {goal}?",
    "What should the architect select as {goal}?",
    "Select {goal}.",
    "Which response provides {goal}?",
    "Which choice gives the team {goal}?",
    "What is {goal}?",
    "Which recommendation supplies {goal}?",
    "Choose {goal}.",
    "Which answer describes {goal}?",
    "What should be recorded as {goal}?",
    "Which proposal supplies {goal}?",
    "Which option best represents {goal}?",
    "Which course of action provides {goal}?",
    "Which finding constitutes {goal}?",
    "Which recommendation delivers {goal}?",
    "Which response meets the need for {goal}?",
    "Which choice should be approved as {goal}?",
    "What should the team use as {goal}?",
    "Which option best establishes {goal}?",
    "Which answer identifies {goal}?",
    "What recommendation gives the reviewers {goal}?",
    "Which action produces {goal}?",
    "What best demonstrates {goal}?",
)

PAIR_FORMS = (
    "{first}; {link}, {second_lower}",
    "{first}. Then, {second_lower}",
    "{first}; afterward, {second_lower}",
    "{first}; then {second_lower}",
    "{first}. Independently, {second_lower}",
    "{first}. Next, {second_lower}",
    "{first}, and then {second_lower}",
    "{first}. Also, {second_lower}",
    "{first}; in a separate step, {second_lower}",
    "{first}. As another control, {second_lower}",
    "{first}; as a separate check, {second_lower}",
    "{first}. Afterward, {second_lower}",
    "{first}; next, {second_lower}",
    "{first}. In addition, {second_lower}",
    "{first}; before approval, {second_lower}",
    "{first}. Separately, {second_lower}",
    "{first}; for this decision, {second_lower}",
    "{first}. Before sign-off, {second_lower}",
    "{first}; as an independent condition, {second_lower}",
)

PAIR_LINKS = (
    "separately",
    "independently",
    "before approval",
    "as a second control",
    "during the same review",
    "for the recorded decision",
    "as another gate",
    "without relying on inference",
    "before closing the checkpoint",
    "for the final assessment",
)

BASIS_ACTIONS = (
    "Rely on the claim that {basis}",
    "Treat it as established that {basis}",
    "Use the premise that {basis}",
    "Proceed on the belief that {basis}",
    "Accept without proof that {basis}",
    "Take it as conclusive that {basis}",
    "Base approval on the claim that {basis}",
    "Rely on the belief that {basis}",
    "Use as justification the claim that {basis}",
    "Consider it sufficient that {basis}",
    "Treat as decisive the assertion that {basis}",
)


@dataclass(frozen=True)
class Draft:
    stem: str
    options: tuple[str, str, str, str]
    explanations: tuple[str, str, str, str]


def make_stem(lab: dict[str, Any], content: dict[str, Any], cp: dict[str, Any], variant: int, angle: int) -> str:
    stakeholders = content["stakeholders"]
    actor = stakeholders[(variant + angle) % len(stakeholders)]
    case_facts = (
        f"Approval requires a positive result plus this independent negative assertion: {sentence(cp['negative'])}.",
        f"The selected architecture is {content['selected']}; object existence alone is not success.",
        f"Evidence must address this risk without retaining credentials: {sentence(cp['failure'])}.",
        f"The target is {sentence(cp['expected'])}, but the latest evidence does not show it.",
        f"The run encountered this modeled failure: {sentence(cp['failure'])}.",
        f"Without making a new change, the team must inspect the risk '{sentence(cp['failure'])}' using the {lab['laneLabel']} lane.",
        f"A passing positive check does not by itself prove this negative assertion: {sentence(cp['negative'])}.",
        f"The board wants the Well-Architected consequence of mitigating this risk: {sentence(cp['failure'])}.",
        f"A material change now applies: {sentence(content['changeRequest'])}.",
        f"After a partial run, cleanup must follow this dependency: {sentence(cp['cleanup'])}.",
    )
    goals = (
        f"the acceptance rule that makes {cp['requirement']} testable",
        "the intended successful finding",
        "sufficient, properly scoped evidence",
        "the most likely cause",
        "the safest recovery action",
        "the read-only, lane-correct inspection",
        "the assertion pair that proves both conditions independently",
        "the consequence attributable to this checkpoint",
        "the correct revision to the decision record",
        "the dependency-safe cleanup plan",
    )
    opener_index = (variant * 10 + angle) % len(CASE_OPENERS)
    opening = CASE_OPENERS[opener_index].format(
        actor=lower_start(actor),
        checkpoint=cp["title"],
    )
    question = ASK_FORMS[(variant + angle) % len(ASK_FORMS)].format(goal=goals[angle])
    return f"{opening} {case_facts[angle]} {question}"


def pair_choice(first: str, second: str, style: int) -> str:
    """Join two concrete actions with varied but concise decision syntax."""
    first = upper_start(first)
    second = upper_start(second)
    return PAIR_FORMS[style % len(PAIR_FORMS)].format(
        first=first,
        first_lower=lower_start(first),
        second=second,
        second_lower=lower_start(second),
        link=PAIR_LINKS[(style // len(PAIR_FORMS)) % len(PAIR_LINKS)],
    ) + "."


def unsupported(proposal: str, claimed_basis: str, style: int) -> str:
    """Express a specific but invalid decision and the premise behind it."""
    basis_action = BASIS_ACTIONS[(style * 7) % len(BASIS_ACTIONS)].format(basis=lower_start(claimed_basis))
    return pair_choice(proposal, basis_action, style)


def rationale(fact: str, consequence: str, ordinal: int) -> str:
    """Compose a fact-first, option-specific explanation without stock verdict text."""
    joins = (
        "Consequently, {consequence}.",
        "For this case, {consequence}.",
        "That evidence means {consequence}.",
        "The resulting architectural conclusion is that {consequence}.",
        "Under the stated constraint, {consequence}.",
        "This matters because {consequence}.",
        "The checkpoint therefore requires that {consequence}.",
        "In the decision record, {consequence}.",
        "The independent assertion shows why {consequence}.",
        "Operationally, {consequence}.",
        "The requirement-to-evidence link establishes that {consequence}.",
    )
    starts = (
        "{fact}.",
        "The controlling fact is that {fact}.",
        "The authored acceptance boundary states that {fact}.",
        "The relevant observation is that {fact}.",
        "The checkpoint specifically records that {fact}.",
        "The scenario makes clear that {fact}.",
        "The architecture evidence must show that {fact}.",
        "The applicable design condition is that {fact}.",
        "The review is governed by this fact: {fact}.",
        "The retained result must be reconciled with the fact that {fact}.",
        "The decision tension comes from the fact that {fact}.",
        "The safe operating boundary says that {fact}.",
        "The traceable checkpoint outcome is that {fact}.",
        "The failure model establishes that {fact}.",
        "The recovery guidance assumes that {fact}.",
        "The WAF consequence identifies that {fact}.",
        "The command-level assertion is anchored in the fact that {fact}.",
    )
    first = starts[ordinal % len(starts)].format(fact=lower_start(fact))
    second = joins[(ordinal // len(starts)) % len(joins)].format(consequence=lower_start(consequence))
    return f"{first} {second}"


def checkpoint_draft(
    lab: dict[str, Any], content: dict[str, Any], cp: dict[str, Any], cp_index: int, angle: int, variant: int
) -> Draft:
    """Build one of ten distinct reasoning tasks from authored checkpoint facts."""
    checkpoints = content["checkpoints"]
    peers = [item for item in checkpoints if item is not cp]
    other = peers[angle % len(peers)]
    other_two = peers[(angle + 1) % len(peers)]
    selected = content["selected"]
    alternatives = [item for item in content["candidates"] if item != selected]
    alt_one, alt_two = alternatives[:2]
    stem = make_stem(lab, content, cp, variant, angle)
    requirement = cp["requirement"]
    expected = sentence(cp["expected"])
    negative = sentence(cp["negative"])
    evidence = sentence(cp["evidence"])
    failure = sentence(cp["failure"])
    retry = sentence(cp["retry"])
    cleanup = sentence(cp["cleanup"])
    waf = sentence(cp["waf"])
    ordinal = ((int(lab["number"]) - 1) * 50 + (cp_index - 1) * 10 + angle) * 4

    if angle == 0:
        options = (
            pair_choice(f"Require the documented positive state for {cp['title']}", f"Verify that {lower_start(negative)}", variant * 41),
            unsupported(f"select {alt_one} before checking {cp['title']}", "a successful deployment will later prove the architecture constraint", ordinal + 1),
            unsupported(f"use the passing result from {other['title']} to approve {cp['title']}", "one control establishes an unrelated acceptance boundary", ordinal + 2),
            unsupported(f"choose {alt_two} and skip the {cp['title']} negative assertion", "the candidate has the lowest implementation effort", ordinal + 3),
        )
        reasons = (
            (expected, f"the positive state and an independent negative assertion jointly make {requirement} testable"),
            (negative, f"a deployment result cannot prove {requirement}, and {alt_one} still has to meet the mandatory boundary"),
            (other["expected"], f"that outcome belongs to {other['title']} and leaves {cp['title']} unverified"),
            (content["businessOutcome"], f"implementation effort cannot justify skipping the negative assertion or displace {requirement}"),
        )
    elif angle == 1:
        options = (
            pair_choice(f"Record {lower_start(expected)}", f"Classify it as success for {requirement}", variant * 41 + 4),
            unsupported(f"use only the negative assertion '{negative}' as the success result", "absence proves every required positive property", ordinal + 4),
            unsupported(f"use the successful finding from {other['title']} as the result for {cp['title']}", "a property from the current checkpoint does not need to be inspected", ordinal + 5),
            unsupported(f"record the failure condition '{failure}' as a successful state", "the command returned an object", ordinal + 6),
        )
        reasons = (
            (expected, f"this is the authored target state for {cp['title']} and directly supports {requirement}"),
            (negative, "this is the independent prohibited-state assertion, not a successful finding"),
            (other["expected"], f"evidence for {other['title']} cannot substitute for the properties required at {cp['title']}"),
            (failure, "resource existence or command output does not convert the documented failure condition into success"),
        )
    elif angle == 2:
        options = (
            pair_choice(f"Retain {lower_start(evidence)}", "Exclude credentials and unrelated response fields", variant * 41 + 8),
            unsupported(f"substitute the evidence from {other['title']} for {cp['title']}", "a related checkpoint proves the current expected state", ordinal + 7),
            unsupported(f"store unredacted {cp['title']} output with operator, tenant, token, and request context", "reproduction requires every captured field", ordinal + 8),
            unsupported(f"record only the {cp['title']} positive inspection's exit status", "projected properties and assertion results can be reconstructed later", ordinal + 9),
        )
        reasons = (
            (evidence, "it captures the checkpoint's observable properties while keeping the evidence boundary narrow"),
            (other["evidence"], f"that evidence supports {other['title']}, so it cannot demonstrate {expected}"),
            ("Unredacted implementation output", "identity, tenant, or token material exceeds the non-secret evidence contract"),
            ("The positive inspection's exit status", f"an exit code alone does not show whether {lower_start(expected)}"),
        )
    elif angle == 3:
        options = (
            pair_choice(f"Investigate {lower_start(failure)}", f"Isolate that cause before changing {selected}", variant * 41 + 12),
            unsupported(f"treat '{sentence(other['failure'])}' as grounds to reject {cp['title']}", f"{other['title']}'s failure model applies unchanged here", ordinal + 10),
            unsupported(f"ignore the negative assertion '{negative}'", "a later material change will make it unnecessary", ordinal + 11),
            unsupported(f"investigate {other_two['title']} instead of diagnosing {cp['title']}", f"a passing result at {other_two['title']} identifies the current cause", ordinal + 12),
        )
        reasons = (
            (failure, f"it is the checkpoint's causal failure model and should be isolated before retrying {cp['title']}"),
            (other["failure"], f"that condition belongs to {other['title']} and does not by itself invalidate {selected}"),
            (negative, "the negative assertion must be evaluated now, independent of a later business change"),
            (other_two["expected"], f"a passing result at {other_two['title']} gives no causal evidence for the failure at {cp['title']}"),
        )
    elif angle == 4:
        options = (
            pair_choice(retry, "Preserve the current run identity and evidence", variant * 41 + 16),
            unsupported(f"perform cleanup immediately: {cleanup}", "the failed operation and its returned identifiers do not need reconciliation", ordinal + 13),
            unsupported(f"create a different run identity before diagnosing '{failure}'", "the first state record and returned identifiers can be discarded", ordinal + 14),
            unsupported(f"change {other['title']} instead", f"success at {other['title']} will repair the failed state at {cp['title']}", ordinal + 15),
        )
        reasons = (
            (retry, "it corrects the narrow cause while retaining the same recovery trail and decision scope"),
            (cleanup, "cleanup before reconciliation can erase evidence or strand a partially created dependency"),
            (failure, "discarding the original run identity breaks ownership reconciliation and can duplicate a partial operation"),
            (other["expected"], f"altering an already separate checkpoint does not repair the modeled failure at {cp['title']}"),
        )
    elif angle == 5:
        options = (
            pair_choice(f"Inspect the documented properties for {cp['title']}", f"Retain this evidence: {lower_start(evidence)}", variant * 41 + 20),
            unsupported(f"rerun the {cp['title']} implementation command and infer the expected state", "absence of a shell error proves every property", ordinal + 16),
            unsupported(f"run only this negative inspection for {cp['title']}: {negative}", "an empty negative result reports every required positive property", ordinal + 17),
            unsupported(f"run the positive inspection for {other['title']} and apply it to {cp['title']}", "any command from the same lane proves the current checkpoint", ordinal + 18),
        )
        reasons = (
            (expected, f"the read-only inspection directly tests the properties required at {cp['title']}"),
            ("The implementation command", "it can mutate state and shell success does not independently assert the expected properties"),
            ("The negative inspection", "absence of the prohibited condition is necessary but does not establish the positive architecture state"),
            (f"The positive inspection for {other['title']}", f"it is lane-correct but proves {other['title']}, not {cp['title']}"),
        )
    elif angle == 6:
        options = (
            pair_choice(f"Verify the positive properties for {cp['title']}", f"Independently verify that {lower_start(negative)}", variant * 41 + 24),
            unsupported(f"verify only the positive result for {cp['title']} and report full compliance", "every prohibited parallel state must therefore be absent", ordinal + 19),
            unsupported(f"prove only that {lower_start(negative)} and report the intended configuration as present", "absence is equivalent to positive-state evidence", ordinal + 20),
            unsupported(f"use {other['title']}'s negative assertion for {cp['title']}", "negative assertions are interchangeable between checkpoints", ordinal + 21),
        )
        reasons = (
            (f"{expected}; {negative}", "two independent observations prevent a passing positive check from concealing an unsafe parallel state"),
            (expected, f"the positive result alone does not test the explicit anti-condition '{negative}'"),
            (negative, f"absence evidence cannot demonstrate the required positive state '{expected}'"),
            (other["negative"], f"the second assertion is valid for {other['title']} but leaves this checkpoint's prohibited state untested"),
        )
    elif angle == 7:
        options = (
            pair_choice(f"Record this consequence: {waf}", f"Tie it to {requirement}", variant * 41 + 28),
            unsupported(f"use the {other['title']} consequence as the result for {cp['title']}", f"a pillar statement remains valid when moved away from {other['title']}", ordinal + 22),
            unsupported(f"remove the control responsible for the {cp['title']} outcome", f"a {content['costClass']} cost classification outweighs the mandatory architecture state", ordinal + 23),
            unsupported(f"treat '{waf}' as proof that all five pillars pass", f"the checkpoint '{cp['title']}' no longer needs its separate negative check", ordinal + 24),
        )
        reasons = (
            (waf, f"it states the authored pillar consequence of the control evaluated at {cp['title']}"),
            (other["waf"], f"that tradeoff belongs to {other['title']} and does not explain this checkpoint's decision"),
            (f"The required outcome at {cp['title']}", f"Cost Optimization cannot remove the acceptance condition '{expected}'"),
            (negative, "one positive command cannot establish every pillar, especially while the negative state remains unchecked"),
        )
    elif angle == 8:
        options = (
            pair_choice(f"Re-score {selected} and both alternatives for {cp['title']}", f"Supersede the ADR using the changed evidence for {requirement}", variant * 41 + 32),
            unsupported(f"retain {selected} at {cp['title']} without recalculating criteria or eligibility", "the original weighted result is permanent", ordinal + 25),
            unsupported(f"select {alt_one} for {cp['title']} without rechecking its mandatory constraints", "being different from the current design is an architecture criterion", ordinal + 26),
            unsupported(f"keep {alt_two} eligible at {cp['title']} by downgrading {requirement}", "stakeholder approval is unnecessary when that requirement blocks the candidate", ordinal + 27),
        )
        reasons = (
            (f"{selected} at {cp['title']}", f"the material change '{content['changeRequest']}' requires fresh eligibility, weighted analysis, and a superseding decision"),
            (selected, "the original ADR remains historical evidence, but its score cannot answer a changed mandatory condition"),
            (alt_one, f"being different is not a criterion, and the candidate still must avoid the prohibited state at {cp['title']}"),
            (requirement, "an architect cannot silently downgrade a stakeholder-owned mandatory requirement to protect a candidate"),
        )
    else:
        options = (
            pair_choice(f"Verify exact run-state IDs and ownership tags for {cp['title']}", f"Follow this dependency rule without purge: {cleanup}", variant * 41 + 36),
            unsupported(f"apply the cleanup rule for {other['title']} before reconciling the current dependency", f"removing a parent needed to identify {cp['title']} is harmless", ordinal + 28),
            unsupported(f"delete candidates by display name before comparing the {cp['title']} ownership tags", f"the dependency rule '{cleanup}' is optional", ordinal + 29),
            unsupported(f"destroy recoverable copies before retaining the {cp['title']} negative assertion '{negative}'", "remaining command logs are sufficient recovery evidence", ordinal + 30),
        )
        reasons = (
            (cleanup, "exact identity, complete ownership tags, and the authored dependency order constrain cleanup and preserve recovery"),
            (other["cleanup"], f"a cleanup rule for {other['title']} cannot override the dependency declared for {cp['title']}"),
            (evidence, "names are not ownership proof; deletion requires the exact recorded identifier and every required tag"),
            (negative, "irreversible purge is outside the lab contract and destroys evidence needed for residual-state validation"),
        )

    explanations = tuple(rationale(fact, consequence, ordinal + offset) for offset, (fact, consequence) in enumerate(reasons))
    return Draft(stem=stem, options=options, explanations=explanations)


def make_bank(lab: dict[str, Any], content: dict[str, Any]) -> dict[str, Any]:
    answers = answer_sequence(lab["id"])
    questions = []
    objectives = list(lab["primaryObjectiveIds"])
    q_number = 0
    lab_index = int(lab["number"]) - 1
    for cp_index, cp in enumerate(content["checkpoints"], 1):
        objective = objectives[(cp_index - 1) % len(objectives)]
        variant = lab_index * 5 + cp_index - 1
        for angle in range(10):
            q_number += 1
            qid = f"LAB{lab['number']}-Q{q_number:02d}"
            draft = checkpoint_draft(lab, content, cp, cp_index, angle, variant)
            answer = answers[q_number - 1]
            answer_index = LETTERS.index(answer)
            ordered_options = [""] * 4
            ordered_explanations = [""] * 4
            ordered_options[answer_index] = draft.options[0]
            ordered_explanations[answer_index] = draft.explanations[0]
            distractor_positions = [index for index in range(4) if index != answer_index]
            for source_index, position in enumerate(distractor_positions, 1):
                ordered_options[position] = draft.options[source_index]
                ordered_explanations[position] = draft.explanations[source_index]
            difficulty = "foundational" if angle < 3 else ("applied" if angle < 8 else "advanced")
            questions.append(
                {
                    "id": qid,
                    "difficulty": difficulty,
                    "objectiveId": objective,
                    "checkpointId": f"LAB{lab['number']}-CP0{cp_index}",
                    "stem": draft.stem,
                    "options": dict(zip(LETTERS, ordered_options)),
                    "answer": answer,
                    "explanations": dict(zip(LETTERS, ordered_explanations)),
                    "remediationAnchor": f"checkpoint-{cp_index}",
                    "source": content["primarySource"]["url"],
                    "verifiedOn": "2026-09-02",
                }
            )
    return {"schemaVersion": "1.0.0", "labId": lab["id"], "questions": questions}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--only", nargs="*", default=[])
    args = parser.parse_args()
    _, catalog, content_model, _, _ = load_model()
    content_by_id = {f"LAB-{str(item['number']).zfill(2)}": item for item in content_model["labs"]}
    only = set(args.only)
    drift = []
    for lab in catalog["labs"]:
        if not 1 <= int(lab["number"]) <= 25 or (only and lab["id"] not in only):
            continue
        body = yaml_text(make_bank(lab, content_by_id[lab["id"]]))
        path = ROOT / "labs" / lab["folder"] / "assessment/questions.yml"
        if write_or_check(path, body, "yaml", args.check):
            drift.append(str(path.relative_to(ROOT)))
    if drift and args.check:
        print("Assessment source drift:\n" + "\n".join(f"- {item}" for item in drift))
        return 1
    print(f"{'would update' if args.check else 'updated' if drift else 'verified'} {len(drift)} assessment banks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
