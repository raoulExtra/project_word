import sys
import os
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))
from split import extract_last_component, split_words, normalize_path, normalize_word


def test_extracts_word_from_filename():
    path = "/some/path/to/myfile.txt"
    result = extract_last_component(path)
    assert result == "myfile.txt"


def test_extracts_last_directory_when_no_extension():
    path = "/some/path/to/mydirectory"
    result = extract_last_component(path)
    assert result == "mydirectory"


def test_raises_error_for_empty_path():
    with pytest.raises(ValueError):
        extract_last_component("")


def test_splits_words_from_camelcase():
    result = split_words("myFileName")
    assert "my" in result
    assert "File" in result
    assert "Name" in result


def test_splits_words_from_snake_case():
    result = split_words("my_file_name")
    assert "my" in result
    assert "file" in result
    assert "name" in result


def test_excludes_numbers_from_words():
    result = split_words("file123name")
    assert "file" in result
    assert "name" in result
    assert "123" not in result


def test_normalizes_path_to_lowercase():
    result = normalize_path("/Path/To/File.TXT")
    assert result == "/path/to/file.txt"


def test_normalizes_word_to_lowercase():
    result = normalize_word("MyWord")
    assert result == "myword"


def test_handles_trailing_slash():
    result = extract_last_component("/path/to/dir/")
    assert result == "dir"


def test_handles_consecutive_slashes():
    result = extract_last_component("/path//to")
    assert result == "to"


def test_handles_relative_path():
    result = extract_last_component("../parent/file.txt")
    assert result == "file.txt"