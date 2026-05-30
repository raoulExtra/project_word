import pytest
import os
import json
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from wd_lookup import wd_lookup

def test_unknown_word_returns_error_json():
    result = wd_lookup('xyznonexistentword12345')
    assert result == {'error': 'Word not found: xyznonexistentword12345'}