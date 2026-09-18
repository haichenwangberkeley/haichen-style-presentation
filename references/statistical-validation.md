# Statistical validation and scientific provenance

Read this reference when the presentation contains statistical fits, contours, nuisance parameters, toy Monte Carlo, Asimov data, systematic variations, or related validation. Apply only checks relevant to the analysis and available material. Do not imply that a validation was performed unless the evidence shows it.

## Provenance and definitions

For every numerical input, fit, contour, and comparison that affects the conclusion, establish:

- its source and version;
- the assumed parameter values or Standard Model relationships;
- the parameterization used in the text, plot, and conclusion;
- why this fit, contour, or parameterization is shown;
- the calibration, production, software, or workspace version when relevant;
- the blinding and provisional status.

Use a single authoritative result snapshot for a headline result. If a later diagnostic or development release is shown, label it separately and do not imply that it was promoted into the nominal result.

Define variables before showing plots that use them. Include the object definitions, overlap removal, selections, vetoes, and category definitions needed to interpret the result. Use consistent terminology, labels, units, notation, and significant figures throughout the deck.

Acknowledge contributors who implemented an important part of the analysis. Include comparison with a prior analysis when it establishes the relevant context or improvement.

## Validate before interpreting

A polished or plausible plot is not evidence that the code, inputs, or statistical model are correct. When a plot looks suspicious, inspect the underlying material before explaining it. Check, as applicable:

- random-seed uniqueness;
- binning and boundary conventions;
- formulas and parameter transformations;
- workspace contents and configuration;
- expected distributions and normalization;
- consistency between plotted inputs and the stated analysis version.

If the underlying material is unavailable, describe the observation and mark the interpretation as pending. Do not invent a cause.

## Stage-specific status

Track availability and validation by stage when a category or region can produce intermediate diagnostics before inference. Separate, as applicable:

- selected events or signed weighted spectra;
- released data sidebands;
- signal shape or probability model;
- continuum or background template prerequisite;
- fit convergence and goodness of fit;
- spurious-signal or closure criteria;
- workspace construction and expected or observed inference.

A failed prerequisite blocks its downstream stages; it does not erase independently available upstream evidence. State the failed stage and the measured value, failed criterion, or unavailable prerequisite. Avoid describing the whole region as impossible when spectra, sidebands, or a signal model remain available.

## Signed Monte Carlo

Negative generator weights are legitimate signed contributions. Distinguish a negative binned estimator from a negative physical Poisson mean or probability density.

When negative bins affect interpretation:

- preserve signed weights and their statistical uncertainties;
- show a zero reference and enough mass or observable detail to locate deficits;
- state the binning and normalization;
- quantify the deficit and its relation to the MC statistical error when available;
- keep template usability, smoothing or rebinning, fit validation, and inference eligibility as separate statuses.

Do not call a small negative fraction negligible without a fit-bias or limit-bias study. Do not suppress an independently valid raw spectrum because a continuum-template prerequisite fails.

## Closure, toys, and Asimov data

- Test closure under the signal hypotheses relevant to the claim, such as `mu=0` and `mu=1` when both matter.
- Increase the event or toy sample when statistical fluctuations can hide a difference.
- Compare Asimov and toy-MC behavior explicitly when both are used. State which diagnostic question each answers.
- Report the fitted quantity, expected behavior, and criterion used to decide whether closure is satisfactory.

## Nuisance parameters and systematic variations

- Plot nuisance-parameter or pull distributions when they are needed to assess the fit. Report diagnostics such as the mean and RMS when appropriate.
- Investigate non-Gaussian distributions, negative pulls, large constraints, or other unexpected behavior.
- Check that up and down variations represent meaningful uncertainty directions. Identical or unjustifiably one-sided variations require explanation or correction.
- Use control-region information to estimate category fractions or construct realistic variations when that is the analysis method.
- Test modeling choices numerically when possible. Do not settle a quantitative modeling question through intuition alone.

## Presentation of the result

Give each important figure one claim. Use a short title that identifies what the figure establishes, define the variables and assumptions, and make the relevant data visually dominant. Use qualitative language that matches the evidence.

Prefer a direct probability or frequency statement when specialized statistical terminology would obscure the point for the intended audience. Preserve the precise statistical term when the distinction matters to the claim.

Keep the independent test result separate from validation diagnostics. Distinguish observed and expected quantities, statistical and systematic effects, and post-fit and pre-fit distributions.

Do not combine potentially overlapping categories or present their limits as statistically independent unless the model includes the correlations or an orthogonal assignment. State explicitly when results are separate category diagnostics.

## Acceptance

Before calling the presentation scientifically ready, confirm that:

- numerical inputs and assumptions are traceable;
- plots and conclusions use the same parameterization and status;
- blinding and masking are stated correctly;
- relevant closure and diagnostic tests have been performed or marked pending;
- systematic variations have a physical or data-based interpretation;
- suspicious behavior has been investigated or remains explicitly unresolved;
- the strength of every conclusion matches the completed validation.
