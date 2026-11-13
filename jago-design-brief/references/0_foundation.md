# Foundation: how the two layers divide the work

**Read:** once, at start. **Governs:** every decision about what the skill settles beforehand and what it leaves to ChatGPT.

## 1. Evidence status (never present an assumption as fact)
| Class | Statement | Use |
|---|---|---|
| **Documented** (OpenAI developer docs, as relayed in the owner's research; the research is itself a ChatGPT answer, so page-level detail is unverified until the docs are checked) | The conversational model can call image generation as a tool and may revise the prompt before the image model sees it (a `revised_prompt` field exists in the Responses API). Prompting guidance asks for clear subject, composition, style, constraints; exact text in quotes with position and typography; for edits, what changes and what stays; one change per refinement. Image models take planning/complexity and quality settings; multi-turn editing exists. Short natural prompts often suffice for simple work; complex requests benefit from structure | Shapes the brief format and the revision method |
| **Observed** (the owner) | A raw brief pasted into ChatGPT consistently beats the previous skill's prompt | The reason for this architecture |
| **Not established** | Whether the ChatGPT app always rewrites the request; how it weighs long or structured input; what its internal prompt contains; why the old skill lost | Design to be robust, not to exploit guesses |

**Why the old output may have lost (competing hypotheses, not findings):** (a) prescribed layout, sizes, and numbers overrode a better decision; (b) very long input diluted the intent; (c) dense text forced into tiny sizes; (d) contradictory or hybrid directives; (e) the prescribed concept was weaker than ChatGPT's own. Only (a) to (d) are cured by prescribing less, so the skill must win under any of them: say less, say it consistently, and contribute only what the raw brief lacks (e).

## 2. What each layer does best (architectural assumptions, to be validated by the A/B test in `5_delivery_and_revision.md`)
- **ChatGPT alone:** reads intent and register, fills harmless gaps, composes, pairs type, sets lighting, turns qualities into visuals, writes its own detailed prompt. It decides in one pass, from the brief alone.
- **Where a raw brief falls short (the skill's contribution):**
  1. Material ambiguity is guessed silently instead of asked.
  2. Nothing is known beyond the brief: the subject's truth, culture, differentiator, so the apparent, category-generic solution wins.
  3. Competing content is never prioritized: dense text is dropped, garbled, or all set equal.
  4. Feasibility is never checked: volume against format and viewing distance.
  5. Assets and references arrive without roles or fidelity levels.
  6. Several images of one project drift apart.
  7. Boundaries (what the piece must not become) are unstated, so default conventions fill them.
- **Not the skill's job:** coordinates, sizes, spacing values, font specifications, rendering recipes, the wording of an image prompt, any decision ChatGPT would make as well or better.

## 3. Consequences for every phase
1. The product is a **design brief**: outcome first, then fixed requirements, then decided direction, then explicit openness. Not a conventional image prompt.
2. Every sentence passes the necessity test (`4_brief_composition.md`). A decision has one owner and is stated once.
3. Direction is stated as intent plus a few defining traits. ChatGPT converts it to visuals.
4. Relationships and priorities replace placement. Viewing conditions are stated as facts, never converted into sizes.
5. Positive wording, with a short list of real exclusions.
6. Length follows the content's need. A brief grows only through verbatim content and real constraints, never through added direction.
7. Calibrate: the first runs are A/B tested against the user's raw brief. If the skill's brief does not win, reduce prescription before adding any.
