# Quality control

No gate is skipped. Read this file at the first gate; afterwards reopen the section the moment requires.

## 1. Gate procedure (every phase)

Run these checks, then the phase file's own "Gate checks".
1. Every required decision of the phase is made.
2. The protocol was applied: each Full decision has its record; each compact comparison shows the apparent option, the options, and the decisive criterion.
3. Sources and qualities: every decision names its source (`SKILL.md` section 4); the brief-quality test below passes where the table runs it, at that phase's level of realization; at Phases 1, 2, and 6 the phase file's own quality checks apply.
4. **One substantive objection:** the strongest case against the phase's riskiest decision, raised by the role that owns it (`SKILL.md` section 2), then resolved or accepted with a recorded reason. Riskiest means highest consequence on thinnest evidence: it can be a decision treated as direct or compact, or an interaction or compounding accepted cost between decisions. The objection must add something the protocol's challenge did not: where the riskiest decision already had a protocol challenge, object to an interaction, an unverified assumption, or the next riskiest decision. Full depth: two objections, one per each of the two riskiest decisions. Focused: one.
5. User-facing: Phase 1 closes only on the user's confirmed summary and mode. Guided mode: each message with real work opened with a wait note; entries for Phases 3 to 5 were printed at their gates as one compact table in plain Indonesian (Phase 2's findings lead the Phase 3 entry); the turn stopped for confirmation after Phases 3 and 4. Auto mode: one wait note, nothing printed at gates. Phase 6 is the final reply.
6. The phase's Forward block (decisions as specifications, carry-forward obligations, open flags) and its Record entries are appended to the Design Log. A passing check is logged in one line; failures, fixes, and objections are written out.

**Cross-phase tests.** Each is defined once, here; a phase file names where it runs. Run them at the listed gates and again, scoped to what changed, when a decision changes.

| Test | Question | Runs at | Routes to |
|---|---|---|---|
| Contradiction scan | Do brand design, theme, idea, style, hero, color, type, mark, and composition agree? | 3 (plan stress tests), 4, 5 | the earliest conflicting phase |
| Brief-quality | Does each stated quality have a visible carrier at this phase's level of realization (plan, elements, composed glance stage), and does any decision signal its opposite? | 3, 4, 5 | Phase 1 for the translation, otherwise the earliest contradicting phase |
| Decided-attribute | Is any look-shaping attribute left to the model's apparent value? | 5, 6 | the phase that should own it |
| Originality | The protocol's three tests (predictable, specific, ambitious) | 3, 4, 5 | the deciding phase |

## 2. Composition review

After Phase 5 (checklist in `05_design_execution.md` F), and again, on the checks a Phase 3 to 5 change touches, whenever such a decision changes. A defect found here is traced to the earliest responsible decision (section 4).

## 3. Prompt audit and reply audit

Run on the drafted prompt, then on the reply.

**Prompt audit**
- **Plan fidelity:** every Execution Specification decision is present; nothing new appears; every printed or amended decision is visible and none contradicted.
- **Mandatory content:** every mandatory string present, verbatim, once, with role and position; suspected typos preserved and flagged.
- **Fixed assets:** supplied logos, colors, and fonts reproduced as provided, not redesigned, restyled, simplified, or recolored.
- **Exclusions:** every user exclusion respected; only minimal, specific exclusions added. No invented business facts. No competitor copying.
- **Identifier:** not merely a styled name unless supplied or requested as plain text; a new mark described by form class, geometry, silhouette, color, boundary, personality device, wordmark relationship, separation from adjacent type; the unit described as one object.
- **Order and roles:** the reading order is stated with ranks; type roles are distinguished; overlaps name the front element and the visible part of the covered one.
- **Containers and balance:** every container states form, corner and edge geometry, and fill mode; any counterweight is a concrete form and region; none relies on a default.
- **Space:** outer margin, isolation, and resting fields as concrete positive features, with proportions where they matter. The stated ratio is the design ratio from S, unchanged.
- **Qualities:** every quality requirement shows in the opening lines through named features; the value key is stated; nothing contradicts a quality.
- **Copy and supporters:** designed copy and each supporter described by traits and forms, matching the printed decisions, none outweighing required text.
- **Visual-effect test** on every sentence: would removing it change what is drawn? If not, delete it.
- **Specifics:** depicted things appear by true specifics; no look-shaping attribute left to the model's apparent value.
- **Hygiene:** no rationale, placeholders, or blank zones except a reserved asset panel; no post-generation editing instructions; no blanket emphasis; no crop marks or annotations unless requested; flat artwork unless a mockup was requested; standalone (an illustrator who never saw the brief could produce the design) and readable; one coherent style logic.

