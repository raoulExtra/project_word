import pytest
import os
import json
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from wd_lookup import wd_lookup, save_to_cache

def test_help_maps_to_l1244():
    result = wd_lookup('help')
    assert result['lexeme_id'] == 'L1244'
    assert result['lexical_category'] == 'verb'
    assert result['language'] == 'en'
    assert isinstance(result['homograph_lexeme_ids'], list)

def test_cli_interface():
    import subprocess
    src_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    result = subprocess.run(['python3', 'wd_lookup.py', 'help'], capture_output=True, text=True, cwd=src_dir)
    output = json.loads(result.stdout)
    assert output['lexeme_id'] == 'L1244'