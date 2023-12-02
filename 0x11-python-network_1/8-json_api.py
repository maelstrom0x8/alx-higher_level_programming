#!/usr/bin/python3

"""
8-json_api.py

This script sends a POST request to a specified URL
('http://0.0.0.0:5000/search_user') with a search query parameter
using the requests library. It then processes the JSON response and prints
the user's ID and name if found.

Usage:
    $ python3 8-json_api.py [search_query]

Arguments:
    [search_query]  The search query parameter to include in
    the POST request. (Optional)

Note:
    The script is designed to be run as a standalone program with an
    optional search query.

Dependencies:
    - Python 3
    - requests library

Example:
    $ python3 8-json_api.py J
    [123] John Doe
    OR
    No result (if the search query has no match)
    OR
    Not a valid JSON (if the response is not in JSON format)
"""


if __name__ == '__main__':
    import requests
    import sys

    target_url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    data = {'q': q}
    response = requests.post(target_url, data)
    try:
        json = response.json()
        if not json:
            print('No result')
            sys.exit(0)
        print('[{}] {}'.format(json.get('id'), json.get('name')))

    except ValueError:
        print('Not a valid JSON')
