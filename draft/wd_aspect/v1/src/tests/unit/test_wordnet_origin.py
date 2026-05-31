import pytest
import os
import json
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from wd_lookup import wd_lookup

def test_cli_with_origin_wordnet():
    import subprocess
    src_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    result = subprocess.run(['python3', 'wd_lookup.py', 'help', 'verb', '--orig', 'wn'], capture_output=True, text=True, cwd=src_dir)
    output = json.loads(result.stdout)
    assert output['lexeme_id'] == 'L1244'
    assert output['lexical_category'] == 'verb'