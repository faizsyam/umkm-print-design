# Phase 6: Prompt Synthesis

## Contents
1. Purpose and scope
2. Assumptions about the target model
3. Language policy
4. Structuring the prompt
5. Writing for image models
6. Handling text on the piece
7. Handling logos and fixed assets
8. Flat artwork versus staged scenes
9. Exclusions
10. Level of detail and length
11. Multi-face pieces and multiple concepts
12. Consistency and fidelity audit
13. Failure modes
14. Completion criteria and delivery

## 1. Purpose and scope

The prompt is the final design specification written in language an image model can follow. It communicates the selected design and its implementation; it does not replay the reasoning. Prompt synthesis is translation, not invention. Nothing new may enter at this stage. If synthesis forces you to invent a concept, style, or element, the plan or execution had a gap: return to that phase.

## 2. Assumptions about the target model

Unless the user names a model, assume a capable current image model that follows natural-language descriptions, renders legible text reasonably well in moderate amounts, and responds to composition and style description. Do not use model-specific syntax, parameter flags, weighting notation, or tool commands unless the user requests a specific model that needs them. Include aspect ratio and orientation in plain language. If the required ratio is more extreme than the model supports (common for long banners), use the nearest ratio it supports, compose the design so it remains valid at that ratio with no unplanned empty zones, and mention the substitution in an outside note.

Models differ in strength. Assume that fine small text, long strings of copy, complex logos, intricate hands, and crowded scenes are high-risk. Design the description to make high-risk content easier: group text, state it plainly, and prefer clear, bold forms where reliability matters.

## 3. Language policy

- Write the prompt in English by default, because descriptive precision usually transfers better. Keep every piece of on-piece text in its original language, exactly as given.
- If the user asks for a prompt in another language, or names a model that performs better in another language, comply.
- Reply to the user in the language they wrote in.
- Do not translate user-specified text unless asked. Do not mix instruction language into the on-piece text.

## 4. Structuring the prompt

Order the content from concept to execution, adapting to complexity:

1. **Identity of the piece**: what it is, its format, orientation, and aspect ratio, and the purpose.
2. **The central creative concept and overall aesthetic**: the core idea and style direction in a form the model can visualize.
3. **Composition and hierarchy**: the spatial organization and reading order, with relative scale and relationships.
4. **Hero and main visuals**: what they are and how they are treated.
5. **Logo mark and brand identifier**: construction, placement, and relationship to the name.
6. **Typography**: the role and character of each text category and where it lives.
7. **Color treatment**: strategy and how it distributes across the composition.
8. **Background and unifying devices**: surface, texture, tone, and connections between zones.
9. **Supporting details and finishing**: only the ones that matter.
10. **All mandatory text**, placed in context, or collected in a clearly organized section, whichever communicates the arrangement more clearly.

Do not force this order into rigid headings if prose communicates the relationships better. Simple pieces may be one or two compact paragraphs; dense pieces may need clear segments.

## 5. Writing for image models

- **Describe what is seen.** Use concrete visual terms for form, composition, material, and light, not abstract aspirations. A phrase must change what the model draws.
- **Use precise design vocabulary** where it has a shared meaning, and plain description where it does not. Replace vague adjectives with the observable trait behind them.
- **Describe relationships, not inventories.** State what dominates and what supports, how elements overlap or align, how groups are separated, how the eye travels, and how brand mark, headline, and imagery relate in prominence. A list of attractive objects does not make a design.
- **Encode hierarchy through relative language**: larger than, nested within, set apart from, anchored to, balanced against. Hierarchy lives in relationships.
- **Retain the distinctive decisions**: the idea, the mark's construction, the hero's treatment, the typographic character, the unifying device. These are what prevent a generic output. Cut generic filler before cutting distinctive specifics.
- **Keep style language coherent.** Use one consistent style logic. Adding many unrelated style terms invites a muddled average.
- **State physical qualities only when they alter the picture**, limited to the surface character and finish that define the style.
- **Avoid pixel measurements, coordinates, and exact angles** unless essential. Position by relationship and broad region when placement matters.

## 6. Handling text on the piece

Text accuracy is the most failure-prone area. Protect it.

- **Include all mandatory text, verbatim**, inside quotation marks so the model recognizes it as literal. Preserve capitalization, punctuation, numerals, price formatting, and contact formatting.
- **Say where each text item lives and what role it plays.** Tie each string to a position and a typographic treatment.
- **Say each text string once.** Duplication creates doubled or garbled text.
- **State that the piece contains only the specified text** and no additional words, invented slogans, filler copy, or pseudo-text, when the risk of hallucinated text is significant. Use plain positive phrasing where possible.
- **Group dense text**: for menus, price lists, and catalogs, structure items into labeled groups in reading order, and describe the consistent row or column behavior (alignment of item and price, separation between groups) once rather than repeating it per item.
- **Make high-stakes text easy**: prices, phone numbers, and handles should be assigned generous size, strong contrast, and clean spacing in the description.
- **Do not omit mandatory text to shorten the prompt.** If volume truly exceeds what models render reliably, keep all of it in the prompt and mention the risk in one outside line, instead of silently dropping content.
- **Optional text** is included only if the design has room for it without damaging hierarchy.
- Specify language and diacritic-free or special characters as given. Do not add characters the user did not provide.

