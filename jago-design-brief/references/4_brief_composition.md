# Phase 4: compose the brief

**Needs:** S, the analysis record, the direction record. **Produces:** one design brief per image, then the final reply (`5_delivery_and_revision.md`). Synthesis is translation, not invention: if composing needs a new concept, return to Phase 3.

## 1. Sort every decision by owner
Walk S and the direction record once. Each decision lands in one class and is stated once, in that class's form.
| Class | What belongs | Stated as |
|---|---|---|
| **Fixed** | the user's facts, exact text, assets (with fidelity), named preferences, format, exclusions, what must be preserved | a requirement, precise and complete: "must", exact quotes |
| **Directed** | the skill's decisions that carry the result: the idea, style lineage and traits, hero truth, hierarchy and grouping relations, boundaries, a new mark's device | intent plus a few defining traits, labeled as decided direction: "follow this idea; the execution is yours" |
| **Recommended** | color roles, type voice, balance, supporting-visual stance | a preference with latitude: "prefer…; adapt if a better solution serves the same aim" |
| **Open** | placement and composition detail, sizes, spacing, type pairing, lighting, decorative treatment and count, supporting detail, the wording of ChatGPT's own prompt | named in one line, or simply omitted |
**Necessity test** (applies to every Directed and Recommended item): if this were left open, would ChatGPT's likely choice harm the objective, a stated quality, the truth of the content, or distinctiveness? If not, delegate it. If yes, state the least that prevents the harm: the intent and the traits that make it recognizable, never an exhaustive description. A skill preference is never worded as the user's requirement: the user must be able to tell what they decided from what was proposed.

## 2. Anatomy of the brief
Outcome first, constraints second, aesthetics third. Use natural headings in the user's language; include only what applies.
```
[Request]      Create a [kind of image] for [subject] to [purpose]. Format: [orientation, ratio]; [where it will be used].
[Must appear]  The exact text, in quotes, each line with its role and reading tier. Nothing else is written.
[Context]      Who it is for, where and from what distance it is seen, what surrounds it, what it must achieve.
[Impression]   What it should feel and communicate, in the user's own qualities; add what each looks like only where it could be misread.
[Fixed]        Assets and their fidelity; reference roles and priorities; exclusions; what to preserve.
[Direction]    Decided: the idea; the look (traits); the hero; color stance; type voice; what leads and how content groups;
               supporting visuals allowed; what the piece must never become (as positives).
[Open]         What you decide: composition and placement, sizes, spacing, type pairing, lighting, decorative detail.
[How to work]  Understand the objective before choosing visuals. Explicit requirements outrank the decided direction, and the direction
               outranks your defaults; anything marked open is yours. Invent no facts, text, or decoration without a purpose.
               Do not ask questions: decide, then generate.
```
- **Core** (Request to Fixed) is always present. **Precision** (reference map, fidelity, tiers, grouping, density note) appears only when the task needs control. **Direction** appears as far as the openness map and the analysis decided it; a Fixed direction decision moves to the Fixed section.
- A complete, simple user brief may need only a few sentences plus the direction's essentials: say less, not more.

## 3. Writing rules
1. **Voice:** the owner's request to ChatGPT, in natural prose with short lists. No commentary about the skill, no rationale beyond one clause where a reading could go wrong.
2. **Intent before execution.** Qualities carry a visible form only where the word is ambiguous; never stack adjectives (a competing or repeated adjective dilutes the rest).
3. **Positive wording.** Describe what success looks like; keep a short list of real exclusions and of failures that are likely and costly (extra text, invented marks, a generic look the boundaries name).
4. **Relations, not placement.** State the order of attention (first read, second, third), groups by job, what belongs with the hero, and where space should stay open. No coordinates, regions, millimeters, pixels, or percentages of layout. Permitted numbers: the format and ratio, viewing distances, counts that matter (exactly two offers), and relative statements ("prices read second after the headline").
5. **Verbatim block:** every mandatory line whole, in quotes, with role and tier (reads at distance / read while approaching / read up close). Add "use exactly this text; do not add, translate, or correct anything". ChatGPT chooses line breaks; the skill does not split a string unless the user did.
6. **Density note** (only for a dense verdict): "This is text-heavy. Group it into a few clear clusters, keep every line, keep [core items] comfortably readable from [distance], let [reference items] be smaller, and never distort letters to fit." No sizes.
7. **References and assets:** a reference map (what each is for, what to take, which wins on conflict) and the fidelity level of each asset; a supplied logo or character is reproduced, never redesigned.
8. **Specificity:** depicted things by their true specifics, not category names; lineage and traits, not medium words. Color by named hue with its role and intensity (the calm field, the sparing accent), never only a hue list.
9. **Length follows need.** The brief grows through verbatim content and real constraints, not through added direction. Typically 200 to 450 words besides the verbatim block; beyond about 600, cut Recommended first, then Directed, never Fixed.
10. **Several images:** one standalone brief each; the shared direction is repeated word for word; each brief names its own format and purpose and never refers to another brief or an earlier generation.
11. **Editing an image the user supplies:** state what changes, what must stay identical, where, and how the change integrates with the rest.
12. **Language:** the user's language (see `1_intake.md`); verbatim strings unchanged.

## 4. Self-check (once, before delivery)
1. **Meaning preserved:** every ledger requirement is present with its priority; none is downgraded; nothing Directed or Recommended reads as the user's requirement.
2. **Necessity:** each Directed and Recommended sentence survives the test in §1; the rest is deleted or moved to Open.
3. **Coherence:** no contradiction, no competing adjectives, no decision stated twice; exactly one first read.
4. **Verbatim:** every string matches the ledger's whole line, punctuation included; no extra text is invited.
5. **Truth:** no invented fact, claim, contact, date, or mark; no placeholder.
6. **Form:** no layout numbers; standalone; within the length rule.
A failure returns to the earliest responsible decision (a missing requirement to Phase 1, an unclear direction to Phase 3).

## 5. Prescription dial (set by feedback only)
**Standard** (default): Fixed, Directed, and Recommended as above. **Lean:** Fixed and Directed only, for users who report that ChatGPT does well with little or that the direction constrained it. **Firm:** adds explicit defining traits for an item ChatGPT ignored. The dial moves one notch at a time, only on evidence from a generated result, and the change is recorded.
