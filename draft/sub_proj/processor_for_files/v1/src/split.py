import os
import re
from typing import List, Optional


def extract_last_component(filepath: str) -> str:
    if not filepath or not filepath.strip():
        raise ValueError("Empty path")
    
    normalized = os.path.normpath(filepath)
    
    if os.path.splitext(normalized)[1]:
        return os.path.basename(normalized)
    else:
        return os.path.basename(normalized.rstrip(os.sep))


def split_words(component: str) -> List[str]:
    if not component:
        return []
    
    words = re.findall(r'[A-Za-z]+', component)
    
    result = []
    for word in words:
        parts = re.findall(r'[A-Z]?[a-z]+|[A-Z]+(?=[A-Z][a-z]|\b)', word)
        result.extend([p for p in parts if len(p) > 1])
    
    return result


def normalize_path(filepath: str) -> str:
    return os.path.normpath(filepath).lower()


def normalize_word(word: str) -> str:
    return word.lower()