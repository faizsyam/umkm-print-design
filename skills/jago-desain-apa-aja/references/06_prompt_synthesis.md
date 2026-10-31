# Phase 6: Prompt Synthesis

## Phase card

| Item | Content |
|---|---|
| Goal | A set of standalone image-generation prompts, one per deliverable, each describing its finished static design so exactly that an illustrator who never saw the brief or the other prompts could produce it. Synthesis is translation, not invention |
| Receives | S (deliverable set, mandatory strings verbatim, fixed assets, exclusions, quality requirements with their carriers, the generator and language if named); each deliverable's Execution Specification; the Phase 4 element specifications it names (palette, type character, mark and lockup construction, copy treatments, supporter forms, figure design); Phase 3 style dimensions and hero specifics. **Not received:** any Record, candidate or rejected option, research, tension, rationale text, or purpose line (the Execution Specification carries their consequences). Source tags on Forward fields are not prompt content. The pre-synthesis check (`SKILL.md` section 9) has already passed |
| Decisions | The prompt set (how many, what each is for); what is in each prompt and what stays out; structure; placement and wording of every mandatory text item; how the mark and fixed assets are described; how space is expressed; minimal exclusions; each deliverable's stated ratio; the labels, usage steps, and notes |
| Exploration | None. If translation needs a new concept, style, or element, an earlier phase had a gap: return to it and re-run forward |
| Output | The audited prompts, each labeled with its purpose, with brief usage steps and any short notes, delivered per `00_conversation_ux.md` section 6. Phase 6 is not summarized or shown as an entry |

## 1. Process

1. Confirm entry: the Phase 5 gate passed and the pre-synthesis check (`SKILL.md` section 9) is complete.
2. Fix the prompt set from the deliverable set (G). Sort every design element into "in the prompt" or "stays out" (A).
3. Write each prompt separately from S, the shared specifications, and that deliverable's Execution Specification.
   - Choose a structure suited to the design's complexity (B).
   - Write each clause specifically, as relationships, with space as a positive feature (C to E).
   - Place text and describe marks and fixed assets exactly (E).
4. Calibrate length, describe the static artwork as seen, set minimal exclusions, and state the ratio (F). Apply language and the prompt set (G).
5. Run the prompt audit (`quality_control.md` section 3) on every prompt and on the set; on failure, return to the earliest cause. If the audit forces a change to a shown decision, show the amendment first.
6. Compose each prompt's label, the usage steps, and the notes, and deliver.

## 2. Guidance

### A. In and out

**Out:** strategy, brand story, audience and environment analysis, research, the piece's purpose, success criteria, alternatives, and any "because" or "in order to". These acted through decisions; the prompt carries the visible traits they produced. An impression word may remain only as a brief tone anchor that steers rendering and justifies nothing.

**In:**
- Piece type and format (orientation, aspect ratio, sides or panels), which is all a prompt says about what the piece is for. The purpose and relationship go in the label outside the prompt.
- The overall look as seen (value key, dominant field, mood, finish).
- What is depicted and how.
- Composition and relationships; the reading order stated as first, second, third, with the visible means each rank holds.
- Typography character per role and designed copy; mandatory text.
- Supporters as concrete forms; color and surface; mark construction; background and unifying devices.
- The few finishing details that matter; rendering technique; necessary exclusions.

Express size as proportions and steps between elements. State emphasis only where the specification holds it, never as blanket emphasis words.

### B. Structure

Order by consequence:
1. piece and format;
2. overall look as seen (value key and dominant field first, so stated qualities govern generation);
3. spatial composition (overall density, the open regions, separation between zones), then hierarchy;
4. hero and main visuals;
5. identity unit;
6. typography;
7. color;
8. background and unifying devices;
9. supporting details;
10. mandatory text placed in context.

Adapt the order to complexity, and keep one coherent style logic from first sentence to last.

### C. Specificity

- Use precise design vocabulary (`protocol.md` section 4) and concrete visual description. A sentence an illustrator could read two ways is not yet specific.
- Describe each depicted thing by its true specifics (form, material, construction, arrangement) as decided in Phases 3 and 4, not by category name: a category name summons the model's apparent instance.
- State every look-shaping attribute the plan decided; an unstated one takes the model's apparent value. If no earlier phase decided it, return to the phase that owns it rather than invent it here. Silence is allowed only where that value is the intended result.
- Describe illustration, photography, and mixed media by their decided language (lineage, proportions, linework, rendering, texture, detail level, color treatment, stylization; framing, light, grade, and finish for photography), never by the medium's name.

### D. Relationships and space

**Relationships.**
- State the reading order explicitly (few ranks, each with its distinguishing means).
- Describe relative prominence and grouping, contrast and integration, plane order rearmost to front, and how identity, message, and supporting visuals interact.
- Position by relationship and broad region, not coordinates.

**Space.** Models fill space unless told otherwise.
- Describe the outer margin, separation between zones, isolation around key elements, internal spacing within zones, and resting fields as positive features (where, roughly how much of the format, what they frame, that they stay quiet and uncluttered). Keep lower-tier text small relative to the format, enlarge no element to occupy available area, and add no decoration beyond the decided supporters and counterweights.
- Write space as the layout's own structure, not a mood or a closing phrase: name the open regions by what they separate or frame and roughly how much of the format they hold, and state the overall density in plain words as the plan set it. Both appear before element detail, with as much specificity as the elements.
- Keep space clauses and element clauses in agreement. Each zone's clause gives its content and the open ground around it, and no clause describes an element as filling, spanning, covering, or packing its zone.
- Group long content lists into few zones with the arrangement described once, since a long description signals importance and density to the generator.

