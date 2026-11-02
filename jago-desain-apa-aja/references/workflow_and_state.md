# Workflow, decision ownership, execution rules, and the Design Log (all phases)

Defines the phase order and exit artifacts, which phase owns and reads which decision, the execution rules every phase obeys, and the Design Log that carries state between phases and turns.

**Read this when:** at the Phase 1 gate, before the Design Log is created; reopen section 3 (ownership map) or section 4 (rules, state) whenever a hand-off, return, or log question arises.

**Inputs needed:** The Phase 1 gate is being run; S is about to be created from the confirmed summary.

## 3. Workflow

**Reading order.** The routing table in `SKILL.md` names which file to open at which step; each file's "Read this when" repeats the trigger.
- On entering a phase: that phase's files, in order, never earlier, never skipped. The first file of each phase opens with a phase sheet listing what the phase reads, decides, and hands forward.
- Cross-phase files are read at the step the routing table names: the glossary parts at Phases 1 and 3, `exploration_protocol.md` and `global_standards.md` on entering Phase 2, this file and `quality_gates.md` at the first gate (Phase 1's).
- Each file is read once and stays in context; reopen only a section a decision needs. If a standard or term referenced in a step file is no longer visible, re-open the file that defines it before continuing.
- On a resumed or revision turn, read `workflow_and_state.md`, `quality_gates.md`, the files of the phases being re-entered, and the cross-phase files the routing table names for those phases (glossary parts, protocol, standards, UX, audit) when they are not in context.

| Phase | Exit artifact | File |
|---|---|---|
| 1 Brief | Standing block S (Brief Ledger with deliverable set and quality translations, depth, mode), research questions, tensions; user-confirmed summary and mode | `01_brief_and_requirements.md` |
| 2 Analysis | Communication Problem with the message, Environment Profile (encounter, medium reading, encounter stages), audience encounter, differentiation strategy, Visual source inventory, design implications | `02_research_and_analysis.md` |
| 3 Design Plan | Brand design, theme, core idea, style, hero, governing principles (incl. space intent, mark role), quality carrier map, seed bank | `03_core_idea_style_and_hero.md`, `04_principles_and_plan_evaluation.md` |
| 4 Design Elements | Element system: color with value key, type with copy treatments, identity unit, supporters, background; each with purpose line and space cost | `05_color_and_typography.md`, `06_identity_unit_and_copy_treatment.md`, `07_visual_supporters_and_figures.md`, `08_containers_and_ground.md`, `09_element_system_evaluation.md` |
| 5 Design Execution | Execution Specification per deliverable: confirmed message, stage assignment, space plan, spatial strategy, hierarchy, placement of every item | `10_stage_assignment_and_relationship_map.md`, `11_space_plan_and_spatial_strategy.md`, `12_hierarchy_and_element_placement.md`, `13_load_balance_and_capacity_checks.md`, `14_backgrounds_review_and_gate.md` |
| 6 Prompt Synthesis | Audited standalone prompt per deliverable, labels, usage steps, short notes | `15_prompt_set_and_structure.md`, `16_prompt_clauses_and_delivery.md` |

`quality_gates.md` holds the gate procedure and cross-phase tests; `prompt_and_reply_audit.md` the prompt audit, reply audit, and release checklist; `triage_and_revisions.md` the triage, routing, and revision re-entry.

### Decision ownership and reads

Each decision has one owning phase and reads only the inputs listed. **S** is the standing block (section 4), readable by every decision. A decision's inputs include the earlier decisions it reads.

| Owner | Decision | Reads | Yields |
|---|---|---|---|
| 1 | Ledger, deliverable set, quality translations, depth | user input | S |
| 2 | Environment Profile (encounter, medium reading, stages, departure, fit), audience encounter | S (deliverable set, medium, use), research | profile, encounter |
| 2 | Differentiation, Visual source inventory | S, research, peers from the profile | strategy, inventory |
| 2 | Communication Problem: weakest link, tensions, message | S priorities, profile, encounter, differentiation | problem, message |
| 3 | Plan criteria: space budget (quiet share, role allocations), tension leads, carry targets | S formats, content volume and load read, and qualities; stages and their reach; problem (message, tension leads) | criteria |
| 3 | Core idea → style → hero | message, inventory, differentiation, audience encounter, survey, criteria, S qualities, brand design (each reads the one before) | the three choices; hero's hosting capacity and permitted mark roles |
| 3 | Governing principles, quality carrier map | the three choices, criteria, S qualities | space intent, imagery, integration, mark role and the rest; carrier map |
| 4 | Color, type → mark and lockup | style dimensions 6 and 7, S fixed assets and reproduction limits, profile surroundings, encounter stages, and medium reading, carrier map, mark role, seed bank | palette with value key, type roles, identity unit |
| 4 | Copy treatment (provisional rank), supporters, containers, ground | content roles, Communication Problem (objective, weakest link, message), encounter stages, hero, mark role, imagery stance, space intent, style dimensions 1, 4, and 5 (corner and edge geometry included), boundaries, character carriers, layering stance, tone and positioning, figure stance | element system with purpose lines |
| 5 | Per deliverable: stages → space plan → strategy | S (that deliverable's format and ratio), message, profile (stages, reading path, medium reading), element system, hero hosting, integration stance, balance type, space budget and density level | stage assignment, space plan (area shares accounting for the whole format), strategy (each card tested for fit) |
| 5 | Per deliverable: ranks, reading sequence, placement, balance, load and capacity freeze | strategy, element system with purpose lines, mark role, layering stance, tone and positioning, density, point of tension, counterweight | Execution Specification |
| 5 | Per deliverable: realization of the Phase 4 ground and unifying devices; reproduction-condition adjustments; across the set: consistency | frozen composition, Phase 4 ground and unifying devices, S reproduction limits, profile (medium reading) | Execution Specification (backgrounds, adjustments, set rules) |
| 6 | Prompt set, then each prompt | S, the Execution Specifications, the Phase 4 specs they name, style dimensions, hero specifics | prompts, labels, usage steps, notes |

A later phase applies the decisions it reads and does not re-weigh them. Records are never inputs to a decision (section 4).

Copy treatment has one owner: Phase 4, rule B2. An item first promoted to rank 1 or 2 in Phase 5 takes its treatment under the same rule; the result is logged as a Phase 5 item with Source "Phase 4 rule B2".

## 4. Execution rules

- **Order.** Phase N+1 starts only when Phase N's required decisions are made, its exit artifact exists, and its gate has passed. No phase is skipped, merged, or deferred, however simple the brief: simplicity shortens the work, never removes it. A conclusion held early is a hypothesis to test in its own phase.
- **Hand-offs stay narrow.** A phase reads S and the Forward fields its card lists, nothing else. Candidates, rejected options, survey detail, research notes, and rationale stay in the Record. A reason a later phase must honor travels as a carry-forward obligation (see State), not as narrative.
- **Ownership.** Each decision has one owning phase (section 3 map). Later phases apply it and do not re-decide it. It reopens only through the return rule, on a named failed check, test, or contradiction, never on preference.
- **Traceability.**
  - Every decision names its source: Ledger item or finding → implication → plan → element → execution → prompt clause. A decision with no nameable source was made from habit and fails its gate.
  - Every quality requirement traces Phase 1 translation → plan carrier → value key and element carrier → placement → prompt clause. A requirement that any phase contradicts, or that reaches no visible carrier, fails that gate.
  - Every carry-forward obligation is realized by a named later decision or recorded as an accepted cost.
- **Gate integrity.** State no number or decision to the user until the checks that could change it have run (load budget test in Phase 3, value key in Phase 4, load and capacity checks in Phase 5). Amendments are for genuine returns only.
- **Return, then re-run forward.** A failed gate, or a flaw exposed later, goes to the earliest responsible phase. Redo, in order, only the decisions that read the changed one (section 3 map); a dependent whose inputs did not materially change is re-checked, not redecided. Cap each issue at two revision cycles, then take the best available resolution and record it. Never patch the prompt for an upstream cause.
- **Gates and entries.** Each phase ends at its gate (`quality_gates.md` section 1).
  - Guided mode: show the entry immediately, in the user's language. Phase 2's findings lead the Phase 3 entry; there is no separate Phase 2 stop. End the turn with a confirmation question after Phases 3 and 4 and continue only on the go-ahead. Phase 5's entry is shown and Phase 6 follows without stopping.
  - Auto mode: show nothing at gates; the checks still run.
- **Phase entry.** Read the phase's files in order, take S and the Forward fields its phase sheet lists from the Design Log or context, and decide one decision at a time, each against the whole (principle 1). When lost or overloaded, return to the phase sheet, then the log. Do not rush to the prompt.
- **Working notes** record decisions and reasons, not deliberation. Trivial decisions are made directly. A gate that passes is one line in the log; only failures, fixes, objections, and amendments are written out.

**State: the Design Log.** The only carrier of state between phases and turns. Compact English, in three parts:
- **S, the standing block.** Created when the user confirms the summary; readable by every phase. Contents:
  - the deliverable set: each deliverable's purpose in the request, medium and use, format and ratio (as the user intends, or derived and tagged inferred), content volume and load read, and relationship to the others;
  - the setting of each (provisional if inferred);
  - the generator if named; the user's language and design literacy as read;
  - mandatory strings verbatim, with role and deliverable;
  - fixed assets (exactly what is fixed); exclusions; reproduction limits;
  - quality requirements (user's words, translation); depth; mode.

  Phase 3 adds the quality carrier map. Apart from that, S changes only by user corrections.
- **Forward block**, one per phase, appended at its gate. Each phase sheet lists its Forward fields. It holds:
  - the phase's decisions as log items (Decision, Specification, Source, Constrains, Status; schema below), each a specification later phases act on;
  - **carry-forward obligations**: every mitigation, accepted cost, and "amplify here" move the protocol recorded, so a later phase can realize it;
  - **open flags**: assumptions, provisional items, unresolved uncertainty, kept apart from the decisions so nothing unresolved reads as settled.

  A decision that rests only on provisional items stays tagged and is disclosed in the summary or entry (auto mode: the key decisions).
- **Record:** the Basis and Rejected fields of every log item, candidates and tables, objections with resolutions, research notes, shown amendments. Read only by gates and audits, by revisions, and by the return rule; never passed to a later decision or to Phase 6.

**Log item schema.** Every decision is one log item. Field names are fixed; phase sheets, gates, and revisions use them.

| Field | Holds | Kept in |
|---|---|---|
| Decision | the decision's name exactly as in its phase sheet's Decisions row | Forward |
| Specification | the chosen option, stated so a later phase can act on it without the Record | Forward |
| Source | provenance tag (given, researched, inferred, creative choice) and the origin it traces to (ledger item, finding, plan commitment) | Forward |
| Constrains | the later decisions whose Reads (ownership map) include this one | Forward |
| Status | current, stale, or re-derived | Forward |
| Basis | the principle number (`global_standards.md` section 5) or the evidence that decided it | Record |
| Rejected | the runner-up, the decisive criterion, and the rejected alternatives | Record |

A decision made directly logs Basis as one line and Rejected as none. A decision fixed by the user, a supplied asset, or evidence logs Source as fixed and Rejected as none.

**Stale flag.** When a decision changes, set Status to stale on every item whose Decision is in the changed item's Constrains, transitively. Re-derive stale items in phase order and set them to re-derived. An item whose inputs did not materially change is re-checked and set to current without being redecided.

**Persistence.** With file tools, keep the log at `/home/claude/design_log.md`: create it when the user confirms the summary (S and the Phase 1 Forward block); append one Forward block and its Record items per later phase at its gate; read S and the Forward blocks when a turn resumes work and before any revision. It is never presented. Without file tools, keep it in notes. If it is lost, rebuild it from the confirmed summary, shown entries, prompts, and user messages, marking rebuilt items provisional.

## Quality checks

- Pass: the Order, Hand-offs, Traceability, Gate integrity, and Return rules of section 4 hold, and every log item has all Forward fields of the schema; `quality_gates.md` section 1 runs these at each gate.

## Next

Read `quality_gates.md` and run the Phase 1 gate. Then create the Design Log (S and the Phase 1 Forward block) once the user confirms the summary and mode.
