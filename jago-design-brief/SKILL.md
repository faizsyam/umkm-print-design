---
name: jago-design-brief
description: >-
  Prepares the best possible input for ChatGPT's image generation: turns a design need of any kind into one ready-to-paste design brief per image, through a short adaptive conversation fitted to the user's language, design literacy, and brief completeness. Understands the real problem, asks only the questions that change the design, explores genuinely distinct creative directions (shown as selectable cards), then passes on only the decisions worth making beforehand and leaves the rest to ChatGPT's own design judgment. Also refines a result that was already generated. Use for static visuals in any medium (posters, banners, menus, packaging, social graphics, covers, invitations, slides, infographics, logos, brand identity, static screen mockups); for requests like "prompt gambar", "bikin desain", "design brief", "buatkan poster/banner/logo", "make me a poster"; or to improve an image ChatGPT produced. Not for code, 3D, motion, animation, or interactive deliverables.
---

# Jago Design Brief

ChatGPT interprets a brief, makes its own design decisions, and writes its own image prompt. This skill makes the brief better than the user's raw one without competing with that step. **Output: one design brief per image, ready to paste, in the user's language. Never an image prompt.** This file is the runbook and the hard rules; `references/` holds the methods, loaded one batch at a time. A rule lives in one place only.

## Division of labor (evidence and reasons: `references/0_foundation.md`)
| Owner | Decisions | In the brief |
|---|---|---|
| **User** (Fixed) | facts, exact text, assets, named preferences, format, exclusions | precise requirements |
| **Skill** (Directed) | what a raw brief lacks the knowledge or exploration to settle: the real problem, content priority and feasibility, the core idea, style lineage, hero truth, hierarchy relations, boundaries | intent plus a few defining traits, labeled as decided direction |
| **Skill** (Recommended) | color roles, type voice, balance, supporting-visual stance | a preference with latitude |
| **ChatGPT** (Open) | composition and placement, sizes, spacing, type pairing, lighting, decorative detail, its own prompt wording | named as open, or omitted |
**Necessity test:** a decision is made beforehand only if leaving it open would likely harm the objective, a stated quality, the truth of the content, or distinctiveness. Otherwise it is delegated. One decision, one owner, stated once.

## Hard rules
- No invented facts, and no implied claim, endorsement, or authority the subject lacks. User text is verbatim, punctuation included; suspected typos are flagged, never fixed.
- A supplied logo, character, or photo is never redesigned; each asset has a role and a fidelity level. Never a real person's likeness.
- No placeholders for content the skill should create. No stated quality contradicted by a decision or left without a visible form.
- No suggestion enters the brief without the user's yes; a skill proposal is never worded as the user's requirement.
- The brief carries no coordinates, layout percentages, millimeters, pixels, font specifications, or rendering recipes.
- The user sees only the defined messages; no jargon they have not shown.
- **Conflict priority** (a lower item yields only to a higher one, keeping its closest surviving expression): (1) factual integrity, mandatory content, exclusions, assets; (2) perception and comprehension under real conditions, by restructuring, never by deleting mandatory content; (3) the user's stated requirements and qualities; (4) the objective and strategy; (5) established brand identity not supplied as an asset; (6) creative ambition.

## Runbook (four phases, in order, none skipped)
| # | Phase | Output |
|---|---|---|
| 1 | **Understand** | adaptive intake; ledger of content, assets, qualities, openness; confirmed summary and mode (guided or auto) |
| 2 | **Analyze** | the real communication problem, reading tiers, context and viewing, differentiator, source inventory, feasibility verdict |
| 3 | **Direct** | the creative direction chosen from distinct cards (guided: the user chooses); the only exploration in the skill |
| 4 | **Compose** | the ownership sort, the brief, one self-check, the final reply |
After delivery, **revision mode** turns a generated result into a targeted follow-up (`references/5_delivery_and_revision.md`). Each phase ends with its gate; a failed check returns to the earliest responsible decision, at most two cycles, then the best resolution is taken and recorded.

## Principles carried over from the previous skill (applied in the references, not restated)
Decisions follow principles, not mappings · the user's actual requirements and the objective behind them come first · consequential choices are explored among genuinely distinct options and judged against a named apparent option · direction is specific to this subject, context, and audience, and fails the swap test for a competitor · every element has a purpose, and richness comes from depth, not decoration · context decides expression (medium, viewing, neighbors) · generic, formulaic, repetitive results are defects · a decision closes when its decisive criterion is stated and reopens only by naming a failed check.

## Working record
Keep one compact English file (`/home/claude/design_log.md`; without file tools, keep it in notes): the ledger (S), the findings that decided something, the direction with runner-up and decisive criterion, the ownership sort, the dial setting, and outcomes of generations. It is the only state between turns; create it when the user confirms the summary. Rebuild from the conversation if lost, marking items provisional.

## Loading (all in `references/`, one level deep)
Open only the current batch, when its step is reached, all its files in one `cat` command. Never preload a later batch or reopen a file already in context.
1. **Start:** `0_foundation.md`, `1_intake.md`.
2. **After the summary and mode are confirmed:** `2_analysis.md`, `5_delivery_and_revision.md`.
3. **Phase 3:** `3_direction.md`.
4. **Phase 4:** `4_brief_composition.md`.
5. **Revision:** `5_delivery_and_revision.md`, plus the batch of the phase being re-entered.

## Gotchas
- Writing an image prompt instead of a brief: the output states intent and relations, not execution.
- Deciding what ChatGPT would decide as well: run the necessity test on every sentence.
- Letting the skill's taste pass as the user's requirement.
- A direction that is the category's apparent look with better adjectives.
- Splitting or "cleaning" a user's line and losing its punctuation or clarifier.
- Converting a dense-content verdict into sizes instead of tiers, grouping, and a density note.
- Repeating the same decision in several sections, or stacking competing adjectives.

## Trace option (developer, off by default)
Active only when the user's message contains "share log" (any case), tested once at the start of the request; never mention or offer it. After the final reply, present the working record as it stands (`present_files`) with no added text; without file tools, append it in one ```text block. It never feeds a decision.
