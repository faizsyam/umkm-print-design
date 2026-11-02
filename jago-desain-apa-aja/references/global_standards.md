# Global standards: principles, conflict priority, non-negotiables (all phases)

The ten design principles every decision obeys, the order in which colliding requirements are resolved, and the rules that are never broken.

**Read this when:** on entering Phase 2 (and reopen a principle, the conflict order, or a non-negotiable whenever a decision is in doubt). The non-negotiables are also summarized in `SKILL.md`.

**Inputs needed:** S and the Phase 1 Forward block.

## 5. Principles

1. **Whole-system thinking.** Judge every decision, major or minor, against the entire design: the role it plays, its relationships to other elements and to the information, its effect on hierarchy, space, and communication, and what it constrains downstream. A decision optimized alone, or taken from a familiar template or habitual pattern, is unfinished.
2. **Structured exploration.** Consequential decisions go through the protocol (`exploration_protocol.md`); trivial ones are decided directly. A familiar solution is admissible only after it has beaten alternatives derived from this problem.
3. **Evidence-informed judgment.** Use expertise, reliable research, and the brief. Keep given, researched, inferred, and creative-choice content apart with provenance tags; an inference carries the reasoning that supports it.
4. **Contextual specificity.** Justify every direction by this subject and this deliverable; a direction that works unchanged for a peer is unfinished. A look-shaping attribute that no decision names is filled by the image model's apparent value, so specificity must reach every such attribute.
5. **Functional creativity and restraint.**
   - Novelty names its purpose (faster read, truer message, longer impression).
   - Every element carries a purpose line (`terms_design_system.md`): the function it serves toward the piece's job, what is lost without it, and the effect it must have on the viewer. It earns its place and its share of space and attention through that purpose, and no other element serves the same one. It must also be worth its marginal cost (space, attention, rendering risk): the piece is better with it than with the next-lighter alternative (nothing, spacing alone, a smaller or simpler form).
   - Design maximizes that effect within the element's rank, weight ceiling, style, and relationships.
   - Neither minimalism nor maximalism is a default, nor is any supporter. Plainness is a decision with a reason, never the safe default.
   - Restraint removes what has no purpose. It does not excuse omitting what the piece lacks (interest, character, evidence of the offer, mood, scanning aids, surface and material character).
   - **Reduction never costs character:** the fewer the elements, the more each must carry (depth within it, an ownable trait, a link to its neighbors). Character is carried first by what the piece already needs (depth in the hero and lettering, color logic, edge character) and added as new elements only where those cannot carry it.
   - Decoration never outranks the required information it serves.
6. **Explicit rank, budgeted space, and cumulative load.**
   - **Rank.** Attention is directed, never left to compete: every element holds a stated rank, and ranks are separated by contrast the viewer cannot miss. Form follows purpose: each text and element is styled for the job it does.
   - **Importance is not prominence.** Prominence is the combined effect of allocated area, scale, value and chroma contrast, weight, position, and the container or treatment around it, judged for each element as drawn (its text together with its container, fill, edge, and effect). It follows rank.
   - **Space is a budget, set before content and spent top-down.** Phase 3 fixes the quiet share and the rough share each occupying role may take. Every later size derives from its zone's share (format, then zones, then elements, then text tiers) and is never set by the element's own wish. Space is allocated before content is placed, at every level (outer margin, separation between zones, padding inside each zone, gaps between related elements), each scaled to the format, its viewing distance, and content density. A zone's share follows its communication role, never the volume of its content.
   - **Quiet is genuinely open, protected, and local.** Quiet is contiguous, calm, undecorated ground with a job; decorated ground is occupied. Breathing room is judged where content sits (around each zone, between neighbors, inside each container): open area parked elsewhere does not compensate for a tight zone. Area the plan does not need is never spent on enlarging elements or adding decoration.
   - **Crowding is a fit failure,** resolved in the fixed order of the fit ladder (`terms_design_system.md`, Fit ladder (full)), with the quiet share narrowed last. It is never resolved by shrinking below legibility minimums or distorting letters. A composition that fits only with every item at its minimum and every gap at its tightest does not fit.
   - **Visual load is judged cumulatively.** Each element can be justified alone yet overload the whole. Information, imagery, supporters, containers and their edges, designed and rendering treatments, surface, and color intensity are counted together against the budget and the stage's parsing time.
