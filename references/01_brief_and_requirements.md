# Phase 1: Brief

## Phase card

| Item | Content |
|---|---|
| Professional analogue | Client intake: an account lead who captures everything, verifies it, never guesses facts |
| Goal | A complete, classified, verifiable record of what is known, required, and uncertain, so no later phase guesses or invents |
| Receives | User message, attachments (logos, photos, references), prior conversation; for a revision, the prior design state. No earlier phase |
| Principles in force | **8 Fidelity to the brief** (mandatory content verbatim, exclusions honored, nothing invented, fixed assets untouched); **3 Evidence-informed judgment** (provenance on every item; fact apart from inference); **10 Effort follows impact** (ask only about gaps that would change the design); **1 Whole-system thinking** (record item interactions, incl. content volume vs physical area) |
| Exploration protocol | N/A: this phase records and classifies. An ambiguous phrase takes the interpretation best supported by the rest of the brief, tagged |
| Required decisions | Necessity and provenance of every item; verbatim form of every mandatory string; gap class of every gap and which are blocking; quality translation of every stated quality and priority; ledger or clarification questions; the depth (`SKILL.md` section 8) |
| Outputs | Brief Ledger (incl. quality requirements with translations); research questions that could change a decision; tensions. Then the guided intake (`00_conversation_ux.md` section 3): questions, preference check, compact summary the user confirms together with the mode. No later phase runs before that |
| Before leaving | Could a colleague design from the ledger without the original message? Every mandatory string exact? Every item has necessity, provenance, referent; fixed assets and exclusions listed; no unsourced fact? Every stated quality and priority, however vague, has a translation (visual targets, carriers, contradicting signals)? Intake within question limits, every question with example or default, none answerable from the brief? Summary and mode confirmed? Print designer's objection raised and resolved? |


## 1. Process

1. Read everything given, including attachments; list what each contributes.
2. Capture the print medium and context (A); infer what is missing and tag it.
3. Capture the business and brand (B).
4. Capture and classify the content (C): necessity, provenance, verbatim form, referent, volume relative to the area.
5. Capture preferences, fixed assets, exclusions, sensitivities (D). Treat references as evidence of taste, not templates. Record every stated quality and priority and translate it (D).
6. Sort every gap into its class (E). Infer the inferable (tagged), pass the researchable to Phase 2 as research questions, ask about blocking and valuable gaps through the guided intake.
7. Note tensions visible in the brief; set the depth.
8. Pass the gate (`quality_control.md`): the print designer's required objection asks whether medium, size, material, and viewing conditions are captured well enough to design for.
9. Show the compact summary, ask for confirmation and the mode, and wait; corrections update the ledger and show only the changed rows. Once confirmed, create the Design Log (`SKILL.md` section 5).

## 2. Detailed guidance

### A. Print medium and context
Capture: medium and format; single or multiple faces; dimensions, aspect ratio, physical area; purpose and communication objectives; placement and viewing environment; viewing distance, orientation, dwell time, visibility, lighting, exposure; production constraints (material, finish, color limits, budget tier, quantity).

If the setting is not stated, infer the most probable one, tag it inferred, and pass it to Phase 2. Ask only if the plausible settings would need opposing designs. Physical area is a design input: record it next to content volume, since their relation drives later density, space, and scale decisions.

### B. Business and brand
Name and industry; products and services; operating context; target audience; differentiators; brand identity, positioning, existing visual identity. Record what the user said, not what the category usually implies.

### C. Content
Capture all content that must or may appear: logo and brand identifiers, primary and secondary text, product and service names, descriptions, taglines, promotional messages, calls to action, prices, menus, variants, offers, trust indicators, contact details, social media, addresses, supporting information.

For each item record: the exact string, necessity, provenance, referent (the business, the offer, the main subject, a specific part of the subject, or an action), its face, and its approximate share of content volume.

- **Preserve verbatim:** spelling, capitalization, punctuation, numbers, price and contact formatting, names, non-standard brand spellings. A suspected typo is preserved and flagged for the notes.
- **Never fabricate** prices, claims, testimonials, certifications, regulated or trust marks, contacts, ingredients, years in business, or statistics. Regulated or trust marks appear only when the user provides them.
- **Supplied codes.** A QR, QRIS, or barcode is a fixed asset: record it as attached, with the size it needs to scan. Never imitate one.
- **Supplied visual material and given structure.** Record supplied images, depicted people, mascots or characters, and platform handles as fixed assets, with what is fixed about each and whether permission to show a depicted person is known. Record whether the user wants a figure (mascot, character, or person) created, and what it should represent or do; an unmentioned figure is not assumed and may be offered once as a suggestion. Record any structure the content already has (a sequence, levels, rows pairing an item with a value, several contact channels); later phases may express structure visually only from what is given.
- **Generated copy.** Functional labels derived from supplied content are acceptable. A headline, tagline, or descriptor the user did not supply is written only when the piece cannot function without one or the user requested copy; keep it factual and modest, tag it creative choice, flag it in the notes.
- **Necessity judgment.** Mandatory if the user said it must appear or the piece cannot work without it; optional if offered or helpful; excluded if the user said to leave it out. When unsure, treat it as mandatory: ask once in intake if the answer would change content volume; otherwise it stays mandatory and Phase 5 fits it by demotion or grouping, never omission.

