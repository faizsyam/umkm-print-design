# Phase 1: Brief and Requirements

## Contents
1. Purpose and scope
2. What to extract
3. Classifying content
4. Assessing completeness and ambiguity
5. The clarification protocol
6. Inference rules
7. Fixed assets and multi-face pieces
8. Failure modes
9. Completion criteria and hand-off

## 1. Purpose and scope

Convert whatever the user wrote, which may be a single casual sentence or a detailed specification, into a **Brief Ledger**: an organized, provenance-tagged account of what is known, what is inferred, what needs investigation, and what is genuinely uncertain. This phase decides *what is true and required*. It does not decide what the design should look like.

Indonesian briefs are often informal, mix Indonesian with regional or colloquial terms, and may describe the piece by its everyday name rather than its specification. Interpret generously, but never rewrite the user's own text.

## 2. What to extract

### A. Print medium and context
- Physical piece and format; single face or multiple faces/panels; folds or assembly.
- Dimensions and aspect ratio. If only a common name is given, infer the conventional proportions and tag them *inferred*.
- Purpose and communication objective, as the user understands it.
- Placement and viewing environment: indoors or outdoors, mounted, handheld, on a product, on a counter, on a wall, on a vehicle.
- Viewing distance, orientation, dwell time, lighting, weather or handling exposure.
- Production constraints that are known: material, finish, color limitation, quantity, budget tier, printer capability.

### B. Business and brand
- Name, industry, products and services, operating context (location type, scale, channel: physical, online, marketplace, event).
- Target audience as described.
- Stated differentiators and positioning.
- Existing visual identity: logo, colors, fonts, mascots, previous materials, signage already in place.

### C. Content
Everything that must or may appear: logo and identifiers, headline and body text, product names, descriptions, tagline, promotions, calls to action, prices, menus, variants, offers, trust indicators, contact details, social handles, addresses, operating hours, payment or ordering information, legal or certification marks.

### D. Preferences and constraints
Style, color, mood, theme, references, existing assets, taboos, religious or cultural sensitivities, explicit exclusions, and anything the user said they dislike. Treat a reference image or reference description as evidence of taste, not as a template to reproduce.

### E. Intent signals between the lines
Note the register of the request (formal, playful, price-driven, aspirational), what the owner emphasized or repeated, and what they conspicuously omitted. These guide inference but are never promoted to facts.

## 3. Classifying content

For every content item assign two labels.

**Necessity**
- *Mandatory*: the user said it must appear, or the piece cannot do its job without it.
- *Optional*: the user offered it, or it would help, but the piece survives without it.
- *Excluded*: the user said not to include it.

**Provenance**: given, fixed asset, inferred, researched, creative choice.

Rules:
- **Verbatim preservation.** Keep spelling, capitalization pattern, punctuation, numerals, price formatting, phone number grouping, handle spelling, and non-standard brand spellings exactly as given. Do not normalize, translate, or "correct." If something looks like a typo, preserve it and flag it in a note outside the prompt.
- **No fabrication.** Missing content is either left out or requested. Never fill a gap with plausible filler: invented taglines presented as the brand's own, made-up prices, fake reviews, unverified certifications, or unsupported superlatives.
- **Generated copy is a creative choice.** Functional labels derived directly from supplied content (a section heading for a group of items the user listed) are always acceptable. A headline, tagline, or descriptor the user did not supply may be written only when the piece cannot do its job without one or the user asked for copy; keep it factual, modest, and free of claims, tag it *creative choice*, and mention it in the outside note. Otherwise omit it.
- **Regulated or trust marks** (halal status, food-safety registration, health claims, official numbers) appear only when the user provides them. Their presence is a fact claim.

## 4. Assessing completeness and ambiguity

Sort every gap into one of four bins.

