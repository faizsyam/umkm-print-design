# Phase 6: Prompt Synthesis

## Phase card

| Item | Content |
|---|---|
| Professional analogue | A production brief from an art director to an illustrator: the design is finished; the task is to describe it so exactly that someone who never saw the original brief could produce it |
| Goal | A polished, standalone image-generation prompt that translates the Execution Specification into visible instructions. Synthesis is translation, not invention |
| Receives | From Phase 5: Execution Specification. From the Design Log: all earlier decisions. From Phase 1: mandatory text verbatim, fixed assets. From SKILL.md section 11: the decision commitments. From the user: target model if named, language preference |
| Principles in force | **8 Fidelity to the brief** (every mandatory string verbatim, once; fixed assets reproduced as provided); **7 Internal consistency** (no contradictions; nothing new introduced); **10 Effort follows impact** (retain the distinctive decisions; cut filler before specifics); the non-negotiables and the output contract (SKILL.md sections 10 and 13) |
| Exploration protocol | Not applicable. This phase translates decisions already made. If translation requires a new concept, style, or element, the plan or execution had a gap: return to the responsible phase, then re-run forward |
| Required decisions | What is in the prompt and what stays out; the prompt's structure; placement and wording of every mandatory text item; how the mark and any fixed asset are described; how space is expressed; which minimal exclusions apply; the ratio handling; the language policy; the notes |
| Outputs | The final prompt(s) and any short notes (SKILL.md 13.2). The decision summary was printed phase by phase at earlier gates and is not repeated |
| Before leaving | Could an illustrator who has never seen the brief produce the intended design, and is every printed or amended decision visible in the prompt and none contradicted? Does every sentence pass the visual-effect test, and is every look-shaping attribute stated rather than left to the model's apparent value? Is all mandatory text present, verbatim, once, with role and position? Are there no contradictions, no rationale, no placeholders, no blanket emphasis words? Do the distinctive decisions survive (idea, stated qualities as visible look, mark construction and personality device, hero treatment, typographic character and designed copy treatments, supporters, unifying device, space plan)? Is length proportional to complexity? Was the gate objection raised and resolved, or accepted with a reason (`quality_control.md` section 2)? |

## Contents
1. Process
2. Detailed guidance (A to J)
3. Failure modes
4. Completion criteria, hand-off, and delivery

## 1. Process

1. Confirm the entry condition: the Phase 5 gate passed and the decision commitments (SKILL.md section 11) are complete.
2. Sort every element of the design into "in the prompt" or "stays out" using A.
3. Choose a structure from concept to execution suited to the design's complexity (B).
4. Write each clause with specificity, in relationships, and with space as a positive feature (C to E).
5. Place text and describe logos and fixed assets exactly (F).
6. Calibrate detail and length, describe flat artwork, set minimal exclusions, handle ratio limits (G, H).
7. Apply the language policy and the multi-concept and multi-face rules (I).
8. Run the prompt audit (J); on failure, return to the earliest cause.
9. After the prompt passes the audit, compose the notes and deliver per SKILL.md 13.2. If the audit forced a change to a printed decision, print the amendment first (SKILL.md 13.1).

## 2. Detailed guidance

### A. What belongs in the prompt, and what does not
**Stays out:** business strategy, brand story, audience and environment analysis, research findings, the piece's business purpose, success criteria, alternatives, and any "because" or "in order to" justification. These acted through decisions; the prompt carries the visible traits they produced. An impression word may remain only as a brief tone anchor that steers rendering and justifies nothing.

**Goes in:** type and format of the piece (orientation, aspect ratio, faces); the overall look as seen (value key, dominant field, mood, finish); what is depicted and how; composition and relationships; hierarchy through relative scale, position, and plane order; typography character and the treatment of designed copy; mandatory text; supporters as concrete forms; color and surface treatment; mark construction; background and unifying devices; the few finishing details that matter; rendering technique; necessary exclusions.

**Scale as proportion:** express size as proportions of the format and steps between elements. State emphasis only for the elements that hold it; avoid blanket emphasis words across many elements.

