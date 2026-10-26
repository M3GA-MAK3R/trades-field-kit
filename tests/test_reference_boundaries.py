"""Content regression guards, not technical or regulatory certification."""

from pathlib import Path
import re
import unittest
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]


class ReferenceBoundaryTests(unittest.TestCase):
    def test_skill_export_matches_canonical(self):
        self.assertEqual(
            (ROOT / "skill/trades-field-work/SKILL.md").read_bytes(),
            (ROOT / "skill/trades-field-work.skill.md").read_bytes(),
        )

    def test_removed_unsafe_shortcuts_do_not_return(self):
        surfaces = [
            *ROOT.glob("docs/**/*.md"),
            *ROOT.glob("skill/**/*.md"),
            ROOT / "generate_umbrella_pdf.py",
        ]
        patterns = (
            r"20k(?:Ω|-ohm)",
            r"short terminals again",
            r"wait 30s,\s*short again",
            r"≤\s*1500\s*PSI",
            r"normal:\s*8-[0-9]+",
            r"Normal \(8-12",
            r"CAT III for HVAC",
            r"±10%\s*(?:acceptable|tolerance|of rated)",
        )
        for file in surfaces:
            content = file.read_text()
            for pattern in patterns:
                with self.subTest(file=str(file.relative_to(ROOT)), pattern=pattern):
                    self.assertIsNone(re.search(pattern, content, flags=re.I))

    def test_discussion_checklists_link_safety_boundaries(self):
        for file in (ROOT / "docs/field-checklists").glob("*.md"):
            content = file.read_text()
            with self.subTest(file=file.name):
                self.assertIn("../SAFETY.md", content)
                self.assertIn("private systems", content)

    def test_safety_reference_covers_key_boundaries(self):
        content = (ROOT / "docs/SAFETY.md").read_text()
        for required in (
            "not official paperwork", "work ethic", "reaccumulation",
            "qualified", "Return to service", "Group work", "shift changes",
            "improvised terminal shorting", "component marking",
            "TPM-SI0245", "apprentice exception",
        ):
            with self.subTest(required=required):
                self.assertIn(required, content)
        for standard in ("1910.147", "1910.333", "1910.334", "1910.335"):
            self.assertIn(
                f"https://www.osha.gov/laws-regs/regulations/standardnumber/1910/{standard}",
                content,
            )

    def test_markdown_local_links_resolve(self):
        count = 0
        for file in ROOT.rglob("*.md"):
            if ".git" in file.parts:
                continue
            for target in re.findall(r"\]\(([^)]+)\)", file.read_text()):
                if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
                    continue
                relative = unquote(target.split("#")[0])
                with self.subTest(file=str(file.relative_to(ROOT)), target=target):
                    self.assertTrue((file.parent / relative).exists())
                count += 1
        self.assertGreater(count, 20)

    def test_readme_stays_slim_and_aligned(self):
        content = (ROOT / "README.md").read_text()
        self.assertLessEqual(len(content.splitlines()), 45)
        for required in ("toolbox", "work ethic", "sanitized", "docs/SAFETY.md"):
            self.assertIn(required, content)

    def test_public_issue_paths_warn_about_privacy(self):
        for relative in (
            ".github/ISSUE_TEMPLATE/field-issue.yml",
            ".github/ISSUE_TEMPLATE/field-issue-cli.md",
            "scripts/file-issue.sh",
        ):
            content = (ROOT / relative).read_text()
            with self.subTest(file=relative):
                self.assertIn("PUBLIC", content)
                self.assertIn("authorized readings", content)
                self.assertIn("job record", content)

    def test_arrival_contact_and_waiting_boundaries(self):
        content = (ROOT / "templates/field-preflight.md").read_text()
        section = content.split("## Arrival, Contact, and Waiting\n", 1)[1].split(
            "\n## Hazards and Approved Controls", 1
        )[0]
        for required in (
            "Before dispatch", "Arrived early", "Initial check-in", "No answer",
            "backup contact", "agreed contact", "safe waiting location",
            "No response is not permission", "bypass security",
            "Read back", "mutual understanding", "task authorization",
            "reschedule", "next agreed check-in", "Private record and handoff",
            "not a timesheet or billing authorization",
        ):
            with self.subTest(required=required):
                self.assertIn(required, section)
        self.assertNotIn("- [ ]", section)
        self.assertNotRegex(section, r"\b(?:10|15|30)\s*(?:min|minutes)\b")
        mobile = (ROOT / "docs/MOBILE-QUICKSTART.md").read_text()
        self.assertIn(
            "../templates/field-preflight.md#arrival-contact-and-waiting", mobile
        )


if __name__ == "__main__":
    unittest.main()
