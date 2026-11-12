# Phase 6: Prompt Synthesis, part 2 of 2: relationships and space, text, marks, assets, length, exclusions, gate

Write the clauses of each prompt (relationships, space, balance, text, marks, fixed assets, figures, grounds), calibrate length, state the ratio, and pass the prompt audit.

**Inputs needed:** The prompt set and structure from `15_prompt_set_and_structure.md`; each deliverable's Execution Specification and the Phase 4 specifications it names.

## 2. Guidance (continued from `15_prompt_set_and_structure.md`)

### D. Relationships and space

**Relationships.**
- State the hierarchy explicitly (few ranks, each with its distinguishing means) and the reading sequence as a route over the described regions, in agreement with the placement clauses: an element described as read first or second sits where the route puts it, and no ordering word contradicts a position word.
- Describe relative prominence and grouping, contrast and integration, plane order rearmost to front, and how identity, message, and supporting visuals interact.
- Position by relationship and broad region, not coordinates.
- State relationships between neighbors in relational words: alignment to a shared edge or axis, the size of the gap (small, generous), beneath, beside, in front of, and clear ground where nothing touches. An overlap names the front element and the visible part of the covered one.
- Describe the composition as relationships among the hero, the groups, and the ground around them. Partition words (zone, section, block, panel, band, column) appear only where the design contains that physical form; a group is described by what it holds, how it relates to the hero and its neighbors, and the ground around it.

**Space.** Models fill space unless told otherwise. State space as the layout's own structure, positively and before element detail:
- the outer margin, the separation between groups, the isolation around the hero and the unit, each container's inner padding in relation to its text (about one line-height; its height follows its content, so text is neither squeezed nor enlarged), the open regions by what they separate or frame and roughly how much of the format they hold, and the overall density in plain words;
- text sizes as ratios between tiers and relative to neighbors, so the generator neither inflates nor shrinks them; shares of the format only for the major regions (`F`, Numbers); enlarge no element to occupy available area, and add no decoration beyond the decided supporters, atmosphere fields, and counterweights;
- the quantity of every repeated or decorative form as the plan decided it, so the generator neither multiplies forms nor fills the quiet; richness the plan decided is as concrete as restraint, and a count is never set at the smallest safe number when the stance calls for a developed world; name what is deliberately absent only where the generator would otherwise add it;
- atmosphere fields apart from the quiet regions, which stay plain and undecorated: the motif or pattern, its scale and contrast, where it sits, and how it recedes under information;
- agreement between space clauses and element clauses: each zone's clause gives its content and the open ground around it, no clause describes an element as filling, spanning, covering, or packing its zone, and long content lists are grouped into few zones with the arrangement described once, since a long description signals importance and density to the generator.

**Balance.** State the balance relation as built (which side carries the mass and which quiet carrier answers it), as concrete forms and regions.

### E. Text, marks, and fixed assets

- **Mandatory text:** verbatim in quotation marks, once, tied to position and typographic role.
  - Dense text is grouped in reading order, with row behavior described once.
  - Prices and contacts get clarity proportionate to their stage.
  - State that the piece contains only the specified text when hallucinated text is a risk.
  - Never omit mandatory text to shorten the prompt; flag volume risk in the notes.
- **Art direction (the look clause).** It carries the style card's visual language, image-making technique, and light as drawable traits, stated once and applied to every element by name: the lineage (a tradition, era, technique, or material, never a living artist, studio, or protected character) and the traits borrowed from it; how shapes are built and proportioned (geometric or organic, the basic forms, how large head, hands, and props run against the body); line behavior (weight, whether it varies, how ends and corners finish, whether contours close); how form is rendered (flat steps, one shade tone, hatching, brush or cut-paper edges, overprint) and where rendering stops; surface and print character (paper tooth, grain, registration, ink behavior) and where it lives; detail steps by rank; and the color treatment. Strike every category and medium word (flat, vector, sticker, kawaii, cartoon, pop) and bare mood adjectives (cute, playful, friendly, modern, minimal, clean) from the clause: what remains must still tell an illustrator how to draw it. Mascot, objects, lettering, supporters, and ground share this one logic, with texture and detail confined to the zones the style card assigned them so the type zones stay clean.
- **Hero group:** one composition. The hero first; then each integrated item with the exact part it points to, its side or path, and the pointer style (its form, weight, terminal, and the exact part it ends on); attached items by position against the hero; and the relationship in one sentence. Arched text is one short line on one smooth curve. Overlapping or floating supporting elements name the front element and the visible part of the covered hero.
- **Type per role:**
  - State the distinguishing contrast of each role (classification, weight, posture, case, scale, color) once, so descriptions read clearly and hooks stand apart.
  - Each role also states its letterform proportions and baseline (natural, upright, and level unless decided otherwise), plus its letter-spacing, line spacing, case, and alignment as decided.
  - Describe every text region with room to spare, so the generator has no reason to compress or tilt letters.
  - State equivalent items once as sharing the same size, weight, and style regardless of length, with length handled by width, wrapping, or columns. For equivalent cards or rows, state identical outer size, identical internal layout, and fields aligned to the same positions, with longer text wrapping onto an extra line rather than shrinking.
  - Where a string takes more than one line, state its planned wrap (the line breaks decided in Phase 5), keeping the verbatim text split only at those breaks.
