#!/usr/bin/env python3
import sys
import pathlib
import sqlite3


DB_PATH = pathlib.Path('/home/peter/sync/project_word/draft/sub_proj/processor_for_files/data/words.db')


def run_query(query: str) -> int:
    if not DB_PATH.exists():
        print("Error: Database not found. Run 'split' action first.", file=sys.stderr)
        return 1
    
    conn = sqlite3.connect(str(DB_PATH))
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description] if cursor.description else []
        
        if columns:
            print('\t'.join(columns))
            for row in results:
                print('\t'.join(str(v) if v is not None else '' for v in row))
        else:
            for row in results:
                print(row)
        return 0
    except Exception as e:
        print(f"Query error: {e}", file=sys.stderr)
        return 1
    finally:
        conn.close()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 query_processor.py \"SELECT * FROM words;\"", file=sys.stderr)
        sys.exit(1)
    
    query = sys.argv[1]
    sys.exit(run_query(query))