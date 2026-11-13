---
name: jago-desain-apa-aja-mini
description: >-
  Turns a design need of any kind into one or more standalone image-generation prompts for static visual outputs, through a short adaptive conversation fitted to the user's language, design literacy, and brief completeness. Compact edition: six phases (brief, analysis, design plan, design elements, design execution, prompt synthesis) with brief qualities turned into checkable targets, a binding space budget, developed identity marks, purpose-based information groups, a theme-derived visual world, and a separate composition per deliverable. Use for static visuals in any medium, physical or on screen (posters, banners, signage, menus, packaging and labels, cards, invitations, covers, social and ad graphics, slides, infographics, static screen mockups, brand identity, logos); for requests like "prompt gambar", "bikin desain", "design prompt", "make me a poster/banner/logo"; or to revise such a design. Not for code, 3D, motion, animation, or interactive deliverables.
---

# Jago Desain Apa Aja (mini)

Turns a design need, from a first-time requester to a professional designer, into finished, standalone image-generation prompts for static visuals, through a short design conversation. This file is the runbook and the hard rules; `references/` holds the methods, loaded one batch at a time. A rule lives in one place only: here for routing and non-negotiables, in a reference for method.

## Hard rules (read first, obey always)
- No invented facts about the subject; no implied claim, endorsement, or authority it does not hold.
- User text is verbatim, suspected typos included (flag, never fix).
- Supplied logos and characters are never redesigned, restyled, simplified, recolored; no unasked figure; never a real person's likeness; no copying competitors or existing designs.
- No identifier that is only a styled name, unless supplied or explicitly requested as plain text.
- No placeholders or blank zones for content the skill should create; the one exception is the reserved asset panel.
- No stated quality contradicted by a decision or left without a visible carrier.
- No suggestion enters the brief or design without the user's yes; suggestions are labeled, never counted as facts.
- No unfamiliar jargon or walls of text for the user; no workflow output beyond the defined messages (`references/12_user_messages.md`).
- **Conflict priority** (a lower item yields only to a higher): (1) factual integrity, mandatory content, exclusions, fixed assets; (2) perception and comprehension under real conditions, by restructuring, never by deleting mandatory content; (3) the user's stated requirements and qualities; (4) the communication objective and strategy; (5) established brand identity not supplied as an asset; (6) creative ambition.

## Runbook
Six phases in order; none skipped, merged, or deferred. Each phase: read its batch once, decide by class, append to the Design Log, pass its hand-off check.

| # | Phase | Output |
|---|---|---|
| 1 | **Brief** | adaptive intake; ledger, deliverable set, quality translations, openness map; confirmed summary and mode (guided/auto) → S |
| 2 | **Analysis** | real communication problem, information groups, load table, Environment Profile with floors, differentiation, implications |
| 3 | **Design Plan** | binding space budget in axis extent (the hero is the residual), core idea, style, hero (footprint and hosting screened), principles with density caps, direction check |
| 4 | **Design Elements** | one system decision (color, type, shape and container language, supporters, ground); copy treatments by grade and device; a mark or figure on what the hero left open |
| 5 | **Design Execution** | per deliverable: stages (glance parts split), groups, composition as a region table in shares of the format, space plan measured once, placement, one assembled review |
| 6 | **Prompt Synthesis** | one audited standalone prompt per deliverable; the final reply |

Guided mode stops for the go-ahead after Phases 3 and 4; Phase 5's entry is shown and Phase 6 follows. Auto mode shows nothing at gates.

## Decisions (method: `references/3_standards_and_protocol.md`)
- **Direction** (core idea, style, hero, a new mark or lead figure, spatial strategy): explored, sized by openness (Open, Steered, Fixed; Fixed takes none).
- **System** (palette, type roles, treatment grade and device, shape and container language, supporters, ground): derived from the direction in one comparison.
- **Execution** (copy-treatment details, non-mandatory wording, small items, icons, edge details): specified directly in the prompt; no log item.
- **Escalation:** a System or Execution choice with a named risk gets its own compact comparison.
- A decision closes when its decisive criterion is stated and no recorded check fails it; it reopens only by naming a failed check. What an earlier decision fixes is inherited, not decided again.

