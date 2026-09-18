"""Regression checks for the mandatory slide statement gate (standard library)."""

import unittest

from audit_beamer import statement_errors, structure_errors, visible_text_errors


def frame(body, options=""):
    return r"\begin{frame}" + options + "\n" + body + "\n" + r"\end{frame}"


class StatementGateTests(unittest.TestCase):
    def test_valid_title_and_backup(self):
        content = r"\slideopening{We test the background model.}" + "\n"
        content += r"\includegraphics{model.pdf}" + "\n"
        content += r"\slideclosing{The sideband fit passes the stated criterion.}"
        self.assertEqual([], statement_errors(frame(content, "[plain]") + frame(content, "{Backup}")))

    def test_missing_statements_report_each_frame(self):
        errors = statement_errors(frame("Title", "[plain]") + frame("Backup"))
        self.assertEqual(4, len(errors))
        self.assertTrue(any("frame 2" in error for error in errors))

    def test_comment_cannot_supply_statement(self):
        content = "% " + r"\slideopening{Hidden purpose.}" + "\n"
        content += r"\slideclosing{A visible result.}"
        self.assertEqual(1, len(statement_errors(frame(content))))

    def test_empty_and_formatting_only_arguments_fail(self):
        content = r"\slideopening{ % only a comment" + "\n}"
        content += r"\slideclosing{\textbf{ }}"
        errors = statement_errors(frame(content))
        self.assertEqual(2, len(errors))
        self.assertTrue(all("empty" in error for error in errors))

    def test_reversed_calls_fail(self):
        errors = statement_errors(frame(r"\slideclosing{Result.}\slideopening{Purpose.}"))
        self.assertEqual(1, len(errors))
        self.assertIn("precedes", errors[0])

    def test_duplicate_fails(self):
        content = r"\slideopening{Purpose.}\slideopening{Another purpose.}\slideclosing{Result.}"
        self.assertTrue(any("found 2" in error for error in statement_errors(frame(content))))

    def test_nested_tex_and_escaped_percent(self):
        content = r"\slideopening{We compare \textbf{two} samples.}" + "\n"
        content += r"\slideclosing{The efficiency is 90\%.}"
        self.assertEqual([], statement_errors(frame(content)))

    def test_missing_argument_fails(self):
        errors = statement_errors(frame(r"\slideopening Purpose.\slideclosing{Result.}"))
        self.assertTrue(any("braced argument" in error for error in errors))

    def test_incomplete_frame_fails(self):
        self.assertTrue(statement_errors(r"\begin{frame}\slideopening{Purpose.}"))

    def test_preamble_definitions_do_not_supply_statements(self):
        source = r"\newcommand{\slideopening}[1]{#1}\newcommand{\slideclosing}[1]{#1}"
        source += r"\begin{document}" + frame("Body only") + r"\end{document}"
        self.assertEqual(2, len(statement_errors(source)))

    def test_external_document_content_requires_assembled_source(self):
        self.assertTrue(statement_errors(r"\begin{document}\input{slides}\end{document}"))

    def test_long_talk_requires_outline_as_second_frame(self):
        content = r"\slideopening{This slide previews the content.}\slideclosing{The result follows.}"
        source = frame(content, "[plain]") + "".join(frame(content, "{Topic}") for _ in range(6))
        self.assertTrue(structure_errors(source))

    def test_outline_satisfies_long_talk_structure(self):
        content = r"\slideopening{This slide previews the content.}\slideclosing{The result follows.}"
        source = frame(content, "[plain]") + frame(content, "{Outline}")
        source += "".join(frame(content, "{Topic}") for _ in range(5))
        self.assertEqual([], structure_errors(source))

    def test_short_talk_does_not_require_outline(self):
        content = r"\slideopening{This slide previews the content.}\slideclosing{The result follows.}"
        source = frame(content, "[plain]") + "".join(frame(content, "{Topic}") for _ in range(5))
        self.assertEqual([], structure_errors(source))

    def test_visible_style_prohibitions(self):
        errors = visible_text_errors("One clause; another clause — the plot fixes the result.")
        self.assertEqual(3, len(errors))


if __name__ == "__main__":
    unittest.main()