**Balance.** State the balance relation as built (which side carries the mass and which quiet carrier answers it), as concrete forms and regions.

### E. Text, marks, and fixed assets

- **Mandatory text:** verbatim in quotation marks, once, tied to position and typographic role.
  - Dense text is grouped in reading order, with row behavior described once.
  - Prices and contacts get clarity proportionate to their stage.
  - State that the piece contains only the specified text when hallucinated text is a risk.
  - Never omit mandatory text to shorten the prompt; flag volume risk in the notes.
- **Hero group:** one composition. The hero first; then each integrated item with the exact part it points to, its side or path, and the pointer style (its form, weight, terminal, and the exact part it ends on); attached items by position against the hero; and the relationship in one sentence. Arched text is one short line on one smooth curve.
- **Type per role:**
  - State the distinguishing contrast of each role (classification, weight, posture, case, scale, color) once, so descriptions read clearly and hooks stand apart.
  - Each role also states its letterform proportions and baseline (natural, upright, and level unless decided otherwise).
  - Describe every text region with room to spare, so the generator has no reason to compress or tilt letters.
  - State equivalent items once as sharing the same size, weight, and style regardless of length, with length handled by width, wrapping, or columns.
- **Designed copy:** letterform character, line breaks, emphasis, container, color role, position. "Stylish text" is not a description.
- **Supporters:** concrete forms (what, how drawn, where, how large against neighbors, what color) consistent with the style, never "decorative elements"; each below the weight of the information beside it.
- **Containers and shapes:** for each, its job, form, corner and edge geometry, and fill mode, with the shape language stated once and applied by name. Never leave them unstated, since an unstated container takes the model's default rounded form. Describe containers per information role, so different roles are not collapsed into one phrase or one design.
- **Grounds and edges:**
  - a texture or pattern is a low-contrast surface beneath content;
  - a scrim is a translucent tonal layer behind the named text zone;
  - a bleed is an element running off the trim while text stays inside the stated margin;
  - a cutout is an isolated form on a plain ground;
  - a curved or angled edge is the boundary between two named zones.

  A decided surface character is described concretely (what it is, its scale and contrast, where it recedes under text); a uniform ground is stated as uniform.
- **Planes:** state order in relational words (in front of, behind, over), rearmost to front, with the visible layer cues. For any overlap, state which element is in front and which part of the covered element stays visible; keep mandatory text where every letterform stays whole, and say so.
- **Supplied logo or character:** reproduced as provided (by reference if the model accepts images, otherwise described faithfully), never replaced by an invention.
- **Figure:** one designed character or person: form class, proportions, silhouette, signature trait, rendering language, palette, and the pose, gesture, and relation to the offer its role requires. Fictional and non-identifiable; identical wording in every deliverable; hands, faces, and groups only as simply as the generator holds them.
- **Reserved asset panel:** a designed region with position, share of the format, flat color, frame, and isolation, and nothing inside. No code or photograph is imitated.
- **New mark:** form class, geometry, silhouette, color, boundary type, personality device, relationship to the wordmark, and separation from adjacent type, concretely enough to be drawn the same way each time.
- **Identity unit:** one object: arrangement, shared construction logic of mark and lettering, proportion and spacing relationship, alignment axis, color roles, and the clear space and region that distinguish the whole unit from surrounding type. Never two unrelated items.

### F. Length, static artwork, exclusions

- **Numbers.** No pixel measurements, coordinates, or exact angles unless essential. State a proportion only where the model's default would break the design (the margin, the hero's share, the large scale steps); elsewhere use relational words. A prompt crowded with percentages dilutes the decisions that matter.
- **Length.** Length is proportional to complexity: every sentence carries a decision or a relationship. Word count signals importance and density to the generator, so describe each element in proportion to its rank and give the open regions the same specificity as the elements. Cut filler before specifics; restore specifics before adding length.
- **Static artwork.** Describe finished flat artwork unless a mockup is requested or the physical form is the deliverable. No crop marks, bleed guides, or annotations unless requested.
- **Exclusions.** Express traits positively. Use exclusions only for explicit user exclusions, high-probability failures that matter, and cultural or factual risks.
- **Ratio.** State the deliverable's ratio from S in the opening line and describe the full design at that ratio. No substitute ratio, crop, or ratio note is introduced.

### G. Language and the prompt set

- **One prompt per deliverable** (per concept), fixed by the deliverable set. Never split content that belongs in one image, and never merge deliverables that need different compositions.
- **Each prompt is complete on its own.** It names its piece type and format, restates every shared decision (identity, style, color, type, supporters, figure) in the same words wherever the same thing recurs, and carries its own composition, hierarchy, and text. It never refers to another prompt, an earlier generation, the brief, or a series. Consistency across prompts comes from identical wording of shared decisions and identity elements; composition differs only where format or encounter differs.
- **Delivery.** Each prompt has a label line outside its code block (its number, the deliverable's purpose and its place in the whole request, its format). Usage steps and notes follow `00_conversation_ux.md` section 6.
- **Language.** The prompt is in English by default, with on-image text verbatim in its original language, unless the user requests otherwise or names a model that performs better in another language. Everything outside the prompt is in the user's language; each prompt stays alone in its code block.

## 3. Gate checks

The prompt audit (`quality_control.md` section 3) is this phase's gate. It covers plan fidelity, verbatim content, fixed assets, quality carriers in the opening lines, space, identifier description, standalone completeness of every prompt, the visual-effect and misread tests on every sentence, and the absence of rationale, placeholders, blanket emphasis, and unstated look-shaping attributes.

Objection (senior art director or prompt specialist; two at Full depth): where would the model's apparent value silently replace a decision?