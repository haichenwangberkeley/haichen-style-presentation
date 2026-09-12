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

## Machine-learning sample partition

When machine learning is the event classifier, principal observable, reconstruction method, or another major analysis component, state how the samples are partitioned into training, validation, and testing sets.

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

Explain how the model output enters the physics analysis: selection, categorization, regression, reconstruction, calibration, observable, or fit input. State whether the downstream impact has been measured or is only expected.

## Missing information

Keep the relevant slide even when information is absent. Use precise statements such as:

- `Training/validation/test split not yet implemented.`
- `Independent test sample not identified in the available material.`
- `Parameter count not reported.`
- `Class weighting under study.`
- `Downstream sensitivity impact not yet evaluated.`

Do not substitute an optimistic expectation for a missing result. The standardized slide serves as a technical record and exposes blind spots early.
