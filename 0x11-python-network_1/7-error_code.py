#!/usr/bin/python3

"""
7-error_code.py

This script sends a GET request to a specified URL using the requests library
and prints an error message
if the HTTP response status code indicates an error (status code 400 or
higher).

Usage:
    $ python3 7-error_code.py <URL>

Arguments:
    <URL>       The URL to which the GET request is sent.

Note:
    The script is designed to be run as a standalone program with
    a URL as a command-line argument.

Dependencies:
    - Python 3
    - requests library

Example:
    $ python3 7-error_code.py https://example.com
    Error code: <HTTP error code>
    OR
    (No output if the response status code is below 400)
"""


if __name__ == '__main__':
    import requests
    import sys

    target_url = sys.argv[1]

    response = requests.get(target_url)
    if response.status_code >= 400:
        print('Error code: {}'.format(response.status_code))
