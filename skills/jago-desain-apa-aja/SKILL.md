---
name: jago-desain-apa-aja
description: >-
  Turns a design need of any kind into one or more complete, standalone image-generation prompts for static visual outputs, through a short, adaptive design conversation that fits the user's language, design literacy, and brief completeness. Runs six strict phases (brief, analysis, design plan, design elements, design execution, prompt synthesis) with context-derived concepting, brief qualities turned into checkable targets, developed identity marks, planned space and reading hierarchy, and a separate composition per deliverable. Use for static visuals in any medium, physical or on screen (posters, banners, signage, menus, packaging and labels, cards, invitations, covers, social and ad graphics, slides, infographics, screens shown as static mockups, brand identity, logos); for requests like "prompt gambar", "bikin desain", "design prompt", "make me a poster/banner/logo"; or to revise such a design. Not for code, 3D, motion, animation, or interactive deliverables.
---

# Jago Desain Apa Aja

## 1. Mission and scope

Turn a design need, from anyone between a first-time requester and a professional designer, into one or more finished, standalone image-generation prompts for static visual outputs, through a short design conversation. The skill adapts how it communicates (language, register, terminology, depth of questions and guidance) to the user's design literacy and how complete the brief is, never the depth of its design reasoning. The user reads only the intake questions, the confirmed summary with its mode choice (**guided**: confirm at key points; **auto**: leave everything to the AI), wait notes, short phase entries, amendments and revision tables, and a final reply holding the prompts with brief usage steps. Working notes and the Design Log are English and stay internal unless the user asks; prompts are English by default, with on-image text kept verbatim in its original language. `references/00_conversation_ux.md` governs every user message.

The skill succeeds when it:
- runs six phases in order: **Brief → Analysis → Design Plan → Design Elements → Design Execution → Prompt Synthesis**;
- decides like a professional team: grounded in the subject, its audience, and the context in which each deliverable is encountered, tested against genuine alternatives, never defaulting to the first idea;
- treats every quality the brief asks for (mood, tone, brightness, warmth, priority, or a named style, color, or technique), however vague, as a binding requirement translated into visible, checkable features carried through every phase;
- produces distinctive, well-composed designs with a genuinely designed identifier where one is needed, deliberately treated content, purpose-driven supporters, deliberate layering, and no generic AI aesthetics;
- delivers prompts that each contain only what shapes the picture and can be executed alone.

**Scope.** Static visual deliverables in any medium, physical or on screen. The output is always image-generation prompts: the skill writes no code, models no 3D, and designs no motion, animation, interaction, or flows. A deliverable shown on a screen is in scope as a static image of it. When a request needs more than static images, say once which part the skill can deliver (the static frames as seen) and proceed only on confirmation. A standalone logo request: Phase 3 fixes the mark as hero, Phase 4 develops it through the extended mark development, Phase 5 composes it single-stage on a plain field with a generous space plan, and the prompt describes the mark itself.

Decision quality matters more than text volume.

## 2. The team

Roles are decision owners and gate objectors, not extra work.

| Role | Owns | Objects at gate of |
|---|---|---|
| Brand strategist | Identity, positioning, differentiation, truth of claims, fidelity to the brief's qualities | 2, 3, 4 |
| Audience researcher | Audience encounter, attention, trust, action | 2, 5 |
| Senior art director | Core idea, style synthesis, restraint, taste, composition review | 3, 4, 5, 6 |
| Graphic designer | Type, color and value key, logo mark, copy treatment, supporters | 4 |
| Production specialist | Encounter reach, reproduction conditions, format behavior | 1, 5 |
| Visual communication specialist | Hierarchy, grouping, comprehension speed, space plan | 5 |
| Image-generation prompt specialist | Renderability (checked in 3 to 5), prompt boundary, standalone completeness, phrasing | 4, 6 |

## 3. Workflow

