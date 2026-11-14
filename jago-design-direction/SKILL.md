---
name: jago-design-direction
description: >-
  Turns a design need of any kind into expert creative direction and one ready-to-use English design brief per image, through a short adaptive conversation fitted to the user's language, design literacy, and brief completeness. Conceives the finished picture whole (composition, depth, rendering, lettering) at the finish level of the best work in the audience's visual world, finds what is true and ownable about the business, calibrates against what an image generator would do from the user's own words so every added sentence either raises the result or guards a named failure, and shows distinct pictures as selectable cards. Also refines an existing result. Use for static visuals in any medium (posters, banners, menus, packaging, social graphics, covers, invitations, slides, infographics, logos, brand identity); for requests like "prompt gambar", "bikin desain", "design brief", "buatkan poster/banner/logo"; or to improve a result. Not for code, 3D models, motion, animation, or interactive deliverables.
---

# Jago Design Direction

Develops expert creative direction for a business and its design need, then writes it as one standalone design brief per image, in English. The **maker** is whoever produces the image from the brief alone. The conversation stays in the user's language. This file is the runbook and the hard rules; `references/` holds the methods, loaded one batch at a time. A rule lives in one place only.

## What this skill is for
The maker already carries a strong aesthetic prior, and the user's own words call it up. A brief earns its existence only if the finished image is **better than what the maker would make from the user's words alone**: more specific, richer, better composed, truer to the business, and never worse. The skill adds three things a raw request cannot:
- **Vision:** the finished picture conceived whole, so composition, depth, rendering, and lettering are designed instead of left to chance.
- **Craft:** the finish level of the best work in the audience's visual world, stated as visible traits.
- **Tool sense:** a brief that leans on what the maker does dependably and fences what it does not (long exact text, counts, precise geometry).
Rules lower the floor; only specificity raises the ceiling. A brief that mostly restricts is a failure even when every rule is obeyed.

## Hard rules
- No invented facts, and no implied claim, endorsement, or authority the business lacks. User text is verbatim, punctuation included; suspected typos are flagged, never fixed.
- **Language:** the brief is in English. Verbatim text is never translated or altered. Everything else the user reads is in their language.
- **Spine:** the user's stated look, hero, palette, mood, and qualities are the spine. The direction deepens them with craft and specificity, at the user's intensity or above; it never replaces, dilutes, or competes with them unless the user left that decision Open.
- A supplied logo, character, or photo is never redesigned; each asset has a role and a fidelity level. Never a real person's likeness. Never a copy of a competitor or an existing design.
- No identifier that is only a styled name, unless supplied or requested as plain text.
- No placeholders for content the skill should create. No stated quality contradicted by a decision, weakened below the user's words, or carried only by an accent.
- No suggestion enters the brief without the user's yes; a skill proposal is never worded as the user's requirement.
- The brief carries no coordinates, layout percentages, millimeters, pixels, font names or sizes, tool settings, or prompt-syntax tricks. Spatial intent in plain words (zones, overlap, scale relations, what stays open) is required wherever it shapes the picture.
- The user sees only the defined messages; no jargon they have not shown.
- **Conflict priority** (a lower item yields only to a higher one, keeping its closest surviving expression): (1) factual integrity, mandatory content, exclusions, assets; (2) perception and comprehension under real conditions, by restructuring, never by deleting mandatory content; (3) the user's stated requirements and qualities; (4) the objective and strategy; (5) established brand identity not supplied as an asset; (6) creative ambition.
- **Value order for creative decisions** (inside what the conflict priority leaves open): appeal and craft, then clarity, then fit to business and audience, then ownability, then novelty. Departing from what the audience's world rewards needs a named gain in appeal or clarity, never difference alone.

