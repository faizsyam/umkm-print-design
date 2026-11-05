# Glossary part 1: inputs, records, qualities, context, decisions, reliability (Phases 1 to 6)

One meaning per term for the brief, the analysis, the exploration protocol, and renderability and risk. Terms used for the design system are in `terms_design_system.md`.

**Inputs needed:** None.

## Terms

One meaning per term in every file. Only terms used in more than one file are here; single-file terms are defined where used.

## Inputs and records

| Term | Meaning |
|---|---|
| Brief Ledger | Phase 1 record of everything known about the piece; each item carries necessity, provenance, referent, and (for text) its verbatim form |
| Necessity | **mandatory** (the user said it must appear, or the piece cannot work without it), **optional** (offered or helpful), **excluded** (the user said not to include it) |
| Provenance | **given**, **fixed asset**, **inferred**, **researched**, **creative choice** (the skill's own decision) |
| Fixed asset | A user-supplied element used exactly as provided: logo, brand colors, typefaces, photographs, QR, QRIS or other codes, mascots, established identity |
| Gap classes | **explicit**, **inferable**, **researchable**, **materially uncertain**. A **blocking gap** is a materially uncertain gap that passes the clarification test (`00_conversation_voice_modes_and_intake.md` section 3) and whose answer decides one of the four items listed in `01_brief_and_requirements.md`, section E |
| Subject | What a deliverable represents: a business, organization, product, event, person, or topic. **Brand** is the subject's identity as perceived |
| Deliverable | One image the request needs, with its own purpose in the whole request, medium and use, format and ratio, and relationship to the others. The **deliverable set** is all of them; each gets its own composition (Phase 5) and standalone prompt (Phase 6) |
| Design Log | The persisted state record (`workflow_and_state.md` section 4): the standing block **S**, the decisions **D** (Specification, Source, Basis, Rejected, Status; carry-forward obligations; open flags), and the prompt draft **P**; Basis and Rejected never travel forward |
| Carry-forward obligation | A mitigation, accepted cost, or "amplify here" move recorded by the protocol that a later phase must realize or record as accepted |

## Qualities (Phase 1 terms moved here from "Qualities, copy, supporters" in `terms_design_system.md`)

| Term | Meaning |
|---|---|
| Quality requirement | Any experiential, tonal, affective, or priority statement in the brief, and any style, color, or technique the user names, however vague. Binding, not a preference; a minimal brief makes these the primary requirements |
| Quality translation | For one quality requirement: the visual targets it implies, 2 to 4 **quality carriers** (visible features that deliver it), and the contradicting signals |
| Value key | The area-weighted balance of light, mid, and dark masses (ground and large bands included), with chroma and temperature: high-key, mid-key, low-key. Read by area, not by accent: a small dark logo on a light field is still high-key |

## Context and analysis

| Term | Meaning |
|---|---|
| Communication Problem | The piece's job: objectives, desired audience response, necessary information (gathered into **information groups**), desired perception of the subject, the **message**, the weakest link, and the tensions between needs. The message is the one sentence the glance viewer takes away: written in Phase 2, carried by the core idea, confirmed in Phase 5. The weakest link is the likeliest failure in the chain from encounter to the intended outcome (attention → comprehension → credibility → action, keeping the links the purpose needs) |
| Information group | Phase 2: items of the necessary information that together do one job toward the objective, derived from this brief's content and objective and never from a template. Each records its stage, its referents, its internal hierarchy (members need not share prominence), and its volume. Phase 3 reads the groups for the space budget and the hero's hosting, Phase 4 for supporters, containers, and copy treatment, and Phase 5 refines each into its arrangement, scale, and space need |
| Environment Profile | The context as a design input, one per distinct context: the encounter (where and how the deliverable reaches its audience, neighbors, competing stimuli, audience state, cultural context, reading path), the encounter stages, the medium reading, and the dimensions on which the design departs from or fits its surroundings |
| Medium reading | What the medium **imposes** (what making, reproducing, or displaying does to an image between the generated file and the audience, and the limits it sets), what its audience **relies on** (conventions learned for this kind of piece), and what it **affords**. Derived per deliverable in Phase 2; no convention is applied by default |
| Encounter stage | An ordered moment of an audience's engagement with a deliverable, derived by reasoning from its medium, environment, audience, and purpose. For each: what the audience can perceive, the attention and time it has, what it is trying to decide or do, and what it can reach (physical distance, display scale, zoom, handling). **Glance** is the first stage, with the shortest exposure and widest reach; **approach** and **close** are successively deeper stages. Their number and nature are derived, not assumed: a piece met in passing may have only a glance, a piece handled or inspected has more. A stage the audience cannot reach cannot carry content. **Stage assignment** gives every content item the one stage at which it is needed; items sharing a stage form a **tier**, and the glance tier is the **glance content** |
| Legibility minimum / role floor | Three requirements that are never interchanged. **Legibility limit:** the smallest size a still, attentive viewer with good contrast and light can still decode; angular, so cap height = distance × a ratio, about 1/345 of the distance (tagged assumption). Low contrast, glare, dim light, and ornate or condensed forms raise it; good contrast, even light, and short text lower the margin needed above it. **Comfortable readability:** the size at which text is taken in without effort in its real condition, which depends on exposure: a passing glance about 1/115 of the distance, a few seconds of approach or sustained lines about 1/150 (ordinary printed text at hand distance sits near that). **Prominence:** how strongly an element draws attention; it comes from rank (contrast, isolation, position, and scale only as far as the step needs) and is never part of a floor. A **role floor** sits between the limit and comfortable readability by the role's job, never at a worst case the stage does not contain: text the viewer must take in at once, in passing, or in long runs sits at comfortable readability; text read deliberately by someone who has chosen to read it (short groups and reference details such as contacts, addresses, and fine print) sits near the limit with a margin of about one and a half times it, in good contrast (tagged assumption). The floor used in planning is the larger of the role floor and the raster floor (Render scale), in mm and as a fraction of the format's height. Exposure time bounds what a stage carries: the glance stage holds what a passing viewer needs, the far end of a stated range belongs to that content alone, and later stages use the nearer distances at which the viewer has chosen to look. Phase 2 computes the floors once, per stage and role class, and records them in the Environment Profile; later phases read them and never re-derive them. A floor is a minimum, not a target |
| Departure / fit dimensions | **Departure:** dimensions where neighbors are uniform and the piece can differ to be seen (color field, density, scale, form language, finish, tone). **Fit:** dimensions where the piece must conform for credibility |
| Audience encounter | Phase 2: what the audience does, believes, and must conclude at each encounter stage (cultural references, motivations, decision considerations, trusted register, trust cues). Distinct from the encounter in the Environment Profile, which describes where and how the deliverable reaches the audience |
| Visual source inventory | Phase 2 list of (1) the apparent associations as baseline, (2) deeper true specifics of the subject, its offering, place, or community, (3) which of those are visually workable |
| Design implication | A finding turned into a consequence: "because [finding], the design must / should / must avoid [consequence]", provenance-tagged |

## Decisions and exploration

| Term | Meaning |
|---|---|
| Consequential decision | Core idea, style synthesis, hero, logo mark and lockup, spatial strategy: Full protocol. Other exploratory decisions use the compact comparison or are direct (`exploration_protocol.md` section 1) |
| Apparent option | What most people produce on first association from category, culture, place, or product: a benchmark to beat, never a default. The image model has its own, the **apparent value**: what it supplies for any undecided attribute. **Beyond the apparent** means drawn from true, lesser-seen specifics |
| Look-shaping attribute | Any visible property that changes what is drawn: composition axis and symmetry, container form, corner and edge geometry, fill mode, plane order, rendering finish, rendering treatments (outline, shadow, gradient, highlight, dimension), light, ground, color proportions, lettering with its proportions and baseline, how the subject is depicted (the illustration or photographic language included). One that no decision names takes the model's apparent value |
| Candidate / card | One complete, distinct alternative for one decision. A card has the fields the phase sets, filled in specialist terms (a label alone is not a candidate) |
| Structural axis | A dimension on which candidates must differ to count as distinct: what carries the identity, what the viewer does first, how information is structured, register, image-making method. Color or ornament alone do not count |
| Hybrid / compromise | A **hybrid** combines candidates under one logic, statable as one idea. A **compromise** needs "and also" and is rejected |
| Brand design / theme | **Brand design:** the enduring visual expression of the brand. **Theme:** the creative idea for this piece, built on it |
| Core idea | The single unifying concept from which theme, hero, style, and layout follow: specific, visual, generative, truthful, functional |
| Hero | The dominant visual idea of the piece, or its deliberate absence |

## Reliability and risk

| Term | Meaning |
|---|---|
| Renderability | Whether the image model can draw a thing accurately and repeatably from a description. Reliability falls as: the result must reproduce exact data (characters, digits, codes, specific identities) rather than plausible appearance; more independent details must each be right; detail is fine relative to the image's resolution; the subject is rare or intricate in typical imagery; the same thing must stay identical across separate generations; or it must stay correct under distortion (curves, perspective, overlap). Reduce each by design before relying on it: fewer, larger, simpler, more structured, plainly described. Some things cannot be reproduced and are never imitated: anything whose correctness depends on external truth (scannable or verifiable marks, supplied files that cannot be attached, a real person's likeness, an authority's mark). Capabilities change; a failure the user reports overrides this default |
| Render scale / raster floor | **Physical media:** render scale = the generator's output pixels along the format's long side ÷ the format's physical long side (px per mm). Unless the user states the generator's size, assume about 2,000 px on the long side (tagged assumption; a larger output lowers the raster floor, a smaller one raises it). Print resolution does not enter planning: an A3 print at 300 dpi is about 3,500 × 4,950 px, far more than a generator draws, so the artwork is enlarged afterward and what must hold is the drawing at the generator's own pixels. **Screen media:** the deliverable's pixel size is the medium and its physical size is the device's, so the displayed reduction (image width ÷ displayed width) turns the smallest readable on-screen font size (about 11 to 12 px for sustained text, about 9 to 10 px for brief reference text, tagged assumptions) into the size needed in the image. **Raster floor:** exact text is reliable at a cap height of about 14 px or more and begins to garble below about 10 px (tagged assumptions); in mm it is that pixel height ÷ render scale (A3 at about 2,000 px: about 2.9 mm, 0.7% of the height; at about 1,500 px: about 3.9 mm, 0.9%). The generator reads size only as proportion to the picture, so every size is finally stated as a share of the format |
| Rendering risk | Mandatory text or a form in the at-risk band that design cannot reduce further (shorter lines, larger size, simpler grouping, clearer structure). Mitigate by design first, then tell the user once in the notes what to check in the result |
| Volume risk | Mandatory content that the fit ladder could not fit at its role floors inside the space plan. Kept in full and reported once in the notes with the way out (a larger format, less text, or a second deliverable) |

## Quality checks

- One meaning per term in every file; a term is used only with the meaning given here.
- Only terms used in more than one file are defined here; single-file terms are defined where used.

## Next

Read `scope_roles_and_depth.md` (if not yet read), then `01_brief_and_requirements.md`. Read `terms_design_system.md` on entering Phase 3.
