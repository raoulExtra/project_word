import pytest
import os
import json
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from wd_lookup import wd_lookup_batch

def test_batch_processing():
    results = wd_lookup_batch(['help', 'run'])
    assert len(results) == 2
    assert results[0]['lexeme_id'] == 'L1244'
    assert 'lexeme_id' in results[1]

def test_batch_processing_with_word_types():
    results = wd_lookup_batch(['help', 'tree'], ['verb', 'noun'])
    assert len(results) == 2
    assert results[0]['lexeme_id'] == 'L1244'
    assert results[0]['lexical_category'] == 'verb'
    assert 'lexeme_id' in results[1]