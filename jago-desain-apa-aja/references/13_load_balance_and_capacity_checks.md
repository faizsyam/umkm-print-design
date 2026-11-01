# Phase 5: Design Execution, part 4 of 5: load check, balance, capacity check, proportion/fill/zone checks

Check the whole composition for cumulative load and fit, measure and remedy balance, run the capacity check that freezes sizes, and test proportion, fill, and zones.

**Read this when:** after `12_hierarchy_and_element_placement.md` (every element ranked and placed); the fit ladder is read from `terms_design_system.md` (already read at Phase 3).

**Inputs needed:** The placed composition and provisional sizes from `12_hierarchy_and_element_placement.md`; the space plan and legibility minimums from `11_space_plan_and_spatial_strategy.md`; Phase 3 density level; Phase 4 counterweight.

## 2. Guidance (continued from `12_hierarchy_and_element_placement.md`)

### B5. Budget the content (item 5 of section B)

5. **Budget the content.**
   - **Per tier:** count groups and items against what the viewer can parse in that stage's time.
   - **Load check (whole composition).** Visual load is cumulative: text groups, containers and their edges, supporters, illustrations, designed treatments, rendering treatments, surface detail, and color intensity count together. Each may be justified alone yet together exceed what the budget and the stage's parsing time carry. Tally the load by category against the Phase 3 density level. The composition fits only with headroom (every item at its minimum and every gap at its tightest is not a fit) and with its quiet regions intact. Count the attention claims at each stage (elements that ask to be looked at by contrast, weight, or detail); beyond what the stage's time can parse, the lowest-ranked claims are removed or merged. Subdivide content into no more groups, containers, or repeated forms than its own structure requires.
   - **Fit ladder** and **Never, at any rung**: the full text is in `terms_design_system.md`, Fit ladder (full). Give way in its order, each rung exhausted before the next: least-purpose elements, weight of enclosure, arrangement and strategy, treatment, stage, optional content, rescaling within rank, and last the quiet share.
   - **Renderability:** mandatory text in the at-risk band (`terms_brief_and_context.md`, Renderability) is first made safer by design (shorter lines, larger size, simpler grouping); what remains is recorded as a rendering risk for the notes.

### A3. Balance

Balance is judged on the composed whole after placement. It is measured, not assumed, deliverable by deliverable (and across a spread).

- **Weight.** Estimate each element's weight as area share of the format × intensity (1 pale, low-contrast, sparse; 2 medium; 3 dark or saturated against its ground, dense, detailed), raised for isolation, a figure or face, warm saturated color, an irregular silhouette, or a heavy container fill or edge (weigh the element as drawn, content plus container). Rough values suffice. Pull grows with distance from center, so a small heavy element far out can offset a large one near the center. Empty area weighs nothing: a resting field balances only by letting heavy mass sit nearer the center.
- **Check.** Give each element coordinates x, y in [-1, 1] from the center (y positive downward); centroid X = Σ(w·x)/Σw, Y = Σ(w·y)/Σw.
  - Balanced: |X| ≤ 0.1 and −0.1 ≤ Y ≤ 0.2 (a slightly low centroid is stable; a high one is top-heavy).
  - Leaning: 0.1 < |X| ≤ 0.25 is acceptable only as the chosen asymmetric equilibrium or deliberate tension, with its counterweight named.
  - Beyond that, or outside the Y range: unbalanced.
  - A radial stance is read about its focal center.
  - The tolerances are a working heuristic on rough estimates, not a measurement; a result near a limit is settled by the cross-check: fold along each axis and squint, and the eye must not settle on one side or find one half emptier than planned.
- **Remedy, least new weight first.**
  1. Reposition or reorder existing elements: heavy mass toward the center, swap sides, shift a group axis, resize the hero within its rank.
  2. Rebalance within ranks: lighten the heavy side or strengthen the light side by intensity or area, without breaking the rank order or any weight ceiling.
  3. Deploy the Phase 4 counterweight on the light side, gaining weight from area and distance rather than intensity, linked to the composition, below every rank, never carrying required information.
  4. If the element system has none, return to Phase 4.

  Counterweights count against the element allowance and space intent. No remedy takes area from the quiet reserve or from a separation, and any addition or resize is re-checked against the space plan's shares.

