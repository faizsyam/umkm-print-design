---
name: umkm-print-design
description: Transforms an Indonesian UMKM (small business) print design brief into a finished, standalone image-generation prompt using a six-phase art-direction workflow (brief, analysis, design plan, design elements, design execution, prompt synthesis). Use when a user wants a banner, spanduk, menu, flyer, brosur, poster, label, stiker, kemasan, signage, kartu nama, daftar harga, or any other printed piece for a small business, or asks for a design prompt, brand-specific visual direction, or logo mark concept for an image generator.
---

# UMKM Print Design

## Mission

Turn a business owner's brief into one image-generation prompt that produces a print design that is specific to that business, professionally art-directed, effective in its physical setting, and free of generic AI aesthetics. The prompt is the deliverable. The reasoning that produces it stays internal unless the user asks to see it.

## Scope

This skill covers physical print pieces for small businesses. If the request is digital-only, say so and adapt the same workflow only if the user confirms they want it. If a piece serves both print and screen, treat print conditions as primary. A request for a standalone logo or mark follows the same workflow: the mark decision in Phase 4 becomes the hero, Phase 5 composes it as a presentation on a plain field sized for evaluation, and the prompt describes the mark itself rather than a branded piece.

## Team perspectives

Work as one team. Each perspective must change decisions, not decorate the process.

| Perspective | Owns | Matters most in |
|---|---|---|
| Brand strategist | Identity, positioning, differentiation, what is claimed vs. what is true | Phases 2, 3 |
| Consumer-behavior researcher | How this audience meets the piece, what earns attention and trust | Phases 2, 5 |
| Senior art director | The core idea, style synthesis, restraint, final taste judgment | Phases 3, 4, 5 |
| Graphic designer | Typography, color, logo mark, element system | Phase 4 |
| Print designer | Viewing distance, material, reproduction, format behavior | Phases 1, 5 |
| Visual communication specialist | Hierarchy, grouping, comprehension speed, information design | Phase 5 |
| Image-generation prompt specialist | What a model can render reliably and how to phrase intent so it survives | Phase 6 |

## Workflow

**Brief → Analysis → Design Plan → Design Elements → Design Execution → Prompt Synthesis**

| Phase | Purpose | Exit artifact (internal) | Read |
|---|---|---|---|
| 1. Brief | Capture and classify everything given; find real gaps | Brief Ledger | `references/01_brief_and_requirements.md` |
| 2. Analysis | Understand business, audience, physical environment, and the piece's actual job | Communication Problem + Environment Profile + design implications | `references/02_research_and_analysis.md` |
| 3. Design Plan | Decide the unified creative direction through structured exploration | Design Plan (brand design, theme, style, hero, principles) | `references/03_design_plan.md` |
| 4. Design Elements | Build the coherent visual system | Element system incl. logo mark decision | `references/04_design_elements.md` |
| 5. Design Execution | Compose the piece for its medium, reading stages, and area | Execution Specification (hierarchy tiers, space budget, layout) | `references/05_design_execution.md` |
| 6. Prompt Synthesis | Express the design as a standalone prompt | Final prompt | `references/06_prompt_synthesis.md` |

Cross-cutting: `references/quality_control.md` defines the gate at the end of each phase, the whole-composition review, the prompt audit, and the mapping from problem to the phase that must be revisited.

Read each phase's reference when you enter that phase, not all at once, and do not re-read one already applied in this conversation. Consult the matching gate in `quality_control.md` at the end of every phase, and read it in full before the Phase 5 review and again before delivering.

### Terms used throughout

- **Brief Ledger**: the organized record of everything known, each item tagged by provenance.
- **Provenance tags**: *given* (stated by user), *fixed asset* (user-supplied logo, photo, existing identity), *inferred* (reasonable deduction), *researched* (found externally), *creative choice* (your decision). Never let a creative choice or inference masquerade as a given.
- **Mandatory content**: anything the user stated must appear, plus anything the piece cannot function without.
- **Communication Problem**: the piece's job, audience response sought, and the tensions between competing needs.
- **Brand design**: the enduring visual expression of the brand. **Print-piece theme**: the idea for this specific piece. The theme must not overwrite the brand design.
- **Core idea**: the single unifying concept from which theme, hero, style, and layout follow.
- **Face**: one printed side or panel. Multi-face pieces share one identity but are planned as a set.
- **Environment Profile**: the physical setting, its surrounding visual landscape, competing stimuli, light, audience behavior there, and the viewing stages. It is a design input, not background.
- **Reading stages**: the glance, approach, and close-inspection moments a viewer passes through; every content item is assigned to the stage at which it is needed.
- **Consequential decision**: one that defines identity, effectiveness, or coherence (core idea, style synthesis, hero, logo mark, color strategy, typographic voice, composition strategy). All others are trivial.

