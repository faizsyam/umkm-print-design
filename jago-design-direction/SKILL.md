---
name: jago-design-direction
description: >-
  Turns a design need of any kind into distinctive, business-specific creative direction and one ready-to-use English design brief per image, through a short adaptive conversation fitted to the user's language, design literacy, and brief completeness. Finds what is true and ownable about the business, maps the conventions of its category, derives a specific art direction from audience, mood, price tier, and medium, develops genuinely distinct directions (shown as selectable cards) into one coherent system, and forecasts the literal visual result before choosing; the brief states decisions firmly and leaves unstated details to the maker. Also refines an existing result. Use for static visuals in any medium (posters, banners, menus, packaging, social graphics, covers, invitations, slides, infographics, logos, brand identity); for requests like "prompt gambar", "bikin desain", "design brief", "buatkan poster/banner/logo"; or to improve a result. Not for code, 3D, motion, animation, or interactive deliverables.
---

# Jago Design Direction

Develops expert creative direction for a business and its design need, then writes it as one standalone design brief per image, in English. The **maker** is whoever produces the image from the brief alone. The brief carries what makes the design distinctive, true, effective, and well made; it omits what the maker can decide as well or better. The conversation stays in the user's language. This file is the runbook and the hard rules; `references/` holds the methods, loaded one batch at a time. A rule lives in one place only.

## Hard rules
- No invented facts, and no implied claim, endorsement, or authority the business lacks. User text is verbatim, punctuation included; suspected typos are flagged, never fixed.
- **Language:** the brief is in English. Verbatim text is never translated or altered. Everything else the user reads is in their language.
- **Spine:** the user's stated look, hero, palette, mood, and qualities are the spine of the work. The direction deepens them with craft and specificity; it never replaces, dilutes, or competes with them unless the user left that decision Open.
- A supplied logo, character, or photo is never redesigned; each asset has a role and a fidelity level. Never a real person's likeness. Never a copy of a competitor or an existing design.
- No identifier that is only a styled name, unless supplied or requested as plain text.
- No placeholders for content the skill should create. No stated quality contradicted by a decision, weakened below the user's words, or left without a visible form.
- No suggestion enters the brief without the user's yes; a skill proposal is never worded as the user's requirement.
- The brief carries no coordinates, layout percentages, millimeters, pixels, font specifications, or rendering recipes.
- The user sees only the defined messages; no jargon they have not shown.
- **Conflict priority** (a lower item yields only to a higher one, keeping its closest surviving expression): (1) factual integrity, mandatory content, exclusions, assets; (2) perception and comprehension under real conditions, by restructuring, never by deleting mandatory content; (3) the user's stated requirements and qualities; (4) the objective and strategy; (5) established brand identity not supplied as an asset; (6) creative ambition.

## How the work earns its distinctiveness
| Phase | Question it answers | Output |
|---|---|---|
| 1 **Understand** | What must this do, for whom, where, and what must never change? | ledger; confirmed summary and mode (guided or auto) |
| 2 **Discover** | What is true and ownable about this business, what does its category take for granted, and what opportunities does that open? | communication problem, reading tiers, feasibility, **design truth**, **code map and baseline**, **opportunity pool** |
| 3 **Direct** | Which genuinely distinct idea is right, what art direction follows from the forces on this piece, and what single system follows? | cards judged on eight tests; the chosen idea; the **art direction**; the direction as one chain with **signature moves** |
| 4 **Compose** | What must the maker be told, and what is better left to it? | the ownership sort, the brief, a render-forecast review, the final reply |
Every consequential decision is judged against the **baseline** (the strongest direct execution of the brief as the user stated it) and must name what it improves. After delivery, **revision mode** turns a result into a targeted follow-up. Each phase ends with its gate; a failed check returns to the earliest responsible decision, two cycles at most, then the best resolution is taken and recorded.

## What the brief fixes and what it leaves
| Owner | Decisions | In the brief |
|---|---|---|
| **User** (Fixed) | facts, exact text, assets, named preferences, palette, format, exclusions | Requirements: precise |
| **Skill** (Decided) | the idea as a visual result, art direction, hero truth, signature moves, color roles, lettering voice, hierarchy and grouping relations, boundaries | Direction: firm statements |
| **Maker** (Open) | composition and placement, sizes, spacing, type pairing, lighting setup, decorative and finish detail | omitted; never listed or handed back |
**Necessity test:** a decision is made beforehand only if leaving it open would likely harm the objective, a stated quality, the truth of the content, or the quality or distinctiveness of the image. One decision, one owner, stated once. A matter only the user can resolve is asked in Phase 1 or settled by a flagged default; the brief never carries an unresolved item.

## Working record
Keep one compact English file (`/home/claude/design_log.md`; without file tools, keep it in notes): the ledger (S), the findings that decided something, the design truth, the code map and baseline, the art-direction forces and chosen lineage, the chosen direction with runner-up and decisive criterion, the ownership sort, the prescription setting, and outcomes of use. It is the only state between turns; create it when the user confirms the summary. Rebuild from the conversation if lost, marking items provisional.

## Loading (all in `references/`, one level deep)
Open only the current batch, when its step is reached, all its files in one `cat` command. Never preload a later batch or reopen a file already in context.
1. **Start:** `1_understand.md`.
2. **After the summary and mode are confirmed:** `2_discover.md`, `6_delivery_and_revision.md`.
3. **Phase 3:** `3_create_directions.md`, `4_direction_system.md`.
4. **Phase 4:** `5_compose_brief.md`.
5. **Revision:** `6_delivery_and_revision.md`, plus the batch of the phase being re-entered.

## Gotchas
- A direction that is the category's obvious look with better adjectives: compare with the baseline on named dimensions, not adjectives.
- Taking the stock object or symbol of the trade as the idea: the idea is the specific truth one level beneath it.
- A governing idea grown from a secondary item instead of the hero and the glance message.
- A concept carried as a material, finish, or object-as-surface: it renders as a literal texture or a picture of an object, not as design. State the look, not the metaphor.
- Naming a style by medium, format, or mood adjective and calling it art direction.
- Narrowing or calming a quality below the user's own words, or silently choosing between options the user listed.
- An idea with no signature moves, or signature moves that appear in one place only, or that blanket the whole image as a filter.
- Decoration that restates the category, a default present only because pieces of this kind have it, or plainness that contradicts a stated quality.
- Fixing what the maker would decide as well; letting the skill's taste pass as the user's requirement.
- Hedged wording ("prefer", "may", "ideally") or a closing list of decisions handed back to the user.
- Splitting or "cleaning" a user's line and losing its punctuation or clarifier.
- Converting a dense-content verdict into sizes instead of tiers, grouping, and a density note.

## Trace option (developer, off by default)
Active only when the user's message contains "share log" (any case), tested once at the start of the request; never mention or offer it. After the final reply, present the working record as it stands (`present_files`) with no added text; without file tools, append it in one ```text block. It never feeds a decision.
