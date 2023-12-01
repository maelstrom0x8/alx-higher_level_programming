#!/bin/bash
# Get all available methods
url=$1
allowed_methods=$(curl -sI -X OPTIONS "$url" | grep -i 'allow' | awk '{print $2}')

if [ -n "$allowed_methods" ]; then
    echo "$allowed_methods"
fi
