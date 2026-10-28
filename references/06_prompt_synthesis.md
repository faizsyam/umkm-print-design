# Phase 6: Prompt Synthesis

## Phase card

| Item | Content |
|---|---|
| Goal | A standalone image-generation prompt describing the finished design so exactly that an illustrator who never saw the brief could produce it. Synthesis is translation, not invention |
| Receives | The Execution Specification; the Phase 4 element specifications it places (palette, type character, mark and lockup construction, copy treatments, supporter forms, figure design); Phase 3 style dimensions and hero specifics; Phase 1 mandatory strings (verbatim) and fixed assets; the "Ready for Phase 6" commitments (`SKILL.md` section 9); the target model and language preference if named |
| Decisions | What is in the prompt and what stays out; structure; placement and wording of every mandatory text item; how the mark and fixed assets are described; how space is expressed; minimal exclusions; ratio handling; the notes |
| Exploration | None. If translation needs a new concept, style, or element, an earlier phase had a gap: return to it and re-run forward |
| Output | The audited prompt(s) and any short notes, delivered per `00_conversation_ux.md` section 6. Phase 6 is not summarized or printed as an entry |

## 1. Process

1. Confirm entry: the Phase 5 gate passed and the commitments are complete.
2. Sort every design element into "in the prompt" or "stays out" (A).
3. Choose a structure suited to the design's complexity (B); write each clause specifically, as relationships, with space as a positive feature (C to E); place text and describe marks and fixed assets exactly (E).
4. Calibrate length, describe flat artwork, set minimal exclusions, handle ratio limits (F); apply language and multiples (G).
5. Run the prompt audit (`quality_control.md` section 3); on failure return to the earliest cause. If the audit forces a change to a printed decision, print the amendment first.
6. Compose the notes and deliver.

## 2. Guidance

### A. In and out
**Out:** business strategy, brand story, audience and environment analysis, research, the piece's purpose, success criteria, alternatives, and any "because" or "in order to". These acted through decisions; the prompt carries the visible traits they produced. An impression word may remain only as a brief tone anchor that steers rendering and justifies nothing.

**In:** piece type and format (orientation, aspect ratio, faces); the overall look as seen (value key, dominant field, mood, finish); what is depicted and how; composition and relationships; the reading order stated as first, second, third with the visible means each rank holds; typography character per role and designed copy; mandatory text; supporters as concrete forms; color and surface; mark construction; background and unifying devices; the few finishing details that matter; rendering technique; necessary exclusions. Express size as proportions and steps between elements; state emphasis only where the specification holds it, never blanket emphasis words.

### B. Structure
Order by consequence: piece and format; overall look as seen (value key and dominant field first, so stated qualities govern generation); composition and hierarchy; hero and main visuals; identity unit; typography; color; background and unifying devices; supporting details; mandatory text placed in context. Adapt the order to complexity; keep one coherent style logic from first sentence to last.

### C. Specificity
Use precise design vocabulary (`protocol.md` section 4) and concrete visual description; a sentence an illustrator could read two ways is not yet specific. Describe each depicted thing by its true specifics (form, material, construction, arrangement) as decided in Phases 3 and 4, not by category name: a category name summons the model's apparent instance. State every look-shaping attribute the plan decided; an unstated one takes the model's apparent value. If no earlier phase decided it, return to the phase that owns it rather than invent it here; silence is allowed only where that value is the intended result.

### D. Relationships and space
State the reading order explicitly (few ranks, each with its distinguishing means) and describe relative prominence and grouping, contrast and integration, plane order rearmost to front, and how identity, message, and supporting visuals interact. Position by relationship and broad region, not coordinates. Models fill space unless told otherwise: describe the outer margin, isolation around key elements, and resting fields as positive features (where, roughly how much of the format, what they frame, that they stay quiet and uncluttered), with no filler decoration to relieve emptiness.

