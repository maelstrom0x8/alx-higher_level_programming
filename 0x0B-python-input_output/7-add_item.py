#!/usr/bin/python3

"""A script for loading and saving items to a JSON file.

This script allows you to load a list of items from a JSON file, add new
items provided as command-line arguments, and then save the updated list back
to the same JSON file.
"""

import sys

if __name__ == "__main__":
    json_i = \
        __import__('6-load_from_json_file')
    json_o = __import__('5-save_to_json_file')

    try:
        data = json_i.load_from_json_file('add_item.json')
    except FileNotFoundError:
        data = []
    data.extend(sys.argv[1:])
    json_o.save_to_json_file(data, 'add_item.json')
