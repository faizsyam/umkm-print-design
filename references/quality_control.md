# Quality Control

## Contents
1. Purpose and scope
2. Three levels of review
3. Phase gates
4. Diagnostic tests
5. Whole-composition review
6. AI-slop diagnostics: generic and AI-typical output
7. Compliance audit
8. Issue triage and where to return
9. Controlling iteration
10. Prompt audit and release checklist

## 1. Purpose and scope

Quality control is not a final inspection. It is a set of checks applied at the moment each decision is made, again on the assembled composition, and once more on the finished prompt. This file defines the gates, the tests, the severity levels, and the route back to the phase responsible for a problem.

## 2. Three levels of review

| Level | When | Question |
|---|---|---|
| Decision | At the end of each phase | Is this phase's output complete, justified, and consistent with earlier phases? |
| Composition | End of Phase 5 | Does the assembled design fulfill the Communication Problem and the Design Plan? |
| Prompt | End of Phase 6 | Does the prompt faithfully carry the design, the content, and the constraints, and nothing else? |

## 3. Phase gates

A phase is not finished until its gate passes. The gates below are the short form of the completion criteria in each phase reference; if the two seem to differ, the phase reference governs. At each gate, the perspectives that own the phase (see `SKILL.md`) each raise one objection to the output; resolve it or record why it is accepted.

| Phase | Gate |
|---|---|
| 1 Brief | Every content item classified by necessity and provenance; mandatory text verbatim; fixed assets and exclusions recorded; blocking gaps resolved or asked; no invented facts |
| 2 Analysis | Communication Problem stated; Environment Profile (landscape, competing stimuli, light, audience behavior, viewing stages, departure and fit dimensions) built; tensions listed; differentiation strategy chosen; every design implication traceable to a finding or the brief; research limited to decisions it informed |
| 3 Design Plan | Core idea, style, and hero each chosen from at least three distinct candidates, evaluated and engineered; core idea is specific, visual, generative, truthful, functional; impression expressed through the environment; brand design and theme separated; swap, category, and context-swap tests passed |
| 4 Design Elements | Color strategy, typographic voice, and mark each chosen from at least three candidates (mark fixed if supplied); color judged against the surrounding landscape; mark distinct from surrounding typography by named mechanisms; each element has a role and passes the removal test; consistent rendering treatment |
| 5 Execution | One-sentence message; every item assigned to a reading stage; tiers sized to stage minimums plus hierarchy needs; intended quiet space realized; spatial strategy chosen from three candidates; mark region secured; context-fit review passed |
| 6 Prompt | Prompt audit and release checklist passed, including the prompt-focus test |

## 4. Diagnostic tests

These tests are used wherever relevant. They are tools of judgment, not a required sequence.

- **Swap test**: substitute a competitor; if the design still works unchanged, it is generic.
- **Category test**: remove the product from the description; if the identity could belong to the industry in general, it is stereotyped.
- **Removal test**: take away an element; if nothing is lost, delete it.
- **Distance test**: judge each reading tier at the distance of its own stage. The glance content and brand must survive the farthest stage; closer-stage content must be workable at its stage, without being enlarged to the farthest.
- **Squint test**: blur mentally; the hierarchy and grouping should remain evident as masses of tone and shape.
- **First-glance test**: what is understood in the first moments, and does it match the objective?
- **Isolation test** (mark): remove everything but the mark; it must be recognizable and distinct.
- **Reduction test** (mark): render in one color and small; it must remain clear.
- **Separation test** (mark): the mark must be visually distinct from the hero, lettering, and decoration around it.
- **Text-neighborhood test** (mark): place the mark beside the densest text; squint. It must resolve as a distinct object before any word is read.
- **Proportion test**: for each element name its reading stage and minimum; anything far above its minimum that is not the hero or glance message is oversized.
- **Breathing test**: the quiet space matches the intended share; removing a small element does not simply invite another to fill the gap.
- **Environment test**: place the design among its actual neighbors and light. It must fit the place and separate on the intended dimension.
- **Context-swap test**: the design would not be equally right in a different setting.
- **Candidate test**: each consequential decision shows three candidates that would look different in the real setting, not variants of one idea.
- **Prompt-focus test**: every prompt clause changes the image or constrains the output; deleting it would alter the result.
- **Single-voice test**: do the typography, illustration, color, and decoration appear to come from one designer with one intention?
- **Restraint test**: remove the weakest decorative element; if the design improves, leave it out.
- **Truth test**: can the business honestly stand behind every claim, depiction, and mark the design makes?
- **Renderability test**: can an image model plausibly produce each described element and string of text reliably?