### E. Text, marks, and fixed assets
- **Mandatory text:** verbatim in quotation marks, once, tied to position and typographic role. Dense text is grouped in reading order with row behavior described once. Prices and contacts get clarity proportionate to their stage. State that the piece contains only the specified text when hallucinated text is a risk. Never omit mandatory text to shorten the prompt; flag volume risk in the notes.
- **Hero group:** one composition: the hero first, then each integrated item with the exact part it points to, its side or path, and the pointer style (e.g. a thin straight line ending in a small dot on the named part), attached items by position against the hero, and the relationship in one sentence. Arched text is one short line on one smooth curve.
- **Type per role:** the distinguishing contrast of each role (classification, weight, posture, case, scale, color) stated once, so descriptions read clearly and hooks stand apart.
- **Designed copy:** letterform character, line breaks, emphasis, container, color role, position. "Stylish text" is not a description.
- **Supporters:** concrete forms (what, how drawn, where, how large against neighbors, what color) consistent with the style, never "decorative elements"; each below the weight of the information beside it.
- **Grounds and edges:** a texture or pattern is a low-contrast surface beneath content; a scrim a translucent tonal layer behind the named text zone; a bleed an element running off the trim while text stays inside the stated margin; a cutout an isolated form on a plain ground; a curved or angled edge the boundary between two named zones.
- **Planes:** state order in relational words (in front of, behind, over), rearmost to front, with the visible layer cues. For any overlap, state which element is in front and which part of the covered element stays visible; keep mandatory text where every letterform stays whole, and say so.
- **Supplied logo or character:** reproduced as provided (by reference if the model accepts images, otherwise described faithfully), never replaced by an invention.
- **Figure:** one designed character or person: form class, proportions, silhouette, signature trait, palette, and the pose, gesture, and relation to the offer its role requires; fictional and non-identifiable; identical wording on every face; hands, faces, and groups only as simply as the generator holds them.
- **Reserved asset panel:** a designed region with position, share of the format, flat color, frame, and isolation, nothing inside. No code or photograph is imitated.
- **New mark:** form class, geometry, silhouette, color, boundary type, personality device, relationship to the wordmark, and separation from adjacent type, concretely enough to be drawn the same way each time.
- **Identity unit:** one object: arrangement, shared construction logic of mark and lettering, proportion and spacing relationship, alignment axis, color roles, and the clear space and region that distinguish the whole unit from surrounding type. Never two unrelated items.

### F. Length, flat artwork, exclusions
- No pixel measurements, coordinates, or exact angles unless essential. State a proportion only where the model's default would break the design (the margin, the hero's share, the large scale steps); elsewhere use relational words. A prompt crowded with percentages dilutes the decisions that matter.
- Length is proportional to complexity: every sentence carries a decision or a relationship. Cut filler before specifics; restore specifics before adding length.
- Describe finished flat artwork unless a mockup is requested or the physical form is the deliverable; no crop marks, bleed guides, or annotations unless requested.
- Express traits positively. Exclusions only for explicit user exclusions, high-probability failures that matter, and cultural or factual risks.
- If a required ratio exceeds what the model supports, use the nearest supported ratio, keep the design valid at it, and flag it in the notes.

### G. Language and multiples
The prompt is English by default, with on-piece text verbatim in its original language, unless the user requests otherwise or names a model that performs better in another language. Everything outside the prompt is plain Indonesian; the prompt stays alone in its code block. Several concepts or faces: one complete standalone prompt each (concepts differing in underlying approach; faces restating the shared identity in the same words).

## 3. Gate checks

The prompt audit (`quality_control.md` section 3) is this phase's gate: it covers plan fidelity, verbatim content, fixed assets, quality carriers in the opening lines, space, identifier description, the visual-effect test on every sentence, and the absence of rationale, placeholders, blanket emphasis, and unstated look-shaping attributes. Objection (senior art director or prompt specialist; two at Full depth): where would the model's apparent value silently replace a decision?