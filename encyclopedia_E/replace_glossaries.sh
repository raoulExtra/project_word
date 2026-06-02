#!/bin/bash

# Replace "glossaries/" with "encyclopedia_E/" in file contents within encyclopedia_E folder

set -e

DIR="$(cd "$(dirname "$0")" && pwd)"

# Replace all occurrences of "glossaries/" with "encyclopedia_E/" in all files
find "$DIR" -type f -name "*.md" -exec sed -i 's|glossaries/|encyclopedia_E/|g' {} \;

echo "Done!"