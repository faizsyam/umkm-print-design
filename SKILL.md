---
name: umkm-print-design
description: Transforms an Indonesian UMKM (small business) print design brief into a finished, standalone image-generation prompt using a six-phase art-direction workflow (brief, analysis, design plan, design elements, design execution, prompt synthesis). Use when a user wants a banner, spanduk, menu, flyer, brosur, poster, label, stiker, kemasan, signage, kartu nama, daftar harga, or any other printed piece for a small business, or asks for a design prompt, brand-specific visual direction, or logo mark concept for an image generator.
---

# UMKM Print Design

## Mission

Turn a business owner's brief into one image-generation prompt that produces a print design that is specific to that business, professionally art-directed, effective in its physical setting, and free of generic AI aesthetics. The prompt is the deliverable. It is preceded by a compact decision summary for Phases 2 to 5 so the user can see what was weighed and chosen. The full reasoning stays internal unless the user asks for it.

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

| Phase | Purpose | Exit artifact | Read |
|---|---|---|---|
| 1. Brief | Capture and classify everything given; find real gaps | Brief Ledger | `references/01_brief_and_requirements.md` |
| 2. Analysis | Understand business, audience, physical environment, and the piece's actual job | Communication Problem + Environment Profile + design implications | `references/02_research_and_analysis.md` |
| 3. Design Plan | Decide the unified creative direction through structured exploration | Design Plan (brand design, theme, style, hero, principles) | `references/03_design_plan.md` |
| 4. Design Elements | Build the coherent visual system | Element system incl. logo mark decision | `references/04_design_elements.md` |
| 5. Design Execution | Compose the piece for its medium, reading stages, and area | Execution Specification (hierarchy tiers, space budget, layout) | `references/05_design_execution.md` |
| 6. Prompt Synthesis | Express the design as a standalone prompt | Final prompt | `references/06_prompt_synthesis.md` |

Phases 2 to 5 are summarized to the user in the decision summary (see Output contract). Phases 1 and 6 are not.

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
- **Apparent option**: what most people would produce on first association from the category, culture, place, or product. It is a benchmark to beat, never a default.
- **Design Log**: the compact running record in your working notes of the design's state: Communication Problem, Environment Profile, Visual source inventory, chosen core idea, style, hero, color, type, mark, reading stages, space plan, and open issues.
- **Space plan**: the deliberate allocation of margin, isolation zones, separations, and resting fields, decided before content is placed.
- **Personality device**: an ownable, conceptually grounded feature that makes an identifier unlike any other and could not be removed without the identity collapsing.
- **Consequential decision**: one that defines identity, effectiveness, or coherence (core idea, style synthesis, hero, logo mark, color strategy, typographic voice, composition strategy). All others are trivial.

## Execution discipline

**Order and completeness**
- **Run the phases in order, 1 to 6.** Phase N+1 begins only when Phase N's required decisions have been made, its exit artifact exists, and its gate in `quality_control.md` has passed. No phase is skipped, merged away, or deferred, however simple the brief looks. A simple brief shortens the work; it does not remove it.
- **Required decisions are mandatory; techniques are discretionary.** The Required decisions on each phase's Phase card, the exploration protocol, and the gates cannot be treated as optional. How much research, how many notes, and which tests to use are scaled to the brief.
- **No conclusions ahead of their phase.** Do not choose a style, settle a layout, or draft prompt text before the earlier phases' decisions exist. A conclusion you already hold is a hypothesis to test in its own phase.
- **Each phase consumes the previous hand-off.** Brief Ledger → research questions and tensions; analysis → design implications, Environment Profile, Visual source inventory; plan → element constraints and space intent; elements → composition inputs; Execution Specification → prompt. A decision that ignores a hand-off item fails its gate.
- **Return when needed, then re-run forward.** A failed gate or a flaw exposed later sends the work to the earliest responsible phase (see Backward iteration), and every affected later phase is redone in order.

**Staying oriented**
- **Phase entry.** Read the phase reference. Restate in your notes the inputs from the last hand-off, the principles in force from the Phase card, and the Required decisions. Re-read the Design Log.
- **One decision at a time.** Inside a phase, take the Required decisions one by one, each with its full attention. The sections of a reference are a map of the thinking each decision needs, not a list to recite.
- **Phase exit.** Confirm every Required decision was made deliberately, apply the exploration protocol where it applies, pass the gate, write the decision-summary entry, and update the Design Log.
- **When lost or overloaded.** Return to the Phase card, then the Design Log, then Decision commitments. Resolve the current decision before looking ahead. Do not rush to the prompt to relieve the pressure; a thin earlier phase will show up as a generic prompt.

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

## Principle map

Principles are not background. Each phase reference opens with a Phase card naming the principles in force there. Re-read the card at phase entry and before the gate. Where they bite hardest:

