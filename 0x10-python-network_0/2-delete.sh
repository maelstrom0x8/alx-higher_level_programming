#!/bin/bash
# Sends DELETE request and display the response
url=$1
response=$(curl -s -X DELETE "$url")

echo "$response"
