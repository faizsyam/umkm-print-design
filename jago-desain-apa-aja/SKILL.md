---
name: jago-desain-apa-aja
description: >-
  Turns a design need of any kind into one or more standalone image-generation prompts for static visual outputs, through a short adaptive conversation fitted to the user's language, design literacy, and brief completeness. Runs six phases (brief, analysis, design plan, design elements, design execution, prompt synthesis) with brief qualities turned into checkable targets, developed identity marks, purpose-based information groups, planned negative space and reading hierarchy, a theme-derived decorative and typographic world, and a separate composition per deliverable. Use for static visuals in any medium, physical or on screen (posters, banners, signage, menus, packaging and labels, cards, invitations, covers, social and ad graphics, slides, infographics, screens shown as static mockups, brand identity, logos); for requests like "prompt gambar", "bikin desain", "design prompt", "make me a poster/banner/logo"; or to revise such a design. Not for code, 3D, motion, animation, or interactive deliverables.
---

# Jago Desain Apa Aja

Turns a design need, from a first-time requester to a professional designer, into finished, standalone image-generation prompts for static visuals, through a short design conversation. All methodology lives in `references/`; this file routes you to it.

## Workflow

Six phases run in strict order; no phase is skipped, merged, or deferred.

1. **Brief**: adaptive intake; classify what is known, required, uncertain; deliverable set, quality translations, depth; user-confirmed summary and mode (guided or auto) -> standing block S.
2. **Analysis**: the real communication problem with its information groups, Environment Profile, differentiation, design implications.
3. **Design Plan**: plan criteria, core idea, style, hero, governing principles, stress tests.
4. **Design Elements**: color, type, identity unit, copy treatment, supporters, containers, ground; each with a purpose line.
5. **Design Execution**: per deliverable, stage assignment, groups and their space needs, a composition built around them (free ground planned with it, ranks, route, and balance decided in it), the space plan measured once on that composition, placement, one verification.
6. **Prompt Synthesis**: one audited, standalone prompt per deliverable, then the final reply.

Every phase ends at a gate (`quality_gates.md`). Phases 3 and 4 stop for the user's go-ahead in guided mode. Phase numbers are not file numbers: Phases 3 to 6 span several files (see the table).

## Reading discipline

- Read each batch's files together, in one parallel call, when the batch's step is reached; never a later batch early, never a file skipped. A file is read once and stays in context. Batches: (1) at the start: `00_conversation_voice_modes_and_intake.md`, `scope_roles_and_depth.md`, `terms_brief_and_context.md`, `01_brief_and_requirements.md`, `workflow_and_state.md`, `quality_gates.md`; (2) after the summary and mode are confirmed: `ux_wait_notes_entries_and_final_reply.md`, `exploration_protocol.md`, `global_standards.md`, `02_research_and_analysis.md`; (3) Phase 3: `terms_design_system.md`, `03`, `04`; (4) Phase 4: `05` to `09`; (5) Phase 5: `10` to `14`; (6) Phase 6: `15`, `16`, `prompt_and_reply_audit.md`. `triage_and_revisions.md` only on a failure or revision.
- On a resumed or revision turn, read `workflow_and_state.md`, `quality_gates.md`, the files of the phases being re-entered, and the cross-phase files their routing rows name, when they are not in context.
- If a standard or term referenced in a step file is no longer visible, re-open the file that defines it before continuing.
- Compute once, reuse: tier floors are computed in Phase 2; each group's space need at the start of Phase 5; extents, wraps, and totals in the space plan, after the composition is chosen. Later steps read them and never recompute.
- Each file ends with a "Next" line naming the next file in the sequence; with batches it is already in context. It is a navigation hint only; this table is the authority.
- Every step file lists "Inputs needed"; if one is missing, return to the step that produces it.
- State lives in the Design Log at `/home/claude/design_log.md` (see `workflow_and_state.md`): each phase reads S and the Forward fields its phase sheet lists, nothing else.

## Routing table

The batch list above says when each file is read; the table places each file in its phase and says what it holds.