| Principle | Where it bites | What it demands there |
|---|---|---|
| 1 Whole-system thinking | Phases 3–6, every gate | Test each decision against the Design Log, never in isolation |
| 2 Structured exploration | Phases 2–5 | Apparent option named, three candidates, one beyond the apparent, anti-anchoring evaluation, runner-up named |
| 3 Evidence-informed judgment | Phases 1–2; mark and hero sourcing | Provenance tags; research only what changes a decision; nothing invented |
| 4 Contextual specificity | Phase 3 stress tests, Phase 4 mark, quality control | Swap, category, context-swap tests; nothing that works unchanged for a competitor |
| 5 Functional creativity | Phases 3–5 | Every novel element names the job it does; arbitrary novelty is rejected |
| 6 Intentional restraint | Phases 4–5 | Element allowance against the space plan; removal and fill tests |
| 7 Internal consistency | Phases 3–6, gates | Resolve contradictions at their source; single-voice test |
| 8 Fidelity to the brief | Phases 1, 4, 6 | Verbatim text, fixed assets untouched, exclusions honored |
| 9 Iterate at the root | Every gate | Return to the earliest cause; re-run forward |
| 10 Effort follows impact | Every phase | Longest deliberation on the mark, core idea, hero, and space plan; brisk on trivial decisions |

## Depth calibration

Scale effort to the brief, not to a fixed ritual.

- **Rich brief, low stakes or small format**: shorten Phases 1–2 (less research, briefer notes), and spend effort on Phases 3–5.
- **Sparse brief, high visibility or large format**: invest in analysis and research, ask blocking questions first.
- **Multi-face or multi-piece request**: establish the shared identity once, then plan each face's job separately.

Whatever the depth, every phase's exit artifact must exist in your working notes before the next phase begins. Compact is acceptable; missing is not. A compact depth shortens notes; it never waives the exploration protocol for consequential decisions.

## Exploration protocol

Applies to each consequential decision in Phases 3, 4, and 5, and to the genuine option sets in Phase 2. It does not apply to trivial decisions. The first idea to arrive and the most familiar option exert a strong pull, and the protocol is built to counter it. A consequential decision resolved in one pass, with no recorded challenge step, has not been decided.

1. **Name the apparent option first.** Write down what most people would produce on first association. It is the benchmark. It may stay in the field as one candidate, but it has to earn its place.
2. **Generate at least three candidates, at most one of them apparent, and at least one drawn from beyond the apparent.** Candidates differ on a structural axis: what carries the identity, what the viewer is asked to do first, how information is structured, the register and commercial posture, or the image-making method. Color or ornament alone does not count. Source them differently: product truth, customer moment, environment, differentiator, category tension, name or origin, material, and the deeper specifics in the Visual source inventory. Finish writing all candidates before evaluating any.
3. **Evaluate in a different order than you generated, starting with the last.** Use the phase's criteria: brief, analysis, Environment Profile, audience, objective, content capacity, space plan, feasibility. Record concrete strengths, weaknesses, and trade-offs, one line each, not adjectives.
4. **Challenge before choosing.** Name the strongest runner-up. State the strongest case against the leading candidate and the strongest case for the runner-up. Remove the leading candidate and see which of the rest you would choose; then compare them head to head. If the leader's margin cannot be stated as one decisive criterion, keep working. An apparent option that wins must show the specific criterion on which the less obvious candidates fell short. "It is fitting" or "it is common for this category" is not a reason.
5. **Engineer the strongest solution**: select outright, transplant a specific strength, combine under one logic, repair an identified weakness, or build a new candidate from what the comparison revealed. A hybrid is valid only if it can be stated as one idea; if it needs "and also," it is a compromise.
6. **Record** the choice, the decisive reason, why it beat the strongest runner-up, and what was kept from the others.

The logo mark has an extended version of this protocol in `references/04_design_elements.md`. Candidates are brief working notes of a few lines each. The full notes stay internal; the decision summary shows the material alternatives with their key strengths and weaknesses.

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
- Do not deliver an identifier that is only the business name set in type. Unless the user supplied a logo or explicitly asked for plain text, every identifier carries a personality device.
- Do not leave placeholders, blank zones for later manual work, or "insert here" instructions in the final prompt.
- Do not output the workflow beyond the decision summary and the prompt unless the user asks for fuller analysis, concepts, or rationale.

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

After any return, re-run in order every later phase the change affects before continuing; never patch forward. Limit each unresolved issue to two revision cycles. After that, choose the best available resolution and proceed. The decision summary always reflects the final decisions, and notes a revision when it materially changed an earlier decision.

## Decision commitments

Before Phase 6, the working notes must contain explicit answers to the following. Each answer must be justified by a finding in the Brief Ledger or analysis; a decision that can only be justified by "it looks good" or "it is typical for this industry" is not committed and must be redone.

