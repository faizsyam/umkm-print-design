# Phase 4: Design Elements

## Contents
1. Purpose and scope
2. Method
3. Color system
4. Typography
5. Brand logo mark
6. Visual supporters
7. Background and unifying devices
8. Additional design systems
9. Element-level evaluation
10. Failure modes
11. Completion criteria and hand-off

## 1. Purpose and scope

Translate the Design Plan into a cohesive visual system. For each element, decide its purpose, treatment, relationships to other elements, and contribution to the whole. The categories below define the scope of consideration, not a checklist: add, merge, or omit according to the piece. System-wide coherence outranks the appeal of any single element.

## 2. Method

For every element:
1. **Role**: what job does it do that no other element does?
2. **Treatment**: how is it constructed and rendered, consistent with the style direction?
3. **Relationships**: how does it relate in scale, weight, color, and character to its neighbors?
4. **Cost**: what attention, space, or legibility does it consume?

Explore alternatives proportionally. Spend real comparison effort on the logo mark, the typographic voice, the color logic, and the hero's treatment. Decide quickly on secondary details.
**Consequential element decisions** are the color strategy, the typographic voice, and the logo mark (unless fixed), plus any hero treatment left open by Phase 3. Each follows the exploration protocol in `SKILL.md`: at least three structurally distinct candidates, evaluated against the plan, Environment Profile, content, and feasibility, then engineered into the strongest solution. Other element decisions are trivial and are decided directly.

## 3. Color system

Define a color *strategy*, then the palette that implements it.

Decide:
- **The logic**: what the color is doing (identifying the brand, signaling the product, creating contrast, setting mood, separating information zones).
- **Roles**: which colors dominate, which support, which accent. Not every design needs the same number of colors. A single-hue system, a restrained two-tone, a controlled multicolor, or a rich full palette are all valid when the strategy justifies them.
- **Contrast structure**: which pairs carry text, which carry attention, and how they perform under the actual ambient light of Phase 2.
- **Environmental position**: judge the palette against the surrounding color field and the ambient light, not only against the brand. Decide whether it should depart from the landscape or sit within it, and on which dimension (hue, value, saturation, area), consistent with Phase 2.
- **Relationship to imagery**: how photographic or illustrated color sits with the flat palette; whether imagery is harmonized with the palette or allowed to be the exception.
- **Brand continuity**: existing brand colors are fixed assets and take precedence; extend them, do not replace them.
- **Cultural and category associations**: verify rather than assume; colors read differently across communities and categories, and category defaults may be exactly what to avoid or to deliberately use.
- **Reproduction**: the user's printing budget and method can limit practical color count, gradients, and subtle tonal differences. If production is basic, favor a system that survives imperfect printing.

Describe colors to a model by clear named hues with relevant qualifiers (depth, saturation, warmth, temperature) and role, and give hex values only when matching a supplied brand color or when precision is essential.

## 4. Typography

Typography is part of the identity and the composition, not a final overlay.

Define:
- **Roles**: display or headline voice, supporting voice, informational text, numerals and prices, small print. Not every piece needs every role.
- **Character**: construction and personality: proportion, contrast, stroke behavior, terminal shapes, width, weight, posture, case.
- **Relationships**: how voices contrast with each other in function and character, so hierarchy is felt without relying on size alone.
- **Readability**: legibility at the actual viewing distance, in the actual light, on the actual material; letterspacing and line spacing suited to the role; sufficient contrast with the background; behavior of long words and the user's language.
- **Numerals**: prices and quantities are high-stakes text. Give them clarity and consistency.
- **Integration**: how type interacts with the hero, the mark, and the background without being swallowed by them or colliding.
- **Fixed assets**: a brand's established typeface or lettering style must be respected.

When describing type to an image model, describe the *characteristics* of the lettering, because exact font names are unreliable across models. Use a font name only if it is a brand requirement and the user has stated it, and pair it with a characteristic description as a fallback.

Large amounts of text increase rendering risk. Plan typographic structure so that dense information is grouped, consistently styled, and large enough for the model to reproduce accurately.
**Landscape and scale economy.** Judge the typographic voice against the lettering of the surrounding landscape: it should depart on an open dimension while staying appropriate to the place. Keep the number of roles small. Set role sizes as ratios between roles that follow reading stages (see `05_design_execution.md`), not as independent sizes, so that no role is large merely because it must be legible.

## 5. Brand logo mark

The mark is a critical identity decision. Treat it with the same seriousness as the hero.

### Distinguish the parts of an identifier
- The **wordmark** is the business name set in a particular lettering.
- The **logo mark** (symbol) is a distinctive visual form that can stand for the brand independently of the name.
- A **lockup** is how they combine.

