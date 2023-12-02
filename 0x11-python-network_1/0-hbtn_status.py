#!/usr/bin/python3

"""
0-hbtn_status.py

This script sends a request to the URL 'https://alx-intranet.hbtn.io/status'
using the urllib library and prints information about the response body.

Usage:
    $ python3 0-hbtn_status.py

Note:
    The script is designed to be run as a standalone program.

Dependencies:
    - Python 3
    - urllib library

Example:
    $ python3 0-hbtn_status.py
    Body response:
        - type: <class 'bytes'>
        - content: <raw content of the response>
        - utf8 content: <decoded content of the response in UTF-8>
"""

if __name__ == '__main__':

    from urllib import request

    target_url = 'https://alx-intranet.hbtn.io/status'

    with request.urlopen(url=target_url) as con:
        raw = con.read()
        utf = raw.decode('utf-8')
        print('Body response:')
        print(' - type: ', type(raw), sep='')
        print(' - content: ', raw, sep='')
        print(' - utf8 content: ', utf, sep='')
