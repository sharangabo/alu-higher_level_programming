#!/usr/bin/python3
"""A base class"""

import json
import csv


class Base:
    """A base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert a list of dictionaries to a JSON string"""
        if list_dictionaries is None:
            return "[]"

        if len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a list of objects to a file"""
        file_name = cls.__name__ + ".json"
        new_list = []
        if list_objs:
            for i in list_objs:
                new_list.append(cls.to_dictionary(i))

        with open(file_name, mode="w") as myFile:
            myFile.write(cls.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """Convert a JSON string to a list of dictionaries"""
        if json_string is None:
            return []

        if len(json_string) == 0:
            return []

        list_dicts = json.loads(json_string)
        return list_dicts

    @classmethod
    def create(cls, **dictionary):
        """Create a new object"""
        if cls.__name__ == "Rectangle":
            dummy = cls(3, 2)
        if cls.__name__ == "Square":
            dummy = cls(3)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Load a list of objects from a file"""
        try:
            with open(cls.__name__ + ".json", "r") as file:
                content = file.read()
        except FileNotFoundError:
            return []

        ex_content = cls.from_json_string(content)
        context_list = []
        for instance_dict in ex_content:
            context_list.append(cls.create(**instance_dict))
        return context_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes a list of objects in CSV format."""
        with open(cls.__name__ + ".csv", mode="w") as f:
            writer = csv.writer(f)
            for obj in list_objs:
                writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes a list of objects from a CSV file."""
        try:
            with open(cls.__name__ + ".csv", mode="r") as f:
                reader = csv.reader(f)
                objects = []
                for row in reader:
                    objects.append(cls.create(**dict(row)))
            return objects
        except FileNotFoundError:
            return []