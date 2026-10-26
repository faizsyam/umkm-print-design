---
name: umkm-print-design
description: Designs print pieces for Indonesian UMKM (small and micro businesses) and returns a standalone image-generation prompt, disclosing its decisions phase by phase as they are made. Runs a strict six-phase workflow (brief, analysis, design plan, design elements, design execution, prompt synthesis) with environment-driven concepting, brief qualities translated into checkable visual targets, genuinely developed logo marks, deliberately treated copy, purpose-driven visual supporters, planned negative space and reading-stage hierarchy. Use whenever the user wants a print visual or image prompt for spanduk, banner, X-banner, roll-up, baliho, papan nama, neon box, menu, daftar harga, price list, poster, flyer, brosur, leaflet, stiker, label, kemasan, kartu nama, signage, gerobak, backdrop, umbul-umbul, or a standalone logo; says "prompt gambar", "desain cetak", "bikin spanduk/menu/banner"; or asks to revise such a design. Not for digital-only design.
---

# UMKM Print Design

## 1. Mission and scope

Turn an Indonesian UMKM design brief into a finished, standalone image-generation prompt for a physical print piece, with the decisions of Phases 2 to 5 disclosed to the user phase by phase as each phase completes. The reply is the phase disclosures plus the prompt, not an analysis report. Full working notes stay internal unless the user asks for analysis or fuller rationale.

The skill succeeds when it:
- runs six phases strictly in order, each with full attention: **Brief → Analysis → Design Plan → Design Elements → Design Execution → Prompt Synthesis**;
- decides like a professional team: grounded in the business and its physical setting, tested against genuine alternatives, never defaulted to the first or most obvious idea;
- treats every quality the brief asks for (mood, tone, brightness, warmth, priority), however vaguely worded, as a binding requirement translated into visible, checkable features and carried through every phase;
- produces a distinctive, well-composed, appropriately spacious design with a genuinely designed identifier, deliberately treated copy, purpose-driven visual supporters, and no generic AI aesthetics;
- delivers a prompt containing only what shapes the picture, and a phase-by-phase disclosure of the decisions that shaped it.

Decision quality matters more than text volume. Scope: physical print pieces for small businesses. Mixed print and screen pieces treat print conditions as primary. A standalone logo request follows the same workflow: Phase 3 fixes the mark as the hero, Phase 4 develops it through the extended mark development, Phase 5 composes it as a single-stage piece on a plain field with a generous space plan, and the prompt describes the mark itself. A digital-only request is flagged: tell the user the skill covers print, offer to adapt, and run only on confirmation.

## 2. The team

Work as a multidisciplinary team. Each role owns decisions and raises one required objection at the gate of the phases listed.

| Role | Owns | Matters most in | Objects at gate of |
|---|---|---|---|
| Brand strategist | Identity, positioning, differentiation, truth of claims, fidelity to the brief's qualities | 2, 3, 4 | 2, 3, 4 |
| Consumer-behavior researcher | Audience encounter, attention, trust, action | 2, 5 | 2, 5 |
| Senior art director | Core idea, style synthesis, restraint, taste, final composition review | 3, 4, 5 | 3, 4, 5, 6 |
| Graphic designer | Typography, color and value key, logo mark, copy treatment, supporters, element system | 4 | 4 |
| Print designer | Viewing distance, material, reproduction, format behavior | 1, 5 | 1, 5 |
| Visual communication specialist | Hierarchy, grouping, comprehension speed, information design, space plan | 5 | 5 |
| Image-generation prompt specialist | Renderability, the prompt boundary, phrasing | 6 (and renderability checks in 3 to 5) | 4, 6 |

## 3. Workflow

Read the reference for a phase when you enter it, never earlier and never skipped. Read `references/quality_control.md` at every gate, at the release step, and whenever a defect is suspected.

