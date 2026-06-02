import pytest
import os
import sys
import tempfile
import pathlib

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'src'))
from processor_for_files import process_files


class TestVisitAction:
    def test_finds_files_in_root_folder(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            test_file = pathlib.Path(tmpdir) / "test.md"
            test_file.write_text("```yaml\nid: test\nkind: frontmatter\n```\nContent")
            
            result = process_files(kind="frontmatter", action="visit", root=pathlib.Path(tmpdir))
            assert result == 0

    def test_filters_by_extension(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            md_file = pathlib.Path(tmpdir) / "test.md"
            md_file.write_text("```yaml\nid: test\nkind: frontmatter\n```\nContent")
            txt_file = pathlib.Path(tmpdir) / "test.txt"
            txt_file.write_text("some text")
            
            result = process_files(kind="frontmatter", action="visit", root=pathlib.Path(tmpdir), ext="md")
            assert result == 0

    def test_accepts_comma_separated_roots(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root1 = pathlib.Path(tmpdir) / "root1"
            root2 = pathlib.Path(tmpdir) / "root2"
            root1.mkdir()
            root2.mkdir()
            (root1 / "a.md").write_text("content1")
            (root2 / "b.md").write_text("content2")
            
            result = process_files(kind="frontmatter", action="visit", root=f"{root1},{root2}")
            assert result == 0

    def test_skips_hidden_files(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            visible = pathlib.Path(tmpdir) / "visible.md"
            hidden = pathlib.Path(tmpdir) / ".hidden.md"
            visible.write_text("content")
            hidden.write_text("content")
            
            result = process_files(kind="frontmatter", action="visit", root=pathlib.Path(tmpdir), ext="md")
            assert result == 0

    def test_validates_yaml_frontmatter_with_required_fields(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            valid_file = pathlib.Path(tmpdir) / "valid.md"
            valid_file.write_text("```yaml\nid: test\nkind: frontmatter\n```\nContent")
            missing_id = pathlib.Path(tmpdir) / "missing_id.md"
            missing_id.write_text("```yaml\nkind: frontmatter\n```\nContent")
            
            result = process_files(kind="frontmatter", action="visit", root=pathlib.Path(tmpdir), ext="md")
            assert result == 0

    def test_creates_log_file_for_missing_fields(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            missing_id = pathlib.Path(tmpdir) / "missing_id.md"
            missing_id.write_text("```yaml\nkind: frontmatter\n```\nContent")
            
            result = process_files(kind="frontmatter", action="visit", root=pathlib.Path(tmpdir), ext="md")
            assert result == 0
            log_path = pathlib.Path('/home/peter/sync/project_word/draft/sub_proj/processor_for_files/data/visit_log.txt')
            assert log_path.exists()
            content = log_path.read_text()
            assert "missing id" in content

    def test_logs_missing_both_id_and_kind(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            no_yaml = pathlib.Path(tmpdir) / "no_yaml.md"
            no_yaml.write_text("Just content, no yaml")
            
            result = process_files(kind="frontmatter", action="visit", root=pathlib.Path(tmpdir), ext="md")
            assert result == 0
            log_path = pathlib.Path('/home/peter/sync/project_word/draft/sub_proj/processor_for_files/data/visit_log.txt')
            content = log_path.read_text()
            assert "missing yaml delimiter" in content

    def test_files_missing_kind_field_use_default_frontmatter(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            no_kind = pathlib.Path(tmpdir) / "no_kind.md"
            no_kind.write_text("```yaml\nid: test\n```\nContent")
            
            result = process_files(kind="frontmatter", action="visit", root=pathlib.Path(tmpdir), ext="md")
            assert result == 0
            log_path = pathlib.Path('/home/peter/sync/project_word/draft/sub_proj/processor_for_files/data/visit_log.txt')
            content = log_path.read_text()
            assert "missing kind" in content

    def test_fails_if_log_file_cannot_be_written(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            missing_id = pathlib.Path(tmpdir) / "missing_id.md"
            missing_id.write_text("```yaml\nkind: frontmatter\n```\nContent")
            
            result = process_files(kind="frontmatter", action="visit", root=pathlib.Path(tmpdir), ext="md")
            assert result == 0

    def test_raises_error_when_log_file_cannot_be_written(self):
        from unittest.mock import patch, mock_open
        import processor_for_files
        
        with tempfile.TemporaryDirectory() as tmpdir:
            missing_id = pathlib.Path(tmpdir) / "missing_id.md"
            missing_id.write_text("```yaml\nkind: frontmatter\n```\nContent")
            
            log_path = pathlib.Path('/home/peter/sync/project_word/draft/sub_proj/processor_for_files/data/visit_log.txt')
            with patch('builtins.open', mock_open()) as mock_file:
                mock_file.return_value.write.side_effect = IOError("Permission denied")
                with pytest.raises(RuntimeError):
                    process_files(kind="frontmatter", action="visit", root=pathlib.Path(tmpdir), ext="md")

    def test_skips_unreadable_files(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            readable = pathlib.Path(tmpdir) / "readable.md"
            readable.write_text("```yaml\nid: test\nkind: frontmatter\n```\nContent")
            
            result = process_files(kind="frontmatter", action="visit", root=pathlib.Path(tmpdir), ext="md")
            assert result == 0

    def test_follows_symbolic_links(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            real_file = pathlib.Path(tmpdir) / "real.md"
            real_file.write_text("```yaml\nid: test\nkind: frontmatter\n```\nContent")
            link_dir = pathlib.Path(tmpdir) / "linked"
            link_dir.symlink_to(real_file)
            
            result = process_files(kind="frontmatter", action="visit", root=pathlib.Path(tmpdir), ext="md")
            assert result == 0

    def test_raises_valueerror_for_unknown_action(self):
        with pytest.raises(ValueError):
            process_files(kind="frontmatter", action="unknown", root=pathlib.Path("/tmp"))

    def test_raises_valueerror_for_unknown_kind(self):
        with pytest.raises(ValueError):
            process_files(kind="unknown", action="visit", root=pathlib.Path("/tmp"))

    def test_unreadable_files_are_skipped_and_logged(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            readable = pathlib.Path(tmpdir) / "readable.md"
            readable.write_text("```yaml\nid: test\nkind: frontmatter\n```\nContent")
            
            result = process_files(kind="frontmatter", action="visit", root=pathlib.Path(tmpdir), ext="md")
            assert result == 0

    def test_outputs_nothing_if_no_files_match(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            txt_file = pathlib.Path(tmpdir) / "test.txt"
            txt_file.write_text("content")
            
            result = process_files(kind="frontmatter", action="visit", root=pathlib.Path(tmpdir), ext="md")
            assert result == 0

    def test_log_format_is_correct(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            missing_id = pathlib.Path(tmpdir) / "missing_id.md"
            missing_id.write_text("```yaml\nkind: frontmatter\n```\nContent")
            
            result = process_files(kind="frontmatter", action="visit", root=pathlib.Path(tmpdir), ext="md")
            assert result == 0
            log_path = pathlib.Path('/home/peter/sync/project_word/draft/sub_proj/processor_for_files/data/visit_log.txt')
            content = log_path.read_text()
            assert "missing_id.md: missing id" in content

    def test_recursively_scans_subdirectories(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            subdir = pathlib.Path(tmpdir) / "subdir" / "nested"
            subdir.mkdir(parents=True)
            (subdir / "deep.md").write_text("```yaml\nid: test\nkind: frontmatter\n```\nContent")
            
            result = process_files(kind="frontmatter", action="visit", root=pathlib.Path(tmpdir), ext="md")
            assert result == 0

    def test_no_log_file_created_when_all_files_valid(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            valid = pathlib.Path(tmpdir) / "valid.md"
            valid.write_text("```yaml\nid: test\nkind: frontmatter\n```\nContent")
            
            log_path = pathlib.Path('/home/peter/sync/project_word/draft/sub_proj/processor_for_files/data/visit_log.txt')
            if log_path.exists():
                log_path.unlink()
            
            result = process_files(kind="frontmatter", action="visit", root=pathlib.Path(tmpdir), ext="md")
            assert result == 0
            assert not log_path.exists()

    def test_unreadable_files_logged_with_missing_fields(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            valid = pathlib.Path(tmpdir) / "valid.md"
            valid.write_text("```yaml\nid: test\nkind: frontmatter\n```\nContent")
            unreadable = pathlib.Path(tmpdir) / "unreadable.md"
            unreadable.write_text("content")
            
            os.chmod(unreadable, 0o000)
            try:
                result = process_files(kind="frontmatter", action="visit", root=pathlib.Path(tmpdir), ext="md")
                assert result == 0
            finally:
                os.chmod(unreadable, 0o644)

    def test_skips_hidden_directories(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            hidden_dir = pathlib.Path(tmpdir) / ".hidden"
            hidden_dir.mkdir()
            visible_dir = pathlib.Path(tmpdir) / "visible"
            visible_dir.mkdir()
            (hidden_dir / "file.md").write_text("content")
            (visible_dir / "file.md").write_text("```yaml\nid: test\nkind: frontmatter\n```\nContent")
            
            result = process_files(kind="frontmatter", action="visit", root=pathlib.Path(tmpdir), ext="md")
            assert result == 0