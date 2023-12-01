#!/bin/bash
# Check if a URL is provided as an argument
url=$1
response=$(curl -s -H "X-School-User-Id: 98" "$url")

echo "$response"
