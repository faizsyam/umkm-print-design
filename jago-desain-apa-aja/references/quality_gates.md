# Quality gates: hand-off check, assembled review, and the Ready-for-Phase-6 check (all phases)

The check run at the end of every phase, the one assembled review, and the completeness check run at the Phase 5 gate.

**Inputs needed:** The phase just completed, its phase file's gate checks, and the Design Log so far.

No gate is skipped, and none repeats work an earlier check did: each check runs once, where it is placed.

## 1. Hand-off check (every phase)

Run these, then the phase file's own "Gate checks".
1. Every required decision of the phase is made by its class (`exploration_protocol.md` section 1): Direction decisions show their record at the openness in S; the System decision shows its comparison or its derivation; Execution items are not logged.
2. Sources and qualities: every decision names its source (`workflow_and_state.md` section 4) and was made after its inputs existed (a decision resting on a later phase's output is provisional and tagged). Each stated quality has a visible carrier at this phase's level of realization (plan, system, composed glance stage), and no decision signals its opposite. At Phases 1, 2, and 6 the phase file's own quality checks apply.
3. Consistency: this phase's decisions agree with the decisions it reads; a conflict returns to the earliest conflicting decision.
4. User-facing: Phase 1 closes only on the user's confirmed summary and mode. Guided mode: each message with real work opened with a wait note; entries for Phases 3 to 5 shown at their gates as one compact table in the user's language (Phase 2's findings lead the Phase 3 entry); the turn stopped for confirmation after Phases 3 and 4. Auto mode: one wait note, nothing shown at gates. Phase 6 is the final reply.
5. The phase's decisions (D), carry-forward obligations, and open flags are appended to the Design Log. A passing check is one line; failures and fixes are written out.
6. **Failure route.** Return as the table says, carry back what it lists, set dependents stale (`workflow_and_state.md` section 4), re-run forward, and count the return against the issue's two-cycle cap (`triage_and_revisions.md` section 4).

| Gate | Return to | Carry back |
|---|---|---|
| 1 | the Phase 1 step (A to E) the failed check names; a user-facing failure returns to the intake | the failed check; the ledger rows concerned |
| 2 | the Phase 2 step that produced the failed artifact: research (2), profile (3), differentiation or inventory (4), problem (5), implications (6) | the failed check; the finding or implication concerned |
| 3 | the card of the failed decision (plan criteria, survey, core idea, style, hero, principles); a failed direction check returns to the earliest decision it implicates, in the order core idea, style, hero, principles | the check; the decisions implicated; the tension or obligation concerned |
| 4 | the Phase 4 file that owns the failed part (`05` to `08`), or Phase 3 principles when the plan caused it | the failed check; the part, its purpose line if it is an addition, and the commitment it realizes |
| 5 | the earliest responsible step: stages and map (`10`), needs, composition, and space plan (`11`), placement (`12`), load, balance, capacity (`13`), review (`14`); Phase 4 when the system is the cause | the failed check; the deliverable; the decisions concerned; frozen sizes are discarded when the return precedes the capacity check |
| 6 | the earliest cause per `triage_and_revisions.md` section 4: a clause (`16`), the prompt set or structure (`15`), or the owning earlier phase when a needed decision does not exist | the failed audit item; the sentence; the Execution Specification field concerned |

## 2. Assembled review (once, at the Phase 5 gate)

Run on the assembled design with the composition checklist (`14_backgrounds_review_and_gate.md` F). Phase 3 runs only its direction check (`04_principles_and_plan_evaluation.md` G). Each test is defined here and runs once; afterwards only the tests a changed decision touches are re-run.

| Test | Question | Routes to |
|---|---|---|
| Contradiction scan | Do brand design, theme, idea, style, hero, system, mark, and composition agree, and do the attention hierarchy, reading sequence, and placement agree? Across the set: are shared decisions identical in every deliverable, with composition differences explained by format or encounter? | the earliest conflicting phase |
| Brief-quality | Does each stated quality have a visible carrier in the composed glance stage, and does any decision signal its opposite? | Phase 1 for the translation, otherwise the earliest contradicting phase |
| Decided-attribute | Is any look-shaping attribute left to the model's apparent value? | the phase that should own it |
| Originality | The protocol's three tests: predictable, specific, ambitious | the deciding phase |
| Load and fit | Does the cumulative visual load (information, imagery, supporters, containers, treatments, surface, color intensity) fit the space budget with headroom, by area and along the governing axis, with the quiet open (glossary: Quiet) and every addition beating its next-lighter alternative (nothing, spacing alone, a smaller or simpler form) at its space cost? | the earliest phase whose allocation or addition broke it |

**One objection:** the strongest case against the riskiest decision of the design (highest consequence on thinnest evidence, or an interaction or compounding accepted cost), raised by the role that owns it (`scope_roles_and_depth.md` section 2), then resolved or accepted with a recorded reason. It must add something the protocol's challenge did not.

A defect is traced to the earliest responsible decision (`triage_and_revisions.md` section 4).

## 9. Ready for Phase 6

A completeness check on the Design Log, run at the Phase 5 gate. It confirms that each commitment exists as a visible, drawable specification, and that every Specification is prompt-ready. Reasons were verified at their own hand-offs; they are not re-argued here or passed to Phase 6. A missing or vague item returns to its owning phase. A reason that names no observable property or comparison fails its check.

| Commitment | Must exist as |
|---|---|
| Deliverable set | per deliverable: its format and ratio as in S, to be stated in its prompt and never substituted; the prompt count equals the set |
| Message | one sentence, confirmed in Phase 5 |
| Each quality requirement | its carriers and the resulting value key, as visible features |
| Each content item | role, treatment grade, encounter stage, group, placement, per deliverable it appears in |
| Supporter set | per addition: its purpose line, form, region, and weight ceiling; or the recorded reason the piece stays plain; and the decoration (atmosphere fields, ornament, pattern) with its vocabulary and where it sits, or the decision that it holds none |
| Any figure | origin, roles, the one design every appearance shares |
| Context | what the design shares with its surroundings and the dimension on which it departs, as visible traits |
| Core idea, style, hero | the chosen option in drawable terms, with the true specifics of what is depicted and the image-making language it is drawn or shot in; the hero's reinforcing content and supporters, or the reason it stands alone; the treatment vocabulary (the few rendering treatments in use, each with its job) |
| Identifier | a fixed asset, or a new mark: personality device, geometry, integration logic, distinction mechanisms, and which identity forms appear where |
| Shape language and balance | each container's function, form, and fill mode; the balance type and its counterweight |
| Space plan | area shares (each between its group's space need and its rank's ceiling) that with the free ground account for the whole format with headroom; the quiet regions and any atmosphere fields by what they separate or frame; internal spacing of each zone; gap and clearance steps between neighbors; the reading sequence as a route over the placed regions, agreeing with the attention hierarchy and the placement; the arrangement form of each information group; the quantity of every repeated form; the planned wrap of every multi-line string; and the placement and role of every mandatory text item, per deliverable |
| Distinguishing traits | the traits that set the design apart from the peers it will be seen beside |
| Carry-forward obligations | each realized by a named decision or recorded as an accepted cost |

## Quality checks

- Pass: steps 1 to 6 of section 1 hold at each phase; at the Phase 5 gate the section 2 review passed and every commitment in section 9 exists as a drawable specification.
