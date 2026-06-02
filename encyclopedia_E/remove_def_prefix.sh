#!/bin/bash

# Remove def_ prefix from files and their contents in encyclopedia_E folder

set -e

DIR="$(cd "$(dirname "$0")" && pwd)"

# Find all files with def_ prefix
find "$DIR" -type f -name "def_*" | while read -r file; do
    # Get the new filename (without def_ prefix)
    new_name=$(dirname "$file")/$(basename "$file" | sed 's/^def_//')
    
    # Replace "def_" with "" in file contents
    sed -i 's/def_//g' "$file"
    
    # Rename the file
    mv "$file" "$new_name"
    
    echo "Processed: $file -> $new_name"
done

echo "Done!"