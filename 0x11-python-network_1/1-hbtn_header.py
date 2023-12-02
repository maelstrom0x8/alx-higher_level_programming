#!/usr/bin/python3

"""
1-hbtn_header.py

This script takes a URL as a command-line argument and sends a request to the
specified URL using the urllib library.
It then prints the value of the 'X-Request-Id' header from the response.

Usage:
    $ python3 1-hbtn_header.py <URL>

Arguments:
    <URL>       The URL to which the request is sent.

Note:
    The script is designed to be run as a standalone program with a URL as a
    command-line argument.

Dependencies:
    - Python 3
    - urllib library

Example:
    $ python3 1-hbtnheader.py https://example.com
    <X-Request-Id value from the response headers>
"""


if __name__ == '__main__':
    import sys
    from urllib import request

    target_url = sys.argv[1]

    with request.urlopen(url=target_url) as response:
        headers = response.headers
        print(headers.get('X-Request-Id'))
