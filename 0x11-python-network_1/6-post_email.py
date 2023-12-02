#!/usr/bin/python3

"""
6-post_email.py

This script sends a POST request to a specified URL with an email
parameter using the requests library. It then prints the content
of the response.

Usage:
    $ python3 6-post_email.py <URL> <email>

Arguments:
    <URL>       The URL to which the POST request is sent.
    <email>     The email parameter value to include in the POST request.

Note:
    The script is designed to be run as a standalone program with a URL
    and email as command-line arguments.

Dependencies:
    - Python 3
    - requests library

Example:
    $ python3 6-post_email.py https://example.com/api/submit user@example.com
    <Content of the response>
"""


if __name__ == '__main__':
    import requests
    import sys

    target_url, email = sys.argv[1:3]

    data = {'email': email}
    response = requests.post(target_url, data)
    print(response.text)