**Reply audit:** the reply follows `00_conversation_ux.md` (turn map, entry format, final reply, failure modes): guided mode printed each entry at its gate and waited after Phases 3 and 4; auto mode printed nothing before the final reply; amendments were printed at once; the prompt(s) are alone in code blocks in English; notes follow the disclosure rule (`SKILL.md` section 11) with no design rationale and no repeated summary.

## 4. Triage and routing

| Severity | Definition | Action |
|---|---|---|
| Critical | Violates a non-negotiable; mandatory content missing or altered; fixed asset altered; invented fact; a required decision never made | Stop; return to the responsible phase; re-run forward; release blocked |
| Major | Fails a gate check, a test, or the audit; generic, context-blind, or filled; the mark absorbed by type | Return to the earliest responsible decision; re-run forward |
| Minor | Weak phrasing; a redundant clause; a small imbalance | Fix in place without altering earlier decisions |

| Symptom | Responsible phase |
|---|---|
| Wrong, missing, or altered content; unsourced fact; a quality missing from the ledger | 1 |
| Unsupported narrative; environment-blind profile; weak inventory | 2 |
| Generic idea, style, or hero; no space intent; tension unresolved | 3 |
| Containers that all share the model's default form or only solid-or-outline fills (3 if the plan set no corner and edge geometry); a container with no job; weak or styled-name mark; clashing color or type; ranked text left as scaled plain type; indistinguishable type roles; blank or category-generic piece at its density (3 if no character carriers were planned); value-key drift; plain-set voice copy, or an item Phase 5 promoted to first or second rank with no treatment decision; text-only look; decoration with no deficit; duplicate jobs; decoration outranking information; a second identifier; an unwanted, roleless, or inconsistent figure; an invented level mark; element costs over the space intent | 4 (3 if the plan caused it) |
| Competing elements or unclear first read; every tier enlarged in a large format; overlap hiding an essential part; unlinked elements; lopsided mass (4 if no counterweight was provided); poor hierarchy; wrong viewing stage; crowding or filling; mark absorbed in composition; text overflowing its container or sizes changed late; bleed against content; a pointer with no referent; a figure covering information; picture-with-captions | 5 |
| Rationale in the prompt; vague wording; mandatory text misplaced; space not stated | 6 |
| A stated quality contradicted by a decision | The earliest contradicting phase |
| A carry-forward obligation realized by no element, placement, or accepted-cost record | The phase that should have realized it |

When several causes are possible choose the earliest; fixing a symptom later while its cause stands is a patch and is not permitted. Cap each issue at two revision cycles, then take the best available resolution and record it; an issue recurring after two cycles has an upstream cause. A returned phase keeps all unaffected decisions; record changes in the log. After any change, re-run the contradiction scan and the checks the change touches, and confirm no earlier text still states the old decision (nothing stale).

## 5. Release checklist

Gates and audits cover the detail; before delivering confirm:
1. Phases 1 to 6 ran in order and every gate passed; every gate has its log line; the pre-synthesis check (`SKILL.md` section 9) is complete and every consequential decision has its record (or is marked fixed by the user or evidence).
2. The prompt audit and reply audit passed; printed decisions match the prompt (amendments where they changed).
3. The Phase 1 summary and mode were confirmed and guided-mode go-aheads obtained.
4. Disclosure is complete: every consequential assumption, yielded preference, written copy, suspected typo, supplied asset, reserved asset panel, and volume or rendering risk reached the user once, with no design rationale.
5. If a blocking gap exists and no urgency was signaled, the reply is the intake questions only.