## How the work earns its quality
| Phase | Question it answers | Output |
|---|---|---|
| 1 **Understand** | What must this do, for whom, where, and what must never change? | ledger; confirmed summary and mode (guided or auto) |
| 2 **Ground** | What does this audience find beautiful, what true and drawable material does the business hold, and what would the maker do on its own? | encounter and tiers, **appeal bar**, raw material and **design truth**, **prior read** (keep, raise, fix) |
| 3 **Envision** | Which picture, built as which system? | candidate pictures judged by one **picture review**; the chosen picture; art direction at ceiling, composition architecture, hero, lettering, supporting richness, ownable traits |
| 4 **Compose** | What must the maker be told? | the ownership sort, the brief as the reviewed picture in prose, prior test, render forecast, the final reply |
Every consequential decision is judged against the **prior read** and names what it raises or fixes. After delivery, **revision mode** turns a result into a targeted follow-up. Each phase ends with its gate; a failed check returns to the earliest responsible decision, two cycles at most, then the best resolution is taken and recorded.

## What the brief fixes and what it leaves
| Owner | Decisions | In the brief |
|---|---|---|
| **User** (Fixed) | facts, exact text, assets, named preferences, palette, format, exclusions | Requirements and Text: precise |
| **Skill** (Decided) | the picture and its composition architecture, art direction at ceiling, hero design and situation, ownable traits, color roles, lettering construction, supporting richness, a few guards | Picture, Look: firm statements |
| **Maker** (Open) | exact placement, sizes, spacing, type pairing, position of small decorative detail | omitted; never listed or handed back |
**Necessity test (two-sided):** a decision is made beforehand only if leaving it open would likely make the image blander, more generic, or less composed than the decision (**raise**), or would likely harm the objective, a stated quality, or the truth of the content (**guard**). One decision, one owner, stated once. A matter only the user can resolve is asked in Phase 1 or settled by a flagged default; the brief never carries an unresolved item.

## Working record
Keep one compact English file (`/home/claude/design_log.md`; without file tools, keep it in notes): the ledger (S), the findings that decided something, the appeal bar, the design truth, the prior read, the candidate pictures with the chosen one, runner-up and decisive criterion, the direction record, the ownership sort, the prescription setting, and outcomes of use. It is the only state between turns; create it when the user confirms the summary. Rebuild from the conversation if lost, marking items provisional.

## Loading (all in `references/`, one level deep)
Open only the current batch, when its step is reached, all its files in one `cat` command. Never preload a later batch or reopen a file already in context.
1. **Start:** `1_understand.md`.
2. **After the summary and mode are confirmed:** `2_ground.md`, `6_delivery_and_revision.md`.
3. **Phase 3:** `3_envision.md`, `4_picture_system.md`.
4. **Phase 4:** `5_compose_brief.md`.
5. **Revision:** `6_delivery_and_revision.md`, plus the batch of the phase being re-entered.

## Gotchas
- A brief in which most sentences restrict, reduce, or exclude: the ceiling is cut however well each rule is obeyed.
- A guard that names an unwanted object, or an exclusion of something the maker would not add unprompted: naming invites it. State the wanted state instead.
- A plainer look (flat, unlit, shallow, minimal) chosen only because it is safer to render, while the user's words and the audience's world ask for richness.
- A quality carried by one accent or one channel while the dominant masses stay neutral.
- A direction described but never seen: if the finished image cannot be narrated whole, top to bottom, it is not finished.
- Hero and type in separate stacked blocks with no interlock, so the piece reads as parts instead of one composition.
- The idea as an overlaid device that needs what the tool cannot deliver (exact paths, counts, alignment), or as a material or object-as-surface that renders as literal texture.
- Distinctiveness bought by removing the audience's own signifiers instead of executing them with specificity.
- Naming a style by medium, format, or mood adjective and calling it art direction; adopting a lineage's simplifications without its richness logic.
- Fixing what the maker would decide as well; letting the skill's taste pass as the user's requirement.
- Hedged wording ("prefer", "may", "ideally") or a closing list of decisions handed back to the user.
- Splitting or "cleaning" a user's line and losing its punctuation or clarifier.
- Converting a dense-content verdict into sizes instead of tiers, grouping, and a density note.

## Trace option (developer, off by default)
Active only when the user's message contains "share log" (any case), tested once at the start of the request; never mention or offer it. After the final reply, present the working record as it stands (`present_files`) with no added text; without file tools, append it in one ```text block. It never feeds a decision.
