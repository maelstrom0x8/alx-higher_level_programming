#!/usr/bin/python3

"""
10-my_github.py

This script sends a GET request to the GitHub API
('https://api.github.com/user') with authentication using the
provided username and access token. It then processes the JSON response
and prints the user's ID if available.

Usage:
    $ python3 10-my_github.py <username> <access_token>

Arguments:
    <username>      The GitHub username for authentication.
    <access_token>  The GitHub access token for authentication.

Note:
    The script is designed to be run as a standalone program with a GitHub
    username and access token as command-line arguments.

Dependencies:
    - Python 3
    - requests library

Example:
    $ python3 10-my_github.py your_username your_access_token
    <GitHub user ID>
    OR
    None (if the response does not contain a user ID or if there's an error)
"""


if __name__ == '__main__':
    import requests
    import sys

    url = 'https://api.github.com/user'

    user, secret = sys.argv[1:]
    auth = (user, secret)
    response = requests.get(url, auth=auth)

    try:
        json_data = response.json()

        if 'id' in json_data:
            print(json_data['id'])
        else:
            print("None")

    except ValueError:
        print("None")
