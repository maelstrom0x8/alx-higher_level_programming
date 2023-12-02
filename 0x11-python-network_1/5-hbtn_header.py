#!/usr/bin/python3


"""
5-hbtn_header.py

This script takes a URL as a command-line argument and sends a GET
request to the specified URL using the requests library.
It then prints the value of the 'X-Request-Id' header from the response.

Usage:
    $ python3 5-hbtn_header.py <URL>

Arguments:
    <URL>       The URL to which the GET request is sent.

Note:
    The script is designed to be run as a standalone program with
    a URL as a command-line argument.

Dependencies:
    - Python 3
    - requests library

Example:
    $ python3 5-hbtn_header.py https://example.com
    <X-Request-Id value from the response headers>
"""

if __name__ == '__main__':
    import requests
    import sys

    target_url = sys.argv[1]
    response = requests.get(url=target_url)
    print(response.headers.get('X-Request-Id'))
