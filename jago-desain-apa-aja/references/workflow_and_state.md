# Workflow, decision ownership, execution rules, and the Design Log (all phases)

Defines the phase artifacts, which phase owns and reads which decision, the execution rules every phase obeys, and the Design Log that carries state between phases and turns.

**Inputs needed:** The Phase 1 hand-off is being run; S is about to be created from the confirmed summary.

## 3. Workflow

Loading follows the batch list in `SKILL.md`. The first file of each phase opens with a phase sheet listing what the phase reads, decides, and hands forward. On a resumed or revision turn, read this file, `quality_gates.md`, and the batches of the phases being re-entered when they are not in context.

| Phase | Exit artifact | Files |
|---|---|---|
| 1 Brief | Standing block S (Brief Ledger with deliverable set, quality translations, openness map, mode), research questions, tensions; user-confirmed summary and mode | `01_brief_and_requirements.md` |
| 2 Analysis | Communication Problem with the message, information groups, and load table; Environment Profile (encounter, medium reading, encounter stages with role floors); differentiation strategy; Visual source inventory; design implications | `02_research_and_analysis.md` |
| 3 Design Plan | Brand design, theme, core idea, style, hero, governing principles (space intent, mark role), quality carrier map, seed bank | `03_core_idea_style_and_hero.md`, `04_principles_and_plan_evaluation.md` |
| 4 Design System | The system decision (palette with value key, type roles, shape and container language, supporter policy, ground), identity unit and any created lead figure; additions with purpose lines | `05` to `09` (`07` on trigger) |
| 5 Design Execution | Per deliverable: confirmed message, stage assignment, groups with space needs, composition as a region table, space plan, hierarchy, placement; the assembled review | `10` to `14`, `quality_gates.md` |
| 6 Prompt Synthesis | Audited standalone prompt per deliverable, labels, usage steps, short notes | `15`, `16`, `prompt_and_reply_audit.md` |

`quality_gates.md` holds the hand-off check, the assembled review, and the Ready-for-Phase-6 check; `triage_and_revisions.md` the triage, routing, and revision re-entry.

### Decision ownership and reads

Each decision has one owning phase and reads only the inputs listed. **S** is the standing block (section 4), readable by every decision.

| Owner | Decision | Reads | Yields |
|---|---|---|---|
| 1 | Ledger, deliverable set, quality translations, openness map | user input | S |
| 2 | Environment Profile with role floors, audience encounter | S (deliverable set, medium, use), research | profile, encounter |
| 2 | Differentiation, Visual source inventory | S, research, peers from the profile | strategy, inventory |
| 2 | Communication Problem: weakest link, tensions, message, information groups, load table | S (content, priorities), profile, encounter, differentiation | problem, message, groups, load table |
| 3 | Plan criteria: space budget (free ground, role shares), tension leads, carry targets | S formats, load read, qualities; stages; problem; load table | criteria |
| 3 | Core idea → style → hero | message, groups, inventory, differentiation, encounter, survey, criteria, S qualities, brand design (each reads the one before) | the three choices; hero's hosting capacity and permitted mark roles |
| 3 | Governing principles, quality carrier map | the three choices, criteria, S qualities | space intent, imagery and decoration, integration, mark role, the rest; carrier map |
| 4 | System decision: color, type, shape and container language, supporter policy, ground | style dimensions 1, 4, 5, 6, 7, S fixed assets and reproduction limits, profile surroundings and medium reading, stages, carrier map, hero, principles, groups, message | the design system |
| 4 | New mark and lockup, created lead figure | the system's palette and type, mark role, seed bank, style dimension 5, S fixed assets | identity unit, figure design |
| 5 | Per deliverable: stages → groups and needs → composition (region table) → space plan | S (format and ratio), message, groups, load table, profile, system, hero hosting, integration stance, balance type, space intent | stage assignment, arrangement forms, composition, space plan |
| 5 | Per deliverable: ranks, placement, balance, capacity freeze | composition, system, mark role, layering, tone, density, tension, counterweight | Execution Specification |
| 5 | Per deliverable: backgrounds, reproduction adjustments; across the set: consistency | frozen composition, system ground, S reproduction limits, profile | Execution Specification (backgrounds, set rules) |
| 6 | Prompt set, then each prompt | S, D, the Execution Specifications | prompts, labels, usage steps, notes |

A later phase applies the decisions it reads and does not re-weigh them. An item first promoted to rank 1 or 2 in Phase 5 takes its treatment under `06_identity_unit_and_copy_treatment.md` B2.

## 4. Execution rules