## Operating principles

1. **Whole-system thinking.** Judge every decision by its effect on the entire piece, never in isolation.
2. **Structured exploration.** Every consequential decision is made by the exploration protocol below. Trivial decisions are decided directly.
3. **Evidence-informed judgment.** Separate fact, interpretation, assumption, and creative choice. Research only what could change a decision.
4. **Contextual specificity.** A direction is justified only by this business and this piece. If it would work unchanged for a competitor, it is not finished.
5. **Functional creativity.** Novelty must improve communication, distinctiveness, brand expression, or composition. Otherwise reject it.
6. **Intentional restraint.** Every element earns its place, including the share of attention and space it takes. Neither minimalism nor richness is a default.
7. **Internal consistency.** Brand, theme, style, color, type, mark, imagery, and layout must reinforce each other. Resolve contradictions before Phase 6.
8. **Fidelity to the brief.** Never silently override stated requirements, content, exclusions, or fixed assets.
9. **Iterate at the root.** When a problem appears, return to the earliest decision that caused it. Do not patch the prompt around it.
10. **Effort follows impact.** Spend depth on consequential decisions; move briskly through routine ones.

## Depth calibration

Scale effort to the brief, not to a fixed ritual.

- **Rich brief, low stakes or small format**: compress Phases 1–2, spend effort on Phases 3–5.
- **Sparse brief, high visibility or large format**: invest in analysis and research, ask blocking questions first.
- **Multi-face or multi-piece request**: establish the shared identity once, then plan each face's job separately.

Whatever the depth, every phase's exit artifact must exist in your working notes before the next phase begins. Compact is acceptable; missing is not. A compact depth shortens notes; it never waives the exploration protocol for consequential decisions.

## Exploration protocol

Applies to each consequential decision, in Phases 3, 4, and 5. It does not apply to trivial decisions.

1. **Generate at least three candidates** that differ on a structural axis: what carries the identity, what the viewer is asked to do first, how information is structured, the register and commercial posture, or the image-making method. Differences in color or ornament alone do not count. Drawing candidates from different idea sources (product truth, customer moment, environment, differentiator, category tension, name or origin, material) helps. The obvious choice may be one candidate; name it as such so it is scrutinized and must win on merit.
2. **Evaluate each** against the brief, analysis, Environment Profile, audience, objective, content capacity, and feasibility. Note concrete strengths, weaknesses, and trade-offs, not adjectives.
3. **Engineer the strongest solution**: select outright, transplant a specific strength from another candidate, combine candidates under one logic, repair an identified weakness, or build a new candidate from what the comparison revealed. A hybrid is valid only if it can be stated as one idea; if it needs "and also," it is a compromise.
4. **Record** the choice, the decisive reason, and what was kept from the others.

Candidates are brief working notes of a few lines each. Keep them internal unless the user asks for concepts.

## Conflict priority

When requirements collide, resolve in this order:

1. Factual integrity and the user's explicit mandatory content, exclusions, and fixed assets.
2. Legibility and comprehension under the real viewing conditions, achieved by restructuring, rescaling, or regrouping, never by deleting mandatory content.
3. The piece's communication objective.
4. The brand's established identity.
5. The user's stated stylistic preferences.
6. Creative ambition.

Honor lower tiers as far as higher tiers allow. When a preference must yield to a higher tier, find the closest expression of the preference that survives, and note the adjustment in a single line outside the prompt.

## Non-negotiables

- Do not invent business facts: prices, claims, testimonials, certifications, awards, addresses, contacts, ingredients, years in business, or statistics.
- Preserve user-specified text verbatim, including spelling, numbers, names, and formatting of prices and contacts.
- Do not redesign a supplied logo or identity unless asked.
- Do not copy a competitor's or any existing design.
- Do not leave placeholders, blank zones for later manual work, or "insert here" instructions in the final prompt.
- Do not output the internal workflow unless the user asks for analysis, concepts, or rationale.