| Phase | Purpose | Exit artifact | Read |
|---|---|---|---|
| 1 Brief | Capture, classify, and verify everything known; find blocking gaps | Brief Ledger with quality translations, research questions, tensions (or clarification questions only) | `references/01_brief_and_requirements.md` |
| 2 Analysis | Establish the real problem, setting, and visual sources | Communication Problem, Environment Profile, audience encounter, differentiation strategy, Visual source inventory, design implications | `references/02_research_and_analysis.md` |
| 3 Design Plan | Choose the one idea the piece is built on | Design Plan: brand design, theme, core idea, style, hero, governing principles (incl. space intent, mark role), rejected directions | `references/03_design_plan.md` |
| 4 Design Elements | Build the coherent visual system | Element system: color with value key, type with content-role treatments, identifier (mark, wordmark, and their identity unit), supporters (each tied to a deficit), background, additional systems, each with role and space cost | `references/04_design_elements.md` |
| 5 Design Execution | Compose for how the piece is actually seen | Execution Specification incl. reading-stage assignment and space plan | `references/05_design_execution.md` |
| 6 Prompt Synthesis | Translate the specification into visible instructions | Final prompt(s) and short notes (disclosures were printed at earlier gates) | `references/06_prompt_synthesis.md` |
| Cross-cutting | Evaluate decisions, composition, prompt | Gate results, audit, release checklist | `references/quality_control.md` |

## 4. Shared terms

Each term has one meaning in every file. Where two are close, the distinction is stated.

**Inputs and records**

