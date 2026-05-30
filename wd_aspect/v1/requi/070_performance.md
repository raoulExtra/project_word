# Performance Requirements

## Lookup Performance

### Cached Queries
- Response time: Under 2 seconds
- Cache hit rate: Above 80% for repeated queries

### Fresh API Calls
- Response time: Under 5 seconds
- Includes Wikidata API latency + processing

## Optimization Strategies

### Caching
- Store results in JSON files
- Path-based caching: `wd_cache/lang_en/<category>/<first_letter>/wd_<word>.json`
- Cache assumed stable (Wikidata lexeme data rarely changes)

### Retry Logic
- 3 retry attempts for network failures
- Fixed 0.5 second delay between retries
- Total max wait: ~1.5 seconds before failure response

## Concurrent Access
- No locking mechanism (simple file-based cache)
- Race conditions possible but acceptable for this use case