### B7 and B8. Capacity check; proportion, fill, and zone checks (items 7 and 8 of section B)

7. **Capacity check (before any size is stated).**
   - **Estimate:** for each text string, width = characters × cap height × a width factor for the role's decided width class (about 0.75 to 0.9 for text faces, up to about 1.0 for heavy or wide display faces), against its inner container area after padding at the planned size, with headroom (a string that only just fits counts as not fitting, since a render short of room compresses or skews letters). Count lines against container height.
   - **On failure change, in order:** line breaks and grouping, container size or shape, tier size down to (never below) its minimum, then the fit ladder (B5; full text in `terms_design_system.md`) and, if the group still fails, the next strategy (`11_space_plan_and_spatial_strategy.md` C).
   - **Remedies act on the group or role,** never on one member: the longest member sets the group's fit, and no single member is resized, reweighted, or compressed to pass. Letterform proportions and baseline are never a remedy.
   - **Then** record final sizes and the planned wrap (line breaks) of every string that takes more than one line; the sizes and wraps recorded at this gate are the ones the prompt uses. The check runs after balance (A3).

8. **Proportion, fill, and zone checks.**
   - **Proportion:** reduce any role or group whose size sits far above its minimum without being the hero or the glance message (as a whole, never member by member). Area ratios between zones agree with rank (no secondary zone's share approaches a higher rank's), and sizes inside a zone stand in clear steps, never near-equal sizes that read as indecision.
   - **Fill test:** every quiet area has a job (rest, isolation, separation, framing the hero, or hosting the hero group's text within the A2 limit (`10_stage_assignment_and_relationship_map.md`)) or is reassigned in the plan, never filled with an item and never taken later by decoration, motif, or surface detail, which live in the zones and edges allocated to them. A uniform, tonal, or fine-grain ground runs through it; a visible pattern or ornament does not.
   - **Zone test:** each zone's internal spacing is set at its own scale and reading distance, in proportion to the text it holds. A zone whose spacing is only what remained after sizing is re-planned, by arrangement and grouping first. Content sits inside its allocated region with resting room left, never at its edges. A zone that needs more room finds it within its own content (arrangement, grouping, the fit ladder), never by taking separation from its neighbors. Open ground elsewhere never compensates for a tight zone: breathing room is checked at each zone's perimeter, between neighbors, and inside each container.

## Quality checks

**Gate checks for this step (fails if any is false):**
- Legibility minimums are respected and the fit ladder is applied in its order; no mandatory content is deleted.
- The load check passed with headroom and the capacity check passed before sizes were stated; no size changed after, and no letterform was altered to fit; remedies acted on groups, not on individual members; equivalent units share dimensions and rails.
- The quiet share narrowed only at the last rung of the fit ladder (B5).
- Balance was measured in A3 and remedied in order, with any counterweight named.

**Reminders at the point of use:**
- Visual load is cumulative: tally text groups, containers and edges, supporters, illustrations, designed and rendering treatments, surface detail, and color intensity by category against the density level; the composition fits only with headroom and with its quiet regions intact.
- Never, at any rung of the fit ladder: shrink a tier below its minimum; compress, stretch, or slant letterforms; delete mandatory content; resize one member of an equivalent group; take separation from a neighbor.
- Balance is measured (weights x coordinates, centroid), then remedied in order: reposition, rebalance within ranks, deploy the Phase 4 counterweight, else return to Phase 4.
- The capacity check runs after balance and before any size is stated; remedies act on the group or role, never on one member; record final sizes and planned wraps.

## Next

Read `14_backgrounds_review_and_gate.md`. Carry forward: the load-checked, balanced composition with final sizes and planned wraps frozen. If group-level remedies fail, return to the spatial strategy step (`11_space_plan_and_spatial_strategy.md`, C) for the next strategy; never shrink to pass.
