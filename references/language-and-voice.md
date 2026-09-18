# Physicist-facing language and voice

Use language natural to ATLAS and CMS papers, notes, and meeting presentations. The user's current language instructions in this reference are authoritative. Older writing samples may inform rhythm and reasoning, but they do not override the current preference for direct statements.

## Central rule

State the scientific point directly. Prefer the actor, object, action, method, evidence, and consequence over an abstract narrative about a framework, layer, pathway, pillar, or landscape.

For example:

| AI-associated wording | Physicist-facing wording |
| --- | --- |
| The framework unlocks a new analysis capability. | The new selection accepts events that are rejected by the current analysis. |
| The classifier serves as a first-class component of the pipeline. | The classifier defines the event categories used in the fit. |
| This is not only an improvement in efficiency; it is a new paradigm. | The method increases the efficiency at the same background rejection. |
| The two efforts form an integrated research pillar. | The two analyses use the same calibration and validation samples. |
| This underscores the broader impact of the work. | The same correction can also be used in the second measurement. |

The examples are patterns, not fixed wording. Use only statements supported by the source material.

## Word choice

Prefer ordinary technical verbs: use, develop, test, measure, perform, apply, train, validate, compare, improve, select, reconstruct, calibrate, fit, and complete.

Prefer literal nouns: analysis, method, model, classifier, sample, selection, control region, correction, observable, calibration, software, test, and result.

Reconsider these terms when they are decorative:

- layer;
- first-class;
- thrust;
- pillar;
- anchor;
- pathway;
- ecosystem;
- landscape;
- synergy;
- seamless;
- transformative;
- holistic;
- unlock;
- harness;
- leverage;
- underscore;
- showcase.

Keep them when they are literal or established technical terms. A detector layer, neural-network layer, software framework, or ATLAS analysis framework should retain its correct name.

Do not rotate among model, architecture, framework, system, and engine merely for variety. Repeat the correct technical noun when the referent is unchanged.

## Sentence structure

Avoid the stock construction `not A; it is B` when B can be stated directly. The same applies to decorative `not only A, but also B` and `rather than A, B` constructions.

Do not use semicolons or em dashes in visible presentation text. Use a full stop, comma, colon, or two sentences. This applies to titles, opening and closing statements, bullets, captions, table text, source lines, footers, and text embedded in figures.

Avoid making a sample, simulation, table, plot, or other artifact sound like an actor when describing how it was used. Prefer a construction that names the analysis action. For example:

| Avoid | Use |
| --- | --- |
| Single-Higgs simulation fixes the resonant contribution and signal shape. | Single-Higgs simulation was used to determine the resonant contribution and signal shape. |
| The table establishes the sample coverage. | The samples included in the study are listed in the table. |
| The plot proves that the model is robust. | The comparison in the plot was used to test the model. |

Do not use `fixes` as a general scientific verb. Use `determine`, `constrain`, `derive`, `estimate`, `define`, or `use`, according to the actual relationship. Use `fixed` only when a parameter was deliberately held constant, and state what it was fixed to or which procedure fixed it.

Introduce unresolved information with `Caveat:` and state the check that remains. Prefer `Caveat: the generator and shower configurations must be confirmed` over labels such as `Open metadata` or `Pending tags`.

Keep a contrast when it carries scientific information. A comparison between the current method and the proposed method may be essential. Express it plainly, using `while`, `by comparison`, `instead`, or two direct sentences when appropriate.

The user's writing often lets the reader follow the reasoning:

1. the situation or observation;
2. why it matters;
3. the action, method, or judgment;
4. the result, consequence, or next step.

Preserve that explanation. A shorter rewrite is worse when it removes the reason that connects a limitation to a decision.

Use first person when appropriate to the document and collaboration practice. `I` identifies an individual decision or contribution; `we` identifies group work; the analysis, model, or collaboration may be the subject when it performs the relevant action.

Allow a moderately long explanatory sentence when its clauses belong together. Follow it with a short result or commitment when that improves emphasis. Do not make every bullet or sentence follow the same rhythm.

## Mechanism, planned work, and contingency

Explain the physical or computational mechanism before claiming a broad benefit. State what information, detector response, event selection, correction, or statistical procedure produces the change. A statement such as `The model captures complex correlations` is incomplete unless the relevant inputs, use of those correlations, and observed consequence are identified.

When presenting planned work, use the parts that apply:

1. current method or analysis;
2. specific limitation;
3. proposed model, selection, control region, correction, or test;
4. implementation and validation procedure;
5. measured or expected result;
6. next deliverable or fallback.

State a contingency through the specific technical risk, the evidence for it, its consequence, the test or decision criterion, and the baseline result retained if the proposed method fails. Avoid replacing these details with a general claim of robustness or risk management.

## Claims and status

- Tie strong words such as significant, robust, novel, or improved to a number, comparison, test, publication, adoption status, or clearly stated criterion.
- Distinguish observation, evidence, measurement, exclusion, expected sensitivity, and projection.
- Preserve the difference between led, developed, contributed, supervised, reviewed, and used.
- Preserve the difference between completed, ongoing, preliminary, planned, and expected work.
- Do not invent a mechanism or metric to replace vague source language. Mark the missing detail for the author.

## Slide titles and bullets

Use short phrase titles that carry the subject or message. Avoid long sentence titles and generic headings such as `Methodology overview` when a specific title such as `Training samples` or `Photon calibration` is available.

Write bullets as compact scientific statements. Each bullet should add motivation, method, evidence, status, or consequence. Remove rhetorical setup that delays the technical content.

Write the opening statement as a preview of the rest of the slide. It should help the audience switch context by naming what will be described, compared, or checked. Do not use the opening only to announce a conclusion or repeat the title. The body supplies the evidence, and the closing states the resulting conclusion, caveat, or action.

Do not expose private proposal language, internal source paths, prompt names, or production notes. Adapt general writing preferences to the presentation; do not copy passages from private source documents.

## Revision check

Before accepting visible text, ask:

- Is the scientific object named?
- Is it clear who or what performs the action?
- Does the sentence explain the actual technical relationship?
- Is the mechanism stated before the claimed benefit?
- Is an evaluative claim supported?
- When a limitation matters, are the test, decision criterion, and fallback concrete?
- Can a stock contrast be stated directly?
- Has shortening removed necessary reasoning or a status qualifier?
- Does the wording sound natural in an ATLAS or CMS meeting?
- Is the sentence short enough to read on a slide without becoming vague?
- Does the opening preview the body of the slide?
- Does any sample, simulation, table, or plot appear to act on the analysis when the intended meaning is that it was used by the analysis?
- Are semicolons, em dashes, vague uses of `fixes`, and vague caveat labels absent?
