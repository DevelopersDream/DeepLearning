import os, json


def one_json(dir) -> list:
    """
    one_json() takes all the JSON files in the base path and return their union in a python list.
    """
    data = []

    files = os.listdir(dir)

    for curr_file in files:
        with open(dir + curr_file, "r") as file:
            for line in file:
                data.append(json.loads(line))

    return data


def unique_characters(my_data) -> set:
    """return a set of unique characters besides letters and numbers in a string """

    unique_chars = set()

    for input_string in my_data:
        for char in input_string:

            if not char.isalnum():
                unique_chars.add(char)

    return unique_chars