## 7. Handling logos and fixed assets

- **Supplied logo and the model accepts reference images**: instruct the model to reproduce the supplied logo exactly as provided, specify its position and relative scale, and state that it must not be redrawn or altered.
- **Supplied logo described textually, or model cannot ingest images**: describe the logo's structure, shapes, colors, and lettering faithfully and concretely. If its complexity makes faithful reproduction unrealistic, say so in one outside line; do not substitute an invented logo silently.
- **New mark**: describe its construction as decided in Phase 4: the form, geometry, silhouette, color, boundary type, and relationship to the wordmark, in a way the model can draw consistently.
- Do not leave a blank area reserved for a logo to be added later.
- Supplied photographs, brand colors, and fonts follow the same principle: use as given, describe precisely, never replace.

## 8. Flat artwork versus staged scenes

A print design prompt should normally describe the **finished flat artwork** as the print file would appear: full frame, edge to edge, viewed straight on, without a surrounding room, hand, table, shadow beneath the sheet, or perspective, because the user needs the design itself.

Describe a staged scene or mockup only if the user explicitly wants a presentation mockup, or if the physical form of the piece is itself part of the deliverable. In that case describe the form plainly and keep the design legible on its surfaces.

Do not add crop marks, bleed guides, color bars, rulers, or technical annotations to the artwork unless requested.

## 9. Exclusions

Image models can respond poorly to long negative lists, because mentioning an unwanted thing can invite it. Therefore:

- Express desired traits positively whenever possible. State what the design is instead of listing what it is not.
- Add a short exclusion clause only for: explicit user exclusions, high-probability model failures that matter for this piece (invented extra text, watermarks, surrounding mockup scenery, border artifacts), and cultural or factual risks.
- Keep exclusions minimal and specific.

Do not carry the internal AI-slop diagnostics (`quality_control.md`) into the prompt as a blanket negative list. They are applied during design, not recited to the model.

## 10. Level of detail and length

Length is proportional to the design's complexity and distinctiveness. Every sentence should carry a decision or a relationship. Compact means few wasted words, not few details.

- Include the specifics that determine identity, hierarchy, and distinctiveness.
- Omit adjectives that do not change the image, restatements of the same instruction, rationale, and any instruction about what to do after generation.
- Rigid placement, pixel-level detail, and excessive micro-instructions reduce the model's ability to compose well. Use region and relationship language instead.
- Include exact dimensions, ratio, and orientation when the brief requires them.

If the draft reads like a mood board of adjectives, it lacks decisions. If it reads like a coordinate sheet, it is over-specified. The target is the way a skilled art director briefs a skilled illustrator: clear intent, firm on what matters, free on the rest.

## 11. Multi-face pieces and multiple concepts

- **Multi-face**: write one complete prompt per face. Each prompt must stand alone, restating the shared identity (mark construction, palette logic, typographic voice, style) in the same words so that faces match. Make the face's role clear. Do not refer to "the other side."
- **Multiple concepts**: write one complete prompt per concept. Each must derive from a different core idea, differing structurally as defined in `03_design_plan.md`. Label them minimally for the user's convenience outside the prompts. Do not produce variants that differ only in color or decoration.

## 12. Consistency and fidelity audit

Before delivery, reread the prompt as the model would, and as the user would.

1. **Plan fidelity**: does it express the core idea, style, hero, mark, typography, color, background, and hierarchy as decided? Is anything added that was not in the plan?
2. **Mandatory content**: is every mandatory item present, verbatim, and placed? Check each string against the Brief Ledger.
3. **Contradictions**: scan for conflicting statements about style, color, density, hierarchy, and placement. Resolve at the source.
4. **Generic drift**: have distinctive specifics been softened into safe generalities? Restore them.
5. **Unsupported claims**: has any claim, quantity, or label slipped in that the user did not provide?
6. **Exclusions**: are user exclusions respected and the exclusion clause minimal?
7. **Standalone check**: no reference to analysis, alternatives, earlier phases, or user conversation; no placeholders or manual completion.
8. **Readability**: does it read as a clear, ordered, usable instruction? Could someone who has never seen the brief produce the intended design?

## 13. Failure modes

| Failure | Detection | Correction |
|---|---|---|
| Adjective soup | Descriptors that do not alter the image | Replace with observable traits |
| Inventory prompt | Lists of objects with no relationships | Add hierarchy, grouping, and relational language |
| Lost distinctiveness | Unique decisions replaced with category defaults | Restore specifics |
| Text corruption | Strings duplicated, paraphrased, or altered | Restore verbatim, once, with role and position |
| Over-specification | Coordinates, pixel sizes, exact angles | Use region and relationship language |
| Contradictory style terms | Competing aesthetics | Reduce to one logic |
| Negative-list bloat | Long "no X, no Y" sections | Positive phrasing plus minimal exclusions |
| Meta-leak | Phrases explaining design reasoning | Remove |
| Placeholder leak | Blank areas or "add later" language | Resolve in the design |
| Mockup contamination | Scene or surface surrounding the artwork | Describe flat artwork |

## 14. Completion criteria and delivery

The prompt is complete when it passes the audit in section 12 and the prompt audit in `quality_control.md`. Deliver it in a single code block. Add outside the block only the brief notes defined in the output contract of `SKILL.md`.
