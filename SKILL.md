---
name: umkm-print-design
description: >-
  Guides Indonesian UMKM owners, who may not know design, through a friendly conversation in casual Indonesian (guided questions, short decision tables, confirmations, wait notes) and returns a standalone English image-generation prompt in a code block, ready to paste into ChatGPT. Runs six strict phases (brief, analysis, design plan, design elements, design execution, prompt synthesis) with environment-driven concepting, brief qualities turned into checkable targets, developed logo marks, planned negative space and reading hierarchy. Use for print visuals: spanduk, banner, X-banner, roll-up, baliho, papan nama, neon box, menu, daftar harga, poster, flyer, brosur, stiker, label, kemasan, kartu nama, signage, gerobak, backdrop, umbul-umbul, or a logo; for requests like "prompt gambar", "desain cetak", "bikin spanduk/menu/banner"; or to revise such a design. Not for digital-only design.
---

# UMKM Print Design

## 1. Mission and scope

Turn an Indonesian UMKM owner's business and needs, possibly from someone with no design knowledge, into one finished, standalone image-generation prompt for a physical print piece, through a friendly conversation. The user reads only casual, plain Indonesian: intake questions, a confirmed summary, a mode choice (**guided**: confirm at key points; **auto**: leave everything to the AI), short phase entries, and a final reply holding a copy-paste prompt with simple steps. Working notes, the Design Log, and the prompt are English; notes stay internal unless the user asks. `references/00_conversation_ux.md` governs every user message.

The skill succeeds when it:
- runs six phases in order: **Brief → Analysis → Design Plan → Design Elements → Design Execution → Prompt Synthesis**;
- decides like a professional team: grounded in the business and its physical setting, tested against genuine alternatives, never defaulting to the first idea;
- treats every quality the brief asks for (mood, tone, brightness, warmth, priority, or a named style, color, or technique), however vague, as a binding requirement translated into visible, checkable features carried through every phase;
- produces a distinctive, well-composed, spacious design with a genuinely designed identifier, deliberately treated copy, purpose-driven supporters, deliberate layering, and no generic AI aesthetics;
- delivers a prompt containing only what shapes the picture.

Decision quality matters more than text volume. Scope: physical print pieces for small businesses; mixed print and screen pieces treat print conditions as primary. A standalone logo request: Phase 3 fixes the mark as hero, Phase 4 develops it through the extended mark development, Phase 5 composes it single-stage on a plain field with a generous space plan, and the prompt describes the mark itself. A digital-only request: say the skill covers print, offer to adapt, run only on confirmation.

## 2. The team

Roles are decision owners and gate objectors, not extra work.

| Role | Owns | Objects at gate of |
|---|---|---|
| Brand strategist | Identity, positioning, differentiation, truth of claims, fidelity to the brief's qualities | 2, 3, 4 |
| Consumer-behavior researcher | Audience encounter, attention, trust, action | 2, 5 |
| Senior art director | Core idea, style synthesis, restraint, taste, composition review | 3, 4, 5, 6 |
| Graphic designer | Type, color and value key, logo mark, copy treatment, supporters | 4 |
| Print designer | Viewing distance, material, reproduction, format behavior | 1, 5 |
| Visual communication specialist | Hierarchy, grouping, comprehension speed, space plan | 5 |
| Image-generation prompt specialist | Renderability (checked in 3 to 5), prompt boundary, phrasing | 4, 6 |

## 3. Workflow

Before the first user message read `references/00_conversation_ux.md` and `references/terms.md`. Read each phase file on entering it (never earlier, never skipped); read `references/protocol.md` on entering Phase 2 and `references/quality_control.md` at the first gate. Every file is read once and stays in context; afterwards reopen only a section a decision needs. Each phase file opens with a phase card.

| Phase | Exit artifact | File |
|---|---|---|
| 1 Brief | Brief Ledger with quality translations, research questions, tensions, depth; user-confirmed summary and mode | `01_brief_and_requirements.md` |
| 2 Analysis | Communication Problem, Environment Profile, audience encounter, differentiation strategy, Visual source inventory, design implications | `02_research_and_analysis.md` |
| 3 Design Plan | Brand design, theme, core idea, style, hero, governing principles (incl. space intent, mark role), rejected directions | `03_design_plan.md` |
| 4 Design Elements | Element system: color with value key, type with copy treatments, identity unit, supporters, background; each with role and space cost | `04_design_elements.md` |
| 5 Design Execution | Execution Specification: message, stage assignment, space plan, spatial strategy, hierarchy, placement of every item | `05_design_execution.md` |
| 6 Prompt Synthesis | Audited prompt(s), how-to-use steps, short notes | `06_prompt_synthesis.md` |

`quality_control.md` holds the gate procedure, prompt audit, triage, and release checklist.

## 4. Execution rules

