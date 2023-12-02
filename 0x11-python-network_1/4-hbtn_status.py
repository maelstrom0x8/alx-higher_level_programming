#!/usr/bin/python3

"""
4-hbtn_status.py

This script sends a GET request to the URL
'https://alx-intranet.hbtn.io/status' using the requests library
and prints information about the response body.

Usage:
    $ python3 4-hbtn_status.py

Note:
    The script is designed to be run as a standalone program.

Dependencies:
    - Python 3
    - requests library

Example:
    $ python3 4-hbtn_status.py
    Body response:
        - type: <class 'str'>
        - content: <text content of the response>
"""

if __name__ == '__main__':
    import requests

    target_url = 'https://alx-intranet.hbtn.io/status'

    response = requests.get(target_url)
    print('Body response:')
    print('\t- type: ', type(response.text), sep='')
    print('\t- content: ', response.text, sep='')
