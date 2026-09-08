from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import check_report_archive as checker
from report_archive_layout import find_report_dirs
from release_compressed_archive import copy_report_dirs, group_reports_by_month, write_zip
import zipfile


class ClassificationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        rules = self.root / 'classification'
        rules.mkdir()
        (rules / 'categories.json').write_text(json.dumps({'04-AI模型':['多模态模型与模型架构']}), encoding='utf-8')
        self.patch = patch.object(checker, 'REPO_ROOT', self.root)
        self.patch.start()
        self.addCleanup(self.patch.stop)

    def report(self, prefix, readme='# Demo\n\nA report.'):
        directory = self.root / prefix / '20260908-demo-codex'
        directory.mkdir(parents=True)
        (directory / 'report.html').write_text('<html>demo</html>', encoding='utf-8')
        if readme is not None:
            (directory / 'README.md').write_text(readme, encoding='utf-8')
        return directory

    def check(self):
        errors = []
        checker.check_repo_root(errors)
        for directory in self.root.iterdir():
            if directory.is_dir(): checker.check_archive_branch(directory, errors)
        return errors

    def test_secondary_and_primary_survey_are_valid_and_packaged(self):
        a = self.report('04-AI模型/多模态模型与模型架构')
        b = self.report('04-AI模型', '# Survey\n\n文章类型：综述／综合\n一级分类：04-AI模型\n一级直归理由：跨模态能力演进，无法归入单一模态。')
        self.assertEqual(self.check(), [])
        self.assertEqual(set(find_report_dirs(self.root)), {a,b})
        grouped = group_reports_by_month([a.relative_to(self.root), b.relative_to(self.root)])
        self.assertEqual(set(grouped), {'202609'})
        with tempfile.TemporaryDirectory() as output:
            staging = Path(output) / 'stage'
            staging.mkdir()
            copy_report_dirs(self.root, staging, [a, b])
            archive = Path(output) / 'month.zip'
            write_zip(staging, archive)
            with zipfile.ZipFile(archive) as z:
                self.assertIn((a.relative_to(self.root) / 'report.html').as_posix(), z.namelist())
                self.assertIn((b.relative_to(self.root) / 'report.html').as_posix(), z.namelist())

    def test_registry_matches_human_classification_rules(self):
        rules = Path(__file__).resolve().parents[1] / 'classification'
        categories = json.loads((rules / 'categories.json').read_text(encoding='utf-8'))
        for index, (primary, children) in enumerate(categories.items(), 1):
            text = (rules / f'{index:02d}.md').read_text(encoding='utf-8')
            self.assertTrue(text.startswith('# ' + primary + '\n'))
            actual = [line.split('|')[1].strip() for line in text.splitlines() if line.startswith('| ')][2:]
            self.assertEqual(actual, children)

    def test_unknown_primary_is_rejected(self):
        self.report('其他/子类')
        self.assertTrue(any('Unknown primary' in e for e in self.check()))

    def test_unknown_secondary_and_extra_level_are_rejected(self):
        for prefix in ['04-AI模型/其他','04-AI模型/多模态模型与模型架构/厂商','04-AI模型/scripts']:
            with self.subTest(prefix=prefix):
                self.report(prefix)
                self.assertTrue(any('Invalid category' in e for e in self.check()))

    def test_missing_readme_is_rejected(self):
        self.report('04-AI模型/多模态模型与模型架构', None)
        self.assertTrue(any('missing README' in e for e in self.check()))

    def test_primary_report_requires_specific_reason(self):
        self.report('04-AI模型', '文章类型：综述／综合\n一级分类：04-AI模型\n一级直归理由：\n')
        self.assertTrue(any('needs survey' in e for e in self.check()))

    def test_root_report_is_rejected(self):
        self.report('')
        self.assertTrue(any('two levels' in e for e in self.check()))


if __name__ == '__main__':
    unittest.main()