7. **Internal consistency.**
   - Brand, theme, style, color, type, mark, imagery, and composition reinforce one another; resolve contradictions at the source. One primary visual language leads; secondary rendering treatments (outline, shadow, gradient, texture, highlight, dimensional effect) are few, named, and applied by role.
   - **Grouping by referent.** Group content by what it refers to, not only by when it is read. Text that labels, explains, prices, or substantiates a depicted thing is composed with it, unless the hero carries the message alone. Parallel items are separate units, each placed by its own referent, unless the viewer should read them as one claim.
   - **Form shows relation.** Content that relates internally (sequence, comparison, hierarchy, dependency) shows that relation in form, read from the content, never from a template.
   - **Hierarchy, sequence, and placement agree.** The attention hierarchy (what is noticed first), the reading sequence (the order content is taken in), and the placement (where each item sits) are planned together and stated without contradiction through the final prompt. Relationships are specified, not implied: each element's alignment, gap, relative position, and overlap or clearance to its neighbors.
   - **Equivalent items** (same role, rank, and function) share one typographic treatment wherever they sit, regardless of length: size encodes role and rank, never length, and layout absorbs length. Variation needs a difference in importance, role, emphasis, or purpose. Equivalent units (cards, rows, panels) also share outer dimensions and internal structure, so differing content volume is absorbed inside a constant frame.
8. **Fidelity to the brief.** Mandatory content, user text, exclusions, fixed assets, stated qualities (named style, color, technique included), and priorities are never silently overridden, not even by the skill's own strategy. Constraints are material: seek distinction inside them by committing fully, never by diluting or evading them.
9. **Effort follows impact.** Deliberate longest on the mark, core idea, hero, and space plan; move briskly on routine decisions.
10. **Context before convention.** Universal principles (purpose, hierarchy, coherence, specificity) hold in every medium. What the medium imposes, what its audience relies on, and what it affords are derived from the actual deliverable in Phase 2, never assumed from the medium's name. Keep any convention the audience relies on to read or use a piece wherever departing would cost them effort or credibility; spend distinction on expression and identity.

## 6. Enforcement map

Every standard has a step that enforces it and a check that tests it. A gate check with no source here is sourced in its own file.

| Standard | Enforced at | Checked by |
|---|---|---|
| 1 Whole-system thinking | each decision judged against the whole (`workflow_and_state.md` section 4, Phase entry); system evaluation (`09_element_system_evaluation.md`); composition review (`14_backgrounds_review_and_gate.md`) | contradiction scan (Phases 3 to 5) |
| 2 Structured exploration | `exploration_protocol.md` | gate step 2 (`quality_gates.md` section 1) |
| 3 Evidence-informed judgment | provenance tags in the ledger (`01_brief_and_requirements.md`) and implications (`02_research_and_analysis.md`) | gates 1 and 2; gate step 3 (every decision names its source) |
| 4 Contextual specificity | stress tests (`04_principles_and_plan_evaluation.md` G); decided-attribute rule | swap, context-swap, and decided-attribute tests; prompt audit, Specifics |
| 5 Functional creativity and restraint | purpose line per element (`05` to `08`); removal and distinct-purpose checks (`09_element_system_evaluation.md`) | gate 4; originality and load-and-fit tests |
| 6 Rank, budgeted space, cumulative load | `04_principles_and_plan_evaluation.md` (space intent), `11_space_plan_and_spatial_strategy.md`, `12_hierarchy_and_element_placement.md`, `13_load_balance_and_capacity_checks.md` | load budget test (3); element allowance (4); load and capacity checks (5); load-and-fit test |
| 7 Internal consistency | `10_stage_assignment_and_relationship_map.md`, `12_hierarchy_and_element_placement.md`, `16_prompt_clauses_and_delivery.md` | contradiction scan; composition review; prompt audit, Order and roles |
| 8 Fidelity to the brief | `01_brief_and_requirements.md`; every later phase | brief-quality test; prompt audit, Mandatory content, Fixed assets, Qualities |
| 9 Effort follows impact | decision classes (`exploration_protocol.md` section 1) | gate step 4 (objection on the riskiest decision) |
| 10 Context before convention | Environment Profile (`02_research_and_analysis.md` C) | gate 2 (profile checks) |
| NN: no invented facts | `01` E; `02` G; `07` | gate 1; prompt audit, Exclusions |
| NN: user text verbatim | `01` C; `16` E | prompt audit, Mandatory content |
| NN: supplied logos and characters | `01` D; `06` C; `07` | gates 4; prompt audit, Fixed assets |
| NN: no copying | `02` G; `03` B | gates 2 and 3; prompt audit, Exclusions |
| NN: no styled-name-only identifier | `06` C | gate 4; prompt audit, Identifier |
| NN: no placeholders or blank zones | `12` D (reserved asset panel) | prompt audit, Hygiene |
| NN: no stated quality contradicted | `01` D; carrier map (Phase 3) | brief-quality test; `quality_gates.md` section 9 |
| NN: no suggestion without the user's yes | `00_conversation_voice_modes_and_intake.md` section 3 | reply audit |
| NN: no unfamiliar jargon, no walls of text | `ux_wait_notes_entries_and_final_reply.md` sections 5 to 8 | reply audit |
| NN: no workflow output beyond the defined messages | turn map (`00_conversation_voice_modes_and_intake.md`) | reply audit |

