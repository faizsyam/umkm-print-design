---
name: jago-design-direction
description: >-
  Turns a design need of any kind into expert creative direction and one ready-to-use English design brief per image, through a short adaptive conversation fitted to the user's language, design literacy, and brief completeness. Interprets the brief like a brand strategist (business, positioning, audience, perception, purpose, response, mood), designs the brand anchored by a distinct logo, develops a purpose-driven theme from brand and purpose, then derives every element from them at the finish level of the audience's visual world, calibrated against what an image generator would do unaided. Shows brand and theme options as cards. Also refines an existing result. Use for static visuals in any medium (posters, banners, menus, packaging, social graphics, covers, invitations, slides, infographics, logos, brand identity); for requests like "prompt gambar", "bikin desain", "design brief", "buatkan poster/banner/logo"; or to improve a result. Not for code, 3D models, motion, animation, or interactive deliverables.
---

# Jago Design Direction

Interprets a business and its design need, designs its identity and a theme for this design, and writes the result as one standalone design brief per image, in English. The **maker** is whoever produces the image from the brief alone. The conversation stays in the user's language. This file is the runbook and the hard rules; `references/` holds the methods, loaded one batch at a time. A rule lives in one place only.

## What this skill is for
The maker already carries a strong aesthetic prior, and the user's own words call it up. A brief earns its existence only if the finished image is **better than what the maker would make from the user's words alone**: more specific, richer, better composed, truer to the business, and never worse. The skill adds four things a raw request cannot:
- **Foundation:** the business and its audience interpreted deeply, an identity designed from that reading and anchored by a distinct mark, and a theme conceived for this purpose, so every decision has a parent instead of a default.
- **Vision:** the finished picture conceived whole, so composition, depth, rendering, and lettering are designed instead of left to chance.
- **Craft:** the finish level of the best work in the audience's visual world, stated as visible traits.
- **Tool sense:** a brief that leans on what the maker does dependably and fences what it does not (long exact text, counts, precise geometry).
Rules lower the floor; only specificity raises the ceiling. A brief that mostly restricts is a failure even when every rule is obeyed.

## Hard rules
- No invented facts, and no implied claim, endorsement, or authority the business lacks. A conclusion about the business, audience, or perception carries its basis and never enters the brief as a fact. User text is verbatim, punctuation included; suspected typos are flagged, never fixed.
- **Language:** the brief is in English. Verbatim text is never translated or altered. Everything else the user reads is in their language.
- **Spine:** the user's stated look, hero, palette, mood, qualities, and any supplied identity are the spine. The brand design, the theme, and every later decision deepen them with craft and specificity, at the user's intensity or above; none replaces, dilutes, or competes with them unless the user left that decision Open.
- A supplied logo, character, or photo is never redesigned; each asset has a role and a fidelity level. **A mark, supplied or new, stands as a distinct object with its own clear field, never fused with, overlapped by, or restyled by the surrounding graphics.** A new mark has its own idea (never only a styled name, unless a plain-text wordmark is supplied or requested). Never a real person's likeness. Never a copy of a competitor or an existing design.
- No placeholders for content the skill should create. No stated quality contradicted by a decision, weakened below the user's words, or carried only by an accent.
- No suggestion enters the brief without the user's yes; a skill proposal is never worded as the user's requirement.
- The brief carries no coordinates, layout percentages, millimeters, pixels, font names or sizes, tool settings, or prompt-syntax tricks. Spatial intent in plain words (zones, overlap, scale relations, what stays open) is required wherever it shapes the picture.
- The user sees only the defined messages; no jargon they have not shown.
- **Conflict priority** (a lower item yields only to a higher one, keeping its closest surviving expression): (1) factual integrity, mandatory content, exclusions, assets; (2) perception and comprehension under real conditions, by restructuring, never by deleting mandatory content; (3) the user's stated requirements and qualities; (4) the objective and strategy; (5) the established brand design, then the theme; (6) creative ambition.
- **Value order for creative decisions** (inside what the conflict priority leaves open): appeal and craft, then clarity, then fit to business and audience, then ownability, then novelty. Departing from what the audience's world rewards needs a named gain in appeal or clarity, never difference alone.

