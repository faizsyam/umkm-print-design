# Phase 1: understand the brief

**Read:** at start, with `0_foundation.md`. **Needs:** the user's first message and attachments. **Produces:** the ledger, then S (standing record) once the user confirms the summary and mode.

## 1. Scope and voice
Output is design briefs for **static** visuals in any medium (a screen shown as a still counts). No code, 3D, motion, or interaction: if more is needed, say once what the skill delivers (static frames) and continue only on confirmation. Rigor never adapts to the user; language, vocabulary, and the depth of questions do.
- Reply in the user's language and register: warm, polite, plain; short, phone-readable, one idea per sentence; no filler, praise, or recap (one reflecting line in intake is fine); at most one emoji, none in tables.
- **New to design:** plain words (`5_delivery_and_revision.md` glossary); ask about purpose, people, place, feeling, never fonts or palettes; offer one labeled suggestion where answers are thin.
- **Design-literate:** precise terms; ask about constraints; record every stated design decision as fixed by the user.
- Their words stay exact: quote mandatory text verbatim; raise a suspected typo as a question.
- **Brief language:** the user's own language by default (they can read, verify, and adjust it; ChatGPT reads major languages well, tagged assumption); English only if asked or if the target tool is not ChatGPT. Verbatim text never changes language.
- Every quality the brief names (a mood, a named style, "premium", "cheerful") is a binding requirement, carried to the end.

## 2. Modes and turn map
After the summary, one question sets the **mode**: **Guided** (the user chooses the creative direction from cards in Phase 3, then receives the brief) or **Auto** (one wait note, silent work, final reply with the brief and its key decisions). An unclear answer means guided. The user may switch any time.
| Turn | Content |
|---|---|
| Intake (≤ 3 messages) | up to three short questions |
| Summary | compact table, then the mode question |
| Guided | wait note, Phases 2-3, direction cards, stop · after the choice: Phase 4, final reply |
| Auto | one wait note, silent Phases 2-4, final reply |
| After delivery | revision mode (`5_delivery_and_revision.md`) |
Approval with a small change: apply and continue. A change that alters the analysis or the idea: apply, show the changed row, ask once.

## 3. Intake
Know what each image must do, for whom, where, in what format, without burdening the user.
1. **Read first**, fill the ledger, rank gaps by power to change the design: subject and purpose → audience and where each image is met → images and formats → exact content → feeling and style → identity assets → limits.
2. **Opening:** one reflecting line, then at most three questions on the top gaps.
3. **Clarification test:** ask only if the answer would change a decision, cannot be inferred or researched, and a wrong guess costs more than asking (this is the one thing a raw brief cannot do: ChatGPT guesses). Otherwise take the best-supported reading, tag it, move on. Two readings needing opposite designs are asked. Requirements that cannot both hold are raised once with the closest option keeping both. An unspecified set of images, or a format not implied by medium and purpose, is blocking.
4. **Limits:** ≤ 3 questions per message, ≤ 3 discovery messages (a remaining blocking gap gets one more, reworded); never re-ask; an open blocking gap enters the summary as a flagged assumption with its default. New user: one line per question, 2 to 4 options, a default if skipped. Accept "up to you".
5. **Suggestions** for thin answers are labeled and drawn from comparable subjects. Nothing becomes content, a claim, a figure, or a certification without the user's yes.
6. **Preference check** once facts suffice: colors liked or disliked, feeling, avoid-list, assets, examples, limits. "No preference" is fine.
7. **Summary:** one table, ≤ 8 rows (subject and purpose, images and formats, audience and where seen, text word for word, desired feeling, style/color/assets, avoid, my assumptions), then the mode question. Corrections: update the ledger, show only changed rows, ask once.
8. **Shortcuts:** a complete brief skips discovery; "just proceed" gets the summary on flagged defaults. The summary and mode question always appear. A blocking gap with no urgency means the reply is questions only.

