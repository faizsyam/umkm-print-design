# Glossary part 1: inputs, records, qualities, context, decisions, reliability (Phases 1 to 6)

One meaning per term for the brief, the analysis, the exploration protocol, and renderability and risk. Terms used for the design system are in `terms_design_system.md`.

**Read this when:** at the start of Phase 1 (before the first user message is answered); reopen a row whenever a term's meaning is in doubt.

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
| Design Log | The persisted state record (`workflow_and_state.md` section 4): the standing block **S**, one **Forward block** per phase (decisions as specifications, carry-forward obligations, open flags), and the **Record** (candidates, reasons, objections, rejected directions, research), which never travels forward |
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
| Legibility minimum | The smallest size at which a tier is read at its stage's reach in the real material, light, and contrast. Legibility is angular: required letter height grows in direct proportion to the distance at which it is read (for an image on a display, the display's size and the viewer's distance from it). Derive it from the stage's reach times a ratio set by conditions, never from the format or from other tiers. **Reference calibration** (sign-legibility practice, tagged as an assumption): comfortable reading of simple, high-contrast lettering needs a cap height of about 1/115 of the distance (roughly half a degree of visual angle); the bare limit for a still viewer is about a third of that. Short exposure, motion, low contrast, glare, dim light, and ornate or condensed forms raise the ratio. Exposure time also bounds how many words and groups a stage can carry. Convert each minimum to a fraction of the format's governing dimension (minimum cap height divided by the format's physical or displayed height) at the deliverable's ratio: that fraction is the tier's floor in every load and capacity check, and it shows before layout whether the format can carry the tier's content at its reach. Phase 2 computes the floors once, per stage, and records them in the Environment Profile; later phases read them and never re-derive them |
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
| Rendering risk | Mandatory text or a form in the at-risk band that design cannot reduce further (shorter lines, larger size, simpler grouping, clearer structure). Mitigate by design first, then tell the user once in the notes what to check in the result |
| Volume risk | Mandatory content that the fit ladder could not fit at its legibility minimum inside the space plan. Kept in full and reported once in the notes |

## Quality checks

- One meaning per term in every file; a term is used only with the meaning given here.
- Only terms used in more than one file are defined here; single-file terms are defined where used.

## Next

Read `scope_roles_and_depth.md` (if not yet read), then `01_brief_and_requirements.md`. Read `terms_design_system.md` on entering Phase 3.
