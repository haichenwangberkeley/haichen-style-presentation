# Data-analysis and machine-learning completeness

Read this reference for internal ATLAS data-analysis talks. Its purpose is to make omissions visible and to support reproducibility. The presence of a record slide does not require the presenter to discuss every entry.

## Data and Monte Carlo samples

Include a slide in the main body that records the data and Monte Carlo samples used in the study. Prefer a compact table. Include the fields that apply:

- data-taking period or run;
- integrated luminosity;
- center-of-mass energy when relevant;
- data stream, trigger, or derivation when it affects the selection;
- MC campaign;
- physics process and generator configuration at the level needed to identify the sample;
- DSID;
- normalization or cross-section convention when relevant;
- any restricted period, subset, filter, or special production used by the study.

If the audience knows the samples, the speaker may say that the slide is included as a record and move on. Keep it in the main presentation for completeness.

Do not silently omit a requested field. Mark it as unavailable, not yet identified, not applicable, or pending confirmation.

Separate workflow coverage from data exposure. If an accepted manifest excludes files, periods, samples, or campaigns, state both the completed accepted scope and the missing coverage. Do not describe successful processing of the accepted tasks as complete exposure.

If the sample table becomes unreadable, split it by scientific role across adjacent main-body slides. Do not drop identifiers or shrink the table to preserve a single-slide layout.

## Inherited or externally trained models

Apply the machine-learning record whenever a model output materially affects event selection, categorization, reconstruction, calibration, or inference, even when the current study did not train the model. An inherited score is not self-documenting.

Record, as applicable:

- the model or branch name, implementation or release, and responsible source;
- the analysis use and operating point;
- architecture or model-family parameters;
- input features and preprocessing;
- targets, class and process composition, and sample partition;
- sampling, event, class, or loss weights;
- training schedule and random seeds;
- independent-test performance and overtraining checks;
- calibration, domain, and operating-point validation for the data-taking period and analysis phase space.

When the information is unavailable, keep the record in the main body and mark each unknown field. State the consequence for the affected result, such as a conditional interpretation or an open production-certification gate.

## Machine-learning sample partition

When machine learning is the event classifier, principal observable, reconstruction method, or another major analysis component, state how the samples are partitioned into training, validation, and testing sets. This requirement also applies to an inherited model unless its source record supplies the information.

Record:

- the definition and size or fraction of each partition;
- the unit of splitting, such as events, files, runs, or simulated samples;
- whether related events or repeated representations can enter different partitions;
- class and process composition in each partition;
- whether the test sample was kept independent during model and hyperparameter choices;
- cross-validation or repeated-training procedure, if used.

If the samples have not been split, keep the slide and state that directly. The missing split is a finding and a sanity check, not a reason to omit the documentation.

## Model description

Give a standardized description of the architecture, adapted to the model family. Include the information needed to understand the model's scale and data flow, such as:

- model family and implementation;
- number of layers or blocks when "layer" is a literal neural-network term;
- hidden dimensions, attention heads, message-passing steps, pooling, or other model-specific structure;
- trainable parameter count;
- output definition and loss function;
- regularization or normalization choices that materially affect training.

Transformers, graph neural networks, convolutional networks, boosted decision trees, and other models require different architectural fields. Describe the parameters that define the model rather than forcing every model into the same checklist.

## Inputs and targets

State:

- input features and their physical objects;
- preprocessing, scaling, padding, masking, or graph construction;
- truth labels or regression targets;
- feature selections or exclusions that matter to interpretation;
- possible information leakage from labels, reconstruction, event weights, or split construction.

## Training strategy

Document the training procedure, preferably in a compact table accompanied by the essential plots:

- training from scratch, fine-tuning, or use of a pretrained model;
- source and relevance of pretraining data when used;
- optimizer and learning-rate schedule;
- initial or characteristic learning rate;
- number of epochs completed and stopping criterion;
- batch size;
- number of events or batches in an epoch;
- how physics processes and classes enter each batch;
- event, process, class, or loss weights;
- sampling or balancing strategy;
- random seeds or repeated trainings when they affect the result;
- hardware or training time only when relevant to feasibility or comparison.

Show training and validation behavior when available. Label a curve and its sample unambiguously.

## Evaluation and analysis use

State which sample produces each performance result. Keep the independent test result distinct from training or validation diagnostics. Include the metric definition, operating point, uncertainty or variation, and comparison baseline when they are needed to interpret the result.

Use a metric that represents the relevant statistical power. When raw or weighted event counts are misleading, report effective statistics, equivalent Monte Carlo integrated luminosity, or another physically meaningful quantity and define it.

Explain how the model output enters the physics analysis: selection, categorization, regression, reconstruction, calibration, observable, or fit input. State whether the downstream impact has been measured or is only expected.

## Missing information

Keep the relevant slide even when information is absent. Use precise statements such as:

- `Training/validation/test split not yet implemented.`
- `Independent test sample not identified in the available material.`
- `Parameter count not reported.`
- `Class weighting under study.`
- `Downstream sensitivity impact not yet evaluated.`

Do not substitute an optimistic expectation for a missing result. The standardized slide serves as a technical record and exposes blind spots early.
