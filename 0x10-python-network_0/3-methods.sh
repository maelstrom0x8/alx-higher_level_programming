#!/bin/bash
# Get all available methods
curl -sI -X OPTIONS "$1" | grep -i 'allow' | awk '{print $2}'