## 5. Whole-composition review

Review from each perspective:

- **Brand strategist**: Is the identity true, distinctive, and coherent with the brand design?
- **Consumer-behavior researcher**: Does the sequence attention → comprehension → credibility → action work for this audience in this setting?
- **Art director**: Is there a clear, singular idea? Is taste consistent? Is anything excessive?
- **Graphic designer**: Are type, color, mark, and shapes resolved and related?
- **Print designer**: Does it hold under the viewing distance, light, material, and production limits?
- **Visual communication specialist**: Is the hierarchy unambiguous and the information structure scannable?
- **Prompt specialist**: Can this be described so a model reproduces it faithfully?

Record failures with severity (section 8) and route them.

## 6. AI-slop diagnostics: generic and AI-typical output

Diagnose by mechanism, not by naming forbidden looks. Apply these during design (Phases 3–5) as well as at review; do not recite them to the image model.

- **Default-driven decoration**: effects added to signal "professional" or "premium" that have no function in this design: sheen, glow, depth effects, ornamental sparkle, gratuitous gradient, ornate borders. Test with the removal and restraint tests.
- **Category template**: the design resembles what the category usually looks like rather than what this business is. Test with the swap and category tests.
- **Disconnected decoration**: ornaments, motifs, or props with no link to the business, product, or idea.
- **Uniform emphasis**: everything glossy, lit, and dramatic, leaving no hierarchy or rest.
- **Reflexive symmetry and centering**: composition chosen by default rather than by content.
- **Inconsistent rendering**: mixed styles, light directions, or finish levels across elements.
- **Stock hero**: a generic subject with no tie to the business's actual product or story.
- **Fake culture**: heritage or regional signals added as flavor without connection.
- **Style stacking**: many aesthetic labels combined to appear sophisticated, producing an average.
- **Malformed content**: garbled lettering, invented words, impossible object structures.
- **Crowded dominance**: many elements sized for the farthest distance, leaving no hierarchy or rest.
- **Mark absorbed into typography**: the identifier shares form, weight, and color role with the text around it.
- **Environment-blind direction**: a look chosen from the category and brand alone that would be right anywhere.
- **Unchallenged default**: the obvious aesthetic or first idea adopted without competing candidates.

When detected, return to the phase where the default entered (usually Phase 3 or 4), and replace it with a decision traceable to the brief.

## 7. Compliance audit

| Requirement | Check |
|---|---|
| Mandatory content | Every item present, verbatim, correctly placed |
| Optional content | Included only where it does not harm hierarchy |
| Exclusions | Every user exclusion respected |
| Fixed assets | Logo, colors, fonts, photos used as given; nothing redesigned |
| Format | Medium, orientation, aspect ratio, face count as briefed |
| Factual integrity | No invented prices, claims, certifications, testimonials, contacts, or statistics |
| Objective | The primary objective is served by the first-glance read |
| Viewing conditions | Legible and effective in the stated setting |
| Cultural integrity | No unverified or misused cultural reference; user's language register preserved |
| Originality | No copying of competitor or existing designs |
| Output contract | Prompt standalone; no analysis exposed unless requested |
| Prompt focus | Contains only visual instructions, format, mandatory text, and necessary exclusions; no rationale or context |