- **Order.** Phase N+1 starts only when Phase N's decisions are made and its hand-off check has passed. No phase is skipped, merged, or deferred; a rich brief shortens exploration, never a phase. A conclusion held early is a hypothesis to test in its own phase.
- **Hand-offs stay narrow.** A phase reads S and the decisions its sheet lists, not candidates, rejected options, survey detail, or rationale. A reason a later phase must honor travels as a carry-forward obligation.
- **Ownership and reopening.** A decision is applied, not re-decided, by later phases. It reopens only by a named failed check or contradiction, never on preference. A decision a later phase refines (the space budget envelope, provisional ranks, information groups) travels as provisional; the refining phase re-derives it, and a conflict returns upward.
- **Traceability.** Every decision names its source (ledger item or finding, then plan, system, execution, prompt clause); one with no nameable source was made from habit and fails its check. Every quality requirement traces from its Phase 1 translation to a carrier and to a prompt clause. Every carry-forward obligation is realized by a named decision or recorded as an accepted cost.
- **Gate integrity.** State no number or decision to the user until the checks that could change it have run (load budget test in Phase 3, value key in Phase 4, load and capacity checks in Phase 5). A check that passed is re-run only when a decision it reads changed.
- **Return, then re-run forward.** A failed check goes to the earliest responsible phase. Redo, in order, only the decisions that read the changed one; a dependent whose inputs did not materially change is re-checked, not redecided. Cap each issue, and every loop inside a phase (a protocol rebuild, a fit remedy, a strategy swap), at two cycles, then take the best available resolution and record it. Never patch the prompt for an upstream cause.
- **Gates and entries.** Each phase ends at its hand-off check (`quality_gates.md` section 1). Guided mode: show the entry immediately, in the user's language; Phase 2's findings lead the Phase 3 entry; stop with a confirmation question after Phases 3 and 4 and continue only on the go-ahead; Phase 5's entry is shown and Phase 6 follows. Auto mode: show nothing at gates; the checks still run.
- **Phase entry.** Read the phase's batch in one call, work in the order its first file's process gives, take S and the decisions its sheet lists from the Design Log or context, and decide each against what it reads and the commitment it realizes (principle 1). When lost, return to the phase sheet, then the log.
- **Working notes** record decisions and reasons, not deliberation. A figure is recorded once, where first derived; later phases name it and restate only a change. A measurement is stated only if a decision depends on it and it was worked out (contrast ratios, centroids, pixel counts otherwise become a pass or fail). A check that passes is one line; only failures, fixes, and objections are written out.

**State: the Design Log** is the only carrier of state between phases and turns, in compact English, in two parts.
- **S, the standing block**, created when the user confirms the summary and readable by every phase: the deliverable set (each deliverable's purpose, medium and use, format and ratio as intended or derived and tagged inferred, content volume and load read, relationship to the others); the setting of each (provisional if inferred); the generator if named; the user's language and design literacy; mandatory strings verbatim with role and deliverable; fixed assets (exactly what is fixed); exclusions; reproduction limits; quality requirements (user's words, translation); the openness map; mode. Phase 3 adds the quality carrier map; otherwise S changes only by user corrections.
- **D, the decisions**, appended at each hand-off: one line per decision a later phase reads (the ownership map's Reads column), with the fields below, the Specification doubling as the prompt-ready clause; carry-forward obligations (every mitigation, accepted cost, and amplify-here move); open flags (assumptions, provisional items, unresolved uncertainty, kept apart so nothing unresolved reads as settled). A decision resting only on provisional items stays tagged and is disclosed in the summary or entry (auto mode: the key decisions). Other decisions are named in one line.

| Field | Holds |
|---|---|
| Decision | the decision's name as in its phase sheet |
| Specification | the chosen option in prompt-ready wording (traits as seen, no rationale; dimensions as shares of the format, physical mm only to derive floors), so a later phase can act on it and Phase 6 can assemble it without rewriting |
| Source | provenance (given, researched, inferred, creative choice) and its origin |
| Basis | the principle number (`global_standards.md` section 5) or the evidence that decided it |
| Rejected | Direction decisions only: runner-up, decisive criterion, rejected alternatives; otherwise none |
| Status | current, stale, or re-derived |

A decision fixed by the user, a supplied asset, or evidence logs Source as fixed and Rejected as none. Basis and Rejected are read only by hand-off checks, the review, audits, revisions, and the return rule; never by a later decision or Phase 6.

**Stale flag.** When a decision changes, set Status to stale on its dependents in the ownership map, transitively, and re-derive them in phase order; one whose inputs did not materially change is re-checked and set to current.

**Persistence.** With file tools, keep the log at `/home/claude/design_log.md`: create it when the user confirms the summary (S and the Phase 1 decisions), append per phase at its hand-off, read S and D when a turn resumes or before a revision. It is never presented, except under the developer option in `SKILL.md` (Trace log). Without file tools, keep it in notes. If it is lost, rebuild it from the confirmed summary, shown entries, prompts, and user messages, marking rebuilt items provisional.

## Quality checks

- Pass: the Order, Hand-offs, Traceability, Gate integrity, and Return rules hold, and every logged decision has its fields; `quality_gates.md` section 1 runs this at each hand-off.
