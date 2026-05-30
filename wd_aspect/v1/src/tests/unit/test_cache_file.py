import pytest
import os
import json
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from wd_lookup import wd_lookup, save_to_cache

def test_creates_cache_file_at_correct_path():
    result = wd_lookup('help')
    save_to_cache('help', result)
    
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    expected_path = os.path.join(base_dir, 'wd_cache', 'lang_en', 'verb', 'h', 'wd_help.json')
    assert os.path.exists(expected_path), f"Cache file not found at {expected_path}"
    
    with open(expected_path) as f:
        cached = json.load(f)
    assert cached['lexeme_id'] == 'L1244'
    assert 'updated' in cached

def test_creates_cache_file_with_dynamic_category():
    result = wd_lookup('tree')
    if 'error' not in result:
        save_to_cache('tree', result)
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
        expected_path = os.path.join(base_dir, 'wd_cache', 'lang_en', result['lexical_category'], 't', 'wd_tree.json')
        assert os.path.exists(expected_path)