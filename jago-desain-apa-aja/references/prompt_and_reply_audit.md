# Prompt audit, reply audit, release checklist, and output contract (Phase 6)

The audit every prompt and the final reply must pass, the checklist confirmed before delivery, and the output contract for what the user receives.

**Read this when:** in Phase 6, once the prompts are drafted (step 5 of `15_prompt_set_and_structure.md`), and again before delivering a revision.

**Inputs needed:** The drafted prompts, S, the Execution Specifications, and the guided/auto record of what was shown to the user.

## 3. Prompt audit and reply audit

Run on the drafted prompt, then on the reply.

**Prompt audit**
- **Plan fidelity:** every Execution Specification decision is present; nothing new appears; every shown or amended decision is visible and none is contradicted.
- **Mandatory content:** every mandatory string is present, verbatim, once, with role and position; suspected typos are preserved and flagged.
- **Fixed assets:** supplied logos, colors, and fonts are reproduced as provided, not redesigned, restyled, simplified, or recolored.
- **Exclusions:** every user exclusion is respected; only minimal, specific exclusions are added. No invented facts about the subject. No competitor copying.
- **Identifier:** not merely a styled name unless supplied or requested as plain text. A new mark is described by form class, geometry, silhouette, color, boundary, personality device, wordmark relationship, and separation from adjacent type; the unit is described as one object. The name's exact letters are stated and every letter stays fully formed and readable.
- **Order and roles:** the hierarchy is stated with ranks and the reading route agrees with every position clause; type roles are distinguished; overlaps name the front element and the visible part of the covered one.
- **Containers and balance:** every container states form, corner and edge geometry, material impression, layering where it overlaps, and fill mode (open grouping is stated as such); any counterweight is a concrete form and region; none relies on a default.
- **Space:**
  - The open regions are named by what they separate or frame, with their rough share and the overall density in plain words, placed ahead of element detail and consistent with every element clause (no wording that fills, spans, covers, or packs a zone; detail per element proportional to its rank).
  - Outer margin, separation between zones, isolation, internal zone spacing, and resting fields appear as concrete positive features, with proportions where they matter; each group and container carries its share of the governing dimension, and text roles carry their proportions of the format.
  - Quiet regions are described as plain, undecorated ground, and any atmosphere fields as decorated fields apart from them; the quantity of every repeated or decorative form is stated; equivalent units are described with identical dimensions, internal structure, and field alignment; each zone's own breathing room is stated, not only the margin.
  - Each prompt states its own deliverable's ratio from S, unchanged.
- **Qualities:** every quality requirement shows in the opening lines through named features; the value key is stated; nothing contradicts a quality.
- **Copy and supporters:** designed copy and each supporter are described by traits and forms, match the shown decisions, and none outweighs required text; no symbol repeats the words beside it; type roles state spacing and alignment as decided.
- **Visual-effect and misread tests** on every sentence: would removing it change what is drawn (if not, delete it)? What is its likeliest wrong rendering (if that breaks the design, rewrite until the likeliest reading is the intended one)?
- **Standalone:** each prompt is complete by itself (shared decisions restated in identical wording; no reference to another prompt, an earlier generation, or the brief), and the prompt count matches the deliverable set.
- **Specifics:** depicted things appear by true specifics, in the decided illustration or photographic language; no look-shaping attribute is left to the model's apparent value.
- **Hygiene:** no rationale, no partition words (zone, section, panel, band) unless the design contains that form, placeholders, or blank zones except a reserved asset panel; no post-generation editing instructions; no blanket emphasis; no crop marks or annotations unless requested; static artwork as seen unless a scene or mockup is the deliverable; readable by an illustrator who never saw the brief; one coherent style logic.

**Reply audit**
- Each prompt has its label, and the usage steps state any needed attachment or order.
- The reply follows `00_conversation_voice_modes_and_intake.md` (turn map) and `ux_wait_notes_entries_and_final_reply.md` (entry format, final reply, failure modes).
  - Guided mode showed each entry at its gate and waited after Phases 3 and 4.
  - Auto mode showed nothing before the final reply.
  - Amendments were shown at once.
- The prompt(s) are alone in code blocks, in English.
  - Decisions fixed by the user, a supplied asset, or evidence are listed as fixed; no alternative was invented.
  - No suggestion appears as a decision without the user's yes; no internal term appears in user-facing text outside the plain-word glossary.
- Notes follow the disclosure rule (`prompt_and_reply_audit.md` section 11), with no design rationale and no repeated summary.

## 5. Release checklist

Gates and audits cover the detail: their log lines, the confirmed summary, and the go-aheads are the evidence for the phases, gates, audits, and confirmations, and are read, not re-run. Before delivering, confirm only:
1. every gate has its log line, the pre-synthesis check (`quality_gates.md` section 9) is complete, and the prompt and reply audits passed with shown decisions matching the prompts (amendments where they changed);
2. disclosure is complete: every consequential assumption, yielded preference, written copy, suspected typo, supplied asset, reserved asset panel, and volume or rendering risk reached the user once, with no design rationale;
3. if a blocking gap exists and no urgency was signaled, the reply is the intake questions only.

## 11. Output contract

- **No invented alternatives.** Decisions fixed by the user, a supplied asset, or evidence are listed as fixed; alternatives are never invented.
- **Amendments** (guided mode; auto mode shows no decisions). If a later return changes a shown decision, say so at once in one plain line: what changed to what, and why. The audit checks that every shown or amended decision is visible in the prompts and none is contradicted.
- **Final reply** (layout: `ux_wait_notes_entries_and_final_reply.md` section 6). The prompt set plus whatever the user must still know, once.
  - Each prompt carries a label line stating its purpose and its place in the whole request.
  - Usage steps are brief and state any attachment, order, or dependency that applies.
  - Notes carry suspected typos, copy the skill wrote, supplied assets to attach, a reserved asset panel, and any volume or rendering risk (`terms_brief_and_context.md`, Reliability and risk). Never design rationale or repeated tables.
  - Assumptions and yielded preferences are disclosed in the summary and entries (auto mode: the key decisions).
- **Each prompt**, built per `15_prompt_set_and_structure.md` and `16_prompt_clauses_and_delivery.md`, and audited per section 3 of this file:
  - self-contained, executable without any other prompt, generation, or the brief;
  - English by default (`15_prompt_set_and_structure.md`, G), with on-image text verbatim in its original language;
  - alone in its code block;
  - carrying every shown or amended decision and all mandatory content for its deliverable.

## Quality checks

- Pass: every item of section 3 holds for every prompt and the reply, and the three items of section 5 are confirmed.

## Next

Deliver the final reply per `ux_wait_notes_entries_and_final_reply.md` section 6. On any audit failure read `triage_and_revisions.md` and return to the earliest cause.
