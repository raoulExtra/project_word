#!/bin/bash
# rename_glos.sh - Remove "glos_" prefix and "def_for_" prefix from files

cd "$(dirname "$0")" || exit 1

# List of folders with glos_ prefix
folders=(
    "glos_computing"
    "glos_engineering_of_ontologies"
    "glos_morphology"
    "glos_mathematics"
    "glos_linguistics"
    "glos_philospophy"
)

for folder in "${folders[@]}"; do
    if [ -d "$folder" ]; then
        new_name="${folder#glos_}"
        echo "Renaming folder: $folder -> $new_name"
        mv "$folder" "$new_name"
    fi
done

# Rename def_for_*.md files to def_*.md
echo "Renaming def_for_*.md files..."
find . -name "def_for_*.md" -type f | while read file; do
    new_name=$(echo "$file" | sed 's/def_for_/def_/')
    echo "Renaming: $file -> $new_name"
    mv "$file" "$new_name"
done

echo "Done!"