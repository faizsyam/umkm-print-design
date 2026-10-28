# Quality control

No gate is skipped. Read this file at the first gate; afterwards reopen the section the moment requires.

## 1. Gate procedure (every phase)

Run these checks, then the phase file's own "Gate checks".
1. Every required decision of the phase is made.
2. The protocol was applied: each Full decision has its record; each compact comparison shows the apparent option, the options, and the decisive criterion.
3. Sources and qualities: every decision names its source (`SKILL.md` section 4); every quality requirement has a visible carrier at this phase and no decision signals its opposite.
4. **One substantive objection:** the strongest case against the phase's riskiest decision, raised by the role that owns it (`SKILL.md` section 2), then resolved or accepted with a recorded reason. Full depth: two objections, one per each of the two riskiest decisions. Focused: one.
5. User-facing: Phase 1 closes only on the user's confirmed summary and mode. Guided mode: each message with real work opened with a wait note; entries for Phases 3 to 5 were printed at their gates as one compact table in plain Indonesian (Phase 2's findings lead the Phase 3 entry); the turn stopped for confirmation after Phases 3 and 4. Auto mode: one wait note, nothing printed at gates. Phase 6 is the final reply.
6. The phase's hand-off block is appended to the Design Log.

**Cross-phase tests** (run at the gate that names them, or when a decision changes):
- *Contradiction scan:* do brand design, theme, idea, style, hero, color, type, mark, and composition agree? Route to the earliest conflicting phase.
- *Brief-quality:* does each stated quality have a visible carrier at the glance stage, and does any decision signal its opposite? Route to Phase 1 for the translation, otherwise to the earliest contradicting phase.
- *Decided-attribute:* is any look-shaping attribute left to the model's apparent value? Route to the phase that should own it.
- *Originality:* the protocol's three tests (predictable, specific, ambitious) at Phases 3 to 5.

## 2. Composition review

After Phase 5 (checklist in `05_design_execution.md` F), and again whenever a Phase 3 to 5 decision changes. A defect found here is traced to the earliest responsible decision (section 4).

## 3. Prompt audit and reply audit

Run on the drafted prompt, then on the reply.

**Prompt audit**
- **Plan fidelity:** every Execution Specification decision is present; nothing new appears; every printed or amended decision is visible and none contradicted.
- **Mandatory content:** every mandatory string present, verbatim, once, with role and position; suspected typos preserved and flagged.
- **Fixed assets:** supplied logos, colors, and fonts reproduced as provided, not redesigned, restyled, simplified, or recolored.
- **Exclusions:** every user exclusion respected; only minimal, specific exclusions added. No invented business facts. No competitor copying.
- **Identifier:** not merely a styled name unless supplied or requested as plain text; a new mark described by form class, geometry, silhouette, color, boundary, personality device, wordmark relationship, separation from adjacent type; the unit described as one object.
- **Order and roles:** the reading order is stated with ranks; type roles are distinguished; overlaps name the front element and the visible part of the covered one.
- **Space:** outer margin, isolation, and resting fields as concrete positive features, with proportions where they matter.
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
| Weak or styled-name mark; clashing color or type; ranked text left as scaled plain type; indistinguishable type roles; blank or category-generic piece at its density (3 if no character carriers were planned); value-key drift; plain-set voice copy; text-only look; decoration with no deficit; duplicate jobs; decoration outranking information; a second identifier; an unwanted, roleless, or inconsistent figure; an invented level mark; element costs over the space intent | 4 (3 if the plan caused it) |
| Competing elements or unclear first read; every tier enlarged in a large format; overlap hiding an essential part; unlinked elements; poor hierarchy; wrong viewing stage; crowding or filling; mark absorbed in composition; text overflowing its container or sizes changed late; bleed against content; a pointer with no referent; a figure covering information; picture-with-captions | 5 |
| Rationale in the prompt; vague wording; mandatory text misplaced; space not stated | 6 |
| A stated quality contradicted by a decision | The earliest contradicting phase |

When several causes are possible choose the earliest; fixing a symptom later while its cause stands is a patch and is not permitted. Cap each issue at two revision cycles, then take the best available resolution and record it; an issue recurring after two cycles has an upstream cause. A returned phase keeps all unaffected decisions; record changes in the log. Re-review the whole design after any change for consistency and nothing stale.

## 5. Release checklist

Gates and audits cover the detail; before delivering confirm:
1. Phases 1 to 6 ran in order and every gate passed; the "Ready for Phase 6" commitments are complete and every consequential decision has its record (or is marked fixed by the user or evidence).
2. The prompt audit and reply audit passed; printed decisions match the prompt (amendments where they changed).
3. The Phase 1 summary and mode were confirmed and guided-mode go-aheads obtained.
4. Disclosure is complete: every consequential assumption, yielded preference, written copy, suspected typo, supplied asset, reserved asset panel, volume risk, and ratio limit reached the user once, with no design rationale.
5. If a blocking gap exists and no urgency was signaled, the reply is the intake questions only.