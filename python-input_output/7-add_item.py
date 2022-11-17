#!/usr/bin/python3
"""adds all arguments to a Python list, and then save them to a file:"""


import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file') \
        .load_from_json_file

    try:
        loadFile = load_from_json_file("add_item.json")
    except FileNotFoundError:
        loadFile = []

    arg = len(sys.argv)
    for i in range(1, arg):
        loadFile.append(sys.arg[i])
    save_to_json_file(loadFile, "add_item.json")