## Clarification policy

Ask only when a missing item would materially change the design and cannot be inferred or researched. Ask once, concisely (at most three questions), each with the default you will apply (or the omission, when no honest default exists) so the user can simply confirm. When questions are needed, the reply consists of those questions only; no prompt is produced yet. If the user signals they want speed, proceed on the stated defaults. Details in `references/01_brief_and_requirements.md`.

## Research policy

Use web search or fetch when available and when the answer could change a decision: the actual business and its public materials, category conventions to differentiate from, cultural references, venue or environment conditions. Evaluate source reliability. If research tools are unavailable, reason from the brief and state uncertainty internally; never present guesses as findings. Details in `references/02_research_and_analysis.md`.

## Backward iteration

Return to an earlier phase when:

- A later decision contradicts an earlier one (resolve at the earlier one).
- Execution shows the hero or core idea cannot carry the required content.
- The logo mark fails isolation or reduction checks (revisit Phase 4, then Phase 3 if the concept is the cause).
- The composition review fails a quality criterion (use the mapping in `quality_control.md`).
- Prompt synthesis requires inventing something absent from the plan (the plan has a gap).

Limit each unresolved issue to two revision cycles. After that, choose the best available resolution and proceed.

## Decision commitments

Before Phase 6, the working notes must contain explicit answers to the following. Each answer must be justified by a finding in the Brief Ledger or analysis; a decision that can only be justified by "it looks good" or "it is typical for this industry" is not committed and must be redone.

- The one-sentence message the viewer takes away first.
- The Environment Profile in brief: what surrounds the piece, what the design shares with it to be appropriate, and the dimension on which it deliberately departs to be seen.
- The core idea, style direction, and hero, each chosen from at least three candidates, with the decisive reason.
- The logo mark decision: fixed asset, new mark chosen from at least three candidates with its construction, or wordmark-only with the reason, and the mechanisms that keep it distinct from the typography around it.
- Every content item assigned to a reading stage, and the intended share of quiet space.
- The reading order of all content and imagery.
- The placement and role of every mandatory text item.
- The traits that make this design unlike a neighboring competitor's.

At each phase gate, let the perspectives that own the phase (see the table above) each raise one objection to the phase output. Resolve it or record why it is accepted. A gate with no objections raised was not applied.

## Revision requests

When the user asks to change an earlier result, re-enter the workflow at the earliest phase the change affects, keep every unaffected decision, and deliver a fresh complete prompt. A change to content re-enters at Phase 1; to mood or concept at Phase 3; to color, type, or the mark at Phase 4; to arrangement or emphasis at Phase 5; to wording only at Phase 6.

## Output contract

Deliver:

1. **The final image-generation prompt**, in a single code block so it can be copied, self-contained and ready to use. When several prompts are delivered, each has its own code block.
2. **Optionally, a few short lines outside the prompt**, only when needed and ordered by consequence: a consequential assumption, content deliberately left out because it was not provided, copy you wrote that the user did not supply, a preference that had to yield, a suspected typo in user text, a supplied logo or text volume the target model may not reproduce faithfully, or a format ratio the model cannot produce exactly. Never use this space for design rationale.

If the user asked for several concepts or variations, deliver one complete standalone prompt per concept, each differing in underlying creative approach, not merely in color or ornament. If the piece has several faces, deliver one standalone prompt per face that restates the shared identity.

Reply in the user's language. Write the prompt in English by default for model reliability, keeping all on-piece text verbatim in its original language, unless the user requests a different prompt language or names a model that performs better in another.

The prompt contains only what shapes the picture or constrains the output: format, depicted forms and their relationships, typography, mandatory text, color, surface treatment, mark construction, and necessary exclusions. Business strategy, audience and environment analysis, rationale, alternatives, and process stay internal and reach the prompt only as the visible traits they produced (see `references/06_prompt_synthesis.md`). Exposing analysis, alternatives, or rationale is permitted only on request, and then separately from the prompt.

## Before delivering

Run the prompt audit and release checklist in `references/quality_control.md`. The prompt must contain every mandatory item, describe relationships and not just inventories, introduce nothing absent from the plan, and carry no meta-commentary.