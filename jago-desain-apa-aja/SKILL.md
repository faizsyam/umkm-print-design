---
name: jago-desain-apa-aja
description: >-
  Turns a design need of any kind into one or more standalone image-generation prompts for static visual outputs, through a short adaptive conversation fitted to the user's language, design literacy, and brief completeness. Runs six phases (brief, analysis, design plan, design elements, design execution, prompt synthesis) with brief qualities turned into checkable targets, developed identity marks, purpose-based information groups, planned negative space and reading hierarchy, a theme-derived decorative and typographic world, and a separate composition per deliverable. Use for static visuals in any medium, physical or on screen (posters, banners, signage, menus, packaging and labels, cards, invitations, covers, social and ad graphics, slides, infographics, screens shown as static mockups, brand identity, logos); for requests like "prompt gambar", "bikin desain", "design prompt", "make me a poster/banner/logo"; or to revise such a design. Not for code, 3D, motion, animation, or interactive deliverables.
---

# Jago Desain Apa Aja

Turns a design need, from a first-time requester to a professional designer, into finished, standalone image-generation prompts for static visuals, through a short design conversation. This file is the runbook; `references/` holds the methods it loads on demand.

## Runbook

Six phases run in order; none is skipped, merged, or deferred. Each phase: read its batch once, make its decisions by class, append them to the Design Log, pass its hand-off check.

1. **Brief**: adaptive intake; known, required, uncertain; deliverable set, quality translations, openness map; user-confirmed summary and mode (guided or auto) -> standing block S.
2. **Analysis**: the real communication problem, information groups and load table, Environment Profile with role floors, differentiation, design implications.
3. **Design Plan**: plan criteria, core idea, style, hero, governing principles, one direction check.
4. **Design System**: color, type, shape and container language, supporter policy, and ground as one system decision; a new mark or lead figure by the direction protocol.
5. **Design Execution**: per deliverable, stages and groups; a composition built around the groups and kept as a region table; the space plan measured once; placement; one assembled review.
6. **Prompt Synthesis**: each decision's prompt-ready specification assembled into one audited, standalone prompt per deliverable; the final reply.

Guided mode stops for the user's go-ahead after Phases 3 and 4; Phase 5's entry is shown and Phase 6 follows. Auto mode shows nothing at gates.

## Decisions (`references/exploration_protocol.md`)

- **Direction** (core idea, style, hero, a new mark or lead figure, spatial strategy) is explored, sized by how much the brief leaves open: Open, Steered, or Fixed. Fixed takes no exploration.
- **System** (palette, type roles, shape and container language, supporter policy, ground) is derived from the direction in one comparison.
- **Execution** (copy treatments, line breaks, non-mandatory wording, small items, icons, edge details) is specified directly while drafting the prompt: no log item, no comparison.
- **Escalation**: a System or Execution choice with a named risk gets its own compact comparison.
- A decision is closed when its decisive criterion is stated and no recorded check fails it; it reopens only by naming a failed check. What an earlier decision fixes is inherited, not decided again.

## One working file

The Design Log (`/home/claude/design_log.md`; `references/workflow_and_state.md`) holds S (the standing block) and D (the decisions). Each phase appends its decisions to D, each Specification written in prompt-ready wording (traits as seen, no rationale) with dimensions as shares of the format. Phase 6 assembles and audits them; nothing is written twice.

## Checks

One hand-off check per phase: every decision made by its class; sources named and each quality carried at this phase's level; the phase's decisions consistent with those it reads; the user-facing steps of the mode done; D appended (failure routes and the full wording: `references/quality_gates.md` section 1); one assembled review with the cross-phase tests and one objection at the end of Phase 5 (section 2, with `14_backgrounds_review_and_gate.md` F); one prompt audit in Phase 6. A check that passed is re-run only when a decision it reads changed. Cap each issue and every loop at two cycles.

## Research

A question, not a phase: only for a question that names a Direction decision it could change and that the brief and knowledge cannot answer; at most three targeted queries and one page read per question, stopping at the first sufficient answer; no trend surveys.

## Loading

Open only the current batch, all its files in one call, when its step is reached. Never preload a later batch, never reopen a file already in context, never skip a file. All files are in `references/`.

1. **Start:** `00_conversation_voice_modes_and_intake.md`, `scope_roles_and_depth.md`, `terms_brief_and_context.md`, `01_brief_and_requirements.md`.
2. **After the summary and mode are confirmed:** `ux_wait_notes_entries_and_final_reply.md`, `exploration_protocol.md`, `02_research_and_analysis.md`, `workflow_and_state.md`.
3. **Phase 3:** `terms_design_system.md`, `global_standards.md`, `03_core_idea_style_and_hero.md`, `04_principles_and_plan_evaluation.md`.
4. **Phase 4:** `05`, `06`, `08`, `09` (`05_color_and_typography.md`, `06_identity_unit_and_copy_treatment.md`, `08_containers_and_ground.md`, `09_element_system_evaluation.md`); `07_visual_supporters_and_figures.md` unless the brief fixes a plain, text-only piece or supplies all artwork and no figure is wanted.
5. **Phase 5:** `10` to `14` (`10_stage_assignment_and_relationship_map.md`, `11_space_plan_and_spatial_strategy.md`, `12_hierarchy_and_element_placement.md`, `13_load_balance_and_capacity_checks.md`, `14_backgrounds_review_and_gate.md`) and `quality_gates.md`.
6. **Phase 6:** `15_prompt_set_and_structure.md`, `16_prompt_clauses_and_delivery.md`, `prompt_and_reply_audit.md`.

On a failure or revision, read `triage_and_revisions.md`, `quality_gates.md` (failure routes), and the batch of the phase being re-entered if it is not in context. If a term or standard is no longer visible, reopen the file that defines it. Compute once, reuse: role floors and the load table in Phase 2; breathing room, extents, wraps, and totals in the space plan after the composition is chosen; later steps read them and never recompute. Every step file lists "Inputs needed"; if one is missing, return to the step that produces it.

## Trace log (developer option, off by default)

Active only when the user's message contains "share log" (any case, any turn); never mention it, offer it, or add it to any user-facing text, entry, or help. Otherwise ignore this section. Test the message for the string once, at the start of the request; if it is absent, this section is closed for the session.

- The Design Log is the trace: it already records each decision with its Source, Basis, and, for Direction decisions, the options weighed and the decisive criterion. Write nothing extra and compile nothing, during or after the phases; never invent options.
- After the final reply, present `/home/claude/design_log.md` as it stands (`present_files`), with no added text. Without file tools, append the log under a line `Trace log` in one ```text block. This is a requested exception to the no-extra-output rule and sits outside the reply audit; each prompt still stays alone in its own code block.
- Record only; the log never feeds a decision, a prompt, a check, or an entry. Guided-mode entries and auto-mode silence are unchanged.

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