Setting the name in an attractive typeface creates a styled name, not a logo mark. A styled name is a legitimate decision (some identities are properly wordmark-led), but it must be a *decision* with a reason, not what happens when no mark was designed.

### Fixed assets
If the user supplied a logo or has an established mark, use it as given. Do not redesign, restyle, simplify, or recolor it unless asked. Design everything else around it, and record how it constrains color, type, and layout. The distinction mechanisms below then apply to everything around the mark.

### Conceptual development of a new mark
1. **Find conceptual sources.** Where could a recognizable idea come from: the name, the product's defining feature, the origin, a gesture, a process, a founder's story, a visual signature of the business? Use only concepts the brief or research supports and the business can truthfully claim.
2. **Develop at least three distinct candidates** that differ in concept source or in construction. Construction families to weigh against each other: enclosed (symbol held within a boundary), contained (elements held together by a frame or shape), integrated (symbol fused with lettering), emblematic (a unified crest-like arrangement), and open (a freestanding symbol with no boundary). Do not default to one structure across businesses.
3. **Evaluate against**: conceptual relevance; silhouette; distinctiveness from category defaults; scalability; visual weight; relationship with the wordmark; independence from surrounding content (next subsection).
4. **Engineer the strongest mark** by selection, transplant, or a single-logic combination, as the exploration protocol describes.
5. **Run the tests**: isolation (everything else removed, is it still identifiable?), reduction (one color, small), separation (distinct from hero, lettering, and decoration), and the text-neighborhood test below.
6. **Prepare it for generation.** Image models render simple, geometric, clearly described marks far more reliably than intricate ones. Define its geometry, key shapes, relationships, and color concretely. Prefer a bold, legible silhouette to fine internal detail.

### Distinction from typography and content
A mark is recognized as a mark when it belongs to a different visual class from the text around it. When it shares the class of the typography, it reads as more type, and the identity dissolves, most severely in text-heavy layouts. Judge distinction as a relationship in the composition, not only as a property of the mark. Mechanisms, of which the composition should use as many as its conditions require, usually two or more in dense layouts:

- **Form class**: a silhouette built from shapes and masses rather than from the rhythm of letter strokes. If it uses letters, they must be transformed enough to read as a shape first and a letter second.
- **Mass and texture**: a compact, solid visual weight that contrasts with the linear, evenly textured weight of text blocks.
- **Color role**: a color or color field that the mark holds and the body text does not share.
- **Scale step**: a deliberate size step from adjacent text, large enough to be read as an object and sized to its hierarchy role, not enlarged to compensate for weak distinction.
- **Isolation**: protected clear space that no text, ornament, or pattern enters.
- **Containment or anchoring**: a container, field, or fixed anchor region that gives it a stable edge and position, and repeats consistently across faces or pieces.

**Relationship with the wordmark.** Share a logic of proportion, weight, and geometry so the two read as one identity, but not the same form class. The wordmark should recede in form so the mark stays the identifier, or the lockup should be built as one object with a clearly distinct symbol part. The mark must remain recognizable when separated from the wordmark.

**Dense layouts.** The more text on the piece, the more the mark's distinction has to be designed rather than assumed. Resolve it by composition, not by endless enlargement: give the mark its own region, keep neighboring type from echoing its form or crowding its space, and make sure body-text styling does not borrow its color role or construction. Choose the mechanisms from the actual composition; no single arrangement is universal.

**Text-neighborhood test.** Place the mark beside the densest text of the layout and squint. If it does not resolve as a distinct object before any word is read, strengthen the mechanisms or reconsider the construction.

Avoid: a mark that repeats the hero illustration; a mark with the character of category defaults; a mark too intricate to reproduce; a badge border added only to look official; a mark whose meaning the business cannot truthfully claim; a mark whose letters are merely decorated.

If a mark is genuinely not warranted (a minimal identifier, or a fixed wordmark-only identity), the decision to rely on the wordmark must be explicit and justified, and the wordmark itself must still be distinct from the surrounding typography through the mechanisms above.

## 6. Visual supporters

Visual supporters are the elements beyond the required text and mark that make the composition complete, distinctive, and effective.

**Deficit analysis first.** Imagine the piece with only its required text. Ask what is missing: attention, product understanding, emotion, credibility, categorization, rhythm, connection between content groups, brand reinforcement. Add supporters only to address real deficits.

Functions a supporter can serve:
- primary attention and storytelling
- representing the product or service accurately
- reinforcing brand identity
- setting atmosphere and emotion
- helping comprehension and categorizing information
- supporting illustration, iconography, imagery
- compositional balance and refinement
- linking otherwise separate content groups