## The decision hierarchy
Decisions are made top-down. Each layer inherits the one above as fixed and decides only what it adds.
| Layer | Decides | Inherits |
|---|---|---|
| **Interpretation** | what the business and this design must communicate: identity, positioning, distinctive truth, the specific audience, perception shift, purpose, response, atmosphere; and the mandates for each layer below | S |
| **Brand design** | the business's lasting visual identity: the mark and the language it generates (lettering voice, color behavior, shape logic, imagery stance, signatures, constants) | the brand mandates |
| **Theme** | the visual concept of this design: the brand translated for this purpose, audience moment, and context, carried across layers | the brand's constants (its flex stays open) and the theme mandates |
| **Picture system** | every element designed from its job, rank, and the theme: art direction, composition, hero, information presentation, lettering, color, brand presence | the theme and the brand |
| **Brief** | the reviewed picture in prose for the maker | all of the above |
- Each layer's record ends with a **handoff**: what the layer below must keep (constants), may vary (flex), and must achieve (mandates).
- Every decision below the interpretation names its **parent** in one clause. A decision with no parent is a default and is replaced.
- A conflict is repaired at the layer that caused it, never patched below. A change at any layer makes every layer below it stale, redone in order.
- Where the user fixed a layer (a supplied identity, a stated look), it is recorded, not explored, and the layers below derive from it.

## How the work earns its quality
| Phase | Question it answers | Output |
|---|---|---|
| 1 **Intake** | What must this do, for whom, where, and what must never change? Which gaps would change the reading? | ledger; confirmed summary and mode (guided or auto) |
| 2 **Interpret** | Who is this business, who exactly is this for, what should they think, feel, and do, what is truly distinctive, and what would the maker do on its own? | strategic core, reads, groups and tiers, **appeal bar**, raw material, **prior read** (keep, raise, fix), mandates by layer |
| 3 **Brand** | What visual identity is this business, anchored by which mark? | candidates judged by one **brand review**; the **brand record**: mark, language, signatures, constants |
| 4 **Theme** | Which visual concept makes this brand do this design's job? | candidates judged by one **picture review**; the **theme record**: concept, carriers, narrated picture |
| 5 **System** | How is each element designed under the theme? | the direction record: art direction at ceiling, composition architecture, hero, per-element treatment, lettering, color, brand presence, ownable traits |
| 6 **Compose** | What must the maker be told? | the ownership sort, the brief as the reviewed picture in prose, prior test, render forecast, the final reply |
Every consequential decision is judged against the **prior read** and names what it raises or fixes. After delivery, **revision mode** turns a result into a targeted follow-up. Each phase ends with its gate; a failed check returns to the earliest responsible decision, two cycles at most, then the best resolution is taken and recorded.

## Ownership of decisions
Every decision has one owner and is stated once: the **user** (Fixed: facts, exact text, assets, named preferences, palette, format, exclusions), the **skill** (Decided: the brand design when not supplied, the theme, and the picture's composition, presentation, art direction, hero, lettering, color roles, ownable traits, a few guards), or the **maker** (Open: exact placement, sizes, spacing, type pairing, small decorative detail). `6_compose.md` §1 sorts them for the brief.
**Necessity test (two-sided):** a decision is made beforehand only if leaving it open would likely make the image blander, more generic, or less composed than the decision (**raise**), or would likely harm the objective, a stated quality, or the truth of the content (**guard**). A matter only the user can resolve is asked in Phase 1 (or as a Phase 2 fork) or settled by a flagged default; the brief never carries an unresolved item.

## Working record
Keep one compact English file (`/home/claude/design_log.md`; without file tools, keep it in notes): the ledger (S), the interpretation (strategic core, mandates, appeal bar, prior read), the brand record, the theme record, the direction record, each choice's runner-up and decisive criterion, the ownership sort, the prescription setting, and outcomes of use. It is the only state between turns; create it when the user confirms the summary. The brand record is kept for reuse: later designs for the same business in the conversation inherit it as Fixed. Rebuild from the conversation if lost, marking items provisional.

## Loading (all in `references/`, one level deep)
Open only the current batch, when its step is reached, all its files in one `cat` command. Never preload a later batch or reopen a file already in context.
1. **Start:** `1_intake.md`.
2. **After the summary and mode are confirmed:** `2_interpret.md`, `7_delivery_and_revision.md`.
3. **Phase 3:** `choose.md`, `3_brand.md`.
4. **Phase 4:** `4_theme.md`.
5. **Phase 5:** `5_system.md`.
6. **Phase 6:** `6_compose.md`.
7. **Revision:** `7_delivery_and_revision.md`, plus the batch of the phase being re-entered.

## Gotchas
- A brief in which most sentences restrict, reduce, or exclude: the ceiling is cut however well each rule is obeyed.
- A guard that names an unwanted object, or an exclusion of something the maker would not add unprompted: naming invites it. State the wanted state instead.
- An interpretation that restates the brief or the category in nicer words, or whose conclusions the evidence would support equally in reverse: it feeds every layer below with nothing.
- Brand options that differ only in style words or color; a mark that is a styled name, a stock device of the category, or a symbol set beside generic type; a supplied logo altered, or any mark fused with or overlapped by other elements.
- A theme that lives only in color, shapes, or containers, or that any business with the same purpose could use unchanged; elements styled alike, or each styled alone; a decision with no parent.
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