## Solve once (reason: trial layouts were the largest source of wasted effort and weaker designs)
- **Budget:** one table of single numbers summing to 100, in axis extent (planned lines × pitch, never area), the same unit from the Phase 2 load table to the Phase 5 ledger: information groups first, then structure and decoration, quiet, margins, headroom; the hero is the residual, and a hero footprint above its row is dropped at the screen.
- **Arrangements:** a column arrangement or a container tier is pre-applied only after its width floor passes, recorded in Phase 3, and inherited by Phases 4 and 5.
- **Ladder:** Phase 3 walks the fit ladder as a rung ledger in rung order (`references/4_analysis.md` H): each rung's yield is arithmetic on rows, never a re-estimate; after rung 8 the overrun is recorded and the table is final. Phase 5 inherits it; a shortfall above ≈ 10% of the axis returns to the Phase 3 budget once.
- **Claims:** a ladder move that changes a quality carrier updates the carrier map; no review or prompt states a relation the region table contradicts.
- **Floors:** the glance floor applies to an item's glance part only; core content (offers, prices, choices) never takes the deliberate-reading floor.
- **Hosts:** text in a circular or arched host is solved by geometry in one pass; the host follows the text.
- **Units:** after Phase 2 every size and region is a share of the format; the region table carries a mass class and side per region, so balance is read, not measured.
- **Fit failure in Phase 5:** after two cycles take the next strategy and record the risk; never redraw or re-derive.
- **Caps:** supporter and ornament families, container designs, rendering treatments stay within the density caps (`5_plan.md`).

## Gotchas (what goes wrong without this skill's rules)
- Sizing the hero first, then squeezing the menu or price list: the information groups are sized first.
- Applying the largest size to every word of a name; set only its distinctive word at glance size.
- Fixing line counts, name stacks, or container arrangements in Phase 4, then reopening them in Phase 5.
- Re-opening a mark's construction after the hero fixed its form.
- Pre-applying columns or per-unit containers without the width-floor test, then undoing them in Phase 5.
- Closing the budget by re-estimating pitch or gaps, or skipping a rung, instead of summing rung yields.
- Splitting a user's line into label and value and losing its punctuation or parenthetical.
- Sending a modifier away from the text it modifies to find room; counting decoration by theme instead of kind.
- Piling decorative systems on a dense piece; the caps decide, character comes from depth in the hero and lettering.
- Accepting a legibility objection in the review instead of fixing it on the ladder.
- Writing millimeters, coordinates, or many percentages into a prompt.

## Checks
One hand-off check per phase (`references/10_gates_and_revisions.md`): decisions made by class; sources named; qualities carried at this phase's level; consistency with what the phase reads; user-facing steps of the mode done; D appended. One assembled review with the cross-phase tests and one objection at the end of Phase 5; one prompt audit in Phase 6. A passed check re-runs only when a decision it reads changed. Cap each issue and loop at two cycles.

## Research
A question, not a phase: only for a question that names a Direction decision it could change and that the brief and knowledge cannot answer; at most three targeted queries and one page read per question; no trend surveys.

## Loading (all in `references/`, one level deep)
Open only the current batch, when its step is reached, all its files in one `cat` command (one call per batch). Never preload a later batch, reopen a file already in context, or skip a file. Each file's header says what it needs and produces; if an input is missing, return to the step that produces it. If a term is no longer visible, reopen `2_glossary.md`.
1. **Start:** `1_intake_and_brief.md`, `2_glossary.md`.
2. **After summary and mode are confirmed:** `12_user_messages.md`, `3_standards_and_protocol.md`, `4_analysis.md`.
3. **Phase 3:** `5_plan.md`.
4. **Phase 4:** `6_system_identity.md`, `7_system_supporters_containers.md` (skip `7` only for a fixed plain text-only piece or fully supplied artwork with no figure).
5. **Phase 5:** `8_frame_and_space.md`, `9_place_and_check.md`, `10_gates_and_revisions.md`.
6. **Phase 6:** `11_prompt_synthesis.md`.
On a failure or revision: `10_gates_and_revisions.md` plus the batch of the phase being re-entered if not in context. Compute once, reuse: floors and the load table in Phase 2; the region table and space plan once in Phase 5; later steps read them.

## Trace log (developer option, off by default)
Active only when the user's message contains "share log" (any case, any turn), tested once at the start of the request; never mention or offer it. The Design Log is the trace: write nothing extra and never invent options. After the final reply, present `/home/claude/design_log.md` as it stands (`present_files`) with no added text; without file tools, append it under `Trace log` in one ```text block. This is an exception to the no-extra-output rule and sits outside the reply audit; each prompt still stays alone in its code block. The log never feeds a decision, prompt, check, or entry.
