# API Failure Handling

## Scenario
Wikidata API is unreachable or returns an error response.

## Behavior
- Retry logic: 3 attempts with fixed 0.5s delay between retries
- Return JSON with error key: `{"error": "API error: <error_message>"}`
- Timeout: 10 seconds per request
- Do not create cache file for failed API calls

## Retry Logic
1. First request attempt
2. On failure: wait 0.5s, retry
3. Second request attempt
4. On failure: wait 0.5s, retry
5. Third request attempt
6. On failure: return error JSON

## Example
If network is unavailable:
Output: `{"error": "API error: Connection refused"}`