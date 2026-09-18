# UC Berkeley Beamer template

Use this template when the user asks for UC Berkeley styling and does not supply another Berkeley template that must be preserved.

The self-contained asset bundle is [../assets/uc-berkeley-beamer](../assets/uc-berkeley-beamer):

- `template.tex` provides neutral title, outline, evidence, and conclusion frames.
- `beamerthemeUCBerkeley.sty` provides Berkeley colors, serif headings, table colors, the diagonal blue footer, page numbering, and the mandatory opening and closing commands.
- `UCBerkeley_wordmark_white.pdf` provides the footer wordmark.
- `LICENSE.md` records the CC BY 4.0 attribution and the UC Berkeley trademark exclusion.

Copy the theme, template, wordmark, and license into the presentation source directory before adapting `template.tex`. Do not copy instructional or scientific content from a course deck merely because it supplied the visual template.

Preserve the default `Presentation style by Haichen Wang` footer credit, the fuller title-slide credit, the source notices, and the bundled `LICENSE.md`. The footer credit is intentionally separate from the presentation author. If the credit must be relocated for a constrained format, provide equivalent reasonable attribution that identifies Haichen Wang's adaptation, the upstream Overleaf theme and authors, the CC BY 4.0 license, and any changes. Do not imply endorsement by Haichen Wang, Overleaf, or UC Berkeley.

The UC Berkeley wordmark is excluded from the copyright license and remains subject to university trademark and brand requirements. Do not alter the wordmark or treat the CC BY license as permission to use university marks in a context that otherwise requires approval.

Retain the three-component slide contract. Every frame needs exactly one visible `\slideopening{...}` before its body and one visible `\slideclosing{...}` after its body. Put source lines after the closing statement.

The clean template uses a 16:9 aspect ratio. Preserve a user-supplied aspect ratio when revising an existing deck. Use XeLaTeX, LuaLaTeX, or Tectonic because the theme uses `fontspec`. Georgia and Open Sans are selected when installed. Liberation Serif and Liberation Sans are the first portable fallbacks.

Replace all neutral prompts in `template.tex` with presentation-specific content. Add an outline on slide 2 whenever the completed talk has more than five slides after the title. Run the standard Beamer audit and visually inspect every rendered page before delivery.
