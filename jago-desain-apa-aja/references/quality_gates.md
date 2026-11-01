# Quality gates: gate procedure, cross-phase tests, and the Ready-for-Phase-6 check (all phases)

The procedure run at the end of every phase, the five cross-phase tests, the composition-review pointer, and the completeness check run at the Phase 5 gate.

**Read this when:** at the first gate (Phase 1's) and again at the end of every phase; run section 9 at the Phase 5 gate.

**Inputs needed:** The phase just completed, its phase file's gate checks, and S plus the Forward blocks so far.

No gate is skipped. Read this file at the first gate; afterwards reopen the section the moment requires.

## 1. Gate procedure (every phase)

Run these checks, then the phase file's own "Gate checks".
1. Every required decision of the phase is made.
2. The protocol was applied: each Full decision has its record; each compact comparison shows the apparent option, the options, and the decisive criterion.
3. Sources and qualities: every decision names its source (`workflow_and_state.md` section 4). The brief-quality test below passes where the table runs it, at that phase's level of realization. At Phases 1, 2, and 6 the phase file's own quality checks apply.
4. **One substantive objection:** the strongest case against the phase's riskiest decision, raised by the role that owns it (`scope_roles_and_depth.md` section 2), then resolved or accepted with a recorded reason.
   - Riskiest means highest consequence on thinnest evidence. It can be a decision treated as direct or compact, or an interaction or compounding accepted cost between decisions.
   - The objection must add something the protocol's challenge did not. Where the riskiest decision already had a protocol challenge, object to an interaction, an unverified assumption, or the next riskiest decision.
   - Full depth: two objections, one for each of the two riskiest decisions. Focused: one.
5. User-facing:
   - Phase 1 closes only on the user's confirmed summary and mode.
   - Guided mode: each message with real work opened with a wait note; entries for Phases 3 to 5 were shown at their gates as one compact table in the user's language (Phase 2's findings lead the Phase 3 entry); the turn stopped for confirmation after Phases 3 and 4.
   - Auto mode: one wait note, nothing shown at gates.
   - Phase 6 is the final reply.
6. The phase's Forward block (decisions as specifications, carry-forward obligations, open flags) and its Record entries are appended to the Design Log. A passing check is logged in one line; failures, fixes, and objections are written out.

**Cross-phase tests.** Each is defined once, here; a phase file names where it runs. Run them at the listed gates and again, scoped to what changed, when a decision changes.

| Test | Question | Runs at | Routes to |
|---|---|---|---|
| Contradiction scan | Do brand design, theme, idea, style, hero, color, type, mark, and composition agree, and from Phase 5 do the attention hierarchy, reading sequence, and placement agree? Across the set: are shared decisions identical in every deliverable, with composition differences explained by format or encounter? | 3 (plan stress tests), 4, 5 | the earliest conflicting phase |
| Brief-quality | Does each stated quality have a visible carrier at this phase's level of realization (plan, elements, composed glance stage), and does any decision signal its opposite? | 3, 4, 5 | Phase 1 for the translation, otherwise the earliest contradicting phase |
| Decided-attribute | Is any look-shaping attribute left to the model's apparent value? | 5, 6 | the phase that should own it |
| Originality | The protocol's three tests (predictable, specific, ambitious) | 3, 4, 5 | the deciding phase |
| Load and fit | Does the cumulative visual load (information, imagery, supporters, containers, treatments, surface, color intensity) fit the space budget with headroom, with the quiet genuinely open and every addition worth its marginal cost? | 3 (load budget test), 4 (element allowance and load read), 5 (load and capacity checks) | the earliest phase whose allocation or addition broke it |

## 2. Composition review

Run after Phase 5 (checklist in `14_backgrounds_review_and_gate.md`, F), and again, on the checks a Phase 3 to 5 change touches, whenever such a decision changes. A defect found here is traced to the earliest responsible decision (`triage_and_revisions.md` section 4).

## 9. Ready for Phase 6

A completeness check on the Forward blocks, run at the Phase 5 gate. It confirms that each commitment exists as a visible, drawable specification. Reasons were verified at their own gates (with sources, `workflow_and_state.md` section 4); they are not re-argued here or passed to Phase 6. A missing or vague item returns to its owning phase. A reason that is only "it looks good" or "it is typical" fails its gate.

| Commitment | Must exist as |
|---|---|
| Deliverable set | per deliverable: its format and ratio as in S, to be stated in its prompt and never substituted; the prompt count equals the set |
| Message | one sentence, confirmed in Phase 5 |
| Each quality requirement | its carriers and the resulting value key, as visible features |
| Each content item | role, treatment grade, encounter stage, placement, per deliverable it appears in |
| Supporter set | per supporter: its purpose line, form, region, and weight ceiling; or the finding that the text-only baseline has none |
| Any figure | origin, roles, the one design every appearance shares |
| Context | what the design shares with its surroundings and the dimension on which it departs, as visible traits |
| Core idea, style, hero | the chosen option in drawable terms, with the true specifics of what is depicted and the image-making language it is drawn or shot in; the hero's reinforcing content and supporters, or the reason it stands alone; the treatment vocabulary (the few rendering treatments in use, each with its job) |
| Identifier | a fixed asset, or a new mark: personality device, geometry, integration logic, distinction mechanisms, and which identity forms appear where |
| Shape language and balance | each container's function, form, and fill mode; the balance type and its counterweight |
| Space plan | area shares that with the quiet reserve account for the whole format with headroom; internal spacing of each zone; gap and clearance steps between neighbors; the reading sequence as a route over the placed regions, agreeing with the attention hierarchy and the placement; the arrangement form of each information group; the quantity of every repeated form; the planned wrap of every multi-line string; and the placement and role of every mandatory text item, per deliverable |
| Distinguishing traits | the traits that set the design apart from the peers it will be seen beside |
| Carry-forward obligations | each realized by a named decision or recorded as an accepted cost |

## Quality checks

- Every required decision of the phase is made, and the phase file's own gate checks pass.
- Each Full decision has its record; each compact comparison shows the apparent option, the options, and the decisive criterion.
- One substantive objection (two at Full depth) was raised by the owning role and resolved or accepted with a recorded reason.
- The Forward block and Record entries are appended to the Design Log; a passing check is logged in one line.
- At the Phase 5 gate, every commitment in section 9 exists as a visible, drawable specification.

## Next

Continue to the phase's next step as its "Next" line says. On any failed check read `triage_and_revisions.md`. At Phase 6 read `prompt_and_reply_audit.md` after the prompts are drafted.