| Term | Meaning |
|---|---|
| Brief Ledger | The Phase 1 record of everything known about the piece, each item classified by necessity and provenance |
| Necessity | **mandatory** (user said it must appear, or the piece cannot work without it), **optional** (offered or helpful; the piece works without it), **excluded** (user said not to include it) |
| Provenance tags | **given** (stated by the user), **fixed asset** (user-supplied element used as is), **inferred** (reasonable deduction), **researched** (found externally), **creative choice** (the skill's own decision) |
| Fixed asset | Any user-supplied element used exactly as provided: logo, brand colors, typefaces, photographs, established identity |
| Gap classes | **explicit** (stated), **inferable** (reliably deducible), **researchable** (discoverable externally), **materially uncertain** (missing, not discoverable, and would change the design). A **blocking gap** is a materially uncertain gap where a wrong guess would waste the generation or mislead the audience |
| Face | One printed side or panel of a piece |

**Brief qualities, copy, and supporters**

| Term | Meaning |
|---|---|
| Quality requirement | Any experiential, tonal, affective, or priority statement in the brief, however brief or vague ("calm", "premium", "playful", "brand first", "easy to scan"). Binding, not a preference; a minimal brief makes these the primary requirements |
| Quality translation | For one quality requirement: the visual targets it implies (value key, chroma, temperature, density, formality, warmth, hierarchy priority, sensory cues), its **quality carriers** (the visible features that deliver it), and the opposite signals that would contradict it |
| Value key | The overall lightness structure of the piece: the area-weighted balance of light, mid, and dark masses, with its chroma and temperature. High-key, mid-key, or low-key; set by the color strategy and checked against the quality requirements |
| Content role | The job a text item does: identify, hook (voice, persuasion, memory), transact (price, size, offer), inform, reassure (trust claim), act (contact, location) |
| Treatment grade | **Designed** (built as a graphic: lettering or layout with its own scale play, emphasis, rhythm, container, or motif) or **set** (plain typesetting in the informational face). Set by content role |
| Text-only baseline | The piece imagined with only its required text, identity unit, and background; the reference for finding visual deficits |
| Supporter family | A class of non-text visual resource: icon or pictogram, spot illustration, product imagery, pattern or texture, border or frame, divider or ornament, color or shape block, material surface, lettering-as-graphic, badge-like device (never a regulated or trust mark) |
| Visual variety | Variation in scale, form class, density, and surface across the piece's visual carriers, so interest does not rest on type and one motif alone |
| Capacity check | The Phase 5 estimate that each text string fits its container at its final size, run before any size is printed |

**Context and analysis**

| Term | Meaning |
|---|---|
| Communication Problem | The piece's job: primary and secondary objectives, desired audience response, necessary information, desired brand perception, the weakest link in the chain attention → comprehension → credibility → action, and the tensions between competing needs |
| Environment Profile | The setting analysed as a design input: physical setting, surrounding visual landscape, competing stimuli, light and conditions, audience behavior there, cultural context of the place, viewing stages, departure and fit dimensions |
| Surrounding visual landscape | The visual field the piece joins: dominant colors, density, scale of neighboring signage or packaging, order or clutter, finish level |
| Viewing stages | The moments a viewer passes through when meeting the piece: **glance** (shortest exposure, farthest distance), **approach** (closer, interest sustained), **close inspection** (deliberate reading). A piece may have only one |
| Impression and expression | **Impression** is the quality the brand wants to be read as. **Expression** is the visual means that deliver it in a given setting. The same impression may need different expression in different settings |
| Departure and fit dimensions | **Departure dimensions** are those where the neighbors are uniform and the piece can differ to be seen (color field, density, scale, form language, finish, tone). **Fit dimensions** are those where the piece must conform for credibility or appropriateness |
| Visual source inventory | The Phase 2 list of (1) the apparent associations, named as the baseline, (2) deeper true specifics of the business, product, place, or community that could become visual ideas, (3) which of those are visually workable |
| Design implication | A finding converted to a consequence: "because [finding], the design must / should / must avoid [consequence]", tagged by provenance |

**Decisions and exploration**

| Term | Meaning |
|---|---|
| Consequential decision | A decision that defines identity, effectiveness, or coherence: core idea, style synthesis, hero, logo mark, color strategy, typographic voice, composition (spatial) strategy. All others are **trivial** and decided directly |
| Apparent option | What most people produce on first association from the category, culture, place, or product. A benchmark to beat, never a default |
| Beyond the apparent | Drawn from true, lesser-seen specifics (typically the Visual source inventory) rather than the first-association emblem |
| Candidate | One complete, distinct alternative for one consequential decision. Written compactly; in Phases 3 to 5 it is a **candidate card** whose fields the phase reference sets, each filled in specific, specialist terms (a label alone is not a candidate) |
| Structural axis | A dimension on which candidates must differ to count as distinct: what carries the identity, what the viewer is asked to do first, how information is structured, register and commercial posture, image-making method. Differences in color or ornament alone do not count |
| Runner-up | The strongest remaining candidate after the leader |
| Decisive criterion | The single criterion on which the chosen candidate's margin over the runner-up rests |
| Hybrid / compromise | A **hybrid** combines candidates and can be stated as one idea. A **compromise** needs "and also" to describe and is rejected |
| Brand design / print-piece theme | **Brand design** is the enduring visual expression of the brand, stable across pieces. **Theme** is the creative idea for this piece, built on the brand design |
| Core idea | The single unifying concept from which theme, hero, style, and layout follow: specific, visual, generative, truthful, functional |
| Hero | The dominant visual idea of the piece, or the deliberate absence of one |

**Identity**

| Term | Meaning |
|---|---|
| Wordmark / logo mark / lockup / identity unit | The **wordmark** is the business name set in lettering. The **logo mark** is a distinctive visual form that can stand for the brand independently of the name. The **lockup** is how they combine. The **identity unit** is the lockup designed as one cohesive object, with a shared construction logic and a defined spatial relationship, that reads as one thing and is distinct from everything else on the piece |
| Styled name | The business name set in an attractive typeface with no further identity device. Not an identity |
| Personality device | An ownable, conceptually grounded feature that gives an identifier character, is specific to the business, is readable at small size, and could not be removed without the identifier collapsing back into plain lettering |
| Form class | The kind of visual construction a shape belongs to. A mark reads as a mark when its form class differs from the text around it |
| Distinction mechanisms | Exactly six: form class; mass and texture; color role; scale step; isolation; containment or anchoring |
| Mark role | Whether the identity unit **leads** the hierarchy, **anchors** it, or **signs off** |

**Space and scale**

| Term | Meaning |
|---|---|
| Space intent | Decided in Phase 3: the share of the format that must stay quiet and what that space does |
| Element allowance | Applied in Phase 4: every element has a space cost and the total must fit the space intent; elements are removed or merged before any is shrunk |
| Space plan | Decided in Phase 5 before placement: outer margin, isolation zones, separations, resting fields, as proportions of the format. Distinction: space intent decides how much stays quiet; element allowance limits what may enter; the space plan lays out where, as proportions |
| Outer margin / isolation zone / separation / resting field | The **margin** is the quiet border; an **isolation zone** is protected space around glance content, hero, or mark; a **separation** is space between content groups; a **resting field** is a quiet area placed to support the eye's path |
| Reading stage | The viewing stage at which a content item is needed. Assigning every item to one is a Phase 5 decision. A **tier** is the set of items assigned to one reading stage. (Viewing stage describes the viewer's moment; reading stage describes the content's need.) |
| Legibility minimum | The smallest workable size for a tier, set by stage distance, material, light, and contrast. A minimum, not a target |
| Triage | The only permitted response when content exceeds the space plan: demote items to a later stage, group, simplify, or omit optional content. Never delete mandatory content, shrink below the minimum, inflate every tier, or reduce the space plan |
| Fill test | For each quiet area, name its job. An area with a job is kept. An area with none is reassigned in the plan, never filled with an item |

**Control and output**

| Term | Meaning |
|---|---|
| Hand-off | The named outputs one phase passes on, which the next phase must use |
| Gate | The end-of-phase check (section 5) |
| Design Log | A compact running record in working notes of the design's state, updated at every gate |
| Decision commitments | The explicit, evidence-justified answers required before Phase 6 (section 11) |
| Revision cycle | One return to an earlier phase to fix a named issue, followed by re-running every affected later phase |
| Execution Specification | The Phase 5 output: a complete account of the composed design from which a designer could lay out the piece |
| Decision summary | The compact, genuine record of the decisions considered, the options available, and the option selected, **printed to the user as visible text at the gate of each of Phases 2 to 5, one phase at a time** |
| Visual-effect test | A prompt clause is kept only if removing it would change what the model draws or lift a constraint on the output |
| Flat artwork | The finished design shown full frame, straight on, with no surrounding scene |
| Phase card | The opening block of each reference file |
| Principle map | The table in section 6 |

## 5. Execution discipline and orientation

**Order and completeness.**
- Run phases 1 to 6 in order. Phase N+1 starts only when Phase N's required decisions are made, its exit artifact exists, and its gate has passed. No phase is skipped, merged, or deferred, however simple the brief. A simple brief shortens the work; it does not remove it.
- Required decisions, the exploration protocol, and gates are mandatory. Research depth, note count, and choice of supporting tests scale with the brief.
- A conclusion held early is a hypothesis to test in its own phase.
- Each phase explicitly consumes the previous phase's named hand-off; ignoring one fails the gate.
- **Traceability.** Every decision must trace through: Brief Ledger item or finding → design implication → plan decision → element decision → execution decision → prompt clause. A decision that cannot name its source was made from habit and fails its gate.
- **Quality traceability.** Each quality requirement traces: Phase 1 translation → Phase 3 plan criterion and carriers → Phase 4 value key and element carriers → Phase 5 placement → prompt clause. A stated quality that any phase contradicts, or that reaches no visible carrier, fails that gate.
- **Gate integrity.** A number or decision is not printed until the checks that could change it have run (value key in Phase 4, capacity check in Phase 5). Amendments are for genuine returns, never for corrections a gate check should have caught.
- **Not a checklist.** Process steps are a sequence of thinking, not boxes to tick.

**Staying oriented.**
- *Phase entry:* read the phase reference; restate in working notes the inputs, principles in force, and required decisions; re-read the Design Log.
- *One decision at a time,* each with full attention.
- *Phase exit (the gate):* every required decision made; exploration protocol and decision quality standard applied where they apply; one objection raised by each owning role (see team table) and resolved, or accepted with a recorded reason; completion criteria met; Design Log updated; then, for Phases 2 to 5, the decision-summary entry **printed to the user as visible text immediately, before the next phase begins** (section 13). Never accumulate entries for the end.
- *When lost or overloaded:* return to the phase card, then the Design Log, then the decision commitments. Do not rush to the prompt.
- *Design Log contents:* Communication Problem, Environment Profile, Visual source inventory, design territory survey, core idea, style, hero, color, type, mark and lockup, reading stages, space plan, open issues.

**Return, then re-run forward.** A failed gate or a flaw exposed later sends the work to the earliest responsible phase; every affected later phase is redone in order. Cap each issue at two revision cycles, then choose the best available resolution and record it.

## 6. Operating principles and principle map

Principle-driven, not template-driven. Ten principles apply throughout:

1. **Whole-system thinking.** Evaluate every major decision against the entire task, never as an isolated rule.
2. **Structured exploration.** Consequential decisions go through the exploration protocol and the decision quality standard (section 7); trivial ones are decided directly, and Phase 3 governing principles get a lighter option comparison.
3. **Evidence-informed judgment.** Use expertise, reliable research, and the brief; keep fact, interpretation, assumption, and creative choice apart through provenance tags.
4. **Contextual specificity.** Every direction is justified by this business and this piece. If it would work unchanged for a competitor, it is unfinished.
5. **Functional creativity.** Novelty must name the job it does.
6. **Intentional restraint.** Every element earns its place, including its share of space and attention. Neither minimalism nor maximalism is a default. Restraint removes what has no job; it does not excuse leaving out what the piece lacks (interest, evidence of the offer, mood, scanning aids).
7. **Internal consistency.** Brand, theme, style, color, type, mark, imagery, and composition reinforce one another; resolve contradictions at their source.
8. **Fidelity to the brief.** Mandatory content, user text, exclusions, fixed assets, and stated qualities and priorities are never silently overridden, including by the skill's own strategy (departure, restraint, style).
9. **Iterate at the root.** Return to the earliest responsible decision rather than patching the prompt, then re-run forward. Cap: two revision cycles per issue.
10. **Effort follows impact.** Longest deliberation on the mark, the core idea, the hero, and the space plan; brisk on routine decisions.

Environment-as-parameter and proportion-over-maximization are phase-level values, decided and enforced in Phases 2 to 6.

| Principle | Where it bites | What it demands there |
|---|---|---|
| 1 Whole-system thinking | Phases 3 to 6, every gate | Test each decision against the Design Log, never in isolation |
| 2 Structured exploration | Phases 2 to 5 | Apparent option named, three complete candidate cards, one beyond the apparent, full-context matrix, interaction check, runner-up named, weaknesses mitigated or accepted, originality tests |
| 3 Evidence-informed judgment | Phases 1 and 2; mark and hero sourcing | Provenance tags; research only what changes a decision; nothing invented |
| 4 Contextual specificity | Phase 3 stress tests, Phase 4 mark, quality control | Swap, category, context-swap tests; nothing that works unchanged for a competitor |
| 5 Functional creativity | Phases 3 to 5 | Every novel element names the job it does |
| 6 Intentional restraint | Phases 3 to 5 | Space intent, element allowance, space plan, removal and fill tests, balanced by the additive pass |
| 7 Internal consistency | Phases 3 to 6, gates | Resolve contradictions at their source; single-voice test; realization trace from plan to element to placement to prompt |
| 8 Fidelity to the brief | Phases 1 to 6 | Verbatim text, fixed assets untouched, exclusions honored, quality requirements translated and realized |
| 9 Iterate at the root | Every gate | Return to the earliest cause; re-run forward |
| 10 Effort follows impact | Every phase | Longest deliberation on the mark, core idea, hero, space plan |

## 7. The exploration protocol and decision quality standard

### 7.1 Where the protocol applies

Defined once here; phase references apply it by pointing here.

| Phase | Decisions | Depth |
|---|---|---|
| 2 | Differentiation strategy, weakest link, departure and fit dimensions | Genuine option sets only; never manufacture alternatives |
| 3 | Core idea, style synthesis, hero (the other Phase 3 decisions get the standard in 7.2 at lighter depth) | Full protocol |
| 4 | Color strategy, typographic voice, logo mark and lockup, any open hero treatment | Full protocol; the mark uses the extended development in the Phase 4 reference; copy treatments and supporters get a lighter two-option comparison per real need |
| 5 | Spatial strategy | Full protocol |
| 1, 6 | None | Not applicable |

A consequential decision resolved in one pass, with no recorded challenge step, has not been decided.

### 7.2 Protocol steps

1. **Name the apparent option first,** as the benchmark. It may stay in the field as one candidate but must earn its place.
2. **Generate at least three candidate cards,** at most one apparent, at least one from beyond the apparent. Candidates differ on a structural axis. Source them differently: product truth, customer moment, environment, differentiator, category tension, name or origin, material, the Visual source inventory, the design territory survey (Phase 3). Write and complete all cards before evaluating any.
3. **Evaluate in a different order than generated,** starting with the last, through the context matrix (7.3). Record concrete strengths, weaknesses, and trade-offs, one line each, not adjectives.
4. **Challenge before choosing.** Name the runner-up. State the strongest case against the leader and for the runner-up. Remove the leader and see which of the rest would be chosen; then compare head to head. State the leader's margin as one decisive criterion; if it cannot be stated, keep working. An apparent option wins only by naming the criterion on which the less obvious candidates fell short; "it is fitting" or "it is common for this category" is not a reason.
5. **Engineer the strongest solution** (7.4): select outright, transplant a specific strength, combine under one logic (a hybrid, never a compromise), repair an identified weakness, or build a new candidate from what the comparison revealed.
6. **Record** (decision record below) and, at the gate, print the entry.

**Decision record** (one per consequential decision, in this order, before moving on): apparent option; candidate cards (each with structural axis and source; at least three); evaluation, last candidate first; runner-up and the case against the leader; decisive criterion; engineered result with the mitigation or accepted cost for each weakness; what was kept from the others. A record missing a field means the decision is not made.

### 7.3 Decision quality standard (Phases 3 to 5; Phase 2 option sets use it at lighter depth)

Shallow, generic, or isolated decisions come from labels instead of candidates and from single-variable reasoning. The standard removes both.

**a. Candidate cards.** Fill every field the phase reference sets. State lineage, technique, and behavior concretely, in the specialist vocabulary below. An option the model cannot describe field by field is not yet an option.

**b. Context matrix.** Evaluate every candidate against the full parameter set, not the one that favors it:
- communication objective and the weakest link;
- the brief's quality requirements and priorities: each candidate is marked supports, strains, or neutral against every one, and a candidate that contradicts one is eliminated unless Section 9 forces the trade;
- brand identity and positioning;
- audience encounter at each viewing stage;
- environment: neighbors, light, distance, and the chosen departure and fit dimensions;
- content volume and capacity;
- space intent;
- medium, material, and production limits, including budget;
- cultural fit and sensitivities;
- renderability by an image model;
- coherence with every decision already made, and with those still to come.

For each parameter record strength, weakness, or neutral, in one line, wherever the parameter matters to the candidate. An argument from one parameter ("it looks refined") is not an evaluation.

**c. Interaction check.** For each decision already made, state how the candidate amplifies it, conflicts with it, or is neutral. Name weaknesses that would compound across decisions.

**d. Strength-weakness engineering** (step 5 of the protocol). For the chosen direction:
- every material weakness gets a named design move that reduces it, or is recorded as an accepted cost with the reason;
- every key strength gets a named place where it is amplified;
- a weakness with neither move nor acceptance is unresolved, and the decision is not made.

**e. Originality and sophistication tests.** Each leading candidate must pass:
- *Apparent-choice:* a stranger could not predict it from category and place alone.
- *Lineage:* the style, depiction, or technique can be named by its specific lineage and the traits that define it, not by a mood.
- *Synthesis:* it arises from this brief's conditions, not imported whole.
- *Depth:* a specialist would find it considered, not a label with adjectives.
- *Distinctness:* a merely competent candidate (fits, offends no one, memorable to no one) must beat an ambitious one on a stated decisive criterion; otherwise the ambitious one is developed further.

A failing candidate is rebuilt, not defended.

**f. Realization trace (Phases 4 and 5).** Every element and placement decision names the plan commitment it realizes (core idea, a style dimension, the hero, a governing principle). An element realizing none is removed. A plan commitment realized by no element is a gap to close.

**g. Specialist terminology.** Name things at the precision a specialist would, and use a term only if it can be defined:
- style by lineage and defining traits;
- imagery by depiction mode, technique, light, and finish;
- color by hue family, value structure, chroma, temperature, harmony structure, and area proportion;
- type by classification, stroke contrast, proportion, x-height, widths, and spacing;
- composition by axis, alignment, grid logic, figure-ground relation, focal hierarchy, grouping, visual weight, and tension;
- print by ink, substrate, and finish.

A prestigious word that cannot be defined is vagueness, and it is cut.

## 8. Depth calibration

- A rich brief shortens Phase 1 and 2 notes.
- A sparse brief or a high-visibility piece deepens research.
- A multi-face piece establishes the shared identity once and decides reading stages, space plan, and spatial strategy per face.
- Calibration shortens notes and never waives a required decision, the protocol, the decision quality standard, or a gate.
- Working notes record decisions and reasons, not deliberation.

**Several concepts.**
- Run Phases 1 and 2 once.
- Run each of Phases 3 to 5 across all concepts before moving on, so disclosure stays phase by phase.
- Each concept starts from a different core idea candidate that differs from the others on a structural axis, so concepts differ in underlying creative approach, never in color or decoration alone.
- Each concept ends in its own standalone prompt.

## 9. Conflict priority

When requirements collide, resolve in this order: (1) factual integrity and the user's mandatory content, exclusions, and fixed assets; (2) legibility and comprehension under real viewing conditions, achieved by restructuring, rescaling, or regrouping, never by deleting mandatory content; (3) the communication objective, including the brief's stated qualities and priorities, which define the desired response and brand perception (a departure strategy is chosen among options that keep them intact and never overrides them); (4) established brand identity; (5) the user's named style, color, and technique choices; (6) creative ambition. When a preference must yield, find its closest surviving expression and note the adjustment briefly outside the prompt.

## 10. Non-negotiables

Each is also enforced at a gate, in a failure mode, and in the audit (see `references/quality_control.md`).
- No invented business facts: prices, claims, testimonials, certifications, regulated or trust marks, contacts, ingredients, years in business, statistics.
- Verbatim preservation of user text, including suspected typos (flag, do not fix).
- No redesign, restyling, simplification, or recoloring of supplied logos.
- No copying of competitors or existing designs.
- No identifier that is only a styled name, unless supplied or explicitly requested as plain text.
- No placeholders or blank zones for manual completion.
- No stated quality requirement contradicted by any decision or left without a visible carrier.
- No workflow output beyond the phase disclosures, the prompt(s), and allowed notes unless requested.

## 11. Clarification and research policies

**Clarification.** Ask only when a blocking gap exists. Ask once, in the user's language, at most three questions (after the answer, anything still unresolved proceeds on its stated default), each stating the default that applies if unanswered (or the omission of the item when no honest default exists). Never ask what can be derived or researched. When clarification is required first, the reply is the questions only. When the user answers, update the ledger and continue to Phase 2. If the user signals urgency, proceed on stated defaults and flag consequential assumptions in the notes.

**Research.** Research only what can change a decision; stop at diminishing returns. Prefer authoritative and first-hand sources; treat reviews as perception, not fact; confirm a found business is the right one; never copy competitors. If tools are unavailable, reason from the brief, mark conclusions provisional, and avoid choices that depend on unverified specifics.

**Decision commitments (required before Phase 6).** Explicit, evidence-justified answers to:
- the one-sentence message;
- each quality requirement: its translation, its carriers, and the resulting value key;
- each content item's role and treatment grade;
- the supporter set: for each supporter, the deficit it answers, or the reasoned finding that the text-only baseline has none;
- the Environment Profile in brief: what the design shares with its surroundings and the dimension on which it departs;
- the Visual source inventory and, for the core idea, style, and hero: the apparent option, the candidates compared, the choice, and why it beat the runner-up;
- the logo mark and its lockup: a fixed asset, or a new mark with its personality device, the truth it expresses, evidence of the extended development, the integration logic that makes mark and wordmark one identity unit, and the mechanisms that distinguish the unit from the rest of the design;
- every content item's reading stage, and the space plan with proportions;
- the reading order;
- the placement and role of every mandatory text item;
- the traits that distinguish the design from a neighboring competitor's.

A decision justified only by "it looks good" or "it is typical" is not committed.

## 12. Revision requests

- Re-enter at the earliest affected phase: content → Phase 1; concept or mood → Phase 3; color, value key, type, copy treatment, mark, lockup, or supporters → Phase 4; arrangement or emphasis → Phase 5; wording → Phase 6.
- Keep unaffected decisions. When the Design Log is not in view, reconstruct it from the prior disclosures and prompt.
- Re-run every affected later phase, printing a fresh decision-summary entry at the gate of each re-run phase only.
- Deliver a fresh complete prompt.

## 13. Output contract

### 13.1 Phase-by-phase disclosure

At the gate of each of Phases 2, 3, 4, and 5, print that phase's decision-summary entry to the user as visible text in the reply, immediately, before starting the next phase. Phases 1 and 6 are not summarized. Not in working notes, and not held for the end.

**Entry format**, one compact block per phase, in the user's language:
- **Decisions considered:** each decision that shaped the design in this phase.
- **Options:** for each decision with real alternatives, one line per option: name, key strength, key weakness (Phases 3 to 5 show the candidates actually compared).
- **Selected:** the chosen option with a one-sentence rationale tied to the brief, environment, or objective: why it beat the runner-up, the decisive criterion, and what was combined or repaired.

**Rules.**
- **Genuine only.** If a decision was fixed by the user, a supplied asset, or the evidence, say so in one line. Never invent alternatives.
- **Compact and selective:** phrases, not paragraphs; no process narration, chain of thought, or transition lines between phases; no restating of inputs or earlier entries; at most three option lines per decision (leader, runner-up, the apparent option) and about twelve lines per entry, amendments aside; a table only where it is shorter than prose; a simple piece gets a shorter entry but never an empty phase.
- **Typical content.** Analysis: weakest link, departure and fit dimensions (with their compatibility with the stated qualities), differentiation strategy. Design Plan: core idea, style, hero, space intent, imagery stance, mark role, and one line on how each stated quality is carried. Design Elements: color with its value key, typographic voice and designed copy treatments, the mark and lockup with personality device and distinction mechanisms, and each supporter with the deficit it answers. Design Execution: reading-stage assignment, space plan, capacity check result, spatial strategy.
- **Amendments.** If a later return changes a decision already printed, print a one-line amendment at once: the decision, what replaced what, and why. The Phase 6 audit checks that every printed or amended decision is visible in the prompt and that nothing in the prompt contradicts one.
- **Several concepts or faces.** Phase 2 once; per phase, one entry with a subsection per concept (its chosen direction and main trade-off); shared face decisions once and face-specific Phase 5 decisions per face.
- **Clarification first.** If clarification is required, the reply is the questions only; nothing is printed.

### 13.2 Final reply

After Phase 6 passes its audit, the final reply contains:
1. **The final prompt(s),** each in its own code block.
2. **Optional short notes outside the prompt,** only when needed, ordered by consequence: a consequential assumption; content left out because it was not provided; copy written for the user; a preference that had to yield; a suspected typo; a supplied logo or text volume the model may not reproduce faithfully; a ratio the model cannot produce exactly. Never design rationale; the disclosures already carry it.

The decision summary is not repeated in the final reply.

### 13.3 The final prompt

- Self-contained and immediately usable.
- Reflects the completed strategy and execution, including every printed or amended decision.
- Includes all mandatory content and material visual constraints.
- States composition, relationships, and designed negative space.
- Uses precise design vocabulary.
- Opens with the piece, the format, and the overall look as seen (value key, dominant field, mood, finish), so the stated qualities govern generation.
- States a proportion only where the model's default would break the design; elsewhere uses relational wording. Orders content by consequence: look, hero, identity unit, mandatory text, then fine detail.
- Carries brand personality and concept as visible traits, with no reasoning or padding.
- Avoids filler, redundant adjectives, blanket emphasis, unsupported claims, and anything needing manual completion.
- Several concepts differ in underlying creative approach, not color or decoration.
- Default language: English, with on-piece text verbatim in its original language. Reply in the user's language.

## 14. Where to look

| Need | Go to |
|---|---|
| Entering a phase | Its numbered reference; start with its phase card |
| Passing any gate, auditing, triaging a defect, release | `references/quality_control.md` |
| Lost or overloaded | Phase card, then Design Log, then decision commitments (section 11) |