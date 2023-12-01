#!/bin/bash
# Sends a request to that URL, and displays the size of the body of the response
url=$1
size=$(curl -sI "$url" | grep -i 'content-length' | awk '{print $2}' | tr -d '\r\n')

if [ -n "$size" ]; then
    echo "${size}"
fi