| Bin | Meaning | Action |
|---|---|---|
| Explicit | Stated by the user | Record verbatim |
| Inferable | Reliably deducible from the brief or common practice for the medium | Infer, tag, move on |
| Researchable | Discoverable externally and relevant to a decision | Investigate in Phase 2 |
| Materially uncertain | Missing, cannot be researched, and would change the design | Candidate for clarification |

A gap is **blocking** only if guessing wrong would waste the generation or mislead the audience. Typical blocking gaps: the business name when it must appear and cannot be found; the core product or offer when the piece exists to promote it; the physical format when it changes composition fundamentally and cannot be inferred; the content of a price list or menu the user wants reproduced; whether an existing logo must be used.

Typical non-blocking gaps: exact color preferences, mood, fonts, secondary details, optional contact channels. Decide these through analysis.

## 5. The clarification protocol

1. Resolve everything inferable or researchable first. Questions that analysis can answer are a failure of diligence.
2. If blocking gaps remain, ask in one message, at most three questions, written in the user's language, concise and non-technical.
3. For each question, state what you will do if it goes unanswered (a default, or omission of the item when no honest default exists, as with a business name or price), so the user can reply with a single word.
4. Do not ask about aesthetics the user cannot reasonably articulate. Make those decisions yourself.
5. If the user indicates they want immediate output, or has already declined to answer, proceed on defaults and mention consequential assumptions in the outside note.
6. After one round of questions, do not ask again unless the answers reveal a new blocking gap.

## 6. Inference rules

Infer boldly where the evidence is strong and the cost of error is low; infer cautiously or not at all where the claim would appear to the public as a business fact.

- Infer *format behavior* (reading distance, orientation, typical hierarchy demands) from the medium.
- Infer *audience and tone* from products, price points, channel, and the user's own language, but keep it provisional until Phase 2.
- Do not infer *facts the customer will read as promises*: ingredients, guarantees, discounts, delivery coverage, hours, origin claims.
- When two interpretations of an ambiguous phrase are both plausible and lead to materially different designs, treat it as a clarification candidate; if not blocking, choose the interpretation best supported by the rest of the brief and tag it.

## 7. Fixed assets and multi-face pieces

**Logo and identity supplied by the user.** Treat as fixed. Record what can be seen or described: structure, colors, typographic character, relationship between symbol and wordmark. Phase 4 must design around it. If the target model cannot ingest reference images, the prompt must describe the logo faithfully enough to reproduce its essential structure; if that is unrealistic for a complex logo, say so in the outside note rather than inventing a replacement.

**Supplied photos or product images.** Record what they show and what they must be used for. They influence imagery decisions but are not automatically the hero.

**Multi-face or multi-piece requests.** Record the shared elements (identity, content that repeats) and each face's distinct job and content. Do not merge faces into one overloaded composition.

## 8. Failure modes

| Failure | Detection | Correction |
|---|---|---|
| Interrogating the user | Questions answerable from the brief or by research | Delete them; resolve yourself |
| Silent consequential assumption | A decision depends on an untagged guess | Tag it; if blocking, ask |
| Content drift | Text in the ledger differs from the user's | Restore verbatim |
| Brief inflation | Ledger contains "facts" the user never stated | Remove or retag as inferred/creative |
| Missing the real objective | Ledger lists content but not what the piece must achieve | Restate the objective before proceeding |
| Preference treated as constraint | A taste hint recorded as mandatory | Reclassify as preference |

## 9. Completion criteria and hand-off

Phase 1 is complete when:
- Medium, format, viewing context, and objective are recorded (inferred where necessary and tagged).
- Every content item is classified by necessity and provenance, with mandatory content captured verbatim.
- Fixed assets and exclusions are explicit.
- Blocking gaps are either answered, defaulted with the user's implicit consent, or have been asked.
- Non-blocking gaps are assigned to Phase 2 (research or analysis) or to creative decision.

Hand-off to Phase 2: the Brief Ledger, a short list of research questions that could change a decision, and a list of unresolved tensions noticed in the brief.
