#!/usr/bin/python3
'''adds all arguments to a python list and then saves them to a file:'''


import sys

if _name_ == "_main_":
    save_to_json_file = _import_('5-save_to_json_file').save_to_json_file
    load_from_json_file = _import_('6-load_from_json_file')\
        .load_from_json_file

    try:
        loadFile = load_from_json_file("add_item.json")
    except FileNotFoundError:
        loadFile = []

    argc = len(sys.argv)
    for idx in range(1, argc):
        loadFile.append(sys.argv[idx])
    save_to_json_file(loadFile, "add_item.json")
