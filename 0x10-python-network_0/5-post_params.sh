#!/bin/bash
# Check if a URL is provided as an argument
url=$1
email="test@gmail.com"
subject="I will always be here for PLD"

response=$(curl -s -X POST -d "email=$email&subject=$subject" "$url")

echo "$response"
