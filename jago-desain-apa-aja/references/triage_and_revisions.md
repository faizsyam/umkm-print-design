# Triage, routing, and revision requests (all phases)

How a failure is classified (critical, major, minor), which phase owns each symptom, the routing rules for returns, and how a revision request re-enters the workflow.

**Read this when:** when any gate check, cross-phase test, or audit fails, when a defect is found late, or when the user asks for a revision after delivery.

**Inputs needed:** The failed check or the user's revision request; S and the Forward blocks of the phases being re-entered.

## 4. Triage and routing

| Severity | Definition | Action |
|---|---|---|
| Critical | Violates a non-negotiable; mandatory content missing or altered; fixed asset altered; invented fact; a required decision never made | Stop; return to the responsible phase; re-run forward; release blocked |
| Major | Fails a gate check, a test, or the audit; generic, context-blind, or filled; the mark absorbed by type | Return to the earliest responsible decision; re-run forward |
| Minor | Weak phrasing; a redundant clause; a small imbalance | Fix in place without altering earlier decisions |

**Symptoms by responsible phase**

- **Phase 1:**
  - wrong, missing, or altered content; unsourced fact;
  - a quality missing from the ledger;
  - a deliverable or format missing, wrong, or needlessly split;
  - a content load too heavy for the stated format absorbed silently instead of raised.
- **Phase 2:**
  - unsupported narrative;
  - environment-blind profile;
  - a medium convention applied by default;
  - weak inventory;
  - information groups missing, taken from a template, or from the order of the user's list.
- **Phase 3:**
  - generic idea, style, or hero (an image-making language that is only a medium name included);
  - a hero left standalone with no stated reason;
  - no space budget (a quiet share without role allocations, or a plan that fits only with every item at its minimum); density or treatment vocabulary left unstated; a budget set from rank alone without the information groups; no decoration stance, or plainness left undecided;
  - tension unresolved.
- **Phase 4** (Phase 3 if the plan caused it):
  - containers that all share the model's default form or only solid-or-outline fills, or one container design across different information roles or ranks (Phase 3 if the plan set no corner and edge geometry); containers with no material impression or relation to the hero or group they hold where integration was the plan;
  - an element or container with no purpose line;
  - weak or styled-name mark; clashing color or type; value-key drift;
  - ranked text left as scaled plain type; roles that differ only by size; plain-set voice copy; an item Phase 5 promoted to first or second rank with no treatment decision;
  - indistinguishable type roles or undecided letterform proportions;
  - blank or category-generic piece at its density (Phase 3 if no character carriers were planned);
  - text-only look; a ground left uniform without a reason; a theme whose world is unrealized with no recorded decision; supporters chosen without an information job; a generic symbol interchangeable between subjects or repeating the words beside it;
  - decoration with no deficit; duplicate purposes; decoration outranking information;
  - a second identifier; an unwanted, roleless, or inconsistent figure; an invented level mark;
  - element costs over the structure-and-decoration line, or a cumulative load that outgrows the density level; containers multiplied where spacing would serve; a counterweight or character carrier added as a new element while an existing one could serve; decorated ground counted as quiet; rendering treatments outside the vocabulary; a personality device that costs the name's legibility.
- **Phase 5:**
  - hierarchy: competing elements or unclear first read; poor hierarchy; an element whose recorded effect does not register at its stage; a zone's area share or a secondary or utility text mass outranking its rank; a container or treatment lifting a secondary element into a higher rank's salience; a reading sequence that contradicts the placement;
  - scale and space: every tier enlarged in a large format; crowding or filling; a zone crowded at its own scale; cumulative visual load beyond what the space plan carries; quiet that is leftover slivers, decorated, or parked in one band while zones are tight; an element sized by its own wish rather than its group's share; regions or area shares fixed before the groups' space needs were derived; a composition forced into pre-partitioned zones; free ground left as leftover instead of planned; the quiet share narrowed before the earlier rungs of the fit ladder;
  - composition: overlap hiding an essential part; unlinked elements; lopsided mass (Phase 4 if no counterweight was provided); wrong encounter stage; mark absorbed in composition; a deliverable composed by resizing or cropping another's layout; near-touching neighbors with no decided gap or overlap; a strategy locked in that the content cannot fill comfortably;
  - text fit: text overflowing its container, sizes changed late, or letters compressed, stretched, or slanted to fit; equivalent items typeset differently by length;
  - grouping and arrangement: picture-with-captions or a field of separate labels; supplementary information set as one row or container per item by default; a hero isolated while the information that supports it sits apart; parallel claims merged into one statement without being one claim; one arrangement form repeated across groups of different function, or a long or comparable-item list left as one stacked column without a reason; equivalent cards or rows whose dimensions or internal alignment vary with their content length;
  - edges and references: bleed against content; a pointer with no referent; a figure covering information.
- **Phase 6:**
  - rationale in the prompt; vague wording; mandatory text misplaced;
  - space, proportions, or ground character not stated; quantities of repeated forms unstated; an ordering word that contradicts a position word; partition words where the design has no such form; atmosphere fields not stated apart from the quiet;
  - a prompt that depends on another prompt, omits shared identity, or lacks its label.
- **The earliest contradicting phase:** a stated quality contradicted by a decision.
- **The phase that should have realized it:** a carry-forward obligation realized by no element, placement, or accepted-cost record.

**Routing rules**
- When several causes are possible, choose the earliest. Fixing a symptom later while its cause stands is a patch and is not permitted.
- Cap each issue at two revision cycles, then take the best available resolution and record it. An issue recurring after two cycles has an upstream cause.
- A returned phase keeps all unaffected decisions; record changes in the log.
- After any change, re-run the contradiction scan and the checks the change touches, and confirm no earlier text still states the old decision (nothing stale).

## 10. Revision requests

- **Re-entry point.** Re-enter at the earliest affected phase:

  | Change | Re-enter at | Set to stale (`workflow_and_state.md` section 4) |
  |---|---|---|
  | content, deliverables, format, or ratio | Phase 1 | S and every later log item that reads it |
  | audience, setting, medium, or reading conditions | Phase 2 | Phases 3 to 6 items that read the profile, encounter, or message |
  | concept, mood, style, hero, mark role, space intent, or density | Phase 3 | Phase 4 to 6 items that read the changed decision |
  | color, value key, type, copy treatment, mark, lockup, supporters, containers, or ground | Phase 4 | Execution Specification items that name the element; Phase 6 prompts that carry it |
  | arrangement or emphasis | Phase 5 | the affected deliverable's Execution Specification and prompt |
  | wording only | Phase 6 | the affected prompts |

  A request that spans several rows re-enters at the earliest row. A request that fits no row is traced with the symptom list above.

- **Scope.** Set the stale flags first. Unaffected decisions stay settled. Read S and the Forward blocks of the re-entered and dependent phases (Records only where the return rule needs them), and the files of those phases plus the cross-phase files their routing rows name.
- **Rework.** Redo, in order, the decisions that read the changed one (`workflow_and_state.md` section 3 map). Tell the user briefly what is being redone and show only what changed, in a short Before | After table in the user's language.
- **Checks.** Re-run only the design checks the change touches, plus the contradiction scan and any quality whose carrier changed. The prompt audit always runs in full on every fresh prompt.
- **Feedback** at any confirmation takes the same route.
- **Delivery.** A fresh complete prompt for each deliverable whose content changed; name the ones that did not.

## Quality checks

- Pass: the routing rules of section 4 hold, and every stale item of a revision is re-derived or re-checked (section 10).

## Next

Return to the earliest responsible phase's file (named in the symptom list or the re-entry table) and re-run forward from there.
