# Phase 6: Prompt Synthesis, part 1 of 2: prompt set, in and out, structure, specificity, language

A set of standalone image-generation prompts, one per deliverable, each describing its finished static design so exactly that an illustrator who never saw the brief or the other prompts could produce it.

**Inputs needed:** S (deliverable set, mandatory strings verbatim, fixed assets, exclusions, quality requirements with carriers, generator and language if named); each deliverable's Execution Specification; the Phase 4 specifications it names; Phase 3 style dimensions and hero specifics. Not received: any Record, candidate, research, tension, rationale text, or purpose line.

## Phase sheet

| Item | Content |
|---|---|
| Goal | A set of standalone image-generation prompts, one per deliverable, each describing its finished static design so exactly that an illustrator who never saw the brief or the other prompts could produce it. Synthesis is translation, not invention |
| Receives | S (deliverable set, mandatory strings verbatim, fixed assets, exclusions, quality requirements with their carriers, the generator and language if named); each deliverable's Execution Specification; the Phase 4 element specifications it names (palette, type character, mark and lockup construction, copy treatments, supporter forms, figure design); Phase 3 style dimensions and hero specifics. **Not received:** any Record, candidate or rejected option, research, tension, rationale text, or purpose line (the Execution Specification carries their consequences). Source tags on Forward fields are not prompt content. The pre-synthesis check (`quality_gates.md` section 9) has already passed |
| Decisions | The prompt set (how many, what each is for); what is in each prompt and what stays out; structure; placement and wording of every mandatory text item; how the mark and fixed assets are described; how space is expressed; minimal exclusions; each deliverable's stated ratio; the labels, usage steps, and notes |
| Exploration | None. If translation needs a new concept, style, or element, an earlier phase had a gap: return to it and re-run forward |
| Output | The audited prompts, each labeled with its purpose, with brief usage steps and any short notes, delivered per `ux_wait_notes_entries_and_final_reply.md` section 6. Phase 6 is not summarized or shown as an entry |

## 1. Process

1. Confirm entry: the Phase 5 gate passed and the pre-synthesis check (`quality_gates.md` section 9) is complete.
2. Fix the prompt set from the deliverable set (G). Sort every design element into "in the prompt" or "stays out" (A).
3. Assemble each prompt separately from its drafted clauses (P) and complete it from S, the shared specifications, and that deliverable's Execution Specification. Execution decisions (line breaks, non-mandatory wording, small item and icon details) are made here, directly.
   - Choose a structure suited to the design's complexity (B).
   - Write each clause specifically, as relationships, with space as a positive feature (C in this file; D and E in `16_prompt_clauses_and_delivery.md`).
   - Place text and describe marks and fixed assets exactly (`16_prompt_clauses_and_delivery.md` E).
4. Calibrate length, describe the static artwork as seen, set minimal exclusions, and state the ratio (`16_prompt_clauses_and_delivery.md` F). Apply language and the prompt set (G).
5. Run the prompt audit (`prompt_and_reply_audit.md` section 3) on every prompt and on the set; on failure, return to the earliest cause. If the audit forces a change to a shown decision, show the amendment first.
6. Compose each prompt's label, the usage steps, and the notes, and deliver.

## 2. Guidance

### A. In and out

**Out:** strategy, brand story, audience and environment analysis, research, the piece's purpose, success criteria, alternatives, and any "because" or "in order to". These acted through decisions; the prompt carries the visible traits they produced. An impression word may remain only as a brief tone anchor that steers rendering and justifies nothing.

**In:**
- Piece type and format (orientation, aspect ratio, sides or panels), which is all a prompt says about what the piece is for. The purpose and relationship go in the label outside the prompt.
- The overall look as seen, stated once as the unified art direction (value key, dominant field, mood, light, surface and material finish, depth cues, how rendering treatments step down by rank, and the illustration language: its lineage and borrowed traits, how shapes are built and proportioned, line behavior, how form is rendered, surface and detail steps, as visible traits and never as a category or medium name), which the element clauses refer to instead of each repeating one recipe.
- What is depicted and how.
- Composition and relationships; the hierarchy stated as first, second, third with the visible means each rank holds, and the reading route over the described regions, consistent with the placement.
- Typography character per role (spacing, case, alignment, orientation) and designed copy; mandatory text.
- Supporters and decoration as concrete forms (motif, pattern, ornament, border character); color and surface; mark construction; background and unifying devices.
- The few finishing details that matter; rendering technique; necessary exclusions.

Express size as proportions and steps between elements. State emphasis only where the specification holds it, never as blanket emphasis words.

### B. Structure

Order by consequence:
1. piece and format;
2. overall look as seen (value key and dominant field first, so stated qualities govern generation);
3. spatial composition (overall density, the quiet regions and any atmosphere fields, separation between groups), then hierarchy;
4. hero and main visuals;
5. identity unit;
6. typography;
7. color;
8. background and unifying devices;
9. supporting details;
10. mandatory text placed in context.

Adapt the order to complexity, and keep one coherent style logic from first sentence to last.

### C. Specificity

- Use precise design vocabulary (`exploration_protocol.md` section 4) and concrete visual description. A sentence an illustrator could read two ways is not yet specific.
- Describe each depicted thing by its true specifics (form, material, construction, arrangement) as decided in Phases 3 and 4, not by category name: a category name summons the model's apparent instance.
- State every look-shaping attribute the plan decided; an unstated one takes the model's apparent value. If no earlier phase decided it, return to the phase that owns it rather than invent it here. Silence is allowed only where that value is the intended result.
- Describe illustration, photography, and mixed media by their decided language (lineage, proportions, linework, rendering, texture, detail level, color treatment, stylization; framing, light, grade, and finish for photography), never by the medium's name.
- Describe color by hue with qualifiers and by role and intensity: which is the large calm field, which is the single sparing accent and where it sits, so the generator does not distribute saturation by area.
- Describe rendering treatments (outline, shadow, gradient, highlight, texture) only as the treatment vocabulary names them, applied by role. Where the style has none, state the flat, plain rendering positively so the model adds no default effects.

### G. Language and the prompt set

- **One prompt per deliverable** (per concept), fixed by the deliverable set. Never split content that belongs in one image, and never merge deliverables that need different compositions.
- **Each prompt is complete on its own.** It names its piece type and format, restates every shared decision (identity, style, color, type, supporters, figure) in the same words wherever the same thing recurs, and carries its own composition, hierarchy, and text. It never refers to another prompt, an earlier generation, the brief, or a series. Consistency across prompts comes from identical wording of shared decisions and identity elements; composition differs only where format or encounter differs.
- **Delivery.** Each prompt has a label line outside its code block (its number, the deliverable's purpose and its place in the whole request, its format). Usage steps and notes follow `ux_wait_notes_entries_and_final_reply.md` section 6.
- **Language.** The prompt is in English by default, with on-image text verbatim in its original language, unless the user requests otherwise or names a model that performs better in another language. Everything outside the prompt is in the user's language; each prompt stays alone in its code block.

## Quality checks

## Next

Read `16_prompt_clauses_and_delivery.md` and write each prompt separately.
