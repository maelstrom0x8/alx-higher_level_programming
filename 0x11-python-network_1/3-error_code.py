#!/usr/bin/python3

"""
3-error_code.py

This script sends a request to a specified URL using the urllib library
and prints the UTF-8 decoded content of the response. If an HTTP error
occurs during the request, it catches the error and prints
the associated error code.

Usage:
    $ python3 3-error_code.py <URL>

Arguments:
    <URL>       The URL to which the request is sent.

Note:
    The script is designed to be run as a standalone program with a
    URL as a command-line argument.

Dependencies:
    - Python 3
    - urllib library

Example:
    $ python3 3-error_code.py https://example.com
    <UTF-8 decoded content of the response>
    OR
    Error code: <HTTP error code>
"""


if __name__ == '__main__':
    import sys
    from urllib import request
    from urllib import error

    target_url = sys.argv[1]
    try:
        with request.urlopen(url=target_url) as response:
            content_utf8 = response.read().decode('utf-8')
            print(content_utf8)
    except error.HTTPError as e:
        print('Error code: {}'.format(e.code))
