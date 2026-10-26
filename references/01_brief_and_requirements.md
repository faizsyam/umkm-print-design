# Phase 1: Brief

## Phase card

| Item | Content |
|---|---|
| Professional analogue | Client intake and creative briefing: an account lead who captures everything, verifies it, and refuses to guess at facts |
| Goal | A complete, classified, verifiable record of what is known, what is required, and what remains uncertain, so no later phase has to guess or invent |
| Receives | The user's message, attachments (logos, photos, references), prior conversation; for a revision, the prior design state. No earlier phase |
| Principles in force | **8 Fidelity to the brief** (mandatory content verbatim, exclusions honored, nothing invented, fixed assets untouched); **3 Evidence-informed judgment** (provenance on every item; fact apart from inference); **10 Effort follows impact** (ask only about gaps that would change the design); **1 Whole-system thinking** (record how items interact, including content volume against physical area) |
| Exploration protocol | Not applicable. This phase records and classifies; it does not choose among designs. An ambiguous phrase is resolved by the interpretation best supported by the rest of the brief, and tagged |
| Required decisions | Necessity and provenance of every item; the verbatim form of every mandatory string; the gap class of every gap; which gaps are blocking; the quality translation of every stated quality and priority; whether the outcome is a ledger or clarification questions |
| Outputs | Brief Ledger (including quality requirements with their translations); research questions that could change a decision; tensions noticed. If a blocking gap remains and the user has not signaled urgency: the clarification questions only, and no later phase runs yet |
| Before leaving | Could a colleague start designing from the ledger without reading the original message? Is every mandatory string exact? Does every item carry necessity and provenance? Is any fact unsourced? Does every stated quality and priority, however vague, carry a translation (visual targets, carriers, contradicting signals)? Are clarification questions at most three, each with a default, none answerable from the brief? Has the print designer's objection been raised and resolved? |

## Contents
1. Process
2. Detailed guidance (A to E)
3. Failure modes
4. Completion criteria and hand-off

## 1. Process

1. Read everything given, including attachments, and list what each contributes.
2. Capture the print medium and context (A). Infer what is missing and tag it.
3. Capture the business and brand (B).
4. Capture and classify the content (C): necessity, provenance, verbatim form, and volume relative to the area.
5. Capture preferences, fixed assets, exclusions, and sensitivities (D). Treat references as evidence of taste, not templates. Record every stated quality and priority and translate it (D).
6. Sort every gap into its gap class (E). Infer the inferable (tagged), pass the researchable to Phase 2 as research questions, and ask about blocking gaps under the clarification protocol.
7. Note tensions visible in the brief.
8. Pass the gate (see `quality_control.md`): the print designer's required objection concerns whether medium, size, material, and viewing conditions are captured well enough to design for.

## 2. Detailed guidance

### A. Print medium and context
Capture: medium and format; single or multiple faces; dimensions, aspect ratio, physical area; purpose and communication objectives; placement and viewing environment; viewing distance, orientation, dwell time, visibility, lighting, exposure; practical production constraints (material, finish, color limits, budget tier, quantity).

If the setting is not stated, infer the most probable setting, tag it inferred, and pass it to Phase 2. Ask only if the plausible settings would require opposing designs. Physical area is a design input in its own right: record it next to content volume, because the relation between the two drives density, space, and scale decisions later.

### B. Business and brand
Name and industry; products and services; operating context; target audience; differentiators; brand identity, positioning, existing visual identity. Record what the user said, not what the category usually implies.

### C. Content
Capture all content that must or may appear: logo and brand identifiers, primary and secondary text, product and service names, descriptions, taglines, promotional messages, calls to action, prices, menus, variants, offers, trust indicators, contact details, social media, addresses, supporting information.

For each item record: the exact string, necessity, provenance, the face it belongs to, and its approximate share of the content volume.

- **Preserve verbatim:** spelling, capitalization, punctuation, numbers, price and contact formatting, names, non-standard brand spellings. If something looks like a typo, preserve it and flag it for the notes.
- **Never fabricate** prices, claims, testimonials, certifications, regulated or trust marks, contacts, ingredients, years in business, or statistics. Regulated or trust marks appear only when the user provides them.
- **Generated copy.** Functional labels derived from supplied content are acceptable. A headline, tagline, or descriptor the user did not supply is written only when the piece cannot function without one or the user requested copy; keep it factual and modest, tag it creative choice, and flag it in the notes.
- **Necessity judgment.** Mark an item mandatory if the user said it must appear or the piece cannot work without it; optional if offered or helpful; excluded if the user said to leave it out. When unsure whether something is mandatory, treat it as mandatory until a later phase triages it under the rules in Phase 5.