NN = non-negotiable (section 8). Phase file letters (`01` E) name the section of that file.

## 7. Conflict priority

When requirements collide, resolve in this order:
1. factual integrity; the user's mandatory content, exclusions, and fixed assets;
2. perception and comprehension under the real conditions of encounter, for the full range of the audience (low vision and color-vision differences included), achieved by restructuring, rescaling, or regrouping, never by deleting mandatory content;
3. the user's stated requirements: quality requirements (named style, color, technique included) and priorities;
4. the communication objective and the strategy serving it (differentiation, departure), chosen only among options that keep priority 3 intact;
5. established brand identity not supplied as an asset;
6. creative ambition.

A lower priority yields only to a higher one and keeps its closest surviving expression. Within priority 2, space yields last: the fit ladder (`terms_design_system.md`, Fit ladder (full)) orders what gives way when content must fit, and the quiet share narrows only at its final rung. A named choice that weakens the objective stays: mitigate inside it and offer the concern once as a labeled suggestion (in the entry; in auto mode, in the key decisions). Phase 2 tensions take their lead side from this order where it decides them; Phase 3 decides the rest.

## 8. Non-negotiables

- **No invented facts** about the subject: figures, claims, testimonials, ratings or levels, certifications, regulated or trust marks, contacts, credentials, dates, statistics, specifications. A design never implies a claim, endorsement, or authority the subject does not hold.
- **User text is verbatim,** suspected typos included (flag, never fix).
- **Supplied logos and characters** are never redesigned, restyled, simplified, or recolored. No figure (mascot, character, person) is introduced unasked; never a likeness of a real person; never an implied endorsement.
- **No copying** of competitors, peers, or existing designs.
- **No identifier that is only a styled name,** unless supplied or explicitly requested as plain text.
- **No placeholders or blank zones** for content the skill should create. The one reserved region is an asset panel for a supplied asset the generator cannot reproduce faithfully (a scannable code, a supplied photograph or logo file that cannot be attached): designed into the composition, flagged in the notes, never imitated.
- **No stated quality** contradicted by any decision or left without a visible carrier.
- **No suggestion** enters the brief or the design without the user's yes; suggestions are labeled and never counted as facts.
- **No unfamiliar design jargon** and no walls of text in anything the user reads; the user's own vocabulary sets the register.
- **No workflow output** beyond the messages the UX reference defines, unless requested.

## Quality checks

- Pass: each standard is checked where the enforcement map (section 6) says, and every collision was resolved in the order of section 7.

## Next

Read `exploration_protocol.md` (if not yet read), then `02_research_and_analysis.md`. Return to this file whenever a conflict between requirements appears.
