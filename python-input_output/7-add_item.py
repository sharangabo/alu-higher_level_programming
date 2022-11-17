#!/usr/bin/python3
'''adds all arguments to a python list, and then save them to a file'''


import sys

if _name_ == "_main_":
    save_to_json_file = _import_('5-save_to_json_file').save_to_json_file
    load_from_json_file = _import_('6-load_from_json_file')\
        .load_from_json_file

    try:
        loadFile = load_from_json_file("add_item.json")
    except FileNotFoundError:
        loadFile = []

    arg = len(sys.argv)
    for i in range(1, arg):
        loadfile.append(sys.argv[i])
    save_to_json_file(loadfile, "add_item.json")
