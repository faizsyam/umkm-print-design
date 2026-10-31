# Quality control

No gate is skipped. Read this file at the first gate; afterwards reopen the section the moment requires.

## 1. Gate procedure (every phase)

Run these checks, then the phase file's own "Gate checks".
1. Every required decision of the phase is made.
2. The protocol was applied: each Full decision has its record; each compact comparison shows the apparent option, the options, and the decisive criterion.
3. Sources and qualities: every decision names its source (`SKILL.md` section 4). The brief-quality test below passes where the table runs it, at that phase's level of realization. At Phases 1, 2, and 6 the phase file's own quality checks apply.
4. **One substantive objection:** the strongest case against the phase's riskiest decision, raised by the role that owns it (`SKILL.md` section 2), then resolved or accepted with a recorded reason.
   - Riskiest means highest consequence on thinnest evidence. It can be a decision treated as direct or compact, or an interaction or compounding accepted cost between decisions.
   - The objection must add something the protocol's challenge did not. Where the riskiest decision already had a protocol challenge, object to an interaction, an unverified assumption, or the next riskiest decision.
   - Full depth: two objections, one for each of the two riskiest decisions. Focused: one.
5. User-facing:
   - Phase 1 closes only on the user's confirmed summary and mode.
   - Guided mode: each message with real work opened with a wait note; entries for Phases 3 to 5 were shown at their gates as one compact table in the user's language (Phase 2's findings lead the Phase 3 entry); the turn stopped for confirmation after Phases 3 and 4.
   - Auto mode: one wait note, nothing shown at gates.
   - Phase 6 is the final reply.
6. The phase's Forward block (decisions as specifications, carry-forward obligations, open flags) and its Record entries are appended to the Design Log. A passing check is logged in one line; failures, fixes, and objections are written out.

**Cross-phase tests.** Each is defined once, here; a phase file names where it runs. Run them at the listed gates and again, scoped to what changed, when a decision changes.

| Test | Question | Runs at | Routes to |
|---|---|---|---|
| Contradiction scan | Do brand design, theme, idea, style, hero, color, type, mark, and composition agree? Across the set: are shared decisions identical in every deliverable, with composition differences explained by format or encounter? | 3 (plan stress tests), 4, 5 | the earliest conflicting phase |
| Brief-quality | Does each stated quality have a visible carrier at this phase's level of realization (plan, elements, composed glance stage), and does any decision signal its opposite? | 3, 4, 5 | Phase 1 for the translation, otherwise the earliest contradicting phase |
| Decided-attribute | Is any look-shaping attribute left to the model's apparent value? | 5, 6 | the phase that should own it |
| Originality | The protocol's three tests (predictable, specific, ambitious) | 3, 4, 5 | the deciding phase |

## 2. Composition review

Run after Phase 5 (checklist in `05_design_execution.md` F), and again, on the checks a Phase 3 to 5 change touches, whenever such a decision changes. A defect found here is traced to the earliest responsible decision (section 4).

## 3. Prompt audit and reply audit

Run on the drafted prompt, then on the reply.

**Prompt audit**
- **Plan fidelity:** every Execution Specification decision is present; nothing new appears; every shown or amended decision is visible and none is contradicted.
- **Mandatory content:** every mandatory string is present, verbatim, once, with role and position; suspected typos are preserved and flagged.
- **Fixed assets:** supplied logos, colors, and fonts are reproduced as provided, not redesigned, restyled, simplified, or recolored.
- **Exclusions:** every user exclusion is respected; only minimal, specific exclusions are added. No invented facts about the subject. No competitor copying.
- **Identifier:** not merely a styled name unless supplied or requested as plain text. A new mark is described by form class, geometry, silhouette, color, boundary, personality device, wordmark relationship, and separation from adjacent type; the unit is described as one object.
- **Order and roles:** the reading order is stated with ranks; type roles are distinguished; overlaps name the front element and the visible part of the covered one.
- **Containers and balance:** every container states form, corner and edge geometry, and fill mode; any counterweight is a concrete form and region; none relies on a default.
- **Space:**
  - The open regions are named by what they separate or frame, with their rough share and the overall density in plain words, placed ahead of element detail and consistent with every element clause (no wording that fills, spans, covers, or packs a zone; detail per element proportional to its rank).
  - Outer margin, separation between zones, isolation, internal zone spacing, and resting fields appear as concrete positive features, with proportions where they matter.
  - Each prompt states its own deliverable's ratio from S, unchanged.
- **Qualities:** every quality requirement shows in the opening lines through named features; the value key is stated; nothing contradicts a quality.
- **Copy and supporters:** designed copy and each supporter are described by traits and forms, match the shown decisions, and none outweighs required text.
- **Visual-effect and misread tests** on every sentence: would removing it change what is drawn (if not, delete it)? What is its likeliest wrong rendering (if that breaks the design, rewrite until the likeliest reading is the intended one)?
- **Standalone:** each prompt is complete by itself (shared decisions restated in identical wording; no reference to another prompt, an earlier generation, or the brief), and the prompt count matches the deliverable set.
- **Specifics:** depicted things appear by true specifics, in the decided illustration or photographic language; no look-shaping attribute is left to the model's apparent value.
- **Hygiene:** no rationale, placeholders, or blank zones except a reserved asset panel; no post-generation editing instructions; no blanket emphasis; no crop marks or annotations unless requested; static artwork as seen unless a scene or mockup is the deliverable; readable by an illustrator who never saw the brief; one coherent style logic.

