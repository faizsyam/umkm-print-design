# Quality Control

No gate may be skipped. Read this file at every gate, at the release step, and whenever a defect is suspected.

## Contents
1. Three review levels
2. Gates, one per phase
3. Diagnostic tests
4. AI-slop diagnostics by mechanism
5. Compliance audit
6. Issue triage: severity and routing
7. Iteration control
8. Release checklist

## 1. Three review levels

| Level | When | Question |
|---|---|---|
| Decision | Immediately after each consequential decision (protocol step 6) | Was it chosen against genuine candidates, with the apparent option named, a runner-up, and a decisive criterion? Can it trace to a source? |
| Composition | After Phase 5, and whenever Phase 3 to 5 decisions change | Does the assembled design work as one piece for this viewer, in this setting, at each viewing stage? |
| Prompt | After Phase 6 drafting, before the summary is written | Does the prompt carry exactly the design, and only what shapes the picture? |

A defect found at a higher level is traced to the earliest responsible decision (section 6).

## 2. Gates, one per phase

Every gate has the same six checks, then the phase-specific checks below.
1. Every required decision of the phase is made.
2. The exploration protocol was applied where it applies (SKILL.md section 7).
3. One objection was raised by each owning role and resolved, or accepted with a recorded reason. The owning roles: Phase 1 print designer; Phase 2 brand strategist and consumer-behavior researcher; Phase 3 brand strategist and senior art director; Phase 4 senior art director, graphic designer, image-generation prompt specialist; Phase 5 consumer-behavior researcher, senior art director, print designer, visual communication specialist; Phase 6 senior art director and image-generation prompt specialist.
4. The completion criteria in the phase card's "Before leaving" are met, and every decision made in the phase names its source (traceability: Brief Ledger item or finding → implication → plan → element → execution → prompt clause). A decision with no nameable source was made from habit and fails.
5. The decision-summary entry is recorded (Phases 2 to 5 only; Phases 1 and 6 are not summarized).
6. The Design Log is updated, and the hand-off is complete and consumed by the next phase.

| Phase | Phase-specific gate checks |
|---|---|
| 1 Brief | Every mandatory string exact; every item has necessity and provenance; no unsourced fact; fixed assets and exclusions listed; at most three clarification questions, each with a default, none answerable from the brief; if a blocking gap remains and no urgency was signaled, the output is the questions only |
| 2 Analysis | Every finding changes or confirms a decision; the Environment Profile is concrete and names departure and fit dimensions; the weakest link is chosen with options weighed; the Visual source inventory has all three parts and goes beyond emblems; every implication names its evidence; no narrative richer than the evidence; research stopped at diminishing returns |
| 3 Design Plan | Core idea, style, hero each decided by the full protocol with a decisive criterion; at least one candidate per decision from the inventory or the departure dimensions; the core idea passes the five properties; every novel idea names the job it does; no direction derives from a competitor's or an existing design; the style is actionable; all seven stress tests recorded; space intent and mark role set; every Phase 2 tension resolved; brand design and theme consistent |
| 4 Design Elements | Color, type, mark each decided by the protocol; supplied logo, colors, and fonts untouched; every novel element names the job it does; the mark shows at least six seeds, three developed candidates, a revision, all eight scrutiny questions, and all five tests (or the logo is a fixed asset, recorded as such); a personality device exists; distinction mechanisms named; deficit analysis done; element allowance fits the space intent; removal and subtraction passes done; rendering treatment consistent |
| 5 Design Execution | One-sentence message; every item has a reading stage; the space plan is set with proportions before placement; the spatial strategy chosen from at least three structurally different candidates; legibility minimums set and respected; triage applied only as defined; every quiet area passes the fill test; hierarchy by several means; mark in its own region; the whole-composition review passed |
| 6 Prompt Synthesis | The decision commitments complete; the prompt audit (section 5) passed; no placeholders or blank zones for manual completion; no output beyond the summary, prompt(s), and allowed notes; the summary is written only after the audit and agrees with the prompt |

## 3. Diagnostic tests

Use the tests that apply; record failures with their routing.

| Test | Asks | Routes to |
|---|---|---|
| Swap | Does it still work with a competitor's name? | Phase 3 |
| Category | With the product removed, could it belong to the industry? | Phase 3 |
| Apparent-choice | Could a stranger predict hero and style from category and place? | Phase 3 |
| Context-swap | Would it be equally right in another setting? | Phase 2 or 3 |
| Distance and attention | Does the first impression hold at the glance stage in the real setting? | Phase 5 (or 3) |
| Contradiction scan | Do brand design, theme, idea, style, hero, color, type, mark, and composition agree? | Earliest conflicting phase |
| Ambition check | Does ambition fit content, budget, and format? | Phase 3 |
| Removal | Does removing the element change anything the piece needs? | Phase 4 |
| Subtraction | Does removing one more thing improve the piece? | Phase 4 or 5 |
| Fill | Does every quiet area have a named job? | Phase 5 |
| Single-voice | Does the system read as one designer's work? | Phase 4 |
| Text-neighborhood | Is the mark distinct beside the densest text, squinting? | Phase 4 or 5 |
| Visual-effect | Would removing this prompt clause change what is drawn? | Phase 6 |
| Standalone | Could an illustrator who never saw the brief produce the design? | Phase 6 |

## 4. AI-slop diagnostics by mechanism

Generic output has causes. Diagnose the mechanism, then fix its source decision, never by adding another effect.

