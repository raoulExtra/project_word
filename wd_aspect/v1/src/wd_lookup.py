import os
import json
import sys
from datetime import datetime, timezone
import requests
import time

WIKIDATA_API = 'https://www.wikidata.org/w/api.php'
LEXEME_NAMESPACE = 146

VALID_WORD_TYPES = {'verb', 'noun', 'adjective', 'adverb', 'preposition', 'pronoun', 'conjunction', 'interjection', 'article', 'prefix', 'suffix'}

LEXICAL_CATEGORY_MAP = {
    'verb': 'Q24905',
    'noun': 'Q110',
    'adjective': 'Q1065',
    'adverb': 'Q94',
    'preposition': 'Q34297',
    'pronoun': 'Q37924',
    'conjunction': 'Q34298',
    'interjection': 'Q34299',
    'article': 'Q214407',
}

CATEGORY_TO_QID = {v: k for k, v in LEXICAL_CATEGORY_MAP.items()}

def wd_lookup(word, word_type=None):
    headers = {'User-Agent': 'wd-lookup/1.0 (your-email@example.com)'}
    
    for attempt in range(3):
        try:
            search_params = {
                'action': 'query',
                'list': 'search',
                'srsearch': word,
                'srnamespace': LEXEME_NAMESPACE,
                'format': 'json'
            }
            response = requests.get(WIKIDATA_API, params=search_params, headers=headers, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            search_results = data.get('query', {}).get('search', [])
            if not search_results:
                return {'error': f'Word not found: {word}'}
            
            best_match = None
            if word_type and word_type.lower() in VALID_WORD_TYPES:
                target_category = LEXICAL_CATEGORY_MAP.get(word_type.lower())
                for result in search_results:
                    lexeme_id = result['title'].replace('Lexeme:', '')
                    entity_params = {
                        'action': 'wbgetentities',
                        'ids': lexeme_id,
                        'format': 'json'
                    }
                    entity_response = requests.get(WIKIDATA_API, params=entity_params, headers=headers, timeout=10)
                    entity_response.raise_for_status()
                    entity_data = entity_response.json()
                    lexeme = entity_data.get('entities', {}).get(lexeme_id, {})
                    if lexeme.get('lexicalCategory') == target_category:
                        best_match = result
                        break
            
            if not best_match:
                best_match = search_results[0]
            
            lexeme_title = best_match['title']
            lexeme_id = lexeme_title.replace('Lexeme:', '')
            
            entity_params = {
                'action': 'wbgetentities',
                'ids': lexeme_id,
                'format': 'json'
            }
            entity_response = requests.get(WIKIDATA_API, params=entity_params, headers=headers, timeout=10)
            entity_response.raise_for_status()
            entity_data = entity_response.json()
            
            lexeme = entity_data.get('entities', {}).get(lexeme_id, {})
            
            lemma = ''
            for lang_data in lexeme.get('lemmas', {}).values():
                if lang_data.get('language') == 'en':
                    lemma = lang_data.get('value', '')
                    break
            
            lexical_category_id = lexeme.get('lexicalCategory', '')
            lexical_category = CATEGORY_TO_QID.get(lexical_category_id, lexical_category_id.lower().replace('q', '') if lexical_category_id else 'unknown')
            
            homograph_ids = []
            forms = lexeme.get('forms', [])
            for form in forms:
                form_lexeme_id = form.get('id')
                if form_lexeme_id and form_lexeme_id != lexeme_id:
                    homograph_ids.append(form_lexeme_id)
            
            homograph_lexeme_ids = list(set(homograph_ids))
            
            return {
                'word': lemma,
                'lexeme_id': lexeme_id,
                'lexical_category': lexical_category,
                'language': 'en',
                'homograph_lexeme_ids': homograph_lexeme_ids
            }
        except requests.RequestException as e:
            if attempt == 2:
                return {'error': f'API error: {str(e)}'}
            time.sleep(0.5)
    
    return {'error': f'Word not found: {word}'}

def save_to_cache(word, data):
    lexical_category = data.get('lexical_category', 'verb')
    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'wd_cache', 'lang_en', lexical_category, word[0], f'wd_{word}.json')
    os.makedirs(os.path.dirname(path), exist_ok=True)
    data_with_timestamp = {**data, 'word': word, 'updated': datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')}
    with open(path, 'w') as f:
        json.dump(data_with_timestamp, f, indent=2)

def wd_lookup_batch(words, word_types=None):
    results = []
    if word_types is None:
        word_types = [None] * len(words)
    for i, word in enumerate(words):
        result = wd_lookup(word, word_types[i])
        if 'error' not in result:
            save_to_cache(word, result)
        results.append(result)
    return results

if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(description='Lookup word in Wikidata')
    parser.add_argument('word', help='Word to lookup')
    parser.add_argument('word_type', nargs='?', help='Word type (verb, noun, adjective, etc.)')
    parser.add_argument('--orig', choices=['wn'], help='Origin source (wn=WordNet)')
    
    args = parser.parse_args()
    
    result = wd_lookup(args.word, args.word_type)
    if 'error' not in result:
        save_to_cache(args.word, result)
    print(json.dumps(result))