### B. Structure

- Order by consequence: piece and format; the overall look as seen (value key and dominant field first, so the stated qualities govern generation); composition and hierarchy; hero and main visuals; identity unit; typography; color; background and unifying devices; supporting details; mandatory text placed in context.
- Adapt the order to complexity; do not force a rigid template.
- Keep one coherent style logic from first sentence to last.

### C. Specificity

- Use precise design vocabulary (`protocol.md` 3g) and concrete visual description; no vague adjectives.
- A sentence an illustrator could read two ways is not yet specific.
- Describe each depicted thing by its true specifics (form, material, construction, arrangement) as decided in Phases 3 and 4, not by its category name; a category name alone summons the image model's apparent instance.
- State every look-shaping attribute where the plan decided it. An attribute left unstated takes the model's apparent value; if no earlier phase decided it, return to the phase that owns it rather than invent it here. Silence is allowed only where that value is the intended result.

### D. Relationships, not inventories

Describe:
- relative prominence and grouping;
- contrast and integration;
- spatial relationships;
- plane order, from rearmost to front;
- how identity, message, and supporting visuals interact.

Position by relationship and broad region, not coordinates.

### E. Space as a design feature

Image models fill space unless told otherwise. Describe each of these as a positive part of the design:
- the outer margin;
- isolation around key elements;
- resting fields.

For each state: where it is, roughly how much of the format it takes, what it frames, and that it stays quiet and uncluttered. Add no filler decoration to relieve emptiness. This is designed negative space, not a placeholder.

### F. Text, logos, and fixed assets
- **Mandatory text** is included verbatim in quotation marks, once, tied to position and typographic role. Dense text (menus, price lists) is grouped in reading order, with row behavior described once. Prices and contacts get clarity proportionate to their stage, not oversize. State that the piece contains only the specified text when hallucinated text is a risk. Never omit mandatory text to shorten the prompt; flag volume risk in the notes.
- **The hero group** is described as one composition: the hero first, then each integrated item with the exact part it points to, its side or path, and the pointer style (for example, a thin straight line ending in a small dot on the named part), attached items by their position against the hero, and the relationship in one sentence. Arched or contour-following text is one short line on one smooth curve.
- **Designed copy** is described by its traits: letterform character, line breaks, emphasis, container, color role, position. "Stylish text" is not a description.
- **Supporters** are described as concrete forms (what, how drawn, where, how large against neighbors, what color) consistent with the style, never as "decorative elements". Each is stated at a weight below the information beside it, and nothing outweighs required text.
- **Grounds and edges.** A texture or pattern is described as a low-contrast surface beneath the content; a scrim as a translucent tonal layer behind the named text zone; a bleed as an element running off the trim while the text stays inside the stated margin; a cutout as an isolated form on a plain ground; a curved or angled edge as the boundary between two named zones.
- **Planes.** State the plane order in relational words (in front of, behind, over), from rearmost to front, with the visible layer cues that carry it. Keep mandatory text where every letterform stays whole and unobstructed, and say so; describe any overlap involving text once, only as the plan decided it.
- **A supplied logo or character** is reproduced as provided (by reference if the model accepts images, otherwise described faithfully) and never replaced by an invention.
- **A figure** is described as one designed character or person: form class, proportions, silhouette, signature trait, palette, and the pose, gesture, and relation to the offer its role requires; fictional and non-identifiable; the same wording on every face; hands, faces, and groups only as simply as the generator holds them.
- **A reserved asset panel** is described as a designed region: position, share of the format, flat color, frame, and isolation, with nothing inside. No code or photograph is imitated.
- **A new mark** is described by form class, geometry, silhouette, color, boundary type, personality device, relationship to the wordmark, and separation from adjacent type, concretely enough to be drawn the same way each time.
- **The identity unit** (mark with wordmark) is described as one object: arrangement, the shared construction logic of mark and lettering, the proportion and spacing relationship, the alignment axis, the color roles within the unit, and the clear space and region that distinguish the whole unit from surrounding type and content. Never describe mark and wordmark as two unrelated items.