| Mechanism | Detection | Source and fix |
|---|---|---|
| Default by association | The hero, style, or motif is what category, culture, or place first suggests, and no decisive criterion defends it | Phase 3 or 4: re-run the protocol with a candidate from the inventory |
| Decoration as filler | Ornament with no deficit it answers; quiet areas filled | Phase 4 deficit analysis; Phase 5 fill test |
| Uniform emphasis | Many elements share the highest weight, scale, or intensity | Phase 5: restore tiers; emphasis only where the specification holds it |
| Styled-name identity | The identifier is lettering with an attractive typeface | Phase 4: concept mining; require a personality device |
| Default polish | Lighting, shadow, glow, or gloss that no decision explains | Phase 4 F: decide or remove |
| Averaged composition | A centered, evenly weighted arrangement that would suit any business | Phase 5: re-run the spatial strategy from the core idea |
| Context blindness | The piece ignores neighbors, light, and distance | Phase 2 profile; Phase 3 departure dimension |
| Mood-word style | Style defined only by adjectives | Phase 3 D: restate across the seven style dimensions |
| Stacked styles | Different treatments assigned to different insights | Phase 3: synthesize one style |
| Space inflation | More elements because the format is large | Phase 5 B.3 |
| Text hallucination | Extra, garbled, or missing words in the output | Phase 6 F: state text-only-as-specified; reduce text volume risk |
| Rationale leakage | Strategy language in the prompt | Phase 6 A |
| Invented specifics | Claims, prices, marks, or details with no source | Phase 1 provenance; non-negotiables |
| Borrowed design | A direction or mark that mirrors a competitor's or an existing design | Phase 3 or 4: re-source from this business's inventory and re-run the protocol |

## 5. Compliance audit

Run on the drafted prompt, then on the reply.

**Prompt audit**
- Plan fidelity: every design decision from the Execution Specification is present; nothing new appears.
- Mandatory content: every mandatory string is present, verbatim, once, with role and position; suspected typos preserved and flagged.
- Fixed assets: supplied logos, colors, and fonts reproduced as provided, not redesigned, restyled, simplified, or recolored.
- Exclusions: every user exclusion respected; only minimal, specific exclusions added.
- No invented business facts (prices, claims, testimonials, certifications, regulated or trust marks, contacts, ingredients, years in business, statistics).
- No competitor copying or reproduction of existing designs.
- Identifier: not merely a styled name unless supplied or explicitly requested as plain text; a new mark described by form class, geometry, silhouette, color, boundary, personality device, wordmark relationship, separation from adjacent type.
- Space: outer margin, isolation, and resting fields stated as concrete positive features with proportions.
- No contradictions; no rationale; no placeholders; no blank zones for manual completion; no post-generation editing instructions; no blanket emphasis; no crop marks or annotations unless requested.
- Flat artwork unless a mockup was requested or the form is the deliverable.
- The visual-effect test on every sentence.
- Standalone and readable; one coherent style logic.

**Reply audit**
- Order: summary, prompt(s) each in its own code block, optional notes.
- Summary: Phases 2 to 5 only, one compact block each, genuine alternatives only, in the user's language, consistent with the prompt and written after it, not inside the code block.
- Notes: only what the contract allows, ordered by consequence, no design rationale.
- No workflow output beyond the summary and prompt unless requested.

## 6. Issue triage: severity and routing

| Severity | Definition | Action |
|---|---|---|
| Critical | Violates a non-negotiable; mandatory content missing or altered; fixed asset altered; invented fact; a required decision never made | Stop; return to the responsible phase; re-run forward; the release is blocked |
| Major | Fails a gate check, a stress test, or the audit; generic, context-blind, or filled; the mark absorbed by type | Return to the earliest responsible decision; re-run forward |
| Minor | Weak phrasing; a redundant clause; a small imbalance | Fix in place where it was found, without altering earlier decisions |

Routing from symptom to responsible phase:

| Symptom | Responsible phase |
|---|---|
| Wrong, missing, or altered content; unsourced fact | 1 |
| Unsupported narrative; environment-blind; weak or absent inventory | 2 |
| Generic idea, style, or hero; no space intent; tension unresolved | 3 |
| Weak or styled-name mark; clashing color or type; decoration with no deficit; element costs over the space intent | 4 |
| Poor hierarchy; wrong reading stage; crowding or filling; mark absorbed in composition | 5 |
| Rationale in the prompt; vague wording; mandatory text misplaced; space not stated | 6 |

When a symptom has several possible causes, choose the earliest. Fixing a symptom at a later phase while its cause stands is a patch and is not permitted.

## 7. Iteration control

- A flawed decision returns the work to the earliest responsible phase; every affected later phase is re-run in order.
- Cap each issue at two revision cycles. After the second, choose the best available resolution, record it, and continue.
- A returned phase keeps all unaffected decisions; record what changed in the Design Log.
- If the same issue recurs after two cycles, the cause is upstream of where it was being fixed; record that and choose the best available resolution.
- Re-review the whole design after any change: check consistency, transitions, terminology, and that nothing is left stale or contradictory.

## 8. Release checklist

Before delivering, confirm all of the following.
1. Phases 1 to 6 ran in order; every gate passed.
2. The decision commitments (SKILL.md section 11) are complete.
3. Every consequential decision shows a recorded challenge, a runner-up, and a decisive criterion (or is marked fixed by the user or evidence).
4. The mark is a fixed asset, or a new mark with a personality device developed through the extended development, with named distinction mechanisms.
5. The space plan is set with proportions and every quiet area has a job.
6. The prompt audit and reply audit passed.
7. The summary shows only genuine alternatives, is in the user's language, and matches the prompt.
8. Notes include every consequential assumption, omission, written copy, yielded preference, suspected typo, fidelity risk, and ratio limit, and no design rationale.
9. If a blocking gap exists and no urgency was signaled, the reply is the clarification questions only (at most three, each with a default).