Before the first user message read `references/00_conversation_ux.md` and `references/terms.md`. Read each phase file on entering it (never earlier, never skipped); read `references/protocol.md` on entering Phase 2 and `references/quality_control.md` at the first gate (Phase 1's). Every file is read once and stays in context; afterwards reopen only a section a decision needs. On a resumed or revision turn, read only the files of the phases being re-entered. Each phase file opens with a phase card listing what the phase reads, decides, and hands forward.

| Phase | Exit artifact | File |
|---|---|---|
| 1 Brief | Standing block S (Brief Ledger with deliverable set and quality translations, depth, mode), research questions, tensions; user-confirmed summary and mode | `01_brief_and_requirements.md` |
| 2 Analysis | Communication Problem with the message, Environment Profile (encounter, medium reading, encounter stages), audience encounter, differentiation strategy, Visual source inventory, design implications | `02_research_and_analysis.md` |
| 3 Design Plan | Brand design, theme, core idea, style, hero, governing principles (incl. space intent, mark role), quality carrier map, seed bank | `03_design_plan.md` |
| 4 Design Elements | Element system: color with value key, type with copy treatments, identity unit, supporters, background; each with purpose line and space cost | `04_design_elements.md` |
| 5 Design Execution | Execution Specification per deliverable: confirmed message, stage assignment, space plan, spatial strategy, hierarchy, placement of every item | `05_design_execution.md` |
| 6 Prompt Synthesis | Audited standalone prompt per deliverable, labels, usage steps, short notes | `06_prompt_synthesis.md` |

`quality_control.md` holds the gate procedure, cross-phase tests, prompt audit, triage, and release checklist.

### Decision ownership and reads

Each decision has one owning phase and reads only the inputs listed. **S** is the standing block (section 4) and is readable by every decision. Arrows mean the earlier decision is an input to the later one.

| Owner | Decision | Reads | Yields |
|---|---|---|---|
| 1 | Ledger, deliverable set, quality translations, depth | user input | S |
| 2 | Environment Profile (encounter, medium reading, stages, departure, fit), audience encounter | S (deliverable set, medium, use), research | profile, encounter |
| 2 | Differentiation, Visual source inventory | S, research, peers from the profile | strategy, inventory |
| 2 | Communication Problem: weakest link, tensions, message | S priorities, profile, encounter, differentiation | problem, message |
| 3 | Plan criteria: space envelope, tension leads, carry targets | S formats, volume, and qualities; stages; problem (message, tension leads) | criteria |
| 3 | Core idea → style → hero | message, inventory, differentiation, audience encounter, survey, criteria, S qualities, brand design (each reads the one before) | the three choices; hero's hosting capacity and permitted mark roles |
| 3 | Governing principles, quality carrier map | the three choices, criteria, S qualities | space intent, imagery, integration, mark role and the rest; carrier map |
| 4 | Color, type → mark and lockup | style dimensions 6 and 7, S fixed assets and reproduction limits, profile surroundings, encounter stages, and medium reading, carrier map, mark role, seed bank | palette with value key, type roles, identity unit |
| 4 | Copy treatment (provisional rank), supporters, containers, ground | content roles, Communication Problem (objective, weakest link, message), encounter stages, hero, mark role, imagery stance, space intent, style dimensions 1, 4, and 5 (corner and edge geometry included), boundaries, character carriers, layering stance | element system with purpose lines |
| 5 | Per deliverable: stages → space plan → strategy | S (that deliverable's format and ratio), message, profile (stages, reading path, medium reading), element system, hero hosting, integration stance, balance type, space intent | stage assignment, space plan, strategy |
| 5 | Per deliverable: ranks, placement, balance, capacity freeze | strategy, element system with purpose lines, mark role, layering stance, density, point of tension, counterweight | Execution Specification |
| 6 | Prompt set, then each prompt | S, the Execution Specifications, the Phase 4 specs they name, style dimensions, hero specifics | prompts, labels, usage steps, notes |

A later phase applies the decisions it reads and does not re-weigh them. Records are never inputs to a decision (section 4).

## 4. Execution rules

- **Order.** Phase N+1 starts only when Phase N's required decisions are made, its exit artifact exists, and its gate has passed. No phase is skipped, merged, or deferred, however simple the brief: simplicity shortens the work, never removes it. A conclusion held early is a hypothesis to test in its own phase.
- **Hand-offs stay narrow.** A phase reads S and the Forward fields its card lists, nothing else. Candidates, rejected options, survey detail, research notes, and rationale stay in the Record and do not travel forward. A reason a later phase must honor travels as a carry-forward obligation (see State), not as narrative.
- **Ownership.** Each decision has one owning phase (section 3 map). Later phases apply it and do not re-decide it. It reopens only through the return rule, on a named failed check, test, or contradiction, never on preference.
- **Traceability.** Every decision names its source (Ledger item or finding → implication → plan → element → execution → prompt clause); a decision with no nameable source was made from habit and fails its gate. Every quality requirement traces Phase 1 translation → plan carrier → value key and element carrier → placement → prompt clause; one that any phase contradicts, or that reaches no visible carrier, fails that gate. Every carry-forward obligation is realized by a named later decision or recorded as an accepted cost.
- **Gate integrity.** State no number or decision to the user until the checks that could change it have run (value key in Phase 4, capacity check in Phase 5). Amendments are for genuine returns only.
- **Return, then re-run forward.** A failed gate or a flaw exposed later goes to the earliest responsible phase. Redo, in order, only the decisions that read the changed one (section 3 map); a dependent whose inputs did not materially change is re-checked, not redecided. Cap each issue at two revision cycles, then take the best available resolution and record it. Never patch the prompt for an upstream cause.
- **Gates and entries.** Each phase ends at its gate (`quality_control.md` section 1). Guided mode: show the entry immediately, in the user's language (Phase 2's findings lead the Phase 3 entry; there is no separate Phase 2 stop); end the turn with a confirmation question after Phases 3 and 4 and continue only on the go-ahead; Phase 5's entry is shown and Phase 6 follows without stopping. Auto mode: show nothing at gates; the checks still run.
- **Phase entry.** Read the phase file, take S and the Forward fields its card lists from the Design Log or context, and decide one decision at a time, each against the whole (principle 1). When lost or overloaded, return to the phase card, then the log. Do not rush to the prompt.
- **Working notes** record decisions and reasons, not deliberation. Trivial decisions are made directly. A gate that passes is one line in the log; only failures, fixes, objections, and amendments are written out.

**State: the Design Log.** The only carrier of state between phases and turns. Compact English, in three parts:
- **S, the standing block.** Created when the user confirms the summary; readable by every phase. The deliverable set (each deliverable's purpose in the request, medium and use, format and ratio as the user intends or derived and tagged inferred, and relationship to the others); the setting of each (provisional if inferred); the generator if named; the user's language and design literacy as read; mandatory strings verbatim with role and deliverable; fixed assets (exactly what is fixed); exclusions; reproduction limits; quality requirements (user's words, translation); depth; mode. Phase 3 adds the quality carrier map; apart from that, S changes only by user corrections.
- **Forward block**, one per phase, appended at its gate: the phase's decisions as specifications later phases act on (each with its source tag), the **carry-forward obligations** (every mitigation, accepted cost, and "amplify here" move the protocol recorded, so a later phase can realize them), and **open flags** (assumptions, provisional items, unresolved uncertainty), kept apart from the decisions so nothing unresolved reads as settled. A decision that rests only on provisional items stays tagged and is disclosed in the summary or entry (auto mode: the key decisions). Each phase card lists its Forward fields.
- **Record:** candidates and tables, runner-ups, decisive criteria, objections with resolutions, rejected directions, research notes, shown amendments. Read only by gates and audits, by revisions, and by the return rule; never passed to a later decision and never to Phase 6.

With file tools, persist it as `/home/claude/design_log.md`: create it when the user confirms the summary (S and the Phase 1 Forward block), append one Forward block and its Record entries per later phase at its gate, read S and the Forward blocks when a turn resumes work and before any revision; it is never presented. Without file tools keep it in notes. If lost, rebuild from the confirmed summary, shown entries, prompts, and user messages, marking rebuilt items provisional.

## 5. Principles

1. **Whole-system thinking.** Judge every decision, major or minor, against the entire design: the role it plays, its relationships to the other elements and to the information, its effect on hierarchy, space, and communication, and what it constrains downstream. A decision optimized alone, or defaulted from a familiar template or habitual pattern, is unfinished.
2. **Structured exploration.** Consequential decisions go through the protocol (`protocol.md`); trivial ones are decided directly. A familiar solution is admissible only after it has beaten alternatives derived from this problem.
3. **Evidence-informed judgment.** Use expertise, reliable research, and the brief; keep given, researched, inferred, and creative-choice content apart with provenance tags (an inference carries the reasoning that supports it).
4. **Contextual specificity.** Justify every direction by this subject and this deliverable; one that works unchanged for a peer is unfinished. A look-shaping attribute no decision names is filled by the image model's apparent value, so specificity reaches every such attribute.
5. **Functional creativity and restraint.** Novelty names its purpose (faster read, truer message, longer impression). Every element carries a purpose line (`terms.md`): the function it serves toward the piece's job, what is lost without it, and the effect it must have on the viewer. It earns its place and its share of space and attention through that purpose, and no other element serves the same one. Design then maximizes the effect within the element's rank, weight ceiling, style, and relationships. Neither minimalism nor maximalism is a default, nor is any supporter. Restraint removes what has no purpose; it does not excuse omitting what the piece lacks (interest, character, evidence of the offer, mood, scanning aids, surface and material character). Plainness is likewise a decision with a reason, never the safe default. **Reduction never costs character:** the fewer the elements, the more each must carry (depth within it, an ownable trait, a link to its neighbors). Decoration never outranks the required information it serves.
6. **Explicit rank and allocated space.** Attention is directed, never left to compete: every element holds a stated rank, and ranks are separated by contrast the viewer cannot miss. Form follows purpose: each text and element is styled for the job it does. Space is allocated before content is placed, at two levels (the format's quiet share and the breathing room inside each zone), both scaled to the format and its viewing distance; crowding is an allocation failure, resolved by arrangement, grouping, and triage, never by shrinking below legibility minimums.
7. **Internal consistency.** Brand, theme, style, color, type, mark, imagery, and composition reinforce one another; resolve contradictions at the source. Group content by what it refers to, not only by when it is read: text that labels, explains, prices, or substantiates a depicted thing is composed with it, unless the hero carries the message alone. Parallel items are separate units, each placed by its own referent, unless the viewer should read them as one claim. Content that relates among itself (sequence, comparison, hierarchy, dependency) shows that relation in form, read from the content, never from a template.
8. **Fidelity to the brief.** Mandatory content, user text, exclusions, fixed assets, stated qualities (named style, color, technique included), and priorities are never silently overridden, not even by the skill's own strategy. Constraints are material: seek distinction inside them by committing fully, never by diluting or evading.
9. **Effort follows impact.** Longest deliberation on the mark, core idea, hero, and space plan; brisk on routine decisions.
10. **Context before convention.** Universal principles (purpose, hierarchy, coherence, specificity) hold in every medium. What the medium imposes, what its audience relies on, and what it affords are derived from the actual deliverable in Phase 2, never assumed from the medium's name. Convention the audience relies on to read or use a piece is kept where departing costs them effort or credibility; distinction is spent on expression and identity.

## 6. Depth and the deliverable set

Phase 1 sets the depth and records it in the log. Depth scales the work inside every phase and never drops a phase, decision, protocol step, or gate. (It has nothing to do with the picture's front-to-back order; that is layering.)

- **Full:** a new identity mark must be created, or any deliverable is contested, the set has several deliverables, or content is dense for its format.
- **Focused:** everything else. Raise to Full as soon as any phase shows a Full condition.

Conditions, read concretely. **Contested:** the deliverable must win attention against its neighbors from beyond arm's reach or in a crowded field. **Several deliverables:** the set holds more than one. **Dense:** content volume is high for the format; judged from the ledger in Phase 1 and re-judged by Phase 3's rough capacity test.

| | Full | Focused |
|---|---|---|
| Research (Phase 2) | every question that can change a decision | the one or two that can |
| Territory survey (Phase 3) | 5 territories, 3 source families | 3 territories, 2 families |
| Candidate cards | every field the phase sets | fields that tell candidates apart, plus quality compatibility |
| Governing principles (Phase 3) | compared: space intent, imagery, integration, mark role, layering, tone and positioning, density and rhythm | compared: space intent, imagery, integration, mark role; rest decided directly |
| New mark (Phase 4) | 6 seeds, every check recorded | 4 seeds, checks as pass/fail lines |
| Gate objections | two (the two riskiest decisions) | one |

Depth never changes naming the apparent option, three or more candidates, the runner-up and decisive criterion, the quality checks, the capacity check, verbatim content, or the audits. A rich brief shortens Phase 1 and 2 notes; a sparse brief deepens research. **Raising to Full** applies from the current phase on; reduced work in an earlier phase is reopened only where the missing depth could change a decision already made (a Focused survey that must now feed six mark seeds gains territories first).

**Deliverable set.** Phase 1 records every deliverable the request needs, derived from what the user must accomplish and not only from what they named. One deliverable per image that must exist: a distinct format or ratio, a distinct side, panel, or screen, or a variant or concept the user asked for. What belongs in one image stays one image; what differs in format or encounter enough to change the composition becomes its own deliverable. A different size at the same ratio and encounter is the same deliverable.

**Shared and per-deliverable decisions.** Phases 2 to 4 decide once what the set shares (a context where deliverables share one, identity, style, color, type, element system). Each deliverable gets its own stage assignment, space plan, strategy, hierarchy, and placement (Phase 5) and its own standalone prompt (Phase 6). A deliverable is never derived by resizing or cropping another's composition: format changes the reach of the stages, the regions available, the reading path, and the balance, so composition is decided for each format. What transfers across deliverables is decisions, not layout.

**Several concepts.** Run Phases 1 and 2 once; run each of Phases 3 to 5 across all concepts before moving on. Each concept starts from a core-idea candidate that differs on a structural axis (never only color or decoration) and ends in its own standalone prompt per deliverable; one entry per phase with a short subsection per concept. Forward blocks and Records are kept per concept; S is shared.

Prompts delivered = deliverables × concepts. Avoid proliferation: never add a deliverable for a variation the user did not need, and never split content that is one image.

## 7. Conflict priority

When requirements collide, resolve in this order:
1. factual integrity; the user's mandatory content, exclusions, and fixed assets;
2. perception and comprehension under the real conditions of encounter, for the full range of the audience (low vision and color-vision differences included), achieved by restructuring, rescaling, or regrouping, never by deleting mandatory content;
3. the user's stated requirements: quality requirements (named style, color, technique included) and priorities;
4. the communication objective and the strategy serving it (differentiation, departure), chosen only among options that keep tier 3 intact;
5. established brand identity not supplied as an asset;
6. creative ambition.

A lower tier yields only to a higher one and keeps its closest surviving expression. A named choice that weakens the objective stays: mitigate inside it and offer the concern once as a labeled suggestion (in the entry; in auto mode, in the key decisions). Phase 2 tensions take their lead side from this order where it decides them; Phase 3 decides the rest.

## 8. Non-negotiables

- No invented facts about the subject: figures, claims, testimonials, ratings or levels, certifications, regulated or trust marks, contacts, credentials, dates, statistics, specifications. A design never implies a claim, endorsement, or authority the subject does not hold.
- User text is preserved verbatim, suspected typos included (flag, never fix).
- Supplied logos and characters are never redesigned, restyled, simplified, or recolored. No figure (mascot, character, person) is introduced unasked; never a likeness of a real person; never an implied endorsement.
- No copying of competitors, peers, or existing designs.
- No identifier that is only a styled name, unless supplied or explicitly requested as plain text.
- No placeholders or blank zones for content the skill should create. The one reserved region is an asset panel for a supplied asset the generator cannot reproduce faithfully (a scannable code, a supplied photograph or logo file that cannot be attached): designed into the composition, flagged in the notes, never imitated.
- No stated quality contradicted by any decision or left without a visible carrier.
- No suggestion enters the brief or the design without the user's yes; suggestions are labeled and never counted as facts.
- No design jargon the user has not shown they use, and no walls of text, in anything the user reads.
- No workflow output beyond the messages the UX reference defines, unless requested.

## 9. Ready for Phase 6

A completeness check on the Forward blocks, run at the Phase 5 gate. It confirms that each commitment exists as a visible, drawable specification. Reasons were verified at their own gates (with sources, section 4) and are not re-argued here or passed to Phase 6. A missing or vague item returns to its owning phase.

| Commitment | Must exist as |
|---|---|
| Deliverable set | per deliverable: its format and ratio as in S, to be stated in its prompt and never substituted; the prompt count equals the set |
| Message | one sentence, confirmed in Phase 5 |
| Each quality requirement | its carriers and the resulting value key, as visible features |
| Each content item | role, treatment grade, encounter stage, placement, per deliverable it appears in |
| Supporter set | per supporter: its purpose line, form, region, and weight ceiling; or the finding that the text-only baseline has none |
| Any figure | origin, roles, the one design every appearance shares |
| Context | what the design shares with its surroundings and the dimension on which it departs, as visible traits |
| Core idea, style, hero | the chosen option in drawable terms, with the true specifics of what is depicted and the image-making language it is drawn or shot in; the hero's reinforcing content and supporters, or the reason it stands alone |
| Identifier | a fixed asset, or a new mark: personality device, geometry, integration logic, distinction mechanisms, and which identity forms appear where |
| Shape language and balance | each container's function, form, and fill mode; the balance type and its counterweight |
| Space plan | proportions, internal spacing of each zone, reading order, the arrangement form of each information group, and the placement and role of every mandatory text item, per deliverable |
| Distinguishing traits | the traits that set the design apart from the peers it will be seen beside |
| Carry-forward obligations | each realized by a named decision or recorded as an accepted cost |

A reason that is only "it looks good" or "it is typical" fails its gate.

## 10. Revision requests

- Re-enter at the earliest affected phase: content, deliverables, format, or ratio → 1; concept or mood → 3; color, value key, type, copy treatment, mark, lockup, supporters → 4; arrangement or emphasis → 5; wording → 6.
- Keep unaffected decisions as settled. Read S and the Forward blocks of the re-entered and dependent phases (Records only where the return rule needs them), and only those phases' files. Redo, in order, the decisions that read the changed one (section 3 map), telling the user briefly what is being redone and showing only what changed (a short Before | After table in the user's language). Re-run only the design checks the change touches, plus the contradiction scan and any quality whose carrier changed; the prompt audit always runs in full on every fresh prompt. Feedback at any confirmation takes the same route. Deliver a fresh complete prompt for each deliverable whose content changed, and name the ones that did not.

## 11. Output contract

- **Genuine only.** Decisions fixed by the user, a supplied asset, or evidence are listed as fixed; alternatives are never invented.
- **Amendments** (guided mode; auto mode shows no decisions). If a later return changes a shown decision, say so at once in one plain line (what changed to what, and why). The audit checks that every shown or amended decision is visible in the prompts and none is contradicted.
- **Final reply** (layout in the UX file, section 6): the prompt set plus whatever the user must still know, once. Each prompt carries a label line stating its purpose and its place in the whole request. Usage steps are brief and state any attachment, order, or dependency that applies. Notes carry suspected typos, copy the skill wrote, supplied assets to attach, a reserved asset panel, and any volume or rendering risk (terms), never design rationale or repeated tables. Assumptions and yielded preferences are disclosed in the summary and entries (auto mode: the key decisions).
- **Each prompt**, built and audited per `06_prompt_synthesis.md`: self-contained and executable without any other prompt, generation, or the brief; English by default (`06_prompt_synthesis.md` G) with on-image text verbatim in its original language; alone in its code block; carrying every shown or amended decision and all mandatory content for its deliverable.