### G. Detail and length

- No pixel measurements, coordinates, or exact angles unless essential.
- State a proportion only where the model's default would break the design (the margin, the hero's share, the large scale steps); elsewhere use relational words (larger than, flush with, beside). A prompt crowded with percentages dilutes the decisions that matter and repeats the plan instead of translating it.
- Include exact dimensions, ratios, and required text when essential.
- Length is proportional to complexity: every sentence carries a decision or a relationship.
- If a required ratio exceeds what the model supports, use the nearest supported ratio, keep the design valid at it, and flag it in the notes.

### H. Flat artwork and exclusions
Describe finished flat artwork unless a mockup is requested or the physical form is itself the deliverable. No crop marks, bleed guides, or annotations unless requested. Express desired traits positively. Allow minimal, specific exclusions only for: explicit user exclusions; high-probability failures that matter; cultural or factual risks.

### I. Language, multiple concepts, and faces

- Write the prompt in English by default, keeping on-piece text verbatim in its original language, unless the user requests otherwise or names a model that performs better in another language.
- Everything the user reads outside the prompt is plain Indonesian (`00_conversation_ux.md`); the prompt stays English and sits alone in its code block.
- Several concepts: one complete standalone prompt each, differing in underlying creative approach.
- Several faces: one standalone prompt each, restating the shared identity in the same words.

### J. Prompt audit

Run the prompt audit in `quality_control.md` section 4, with the visual-effect test on every sentence.

## 3. Failure modes

| Failure | Detection | Correction |
|---|---|---|
| Rationale in the prompt | "because", "in order to", audience or strategy language | Delete; keep the visible trait |
| New idea introduced | A clause with no source in the specification | Remove, or return to the responsible phase |
| Mandatory text altered, dropped, or repeated | Mismatch against the ledger's verbatim strings | Restore verbatim, once, with position and role |
| Blanket emphasis | Intensifiers on many elements | Keep emphasis only where the specification holds it |
| Mark described as a name in a typeface | No geometry, device, or separation stated | Describe form class, geometry, device, boundary, separation |
| Space omitted | No margin, isolation, or resting field stated | Add as positive features with proportions |
| Mockup by accident | Scene, perspective, or surroundings described | Return to flat artwork |
| Placeholders or blank zones | Any region left for the user to fill other than a reserved asset panel, or a bracketed stand-in for content | Resolve in the responsible phase; deliver a complete design or omit the item and note it |
| Text hallucination | Extra, garbled, or missing words expected in the output | State that the piece contains only the specified text; reduce text volume risk (F) |
| Workflow output leaking | Analysis, alternatives, or process in the final reply beyond prompt(s) and allowed notes | Cut it, unless the user asked for analysis |
| Filler adjectives | A clause fails the visual-effect test | Delete |
| Attribute left to the model | A look-shaping attribute is unstated, or a depicted thing appears by category name only | State the decided trait; if none was decided, return to the owning phase |
| Prompt too long or too short | Padding, or distinctive decisions lost | Cut filler first; restore specifics |
| Prompt and printed decisions disagree | A printed or amended decision is not visible in the prompt, or the prompt contradicts one | Fix the prompt, or print an amendment if the decision changed |
| Mark and wordmark described as separate objects | The unit has no shared logic, spacing, or region stated | Describe the identity unit as one object |
| Qualities absent from the prompt | The opening lines give no look, value key, or mood | Open with the look and its carriers |
| Numeric overload | Many percentages and cap heights the model will ignore | Keep only proportions that change the result |
| Designed copy flattened | A designed item is described as plain text | Describe its treatment traits |
| Hero and its text described apart | Callouts or the hook sit in separate paragraphs or zones instead of one composition | Describe the hero group as one composition |

## 4. Completion criteria, hand-off, and delivery

Complete when the phase card's "Before leaving" check holds and the audit in `quality_control.md` passes. Phase 6 is not summarized. **Hand-off:** the audited prompt(s) go to the reply, delivered per SKILL.md 13.2: each prompt in its own code block, then any short notes.