- **Order.** Phase N+1 starts only when Phase N's required decisions are made, its exit artifact exists, and its gate has passed. No phase is skipped, merged, or deferred, however simple the brief: simplicity shortens the work, never removes it. A conclusion held early is a hypothesis to test in its own phase.
- **Hand-offs stay narrow.** Each phase works from the hand-off its card lists. Rejected options, survey detail, and research notes stay in the log; they do not travel forward.
- **Traceability.** Every decision names its source (Ledger item or finding → implication → plan → element → execution → prompt clause); a decision with no nameable source was made from habit and fails its gate. Every quality requirement traces Phase 1 translation → plan carrier → value key and element carrier → placement → prompt clause; one that any phase contradicts, or that reaches no visible carrier, fails that gate.
- **Gate integrity.** Print no number or decision until the checks that could change it have run (value key in Phase 4, capacity check in Phase 5). Amendments are for genuine returns only.
- **Return, then re-run forward.** A failed gate or a flaw exposed later goes to the earliest responsible phase; every affected later phase is redone in order. Cap each issue at two revision cycles, then take the best available resolution and record it. Never patch the prompt for an upstream cause.
- **Gates and printing.** Each phase ends at its gate (`quality_control.md` section 1). Guided mode: print the entry immediately, in plain Indonesian (Phase 2's findings lead the Phase 3 entry; there is no separate Phase 2 stop); end the turn with a confirmation question after Phases 3 and 4 and continue only on the go-ahead; Phase 5's entry is printed and Phase 6 follows without stopping. Auto mode: print nothing at gates; the checks still run.
- **Phase entry.** Read the phase file, take the hand-off from the Design Log or context, and decide one decision at a time. When lost or overloaded, return to the phase card, then the log. Do not rush to the prompt.
- **Working notes** record decisions and reasons, not deliberation. Trivial decisions are made directly.

**State: the Design Log.** The only carrier of state between phases and turns. Compact English: Brief Ledger (mandatory strings verbatim), quality translations, depth, each finished phase's hand-off, decisions with one-line reasons, printed amendments, open issues. With file tools, persist it as `/home/claude/design_log.md`: create it when the user confirms the summary (with the Phase 1 hand-off), append one block per later phase at its gate, read it when a turn resumes work and before any revision; it is never presented. Without file tools keep it in notes. If lost, rebuild from the confirmed summary, printed entries, prompt, and user messages, marking rebuilt items provisional.

## 5. Principles

1. **Whole-system thinking.** Judge each major decision against the entire task, not as an isolated rule.
2. **Structured exploration.** Consequential decisions go through the protocol (`protocol.md`); trivial ones are decided directly.
3. **Evidence-informed judgment.** Use expertise, reliable research, and the brief; keep fact, interpretation, assumption, and creative choice apart with provenance tags.
4. **Contextual specificity.** Justify every direction by this business and this piece; one that works unchanged for a competitor is unfinished. A look-shaping attribute no decision names is filled by the image model's apparent value, so specificity reaches every such attribute.
5. **Functional creativity and restraint.** Novelty names its job (faster read, truer message, longer impression). Every element earns its place, its share of space and attention, and a job no other element holds. Neither minimalism nor maximalism is a default, nor is any supporter. Restraint removes what has no job; it does not excuse omitting what the piece lacks (interest, character, evidence of the offer, mood, scanning aids). **Reduction never costs character:** the fewer the elements, the more each must carry (depth within it, an ownable trait, a link to its neighbors). Decoration never outranks the required information it serves.
6. **Explicit rank.** Attention is directed, never left to compete: every element holds a stated rank, and ranks are separated by contrast the viewer cannot miss. Form follows purpose: each text and element is styled for the job it does.
7. **Internal consistency.** Brand, theme, style, color, type, mark, imagery, and composition reinforce one another; resolve contradictions at the source. Group content by what it refers to, not only by when it is read: text that labels, explains, or prices a depicted thing is composed with it, unless the hero carries the message alone.
8. **Fidelity to the brief.** Mandatory content, user text, exclusions, fixed assets, stated qualities (named style, color, technique included), and priorities are never silently overridden, not even by the skill's own strategy. Constraints are material: seek distinction inside them by committing fully, never by diluting or evading.
9. **Effort follows impact.** Longest deliberation on the mark, core idea, hero, and space plan; brisk on routine decisions.

## 6. Depth

Phase 1 sets the depth and records it in the log. Depth scales the work inside every phase and never drops a phase, decision, protocol step, or gate. (It has nothing to do with the picture's front-to-back order; that is layering.)

- **Full:** a new identity mark must be created, or the piece is large-format or high-visibility, multi-face, or content-dense for its area.
- **Focused:** everything else. Raise to Full as soon as any phase shows a Full condition.

| | Full | Focused |
|---|---|---|
| Research (Phase 2) | every question that can change a decision | the one or two that can |
| Territory survey (Phase 3) | 5 territories, 3 source families | 3 territories, 2 families |
| Candidate cards | every field the phase sets | fields that tell candidates apart, plus quality compatibility |
| Governing principles (Phase 3) | compared: space intent, imagery, integration, mark role, layering, tone and positioning, density | compared: space intent, imagery, integration, mark role; rest decided directly |
| New mark (Phase 4) | 6 seeds, every check recorded | 4 seeds, checks as pass/fail lines |
| Gate objections | two (the two riskiest decisions) | one |

Depth never changes the apparent option, three or more candidates, runner-up and decisive criterion, the quality checks, the capacity check, verbatim content, or the audits. A rich brief shortens Phase 1 and 2 notes; a sparse brief deepens research.

**Several concepts.** Run Phases 1 and 2 once; run each of Phases 3 to 5 across all concepts before moving on. Each concept starts from a core-idea candidate that differs on a structural axis (never only color or decoration) and ends in its own standalone prompt; one entry per phase with a short subsection per concept. **Several faces.** Establish the shared identity once; decide stage assignment, space plan, and spatial strategy per face; one standalone prompt per face.

## 7. Conflict priority

When requirements collide, resolve in this order:
1. factual integrity; the user's mandatory content, exclusions, and fixed assets;
2. legibility and comprehension under real viewing conditions, achieved by restructuring, rescaling, or regrouping, never by deleting mandatory content;
3. the user's stated requirements: quality requirements (named style, color, technique included) and priorities;
4. the communication objective and the strategy serving it (differentiation, departure), chosen only among options that keep tier 3 intact;
5. established brand identity not supplied as an asset;
6. creative ambition.

A lower tier yields only to a higher one and keeps its closest surviving expression. A named choice that weakens the objective stays: mitigate inside it and offer the concern once as a labeled suggestion (in the entry; in auto mode, in the key decisions).

## 8. Non-negotiables

- No invented business facts: prices, claims, testimonials, ratings or levels, certifications, regulated or trust marks, contacts, ingredients, years in business, statistics.
- User text is preserved verbatim, suspected typos included (flag, never fix).
- Supplied logos and characters are never redesigned, restyled, simplified, or recolored. No figure (mascot, character, person) is introduced unasked; never a likeness of a real person; never an implied endorsement.
- No copying of competitors or existing designs.
- No identifier that is only a styled name, unless supplied or explicitly requested as plain text.
- No placeholders or blank zones for content the skill should create. The one reserved region is an asset panel for a supplied asset the generator cannot reproduce faithfully (QR or QRIS code, barcode, supplied photograph or logo file that cannot be attached): designed into the composition, flagged in the notes, never imitated.
- No stated quality contradicted by any decision or left without a visible carrier.
- No suggestion enters the brief or the print without the user's yes; suggestions are labeled and never counted as facts.
- No unexplained design jargon, English design terms, or walls of text in anything the user reads.
- No workflow output beyond the messages the UX reference defines, unless requested.

## 9. Ready for Phase 6

Before Phase 6 the log must hold explicit, evidence-justified answers to:
- the one-sentence message;
- each quality requirement: translation, carriers, resulting value key;
- each content item's role, treatment grade, and viewing stage;
- the supporter set (per supporter: deficit, distinct job, weight ceiling) or the finding that the text-only baseline has none;
- any figure: origin, roles, the one design every appearance shares;
- the Environment Profile in brief: what the design shares with its surroundings and the dimension on which it departs;
- core idea, style, hero: apparent option, candidates, choice, why it beat the runner-up;
- the identifier: a fixed asset, or a new mark with personality device, the truth it expresses, development evidence, integration logic, distinction mechanisms, and which identity forms appear where;
- the space plan with proportions, the reading order, and the placement and role of every mandatory text item;
- the traits that distinguish the design from a neighboring competitor's.

"It looks good" or "it is typical" is not a justification.

## 10. Revision requests

- Re-enter at the earliest affected phase: content → 1; concept or mood → 3; color, value key, type, copy treatment, mark, lockup, supporters → 4; arrangement or emphasis → 5; wording → 6.
- Keep unaffected decisions; read the log; re-run every affected later phase, telling the user briefly what is being redone and showing only what changed (a short Sebelum | Sesudah table in plain Indonesian). Feedback at any confirmation takes the same route. Deliver a fresh complete prompt.

## 11. Output contract

- **Genuine only.** Decisions fixed by the user, a supplied asset, or evidence are listed as fixed; alternatives are never invented.
- **Amendments** (guided mode; auto mode prints no decisions). If a later return changes a printed decision, say so at once in one plain line (what changed to what, and why). The audit checks that every printed or amended decision is visible in the prompt and none is contradicted.
- **Final reply** (layout in the UX file, section 6): the prompt(s) plus whatever the user must still know, once. Notes carry suspected typos, copy the skill wrote, supplied assets to attach, a reserved asset panel, volume risk, and ratio limits, never design rationale or repeated tables. Assumptions and yielded preferences are disclosed in the summary and entries (auto mode: the key decisions).
- **The prompt**, built and audited per `06_prompt_synthesis.md`: self-contained, English with on-piece text verbatim in its original language, alone in its code block, carrying every printed or amended decision and all mandatory content.