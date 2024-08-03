#!/bin/bash

# Ensure script and log variables are set
if [ -z "$script" ]; then
    echo "Error: script variable is not set."
    exit 1
fi

if [ -z "$log" ]; then
    echo "Error: log variable is not set."
    exit 1
fi

# Run the Python script and log the output
python3 "$script" >> "${log}-$(date +"%F").log"
