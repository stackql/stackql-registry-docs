#!/bin/bash

# Check if provider is passed as an argument
if [ -z "$1" ]; then
  echo "Error: provider is missing"
  exit 1
fi

# Define paths
source_dir="devdocs/$1-docs"
destination_dir="../docs/$1-docs"

# Check if source directory exists
if [ ! -d "$source_dir" ]; then
  echo "Error: $source_dir does not exist"
  exit 1
fi

# Create destination directory if it does not exist
if [ ! -d "$destination_dir" ]; then
  echo "Creating $destination_dir"
  mkdir -p "$destination_dir"
else
  echo "$destination_dir exists, overwriting"
fi

# Copy files
cp -r "$source_dir"/* "$destination_dir"

echo "Files copied successfully from $source_dir to $destination_dir"
