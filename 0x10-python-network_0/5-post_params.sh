#!/bin/bash
# Check if a URL is provided as an argument
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