For each supporter specify: role, relevance, treatment (consistent with style), scale, placement logic, and relationship to its neighbors.

**Product fidelity.** Depictions of products, ingredients, or results must correspond to what the business actually offers. Do not show items, quantities, qualities, or outcomes the business has not claimed.

**People and characters.** Use them only when they serve the concept. Avoid real identifiable individuals, tokenistic or stereotyped portrayals, and compositions that require complex hands, many faces, or fine facial detail unless reliability allows.

**Micro-details.** Fine finishing details (small rules, subtle texture shifts, tiny marks, edge treatments) are valuable when they show deliberate craft. Select a few that carry meaning or refine transitions. Accumulation of micro-details is noise.
**Quantity and scale follow the space budget.** Supporters sit at a lower reading level than the hero, mark, and primary message. Add only as many as the intended share of quiet space allows; a supporter that must be shrunk to fit, or that crowds a glance-stage element, should be removed instead.

## 7. Background and unifying devices

The background contributes to identity and cohesion; it is not leftover space.

Decide:
- **Color and tonal structure**: flat, graduated, zoned, or layered, and how it supports contrast.
- **Texture and imagery**: whether it has material character or environmental imagery, and how that supports the style.
- **Spatial structure**: how it organizes depth and separates foreground from background.
- **Relationship to the foreground**: it must not fight hierarchy or reduce text legibility.
- **Unifying devices**: whether separate zones need connection: recurring shapes, graphic motifs, rules, borders, patterns, material treatments, continuing lines, repeated proportions. Use them only where fragmentation is a real risk.

A background and its unifying devices should be quiet where information lives and expressive where the piece can afford it.
**Environmental role.** The background is also what separates the piece from its landscape. Judge its tone, texture, and finish against the neighbors and the ambient light, and keep it quiet where information lives.

## 8. Additional design systems

Consider as needed: graphic shapes, framing, borders, patterns, textures, material effects, lighting, shadows, image treatments, iconography, information graphics, spatial transitions. Include only what improves the design. Every system added increases the need for restraint elsewhere.

Lighting and shadow are decisions, not defaults: specify them only when they define the style and keep them consistent across all depicted objects. Print pieces often benefit from flat or controlled treatment; decide, do not inherit a rendered, glossy look by habit.

## 9. Element-level evaluation

Apply the same critical process as in Phase 3.

- **Alternatives**: for identity-defining elements, compare real options and record why one wins.
- **Interaction check**: for each pair of major elements, ask whether they reinforce, compete, or ignore each other. Resolve competition by changing scale, weight, treatment, or by removing one.
- **Removal test**: remove each element in turn. If nothing is lost, remove it.
- **Cumulative effect**: assess the set as a whole. An element attractive alone may be wrong in context.
- **Consistency of treatment**: line quality, edge sharpness, level of finish, level of abstraction, light direction, and texture must agree across hero, supporters, mark, and background.
- **Subtraction pass**: before finalizing, remove the weakest decorative element. If the design is stronger, keep it removed.

## 10. Failure modes

| Failure | Detection | Correction |
|---|---|---|
| Default palette | Colors mirror category cliché without a reason | Re-derive from brand logic and contrast needs |
| Type as afterthought | Typefaces chosen without reference to style or role | Re-set voice from the plan |
| Styled name as logo | No decision recorded for mark vs wordmark | Evaluate constructions; document the choice |
| One construction for every brand | Mark structure repeated regardless of concept | Re-evaluate families |
| Unscalable mark | Fails isolation or reduction | Simplify silhouette |
| Decorative stacking | Elements added without a role | Run deficit analysis and removal test |
| Product misrepresentation | Image shows things the business does not offer | Align to actual offering |
| Inconsistent rendering | Mixed finishes and abstraction levels | Unify to the style direction |
| Redesigned fixed asset | Supplied logo altered | Restore as given |
| Mark absorbed by type | Mark passes the isolation test but fails the text-neighborhood test | Apply distinction mechanisms; reconsider form class |
| Mark rescued by size | Mark only distinct because it is oversized | Replace scale with form, color role, isolation, or containment |
| Unexplored element decision | Color, type voice, or mark chosen from a single idea | Run the exploration protocol |

## 11. Completion criteria and hand-off

Complete when: the color strategy and palette, typographic roles and character, the mark decision (fixed, new with justification, or deliberate wordmark-only), visual supporters with roles, background and unifying device decisions, and any additional systems are defined and mutually consistent, and each has survived the removal test.

Hand-off to Phase 5: the element system, with each element's role, treatment, and relationships, and a note of the elements most at risk of competing.
The color strategy, typographic voice, and mark were each chosen from at least three candidates, and the mark's distinction from the surrounding typography is secured by named mechanisms.