### D. Preferences and constraints
Style, color, mood, theme, references, existing assets, exclusions, cultural or religious sensitivities. A supplied reference shows taste; extract what the user responds to (structure, tone, density, material) and never reproduce the reference. Fixed assets are listed with exactly what is fixed about each (a logo's form and color; a palette's values; a typeface). For a supplied logo image, record its form, construction, and colors precisely, so that Phase 6 can reproduce it by description if the model cannot take image input.

**Quality requirements (binding).** Every experiential, tonal, affective, or priority statement ("calm", "premium", "playful", "trustworthy", "the brand comes first", "easy to scan"), however brief or vague, is recorded in the user's own words as a quality requirement. A minimal brief makes these the primary requirements; it is not an absence of requirements. For each, write the **quality translation**:
1. The visual targets it implies, in specialist terms: value key (high, mid, low), chroma, temperature, density, formality, warmth and approachability, hierarchy priority, sensory cues.
2. Two to four **quality carriers**: visible features that will deliver it, drawn from color and value key, shape language, surface, imagery, type treatment, and spacing.
3. The contradicting signals (for example, dominant dark masses contradict "light and airy"; dense small type contradicts "easy to scan").

A quality about the whole piece constrains its dominant field and largest masses, not only an accent. Qualities that pull apart (for example "refined" and "approachable") are recorded as a pair, with a carrier for each side. Ambiguous words are interpreted by the rest of the brief and tagged.

### E. Completeness, ambiguity, and clarification

**Sort every gap**
- **Explicit:** stated. Record it.
- **Inferable:** reliably deducible from the rest of the brief. Infer and tag.
- **Researchable:** discoverable externally. Pass to Phase 2 as a research question, naming the decision it could change; drop it if it changes none.
- **Materially uncertain:** missing, not discoverable, and would change the design. If a wrong guess would waste the generation or mislead the audience, it is a **blocking gap**.

**Resolve**
- Noncritical ambiguity: informed interpretation, tagged.
- Business facts: never invented.
- A missing aesthetic preference is never blocking; Phase 3 decides it. A vague quality statement is not a missing preference: it is the requirement, and Section D translates it.
- A gap is blocking when its answer would change which face carries the message, whether mandatory content exists at all, or whether the piece can physically contain the content.

**Clarify (blocking gaps only)**
- Ask once, in the user's language, at most three questions.
- State, for each, the default that applies if unanswered (or the omission of the item when no honest default exists).
- Do not ask what can be derived or investigated.
- If the user signals urgency, proceed on the stated defaults and flag consequential assumptions.

## 3. Failure modes

| Failure | Detection | Correction |
|---|---|---|
| Interrogating the user | More than three questions, or a question the brief or research could answer | Cut to blocking gaps; infer and tag the rest |
| Silent normalization of text | A mandatory string differs from the user's in spelling, case, numerals, or formatting | Restore verbatim; flag suspected typos in notes |
| Invented fact | An item with no provenance, or provenance "inferred" for a price, claim, mark, or contact | Remove it, or ask if blocking |
| Reference treated as template | The ledger records a reference's layout as a requirement | Re-record as taste evidence only |
| Missing area or volume | No physical area, or no content count, recorded | Capture or infer and tag; it is needed in Phases 3 and 5 |
| Fixed asset altered in the record | A logo or palette described as "to be improved" | Restore as fixed; flag only if the user asked for change |
| Setting left unstated | No setting, not even inferred | Infer the most probable setting and tag it provisional |
| Skipping the phase because the brief is simple | No ledger exists | Write a short ledger; simplicity shortens it, never removes it |
| Vague request read as no requirement | A brief of mood words yields no recorded qualities, or the style is left wholly to later phases | Record each word as a quality requirement and translate it |
| Quality dropped or paraphrased away | A stated quality is missing from the ledger or reworded into something weaker | Restore the user's words and the translation |

## 4. Completion criteria and hand-off

Complete when the phase card's "Before leaving" check holds. Phase 1 is not summarized to the user; print no decision-summary entry. Update the Design Log with the content volume against area, fixed assets, exclusions, and open issues.

**Hand-off to Phase 2:** the Brief Ledger (every item classified, with quality translations), the research questions (each naming the decision it informs), the tensions noticed, and the inferred setting if one was inferred.