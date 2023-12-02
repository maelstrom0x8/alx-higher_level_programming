#!/usr/bin/python3

"""
2-post_mail.py

This script sends a POST request to a specified URL with an email parameter
using the urllib library.
It then prints the UTF-8 decoded content of the response.

Usage:
    $ python3 post_mail.py <URL> <email>

Arguments:
    <URL>       The URL to which the POST request is sent.
    <email>     The email parameter value to include in the POST request.

Note:
    The script is designed to be run as a standalone program with a URL
    and email as command-line arguments.

Dependencies:
    - Python 3
    - urllib library

Example:
    $ python3 2-post_mail.py https://example.com/api/submit user@example.com
    <UTF-8 decoded content of the response>
"""


if __name__ == '__main__':
    import sys
    from urllib import request
    from urllib import parse

    target_url, email = sys.argv[1:3]
    values = {'email': email}
    data = parse.urlencode(values)
    data = data.encode('ascii')
    req = request.Request(target_url, data)

    with request.urlopen(req) as response:
        content_utf8 = response.read().decode('utf-8')
        print(content_utf8)