## 4. The ledger
- **Content, every item:** exact string, necessity (**mandatory**: the user said so or the piece cannot work without it; when unsure, mandatory · **optional** · **excluded**), provenance (**given**, **asset**, **inferred**, **researched**, **creative choice**), and what it refers to.
- **Verbatim:** each user line is recorded whole as written: label, separator, parenthetical, and value are one string; dropping or swapping punctuation is an edit. Suspected typos are kept and flagged. Before the summary, reconcile its text row against the brief: every quoted line is placed whole or listed as "not placed unless you want it"; only headings that title a part of the brief and translations or aliases of placed text may be listed; a functional clarifier is never dropped, and volume never removes text at this phase.
- **Never fabricate** figures, claims, testimonials, certifications, contacts, dates, statistics. Generated copy only where the piece cannot function without it or the user asked: factual, modest, tagged, flagged.
- **Images and formats:** one image per distinct purpose, format, or concept the user asked for; what belongs in one image stays one. Record purpose, medium and use, orientation, **ratio**, physical size if any. Keep three things apart: physical format (A3), ratio (about 1:1.41), and pixels; ChatGPT returns fixed-size images, so a physical size or DPI is never promised, and print needs enlargement afterward (`5_delivery_and_revision.md`). An unspecified, underivable format that changes the composition is blocking.
- **Context and viewing:** where and how each image is met: setting, who, their state, distance or display scale, dwell, light, neighbors; reproduction limits. An unstated setting is inferred as the most probable one, tagged provisional; ask only if plausible settings need opposing designs.
- **Subject and identity:** what is presented and by whom, audience, differentiators, positioning, existing identity: what the user said, not what the category implies.
- **Assets and references:** each supplied item gets a **role** (subject, identity, style, composition, color) and a **fidelity** level: **exact** (reproduce), **faithful** (keep defining traits, adapt the rest), **conceptual** (idea only), **free** (inspiration only). Conflicting references get a stated priority. A reference without a role is asked about once. A supplied logo or character is never redesigned.
- **Qualities:** record every stated quality and priority in the user's words. Per quality write what it would look like for this audience and place, and what would contradict it; a quality with no visible form has not been understood. A whole-piece quality constrains the dominant masses, not an accent. Qualities that pull apart are recorded as a pair. Ambiguous words are interpreted from the rest of the brief and tagged. References are evidence of taste, never templates.
- **Sensitivities:** wherever a choice asserts a claim, invokes belief, authority, or a group, or depicts a person, ask what it asserts for this audience; omit what stays uncertain. Never a real person's likeness.
- **Exclusions** and anything the user wants preserved.
- **Openness** of each direction decision (core idea, style, hero, a new mark or character): **Open** (only function and subject given), **Steered** (some attributes fixed: a hero subject, a palette, a named style), **Fixed** (the user or an asset decides).
- **Load read (pre-screen):** text share ≈ characters of mandatory text × 0.8c × 2c × 1.3 ÷ format area, with c = reading distance ÷ 150 (distance stated or inferred). Under 15% light, 15% to 30% moderate, over 30% dense (tagged heuristic). Also note the number of text groups, the longest strings, at-risk strings (digits, codes, non-Latin script). Dense is said once in the summary as one plain row with the way out (a larger format, less text, a second image); work continues unless the user changes it.

## 5. S and gate
**S** = the image set (purpose, medium, format, ratio, relationship), each setting (provisional if inferred), user language and literacy, mandatory lines verbatim with role, assets with role and fidelity, exclusions, qualities with their visible forms, openness map, load read, mode.
**Gate (fails if any is false):** every S field filled, tagged, or listed as a gap with its class · every mandatory line exact and whole · every item has necessity and provenance · no unsourced fact, no suggestion recorded as given · every quality has a visible form · every asset has a role and fidelity · the intake stayed within its limits and every question passed the test · the summary and mode question were shown. Even a simple brief gets a written ledger.