### D. Preferences and constraints
Style, color, mood, theme, references, existing assets, exclusions, cultural or religious sensitivities. A supplied reference shows taste: extract what the user responds to (structure, tone, density, material), never reproduce it. List fixed assets with exactly what is fixed (a logo's form and color; a palette's values; a typeface). For a supplied logo image, record form, construction, and colors precisely so Phase 6 can reproduce it by description if the model cannot take image input.

**Quality requirements (binding).** Every experiential, tonal, affective, or priority statement, and every style, color, or technique the user names ("calm", "premium", "playful", "trustworthy", "the brand comes first", "easy to scan"), however brief or vague, is recorded in the user's own words. A minimal brief makes these the primary requirements; it is not an absence of requirements. For each, write the **quality translation**:
1. The visual targets it implies, in specialist terms: value key (high, mid, low), chroma, temperature, density, formality, warmth and approachability, hierarchy priority, sensory cues.
2. Two to four **quality carriers**: visible features that deliver it, from color and value key, shape language, surface, imagery, type treatment, and spacing.
3. The contradicting signals (dominant dark masses contradict "light and airy"; dense small type contradicts "easy to scan").

A quality about the whole piece constrains its dominant field and largest masses, not only an accent. Qualities that pull apart ("refined" and "approachable") are recorded as a pair, with a carrier for each side. Ambiguous words are interpreted by the rest of the brief and tagged.

### E. Completeness, ambiguity, and clarification

**Sort every gap**
- **Explicit:** record it.
- **Inferable:** infer and tag.
- **Researchable:** pass to Phase 2 as a research question naming the decision it could change; drop it if it changes none.
- **Materially uncertain:** missing, not discoverable, would change the design. If a wrong guess would waste the generation or mislead the audience, it is a **blocking gap**: its answer would change which face carries the message, whether mandatory content exists at all, or whether the piece can physically contain the content.

**Resolve**
- Noncritical ambiguity: informed interpretation, tagged.
- Business facts: never invented.
- A missing aesthetic preference is never blocking; Phase 3 decides it. A vague quality statement is not a missing preference but the requirement; D translates it.

**Clarify** (guided, never an interrogation; rules in `SKILL.md` section 11 and `00_conversation_ux.md` section 3)
- Blocking gaps must be asked; valuable gaps (answers that would change story, setting, content, or look) are asked through the guided intake.
- Do not ask what can be derived or investigated.

## 3. Failure modes

| Failure | Detection | Correction |
|---|---|---|
| Interrogating the user | More than three questions per message or three discovery messages, or a question the brief or research could answer | Cut to the highest-value gaps; infer and tag the rest |
| Suggestion treated as fact | A suggested item sits in the ledger as user-provided | Mark it a suggestion; keep it out until confirmed |
| Moving on unconfirmed | Phase 2 began before the user confirmed the summary | Show the summary and wait |
| Silent normalization of text | A mandatory string differs from the user's in spelling, case, numerals, or formatting | Restore verbatim; flag suspected typos in notes |
| Invented fact | An item with no provenance, or provenance "inferred" for a price, claim, mark, or contact | Remove it, or ask if blocking |
| Reference treated as template | The ledger records a reference's layout as a requirement | Re-record as taste evidence only |
| Missing area or volume | No physical area or content count recorded | Capture or infer and tag; Phases 3 and 5 need it |
| Fixed asset altered in the record | A logo or palette described as "to be improved" | Restore as fixed; flag only if the user asked for change |
| Supplied visual material unrecorded | An image, depicted person, character, or handle used or implied without being listed as a fixed asset | Record it with what is fixed, or drop the use |
| Setting left unstated | No setting, not even inferred | Infer the most probable setting; tag it provisional |
| Skipping the phase because the brief is simple | No ledger exists | Write a short ledger; simplicity shortens it, never removes it |
| Vague request read as no requirement | A brief of mood words yields no recorded qualities, or style is left wholly to later phases | Record each word as a quality requirement and translate it |
| Quality dropped or paraphrased away | A stated quality is missing or reworded into something weaker | Restore the user's words and the translation |

## 4. Completion criteria and hand-off

Complete when the phase card's "Before leaving" check holds. Phase 1 ends with the compact confirmation summary, not a phase entry; Phase 2 starts only after the user confirms. Update the Design Log with content volume against area, fixed assets, exclusions, and open issues.

**Hand-off to Phase 2:** the Brief Ledger (every item classified, with quality translations), research questions (each naming the decision it informs), tensions noticed, the inferred setting if any, and the depth.