- The one-sentence message the viewer takes away first.
- The Environment Profile in brief: what surrounds the piece, what the design shares with it to be appropriate, and the dimension on which it deliberately departs to be seen.
- The Visual source inventory, and for the core idea, style direction, and hero: the apparent option, the candidates compared (one from beyond the apparent), the chosen direction, and the decisive reason it beat the strongest runner-up.
- The logo mark: a supplied fixed asset, or a new mark with its personality device and the truth it expresses, developed through the extended protocol, and the mechanisms that keep it distinct from the typography around it.
- Every content item assigned to a reading stage, and the space plan: margins, isolation zones, separations, and resting fields, with their intended proportions.
- The reading order of all content and imagery.
- The placement and role of every mandatory text item.
- The traits that make this design unlike a neighboring competitor's.

At each phase gate, let the perspectives that own the phase (see the table above) each raise one objection to the phase output. Resolve it or record why it is accepted. A gate with no objections raised was not applied.

## Revision requests

When the user asks to change an earlier result, re-enter the workflow at the earliest phase the change affects, keep every unaffected decision, and deliver a fresh complete prompt and update the decision summary for the phases that changed. A change to content re-enters at Phase 1; to mood or concept at Phase 3; to color, type, or the mark at Phase 4; to arrangement or emphasis at Phase 5; to wording only at Phase 6.

## Output contract

When a design task reaches delivery, the reply contains, in this order:

1. **Decision summary** for Phases 2, 3, 4, and 5.
2. **The final image-generation prompt**, in a single code block, self-contained and ready to use. When several prompts are delivered, each has its own code block.
3. **Optionally, a few short lines outside the prompt**, only when needed and ordered by consequence: a consequential assumption, content deliberately left out because it was not provided, copy you wrote that the user did not supply, a preference that had to yield, a suspected typo in user text, a supplied logo or text volume the target model may not reproduce faithfully, or a format ratio the model cannot produce exactly. Never use this space for design rationale; rationale belongs in the summary.

If clarification is required first, the reply is the questions only (see Clarification policy).

### Decision summary

Present one compact block per phase, titled with the phase name, in execution order: Analysis, Design Plan, Design Elements, Design Execution. Write it in the user's language. Include only decisions that shaped the design and had real alternatives. For each:

- **Decision**: its name.
- **Alternatives**: one line each, with the alternative's name, key strength, and key weakness. Consequential decisions in Phases 3 to 5 show the candidates actually compared (at least three); Phase 2 shows the genuine options for its choices.
- **Chosen**: the direction and a one-sentence rationale tied to the brief, environment, or objective, including why it beat the strongest runner-up. If the result is a hybrid or a repaired candidate, say what was combined or fixed.

What each phase typically surfaces:

| Phase | Decisions worth summarizing |
|---|---|
| Analysis | The weakest link in the communication problem; the Environment Profile's departure and fit dimensions; the differentiation strategy |
| Design Plan | Core idea; style direction; hero |
| Design Elements | Color strategy; typographic voice; logo mark (its personality device and the mechanisms keeping it distinct) |
| Design Execution | Reading-stage assignment and space plan; spatial strategy |

Rules for the summary:

- **Genuine only.** If a decision was fixed by the user, a supplied asset, or the evidence, give one line saying so and why. Never invent alternatives to fill the format.
- **Compact and selective.** Phrases, not paragraphs. No process narration, no chain of thought, no restating the brief. A simple piece gets a shorter summary but never an empty phase.
- **Order and honesty.** Decisions appear in the order they were made within each phase and reflect the final state after any revision.
- **Consistent with the prompt.** Write the summary after the prompt passes the audit. Every chosen direction must be visible in the prompt, and nothing in the prompt may contradict it. The summary never goes inside the prompt's code block, and the prompt does not absorb its rationale.
- **Several concepts or faces.** For several concepts, show Phase 2 once and give each concept its own chosen direction and main trade-off for Phases 3 to 5. For several faces, show shared decisions once and face-specific Phase 5 decisions per face.

### Deliverable rules

If the user asked for several concepts or variations, deliver one complete standalone prompt per concept, each differing in underlying creative approach, not merely in color or ornament. If the piece has several faces, deliver one standalone prompt per face that restates the shared identity.

Reply in the user's language. Write the prompt in English by default for model reliability, keeping all on-piece text verbatim in its original language, unless the user requests a different prompt language or names a model that performs better in another.

The prompt contains only what shapes the picture or constrains the output: format, depicted forms and their relationships, typography, mandatory text, color, surface treatment, mark construction, and necessary exclusions. Business strategy, audience and environment analysis, rationale, alternatives, and process reach the prompt only as the visible traits they produced (see `references/06_prompt_synthesis.md`). Fuller analysis, complete candidate lists, or extended rationale beyond the summary are given only on request, and separately from the prompt.

## Before delivering

Run the prompt audit and release checklist in `references/quality_control.md`. The prompt must contain every mandatory item, describe relationships and not just inventories, introduce nothing absent from the plan, and carry no meta-commentary. The decision summary must be present, in order, genuine, and consistent with the prompt.