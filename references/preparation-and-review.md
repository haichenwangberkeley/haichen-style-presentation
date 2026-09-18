# Preparation, timing, and review

Read this reference when creating a talk, changing its audience or duration, or preparing a final version. It turns presentation preparation into a controlled sequence with an explicit time budget and review record.

## Write the brief first

Before making slides, establish:

- the audience and its expected background;
- the total slot and how much of it is reserved for discussion;
- the central question;
- the main message in one sentence;
- no more than three takeaways;
- the result, comparison, or decision the talk must support;
- whether the material is blinded, preliminary, internal, approved, or public.

If the source does not establish one of these items, use a visible placeholder in the working plan and ask only when the missing choice would change the deck substantially.

## Adapt to the time budget

Budget content according to speaking time, not the nominal calendar slot. Leave room for transitions, interruptions, and questions. A 10 to 20 percent speaking-time buffer is a useful default when the format does not specify one.

For a longer internal talk, retain the technical record and enough validation to support discussion. Reduce background before reducing the material needed to understand the result.

For a short or lightning talk, keep the motivation, central result, and immediate interpretation. Remove dense explanation, secondary studies, and nonessential comparisons. Put likely technical questions in backup.

Do not solve a timing problem by shrinking text until it is unreadable.

## Build the narrative

Use this order when it fits the subject:

1. motivation and question;
2. analysis or measurement overview;
3. the minimum method needed to understand the result;
4. main result;
5. validation and dominant uncertainties;
6. comparison, implication, or decision;
7. takeaways and next steps.

For routine ATLAS and internal talks, the introductory overview should already reveal the main message. This sequence controls the supporting explanation; it does not postpone the punchline. Use a delayed reveal only when the user or the established format explicitly calls for a discovery-announcement narrative.

For every planned slide, write its visible opening sentence as a preview of the body and its visible closing sentence as the supported takeaway or next action. Use these to choose the title, visual, and amount of text. Apply this to title, outline, section-divider, conclusion, and backup slides as well. Delete or merge a slide whose purpose duplicates another slide.

If the talk contains more than five slides after the title, reserve slide 2 for an outline before planning the remaining sequence. Use the outline to introduce the main sections rather than list every slide title.

## Main deck and backup

Keep the main deck focused on the argument, required decisions, and evidence. Move standard definitions, alternative views, detailed cross-checks, and technical defenses to backup when the main argument does not require them.

Keep required data and Monte Carlo sample documentation in the main deck. Keep required machine-learning sample, architecture, input, and training documentation in the main deck when machine learning is a principal analysis component. The presenter may pass over a record slide briefly.

Prepare backup slides for predictable questions, including:

- detailed selections and object definitions;
- additional validation and closure tests;
- systematic-uncertainty construction;
- alternative parameterizations or fit configurations;
- comparisons with prior analyses;
- supporting numerical tables.

## Review loop

Circulate a draft early enough for substantive changes. Ask reviewers focused questions, for example: `Please focus on systematics and pending items.` Convert the feedback into an itemized working list.

Resolve each item through one of these actions:

- correct the content;
- clarify the explanation;
- move supporting detail to or from backup;
- run or request a technical check;
- label the item as pending with an owner or required input;
- decline the change with a documented scientific reason.

Circulate the revised deck for a quick second look when the changes affect conclusions, analysis status, or major figures. Preserve time before the deadline for plot updates, code checks, and final corrections.

After the review, separate the record into reusable presentation principles, new questions for the analysis checklist, and one-off action items. Update standing guidance only with recurring instructions; keep analysis-specific corrections with the task.

## Preserve requested revisions

When the user asks to retain the current deck, create the revision in a separate sibling directory or under a distinct source and PDF name. Record enough identity information to show which copy is original and which is revised. Verify the original source and PDF after the new deck is built; hashes are useful when exact preservation matters.

## Rehearse and lock

- Give the talk with a timer.
- Practice explaining each main figure in one or two sentences.
- Check that transitions and discussion fit inside the slot.
- Confirm that each backup slide answers a likely question.
- Perform a final check of numbers, captions, links, release status, blinding, and acknowledgements.
- Check visible text for semicolons, em dashes, vague uses of `fixes`, artifact-as-actor constructions, and vague caveat labels. Check that every opening previews its slide body.
- Run the Beamer audit, review its warnings, render every page, and inspect dense or recently corrected slides individually.
- Record the opening and closing statement for every slide in the QA record, with separate source and rendered-review statuses. Missing, empty, invisible, misplaced, or scientifically uninformative statements must be corrected before calling the deck compliant. Verify every overlay or continuation page as well.
- Do not add a result still undergoing essential validation unless it is clearly labeled as preliminary or pending.

## Acceptance

The preparation is complete when the audience, duration, objective, central message, and takeaways are explicit; the talk fits its speaking time; reviewers' substantive comments have a visible disposition; and the presenter can explain what changed in response to review.
