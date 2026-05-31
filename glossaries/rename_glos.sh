#!/bin/bash
# rename_glos.sh - Remove "glos_" prefix from glossary folder names

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
        echo "Renaming: $folder -> $new_name"
        mv "$folder" "$new_name"
    fi
done

echo "Done!"