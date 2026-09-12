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

The user's current instructions and supplied template override these defaults.

## Deliverable

- Use Beamer source as the editable source of truth and compile a PDF. Provide both unless the user requests another deliverable.
- Preserve an existing Beamer theme, macros, branding, aspect ratio, and source organization when revising a deck.
- For a new deck, use a restrained ATLAS-appropriate visual system. Do not add decorative design that competes with plots, tables, or technical content.
- Keep internal paths, prompt names, private working documents, and production notes off the slides.

## Workflow

1. Inspect the available source material and establish the talk's topic, audience, current status, and expected scope. Reuse verified figures and tables when available.
2. Make a slide plan with a title slide, an introductory overview, the required technical record, the analysis narrative, and a conclusion with summary and outlook.
3. Put the main message in the introduction. Use the body to explain and support it.
4. For every non-title slide, identify the slide-level motivation or problem, method or solution, and result, impact, or expected result. These are reasoning components, not mandatory visible labels.
5. Write short titles and concise body text in the physicist-facing style described in the language reference.
6. Compile from the correct source directory. Resolve build errors without replacing the user's template or changing unrelated source files.
7. Render and inspect every slide. Check slide numbers, title length, font size, figure scale, whitespace, wrapping, clipping, overlap, citation visibility, status qualifiers, and accidental disclosure.
8. Iterate until the source compiles cleanly and the rendered deck is readable. Report any missing information that remains visible in the deck.

## Content discipline

- Include established information even when the audience probably knows it. The presenter may skip a record slide verbally, but the slide remains in the main deck for completeness and reproducibility.
- Mark missing, unknown, unimplemented, preliminary, or expected items explicitly. Their absence is part of the technical status.
- Distinguish data from simulation, completed results from work in progress, and observations from projections or expectations.
- Preserve sample definitions, units, uncertainty qualifiers, statistical terms, and collaboration terminology.
- Use backup slides for supporting detail that does not belong in the main narrative. Do not move required sample or machine-learning documentation to backup merely because it is familiar.

## Final acceptance

The deck is complete when another collaborator can determine what question is being addressed, what method and samples are used, what has been done, what remains to be done, and what conclusion or expected result follows. The PDF must match the final Beamer source and every slide must remain legible on a small screen.
