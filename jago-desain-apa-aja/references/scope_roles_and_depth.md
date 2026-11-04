# Scope, team roles, depth, and the deliverable set (all phases)

Defines what the skill delivers, who owns and objects to which decisions, how depth scales the work, and how the deliverable set and several concepts are counted.

**Read this when:** at the start of every new request, before the first user message is answered (Phase 1 sets the depth and the deliverable set); reopen section 2 whenever a gate objection is raised.

**Inputs needed:** The user's first message and any attachments. No earlier step output.

## 1. Mission and scope

Turn a design need, from anyone between a first-time requester and a professional designer, into one or more finished, standalone image-generation prompts for static visual outputs, through a short design conversation.

- **Adaptation.** Language, register, terminology, and the depth of questions and guidance adapt to the user's design literacy and the completeness of the brief. The depth of design reasoning never adapts.
- **What the user reads.** The intake questions; the confirmed summary with its mode choice (**guided**: confirm at key points; **auto**: leave everything to the AI); wait notes; short phase entries; amendments and revision tables; and a final reply with the prompts and brief usage steps. `00_conversation_voice_modes_and_intake.md` and `ux_wait_notes_entries_and_final_reply.md` govern every user message.
- **Language.** Working notes and the Design Log are in English and stay internal unless the user asks. Prompts are in English by default, with on-image text kept verbatim in its original language.

The skill succeeds when it:
- runs six phases in order: **Brief → Analysis → Design Plan → Design Elements → Design Execution → Prompt Synthesis**;
- decides like a professional team: grounded in the subject, its audience, and the context where each deliverable is encountered; tested against genuine alternatives; never settling on the first idea;
- treats every quality the brief asks for (mood, tone, brightness, warmth, priority, or a named style, color, or technique), however vague, as a binding requirement, translated into visible, checkable features and carried through every phase;
- produces distinctive, well-composed designs: a genuinely designed identifier where one is needed, deliberately treated content, purpose-driven supporters, a visual world drawn from the theme (or plainness chosen on purpose), deliberate layering, no generic AI aesthetics;
- delivers prompts that each contain only what shapes the picture and can be executed alone.

**Scope.** Static visual deliverables in any medium, physical or on screen; a screen is in scope as a static image of it. The output is always image-generation prompts: no code, no 3D, no motion, animation, interaction, or flows. When a request needs more than static images, say once which part the skill can deliver (the static frames as seen) and proceed only on confirmation.

A standalone logo request: Phase 3 fixes the mark as hero; Phase 4 develops it through the extended mark development; Phase 5 composes it as a single stage on a plain field with a generous space plan; the prompt describes the mark itself.

Decision quality matters more than text volume.

## 2. The team

Roles are decision owners and gate objectors, not extra work.

| Role | Owns | Objects at gate of |
|---|---|---|
| Brand strategist | Identity, positioning, differentiation, truth of claims, fidelity to the brief's qualities | 2, 3, 4 |
| Audience researcher | Audience encounter, attention, trust, action | 2, 5 |
| Senior art director | Core idea, style synthesis, restraint and richness, taste, composition review | 3, 4, 5, 6 |
| Graphic designer | Type voice, color and value key, logo mark, copy treatment, supporters, containers and decorative vocabulary | 4 |
| Production specialist | Encounter reach, reproduction conditions, format behavior | 1, 5 |
| Visual communication specialist | Hierarchy, reading sequence, grouping and group space needs, comprehension speed, space budget and plan, load and fit | 3, 5 |
| Image-generation prompt specialist | Renderability (checked in 3 to 5), prompt boundary, standalone completeness, phrasing | 4, 6 |

## 6. Depth and the deliverable set

Phase 1 sets the depth and records it in the log. Depth scales the work inside every phase and never drops a phase, decision, protocol step, or gate. (It is unrelated to the picture's front-to-back order, which is layering.)

- **Full:** a new identity mark must be created, or any deliverable is contested, or the set has several deliverables, or content is dense for its format.
- **Focused:** everything else. Raise to Full as soon as any phase shows a Full condition.

Reading the Full conditions:
- **Contested:** the deliverable must win attention against its neighbors from beyond arm's reach or in a crowded field.
- **Several deliverables:** the set holds more than one.
- **Dense:** content volume is high for the format; judged from the Phase 1 load read and re-judged by Phase 3's load budget test.

| | Full | Focused |
|---|---|---|
| Research (Phase 2) | every question that can change a decision | the one or two that can |
| Territory survey (Phase 3) | at least 5 territories from at least 3 source families | at least 3 territories from at least 2 families |
| Candidate cards | every field the phase sets | fields that tell candidates apart, plus quality compatibility |
| Governing principles (Phase 3) | compared: space intent, density and rhythm, imagery and decoration, integration, mark role, layering, tone and positioning | compared: space intent, density and rhythm, imagery and decoration, integration, mark role; rest decided directly |
| New mark (Phase 4) | at least 6 seeds, every check recorded | at least 4 seeds, checks as pass/fail lines |
| Gate objections | two (the two riskiest decisions) | one |

Depth never changes: naming the apparent option, three or more candidates, the runner-up and decisive criterion, the quality checks, the load budget test, the capacity check, verbatim content, or the audits. A rich brief shortens Phase 1 and 2 notes; a sparse brief deepens research.

**Raising to Full** applies from the current phase on. Reduced work in an earlier phase is reopened only where the missing depth could change a decision already made: the survey gains territories until it meets the Full count before the mark seeds are written.

**Deliverable set.** Phase 1 records every deliverable the request needs, derived from what the user must accomplish and not only from what they named.
- One deliverable per image that must exist: a distinct format or ratio, a distinct side, panel, or screen, or a variant or concept the user asked for.
- What belongs in one image stays one image. What differs in format or encounter enough to change the composition becomes its own deliverable.
- A different size at the same ratio and encounter is the same deliverable.

**Shared and per-deliverable decisions.**
- Phases 2 to 4 decide once what the set shares: a context where deliverables share one, identity, style, color, type, element system.
- Each deliverable gets its own stage assignment, space plan, strategy, hierarchy, and placement (Phase 5) and its own standalone prompt (Phase 6).
- A deliverable is never derived by resizing or cropping another's composition. Format changes the reach of the stages, the regions available, the reading path, and the balance, so composition is decided for each format. What transfers across deliverables is decisions, not layout.

**Several concepts.**
- Run Phases 1 and 2 once; run each of Phases 3 to 5 across all concepts before moving on.
- Each concept starts from a core-idea candidate that differs on a structural axis (never only color or decoration) and ends in its own standalone prompt per deliverable.
- One entry per phase, with a short subsection per concept. Forward blocks and Records are kept per concept; S is shared.

Prompts delivered = deliverables × concepts. Never add a deliverable for a variation the user did not need, and never split content that is one image.

## Quality checks

- Pass: depth, deliverable set, and role ownership are recorded as sections 2 and 6 require, and the Phase 1 gate (`01_brief_and_requirements.md`) confirms them.

## Next

Read `terms_brief_and_context.md` if not yet read, then `01_brief_and_requirements.md`.
