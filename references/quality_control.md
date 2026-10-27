# Quality Control

No gate may be skipped. Read this file at the first gate; afterwards reopen the section the moment requires (gate checks, audit, triage, release checklist).

## Contents
1. Three review levels
2. Gates, one per phase
3. Diagnostic tests
4. Compliance audit
5. Issue triage: severity and routing
6. Iteration control
7. Release checklist

## 1. Three review levels

| Level | When | Question |
|---|---|---|
| Decision | Immediately after each consequential decision (protocol step 6) | Was it chosen against genuine candidates, with the apparent option named, a runner-up, and a decisive criterion? Can it trace to a source? |
| Composition | After Phase 5, and whenever Phase 3 to 5 decisions change | Does the assembled design work as one piece for this viewer, in this setting, at each viewing stage? |
| Prompt | After Phase 6 drafting, before delivery | Does the prompt carry exactly the design, and only what shapes the picture? |

A defect found at a higher level is traced to the earliest responsible decision (section 5).

## 2. Gates, one per phase

Every gate has the same six checks, then the phase card's own "Before leaving" checks, which are the phase-specific checks.
1. Every required decision of the phase is made.
2. The exploration protocol and the decision quality standard were applied where they apply (`protocol.md`).
3. **One substantive objection** is raised at the gate (the strongest case against the phase's weakest decision) and resolved, or accepted with a recorded reason. Full depth: one per owning role (Phase 1 print designer; Phase 2 brand strategist and consumer-behavior researcher; Phase 3 brand strategist and senior art director; Phase 4 brand strategist, senior art director, graphic designer, image-generation prompt specialist; Phase 5 consumer-behavior researcher, senior art director, print designer, visual communication specialist; Phase 6 senior art director and image-generation prompt specialist). Focused depth: one, from the owning role holding the phase's riskiest decision.
4. The completion criteria in the phase card's "Before leaving" are met, and every decision made in the phase names its source (traceability: Brief Ledger item or finding → implication → plan → element → execution → prompt clause). A decision with no nameable source was made from habit and fails.
5. User-facing: Phase 1 closed with the user's confirmed summary and chosen mode. Guided mode: each of Phases 2 to 6 opened with a wait note; the Phase 2 to 5 entries were printed at their gates as one compact table in plain Indonesian (`00_conversation_ux.md` section 5); the turn stopped for confirmation after Phases 2, 3, and 4. Auto mode: one wait note, nothing printed at gates, and the checks still ran. Phase 6 is the final reply.
6. The Design Log holds the phase's complete hand-off (persisted per `SKILL.md` section 5) and the next phase read it.

## 3. Diagnostic tests

Use the tests that apply; record failures with their routing.

| Test | Asks | Routes to |
|---|---|---|
| Swap | Does it still work with a competitor's name? | Phase 3 |
| Category | With the product removed, could it belong to the industry? | Phase 3 |
| Apparent-choice | Could a stranger predict hero and style from category and place? | Phase 3 |
| Context-swap | Would it be equally right in another setting? | Phase 2 or 3 |
| Distance and attention | Does the first impression hold at the glance stage in the real setting? | Phase 5 (or 3) |
| Contradiction scan | Do brand design, theme, idea, style, hero, color, type, mark, and composition agree? | Earliest conflicting phase |
| Ambition check | Does ambition fit content, budget, and format? | Phase 3 |
| Removal | Does removing the element change anything the piece needs? | Phase 4 |
| Subtraction | Does removing one more thing improve the piece? | Phase 4 or 5 |
| Fill | Does every quiet area have a named job? | Phase 5 |
| Single-voice | Does the system read as one designer's work? | Phase 4 |
| Unit and disconnection | Does the mark with wordmark read as one object, and does each stay recognizably of the same identity when the other is covered? | Phase 4 |
| Realization trace | Does every element and placement name the plan commitment it realizes, and is every commitment realized? | Phase 4 or 5 |
| Originality (apparent-choice, lineage, synthesis, depth, distinctness) | Is the leader unpredictable, nameable by lineage, derived from this brief, specialist-grade, and more than competent? | Phase 3 to 5 |
| Text-neighborhood | Is the mark distinct beside the densest text, squinting? | Phase 4 or 5 |
| Visual-effect | Would removing this prompt clause change what is drawn? | Phase 6 |
| Standalone | Could an illustrator who never saw the brief produce the design? | Phase 6 |
| Brief-quality | Does each stated quality have a visible carrier at the glance stage, and does any decision signal its opposite? | Phase 1 (translation) or the earliest contradicting phase |
| Value-key | Does the area-weighted light, mid, and dark balance, ground and large bands included, match every quality requirement? | Phase 4 (or 3) |
| Role-fit | Does each text item's treatment grade fit its content role? | Phase 4 |
| Text-only baseline | With the supporters covered, what is lacking, and is each real deficit answered by a supporter? | Phase 4 |
| Distinct-job | Does each element hold a job no other element holds? | Phase 4 |
| Weight-ceiling | Does any decoration outrank the required information it serves, at that information's stage? | Phase 4 or 5 |
| Figure-role | Does each figure appearance name one role, share one design, and stay within its weight ceiling? | Phase 4 or 5 |
| Capacity | Does every string fit its container at its final size? | Phase 5 |
| Referent | For each text item, is it nearest the thing it refers to? | Phase 5 (A2) |
| Caption | Where the stance couples, if the text were covered, would a picture with captions beneath it remain? | Phase 5 (A2), or Phase 3 integration stance |

## 4. Compliance audit

Run on the drafted prompt, then on the reply.

**Prompt audit**
- Plan fidelity: every design decision from the Execution Specification is present; nothing new appears.
- Mandatory content: every mandatory string is present, verbatim, once, with role and position; suspected typos preserved and flagged.
- Fixed assets: supplied logos, colors, and fonts reproduced as provided, not redesigned, restyled, simplified, or recolored.
- Exclusions: every user exclusion respected; only minimal, specific exclusions added.
- No invented business facts (prices, claims, testimonials, certifications, regulated or trust marks, contacts, ingredients, years in business, statistics).
- No competitor copying or reproduction of existing designs.
- Identifier: not merely a styled name unless supplied or explicitly requested as plain text; a new mark described by form class, geometry, silhouette, color, boundary, personality device, wordmark relationship, separation from adjacent type.
- Space: outer margin, isolation, and resting fields stated as concrete positive features, with proportions where they matter.
- Qualities: every quality requirement shows in the opening lines through named features; the value key is stated; nothing contradicts a quality.
- Copy and supporters: designed copy and each supporter described by traits and forms, matching the printed decisions, none outweighing required text.
- No contradictions; no rationale; no placeholders; no blank zones other than a reserved asset panel for a supplied asset; no post-generation editing instructions; no blanket emphasis; no crop marks or annotations unless requested.
- Flat artwork unless a mockup was requested or the form is the deliverable.
- The visual-effect test on every sentence.
- Standalone and readable; one coherent style logic.

**Reply audit**
- The reply follows `00_conversation_ux.md` (turn map, entry format, final reply, failure modes) and `SKILL.md` section 13: guided mode printed each entry at its gate and waited after Phases 2 to 4; auto mode printed nothing before the final reply; amendments were printed at once.
- Final reply: prompt(s) alone in code blocks in English; notes limited to the disclosure rule (`SKILL.md` 13.2); no design rationale, no repeated summary.

## 5. Issue triage: severity and routing

| Severity | Definition | Action |
|---|---|---|
| Critical | Violates a non-negotiable; mandatory content missing or altered; fixed asset altered; invented fact; a required decision never made | Stop; return to the responsible phase; re-run forward; the release is blocked |
| Major | Fails a gate check, a stress test, or the audit; generic, context-blind, or filled; the mark absorbed by type | Return to the earliest responsible decision; re-run forward |
| Minor | Weak phrasing; a redundant clause; a small imbalance | Fix in place where it was found, without altering earlier decisions |

Routing from symptom to responsible phase:

| Symptom | Responsible phase |
|---|---|
| Wrong, missing, or altered content; unsourced fact | 1 |
| Unsupported narrative; environment-blind; weak or absent inventory | 2 |
| Generic idea, style, or hero; no space intent; tension unresolved | 3 |
| Weak or styled-name mark; clashing color or type; decoration with no deficit; element costs over the space intent | 4 |
| Poor hierarchy; wrong viewing stage; crowding or filling; mark absorbed in composition | 5 |
| Rationale in the prompt; vague wording; mandatory text misplaced; space not stated | 6 |
| Stated quality missing from the ledger, or contradicted by a decision | 1 for the translation; otherwise the earliest contradicting phase |
| Value-key drift; plain-set voice copy; text-only look; unanchored supporters | 4 (3 if the plan caused it) |
| Duplicate-job elements; decoration outranking information; a second identifier; an unwanted, roleless, or inconsistent figure; an invented level mark | 4 |
| Bleed against content; a pointer with no referent; a figure covering information | 5 |
| Text overflowing its container; sizes changed late | 5 |

When a symptom has several possible causes, choose the earliest. Fixing a symptom at a later phase while its cause stands is a patch and is not permitted.

## 6. Iteration control

- A flawed decision returns the work to the earliest responsible phase; every affected later phase is re-run in order.
- Cap each issue at two revision cycles. After the second, choose the best available resolution, record it, and continue.
- A returned phase keeps all unaffected decisions; record what changed in the Design Log.
- If the same issue recurs after two cycles, the cause is upstream of where it was being fixed; record that and choose the best available resolution.
- Re-review the whole design after any change: check consistency, transitions, terminology, and that nothing is left stale or contradictory.

## 7. Release checklist

Gates and audits cover the detail; before delivering, confirm:
1. Phases 1 to 6 ran in order and every gate passed.
2. The decision commitments (`SKILL.md` section 11) are complete, and every consequential decision shows its decision record (or is marked fixed by the user or evidence).
3. The prompt audit and the reply audit passed.
4. The Phase 1 summary and the mode were confirmed, guided-mode go-aheads were obtained, and the printed decisions match the prompt (with amendments where they changed).
5. Disclosure (`SKILL.md` 13.2) is complete: every consequential assumption, yielded preference, written copy, suspected typo, supplied asset, reserved asset panel, volume risk, and ratio limit reached the user once, with no design rationale.
6. If a blocking gap exists and no urgency was signaled, the reply is the intake questions only (at most three, each with an example or default).