**Reply audit**
- Each prompt has its label, and the usage steps state any needed attachment or order.
- The reply follows `00_conversation_ux.md` (turn map, entry format, final reply, failure modes).
  - Guided mode showed each entry at its gate and waited after Phases 3 and 4.
  - Auto mode showed nothing before the final reply.
  - Amendments were shown at once.
- The prompt(s) are alone in code blocks, in English.
- Notes follow the disclosure rule (`SKILL.md` section 11), with no design rationale and no repeated summary.

## 4. Triage and routing

| Severity | Definition | Action |
|---|---|---|
| Critical | Violates a non-negotiable; mandatory content missing or altered; fixed asset altered; invented fact; a required decision never made | Stop; return to the responsible phase; re-run forward; release blocked |
| Major | Fails a gate check, a test, or the audit; generic, context-blind, or filled; the mark absorbed by type | Return to the earliest responsible decision; re-run forward |
| Minor | Weak phrasing; a redundant clause; a small imbalance | Fix in place without altering earlier decisions |

**Symptoms by responsible phase**

- **Phase 1:**
  - wrong, missing, or altered content; unsourced fact;
  - a quality missing from the ledger;
  - a deliverable or format missing, wrong, or needlessly split.
- **Phase 2:**
  - unsupported narrative;
  - environment-blind profile;
  - a medium convention applied by default;
  - weak inventory.
- **Phase 3:**
  - generic idea, style, or hero (an image-making language that is only a medium name included);
  - a hero left standalone with no stated reason;
  - no space intent;
  - tension unresolved.
- **Phase 4** (Phase 3 if the plan caused it):
  - containers that all share the model's default form or only solid-or-outline fills, or one container design across different information roles or ranks (Phase 3 if the plan set no corner and edge geometry);
  - an element or container with no purpose line;
  - weak or styled-name mark; clashing color or type; value-key drift;
  - ranked text left as scaled plain type; plain-set voice copy; an item Phase 5 promoted to first or second rank with no treatment decision;
  - indistinguishable type roles or undecided letterform proportions;
  - blank or category-generic piece at its density (Phase 3 if no character carriers were planned);
  - text-only look; a ground left uniform without a reason;
  - decoration with no deficit; duplicate purposes; decoration outranking information;
  - a second identifier; an unwanted, roleless, or inconsistent figure; an invented level mark;
  - element costs over the space intent.
- **Phase 5:**
  - hierarchy: competing elements or unclear first read; poor hierarchy; an element whose recorded effect does not register at its stage; a zone's area share or a secondary or utility text mass outranking its rank;
  - scale and space: every tier enlarged in a large format; crowding or filling; a zone crowded at its own scale; cumulative visual load beyond what the space plan carries;
  - composition: overlap hiding an essential part; unlinked elements; lopsided mass (Phase 4 if no counterweight was provided); wrong encounter stage; mark absorbed in composition; a deliverable composed by resizing or cropping another's layout;
  - text fit: text overflowing its container, sizes changed late, or letters compressed, stretched, or slanted to fit; equivalent items typeset differently by length;
  - grouping and arrangement: picture-with-captions; parallel claims merged into one strip without being one claim; one arrangement form repeated across groups of different function, or a long or comparable-item list left as one stacked column without a reason;
  - edges and references: bleed against content; a pointer with no referent; a figure covering information.
- **Phase 6:**
  - rationale in the prompt; vague wording; mandatory text misplaced;
  - space, proportions, or ground character not stated;
  - a prompt that depends on another prompt, omits shared identity, or lacks its label.
- **The earliest contradicting phase:** a stated quality contradicted by a decision.
- **The phase that should have realized it:** a carry-forward obligation realized by no element, placement, or accepted-cost record.

**Routing rules**
- When several causes are possible, choose the earliest. Fixing a symptom later while its cause stands is a patch and is not permitted.
- Cap each issue at two revision cycles, then take the best available resolution and record it. An issue recurring after two cycles has an upstream cause.
- A returned phase keeps all unaffected decisions; record changes in the log.
- After any change, re-run the contradiction scan and the checks the change touches, and confirm no earlier text still states the old decision (nothing stale).

## 5. Release checklist

Gates and audits cover the detail. Before delivering, confirm:
1. Phases 1 to 6 ran in order and every gate passed; every gate has its log line; the pre-synthesis check (`SKILL.md` section 9) is complete; every consequential decision has its record (or is marked fixed by the user or evidence).
2. The prompt audit passed for every prompt and the reply audit passed; shown decisions match the prompt (amendments where they changed).
3. The Phase 1 summary and mode were confirmed, and guided-mode go-aheads obtained.
4. Disclosure is complete: every consequential assumption, yielded preference, written copy, suspected typo, supplied asset, reserved asset panel, and volume or rendering risk reached the user once, with no design rationale.
5. If a blocking gap exists and no urgency was signaled, the reply is the intake questions only.