- **Designed copy:** letterform character, line breaks, emphasis, container, color role, position. A description names letterform, line breaks, emphasis, container, color role, and position; a quality adjective alone is not a description.
- **Supporters:** concrete forms (what, how drawn, where, how large against neighbors, what color) consistent with the style, never a generic category word; each below the weight of the information beside it. Where a symbol carries an item's kind, the text beside it is the data alone, stated once.
- **Containers and shapes:** for each, its job, form, corner and edge geometry, material impression, edge ornament, fill mode, and layering against its neighbors or the hero, with the shape language stated once and applied by name. A group decided to have no container is stated as open grouping held by spacing and alignment. Never leave containers unstated, since an unstated container takes the model's default rounded form. Describe containers per information role, so different roles are not collapsed into one phrase or one design.
- **Grounds and edges:**
  - a texture or pattern is a low-contrast surface beneath content, in the zones assigned to it and never in the plain quiet regions, calmer where text is denser;
  - a scrim is a translucent tonal layer behind the named text zone;
  - a bleed is an element running off the trim while text stays inside the stated margin;
  - a cutout is an isolated form on a plain ground;
  - a curved or angled edge is the boundary between two named zones.

  A decided surface character is described concretely (what it is, its scale and contrast, where it recedes under text); a uniform ground is stated as uniform.
- **Planes:** state order in relational words (in front of, behind, over), rearmost to front, with the visible layer cues. For any overlap, state which element is in front and which part of the covered element stays visible; keep mandatory text where every letterform stays whole, and say so.
- **Supplied logo or character:** reproduced as provided (by reference if the model accepts images, otherwise described faithfully), never replaced by an invention.
- **Figure:** one designed character or person: form class and construction (the basic shapes it is built from), proportions, silhouette, signature trait, personality as drawn (expression and posture), rendering language, palette, and the pose, gesture, and relation to the offer its role requires. Fictional and non-identifiable; identical wording in every deliverable; hands, faces, and groups only as simply as the generator holds them.
- **Reserved asset panel:** a designed region with position, share of the format, flat color, frame, and isolation, and nothing inside. No code or photograph is imitated.
- **New mark:** form class, geometry, silhouette, color, boundary type, personality device, relationship to the wordmark, and separation from adjacent type, concretely enough to be drawn the same way each time. State the name's exact letters, every letter fully formed and in order, readable as the name at first sight.
- **Identity unit:** one object: arrangement, shared construction logic of mark and lettering, proportion and spacing relationship, alignment axis, color roles, and the clear space and region that distinguish the whole unit from surrounding type. Never two unrelated items.

### F. Length, static artwork, exclusions

- **Numbers.** No pixel or millimeter measurements, coordinates, or exact angles. Sizes are ratios between tiers ("about one and a half times the item-name height") and shares of the format for the major regions only (the hero group, the main information group, the footer, the margin): about six numbers per prompt at most, because a prompt crowded with percentages dilutes the decisions that matter. Stated sizes come from the role floors and the region table, never from conventional or remembered sizes.
- **Length.** Length is proportional to complexity: every sentence carries a decision or a relationship. Word count signals importance and density to the generator, so describe each element in proportion to its rank and give the open regions the same specificity as the elements. Cut filler before specifics; restore specifics before adding length.
- **Static artwork.** Describe finished flat artwork unless a mockup is requested or the physical form is the deliverable. No crop marks, bleed guides, or annotations unless requested.
- **Exclusions.** Express traits positively. Use exclusions only for explicit user exclusions, high-probability failures that matter, and cultural or factual risks. An exclusion never substitutes for a decision: it does not remove the occasion's own world, which Phases 3 and 4 decided how to render.
- **Ratio.** State the deliverable's ratio from S in the opening line and describe the full design at that ratio. No substitute ratio, crop, or ratio note is introduced.

## Quality checks

**Gate (verbatim from the phase file):**

The prompt audit (`prompt_and_reply_audit.md` section 3) is this phase's gate. It covers plan fidelity, verbatim content, fixed assets, quality carriers in the opening lines, space, identifier description, standalone completeness of every prompt, the visual-effect and misread tests on every sentence, and the absence of rationale, placeholders, blanket emphasis, and unstated look-shaping attributes.


## Next

Read `prompt_and_reply_audit.md` and run the prompt audit on every prompt and on the set; on failure read `triage_and_revisions.md` and return to the earliest cause (show an amendment first if a shown decision changes). Then compose each prompt's label, the usage steps, and the notes, and deliver per `ux_wait_notes_entries_and_final_reply.md` section 6.