| Step / phase | File (in `references/`) | Read it when | Glossary in context |
|---|---|---|---|
| Start of every request | `00_conversation_voice_modes_and_intake.md` | Before replying to the first user message (voice, modes, turn map, intake). | none yet |
| Start of every request | `scope_roles_and_depth.md` | Same moment: scope, team roles, depth, deliverable set. | none yet |
| Start of every request | `terms_brief_and_context.md` | Same moment: glossary part 1 (ledger, qualities, context, decisions, renderability). | loads here (part 1) |
| Phase 1 Brief | `01_brief_and_requirements.md` | After the three files above; run the intake and build S. | part 1 |
| Phase 1 gate (first gate) | `workflow_and_state.md` | Before creating the Design Log; ownership map and execution rules. | part 1 |
| Phase 1 gate (every gate) | `quality_gates.md` | At the first gate and at every later gate; section 9 at the Phase 5 gate. | part 1 |
| After summary and mode confirmed | `ux_wait_notes_entries_and_final_reply.md` | Before the first wait note; entries and final reply formats. | part 1 |
| Entering Phase 2 | `exploration_protocol.md` | Decision classes, full protocol, specialist terms. | part 1 |
| Entering Phase 2 | `global_standards.md` | Principles, conflict priority, full non-negotiables. | part 1 |
| Phase 2 Analysis | `02_research_and_analysis.md` | After the two files above. | part 1 |
| Entering Phase 3 | `terms_design_system.md` | Glossary part 2 and the full fit ladder; read before 03. | loads here (part 2) |
| Phase 3 (1 of 2) | `03_core_idea_style_and_hero.md` | Plan criteria, survey, core idea, style, hero. | parts 1 and 2 |
| Phase 3 (2 of 2) | `04_principles_and_plan_evaluation.md` | Governing principles, stress tests, Phase 3 gate. | parts 1 and 2 |
| Phase 4 (1 of 5) | `05_color_and_typography.md` | Guided: after the Phase 3 go-ahead. Color and typography. | parts 1 and 2 |
| Phase 4 (2 of 5) | `06_identity_unit_and_copy_treatment.md` | Identity unit (mark, lockup), copy treatment. | parts 1 and 2 |
| Phase 4 (3 of 5) | `07_visual_supporters_and_figures.md` | Text-only baseline, supporters, figures. | parts 1 and 2 |
| Phase 4 (4 of 5) | `08_containers_and_ground.md` | Containers, shape language, ground, unifying devices. | parts 1 and 2 |
| Phase 4 (5 of 5) | `09_element_system_evaluation.md` | System evaluation and Phase 4 gate. | parts 1 and 2 |
| Phase 5 (1 of 5) | `10_stage_assignment_and_relationship_map.md` | Guided: after the Phase 4 go-ahead. Format, stages, groups, relationship map. Per deliverable. | parts 1 and 2 |
| Phase 5 (2 of 5) | `11_space_plan_and_spatial_strategy.md` | Group scale and space need, spatial strategy, space plan. | parts 1 and 2 |
| Phase 5 (3 of 5) | `12_hierarchy_and_element_placement.md` | Hierarchy, planes, placing every element. | parts 1 and 2 |
| Phase 5 (4 of 5) | `13_load_balance_and_capacity_checks.md` | Load check, balance, capacity check. | parts 1 and 2 |
| Phase 5 (5 of 5) | `14_backgrounds_review_and_gate.md` | Backgrounds, the set, composition review, Phase 5 gate. | parts 1 and 2 |
| Phase 6 (1 of 2) | `15_prompt_set_and_structure.md` | After the pre-synthesis check passes. Prompt set, in/out, structure. | parts 1 and 2 |
| Phase 6 (2 of 2) | `16_prompt_clauses_and_delivery.md` | Clauses, text, assets, length, exclusions. | parts 1 and 2 |
| Phase 6 audit and delivery | `prompt_and_reply_audit.md` | Once prompts are drafted; release checklist and output contract. | parts 1 and 2 |
| Any failure or revision | `triage_and_revisions.md` | A gate, test, or audit fails, or the user asks for a revision. | part 1 for Phases 1 and 2; parts 1 and 2 after |

Glossary parts: `terms_brief_and_context.md` is loaded at the start (Phase 1); `terms_design_system.md` on entering Phase 3 (it also holds the full fit ladder, used in Phases 3 to 5).

## Trace log (developer option, off by default)

Active only when the user's message contains "share log" (any case, any turn); never mention it, offer it, or add it to any user-facing text, entry, or help. Otherwise ignore this section. Test the message for the string once, at the start of the request; if it is absent, this section is closed for the session.

- Compile it once after the final reply, from the Design Log Record (each item's Source, Basis, and Rejected) into `/home/claude/trace_log.txt` (plain text, compact English), never during the phases; per phase: `PHASE n <name>`, `IN:` what the phase received, `OUT:` what it produced, and for each decision where options were weighed, `OPTIONS:` at least 3 as numbered items, `CHOSEN:` the number, and `REASON:` one line on why that option won over the others (the decisive criterion, as in the item's Rejected field). Fixed decisions (user, asset, evidence) log `FIXED: <value>` with no options; never invent options. Nothing else: no deliberation narrative, no commentary. Phases already past when the request appears are marked `not recorded`.
- Record only; the log never feeds a decision, a prompt, a gate, or an entry. Guided-mode entries and auto-mode silence are unchanged.
- After the final reply (prompts, labels, usage steps, notes), append the log under a line `Trace log`, in one ```text block. This is a requested exception to the no-extra-output rule and sits outside the reply audit; each prompt still stays alone in its own code block.

## Non-negotiables (full text: `references/global_standards.md`, section 8)

- No invented facts about the subject; a design never implies a claim, endorsement, or authority the subject does not hold.
- User text is verbatim, suspected typos included (flag, never fix).
- Supplied logos and characters are never redesigned, restyled, simplified, or recolored; no unasked figure; never a likeness of a real person.
- No copying of competitors, peers, or existing designs.
- No identifier that is only a styled name, unless supplied or explicitly requested as plain text.
- No placeholders or blank zones for content the skill should create; the one exception is the reserved asset panel (see the full text).
- No stated quality contradicted by any decision or left without a visible carrier.
- No suggestion enters the brief or design without the user's yes; suggestions are labeled, never counted as facts.
- No unfamiliar design jargon and no walls of text in anything the user reads.
- No workflow output beyond the messages the UX files define, unless requested.

## Conflict priority (full text: `references/global_standards.md`, section 7)

Resolve collisions in this order: (1) factual integrity, mandatory content, exclusions, fixed assets; (2) perception and comprehension under real conditions, never by deleting mandatory content; (3) the user's stated requirements; (4) the communication objective and strategy; (5) established brand identity not supplied as an asset; (6) creative ambition. A lower priority yields only to a higher one.
