---
name: haichen-style-presentation
description: Create or revise Beamer scientific presentations in Haichen Wang's preferred style, with particular support for routine ATLAS and internal HEP talks involving data analysis, detector work, software, or machine learning.
---

# Haichen-style Presentation

Create a complete, conventional ATLAS meeting presentation whose content and status can be checked by collaborators. Treat the supplied analysis materials, public results, and user instructions as authoritative. Never invent a result, sample, method, status, or citation to fill a slide.

## Read the relevant guidance

- Always read [references/slide-contract.md](references/slide-contract.md) before planning or editing slides.
- Always read [references/language-and-voice.md](references/language-and-voice.md) before drafting visible text.
- Read [references/data-analysis-and-ml.md](references/data-analysis-and-ml.md) when the talk concerns data analysis or uses machine learning. Apply only the sections relevant to the project.
- Read [references/analysis-updates-and-comparisons.md](references/analysis-updates-and-comparisons.md) when the talk reports progress since an earlier result, compares methods or trainings, or is a short working-meeting update derived from a fuller analysis record.
- Read [references/preparation-and-review.md](references/preparation-and-review.md) when creating a talk, adapting one to a new audience or duration, or preparing a final review and rehearsal.
- Read [references/statistical-validation.md](references/statistical-validation.md) when the talk contains fits, contours, nuisance parameters, toys, Asimov data, systematic variations, or statistical-model validation.
- Read [references/uc-berkeley-beamer.md](references/uc-berkeley-beamer.md) when the user requests UC Berkeley styling and no supplied Berkeley source must be preserved. Use the clean asset bundle there without importing course or example content.

The user's current instructions take precedence. Preserve the supplied template's styling, but adapt its layout to meet the mandatory opening and closing rule; an existing template is not an exemption.

## Mandatory opening and closing statements

Every slide must display an opening statement and a closing statement. This includes title, overview, section-divider, conclusion, appendix, and backup slides. The opening previews the material on the slide so the audience can recall the context as the slide appears. It must name the subject and tell the audience what will be presented or checked. The closing states the supported takeaway, limitation, or next action after that content. Both must be readable on every displayed page, including overlays. A title, caption, speaker note, source line, or implicit message does not satisfy either requirement.

Use explicit `\slideopening{...}` and `\slideclosing{...}` calls inside each Beamer frame so the audit can check their presence, nonempty arguments, and order. Define these commands to render visible text using the existing theme; [assets/slide-statements.tex](assets/slide-statements.tex) supplies minimal definitions. Never define them as no-ops or hide them in notes or overlays. See the slide contract for placement and review requirements. Missing or invisible statements block delivery as a compliant deck.

## Deliverable

- Use Beamer source as the editable source of truth and compile a PDF. Provide both unless the user requests another deliverable.
- Preserve an existing Beamer theme, macros, branding, aspect ratio, and source organization when revising a deck.
- For a new deck, use a restrained ATLAS-appropriate visual system. Do not add decorative design that competes with plots, tables, or technical content.
- Keep internal paths, prompt names, private working documents, and production notes off the slides.

## Workflow

1. Inspect the available source material and establish the audience, speaking time, discussion time, central question, main message, no more than three takeaways, current status, and expected scope. Reuse verified figures and tables when available.
   - Before drafting numerical claims, select the authoritative result snapshot: completion report, workspace or release, configuration, and active omission or exception ledger. Keep a private source ledger. Do not combine claims from different snapshots unless the slide is an explicit, validated comparison.
2. Make a slide plan with a title slide, the required outline, an introductory overview, the required technical record, the analysis narrative, and a conclusion with summary and outlook. Write the actual opening and closing statements for every slide in the plan. If the talk has more than five slides after the title, slide 2 must be an outline.
3. Put the main message in the introduction. Use the body to explain and support it.
4. Implement the three components on every slide: a visible opening statement for the motivation or problem, the supporting method or evidence in the body, and a visible closing statement for the result, impact, limitation, or next action. Separate labels or boxes are optional; the two statements are mandatory.
5. Write short titles and concise body text in the physicist-facing style described in the language reference. Name the actual analysis object and operation. Flag unclear source language rather than inventing a technical interpretation.
6. Compile from the correct source directory. Resolve build errors without replacing the user's template or changing unrelated source files. When the user requests a separate revision, write to a sibling output and verify that the original source and PDF remain unchanged.
7. Run `scripts/audit_beamer.py` on the final source, log, and PDF when those artifacts are available. Treat a missing required outline, missing, empty, duplicated, or reversed opening/closing statements, prohibited visible punctuation or wording, TeX errors, overfull boxes, a stale PDF, missing pages, and unreadable rendered content as release blockers. Review warnings rather than hiding them.
8. Render and inspect every slide. Verify that each page visibly starts with its opening statement and ends its substantive content with its closing statement, in the correct reading order and at readable size. Check slide numbers, title length, font size, figure scale, whitespace, wrapping, clipping, overlap, citation visibility, status qualifiers, and accidental disclosure. Inspect dense or corrected slides individually in addition to a contact sheet. Source checks alone cannot certify visibility or scientific meaning.
9. When the analysis itself is in scope, verify suspicious plots and numerical claims against the available code, inputs, or validation material before interpreting them. Keep an unsupported or incomplete result clearly labeled.
10. Rehearse to the allotted time when preparing a final deck. Iterate until the source compiles cleanly, the rendered deck is readable, and the main result can be explained within the time budget. Report any missing information that remains visible in the deck.

## Content discipline

- Include established information even when the audience probably knows it. The presenter may skip a record slide verbally, but the slide remains in the main deck for completeness and reproducibility.
- Mark missing, unknown, unimplemented, preliminary, or expected items explicitly. Their absence is part of the technical status.
- Distinguish successful execution of the accepted scope from complete sample, integrated-luminosity, data-use, or validation coverage. A material omission or exception must remain attached to the headline result, its interpretation, and the conclusion.
- Distinguish data from simulation, completed results from work in progress, and observations from projections or expectations.
- Preserve sample definitions, units, uncertainty qualifiers, statistical terms, and collaboration terminology.
- For an updated result, identify the reference, state every material change, and verify comparability before claiming an improvement or difference.
- Use backup slides for supporting detail that does not belong in the main narrative. Do not move required sample or machine-learning documentation to backup merely because it is familiar.
- Treat provenance as part of the scientific result. Keep the source, assumptions, parameterization, calibration version, blinding status, and provisional status visible whenever they affect interpretation.
- Introduce missing information or validation requirements with `Caveat:` and state what must be checked. Do not use vague labels such as `Open metadata` or `Pending tags`.

## Final acceptance

Record per-slide opening and closing coverage in the QA record. Both must be present and visually verified on 100% of delivered slides; no slide type is exempt. An implicit purpose or a takeaway inferred from a plot cannot pass this gate.

The deck is complete when another collaborator can determine what question is being addressed, which result snapshot and coverage are shown, what method and samples are used, what has been done, what remains to be done, and what conclusion or expected result follows. The talk must fit the allotted time, the main figures must support their stated claims, and technical defenses should be available in backup. The PDF must match the final Beamer source, compile without errors or overfull content, and remain legible on a small screen. Required sample, inherited-model, omission, blinding, and status records must be present rather than inferred from speaker knowledge.