## 8. Issue triage and where to return

**Severity**
- **Blocking**: violates a non-negotiable, loses mandatory content, misrepresents the business, or defeats the objective. Must be fixed before delivery.
- **Major**: materially weakens effectiveness, distinctiveness, or coherence. Fix unless it conflicts with a higher-priority requirement.
- **Minor**: polish. Fix if cheap; otherwise accept.

**Route to the cause**

| Symptom | Likely origin | Return to |
|---|---|---|
| Generic feel, swap test fails | Weak core idea or differentiation | Phase 3 (or 2) |
| Brand feels wrong or invented | Brand design not grounded in evidence | Phase 2, then 3 |
| Mixed or conflicting look | Style synthesis incoherent | Phase 3 |
| Mark indistinct or fails isolation/reduction | Mark construction | Phase 4 |
| Palette weak in the light or in print | Color logic | Phase 4 |
| Type unreadable or unrelated to identity | Typographic system | Phase 4 |
| Clutter or noise | Visual supporters or unifying devices | Phase 4 |
| Message unclear at first glance | Hierarchy | Phase 5 |
| Content does not fit or cramps; everything competes | Reading stages, area budget, triage; or hero/layout capacity | Phase 5, then 3 if the concept demands too much content |
| Unreadable at distance | Scale and contrast decisions | Phase 5 |
| Prompt needs content not in plan | Plan gap | Phase indicated by the missing content |
| Text corrupted or missing in prompt | Synthesis error | Phase 6 |
| Missing or ambiguous user information | Brief gap | Phase 1 |
| Design blends into or clashes with its surroundings | Environment Profile or expression of the impression | Phase 2, then 3 |
| Mark reads as part of the typography | Distinction mechanisms or mark region | Phase 4, then 5 |
| Obvious or unexamined direction | Exploration not applied | Phase 3 (or 4, 5) |
| Prompt contains reasoning, context, or blanket emphasis | Synthesis | Phase 6 |

Fix at the earliest responsible point. Never repair a prompt with extra clauses that fight an earlier decision.

## 9. Controlling iteration

Quality control must converge.

- Revisit an issue at most twice. After the second cycle, choose the strongest available resolution and proceed.
- After a revision, re-run only the checks the change could affect, plus the compliance audit if content moved.
- Do not reopen a settled decision because of taste fluctuation. Reopen only on evidence: a failed test, a contradiction, or a missed requirement.
- Do not add checks to compensate for weak early decisions; strengthen the decisions.
- Treat unresolved minor issues as acceptable. Delivering a good, faithful prompt beats polishing indefinitely.

## 10. Prompt audit and release checklist

Confirm each item before delivery:

1. All mandatory content appears verbatim, once, with role and position.
2. No invented facts, no unrequested content, no placeholders.
3. Fixed assets are respected and described or referenced correctly.
4. The prompt expresses the Design Plan's core idea, style, hero, mark, color, type, and hierarchy, and introduces nothing outside it.
5. It describes relationships, not only inventories.
6. Distinctive decisions are preserved; filler and redundancy are removed.
7. No contradictions in style, color, density, or placement.
8. No excessive micro-specification, and no technical print jargon that does not change the image.
9. Format, aspect ratio, and orientation are stated; the artwork is described as a flat finished design unless a mockup was requested.
10. Exclusions are minimal and specific.
11. No reasoning, rationale, alternative concepts, references to phases, or meta-commentary inside the prompt.
12. The prompt is delivered in one code block; any outside notes are short and only the permitted kinds.
13. The reply language matches the user's.
14. If several concepts or faces were requested, each prompt is standalone and the concepts genuinely differ.
15. Every sentence changes the image or constrains the output; no rationale, strategy, audience or environment commentary, or blanket emphasis words.
16. Scale is stated as proportion and hierarchy, quiet space is preserved, and the mark is described as a distinct object.

If any item fails, route it using section 8 and correct it before sending.