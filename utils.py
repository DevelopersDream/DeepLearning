import constants as c
import os, json


def one_json() -> list:
    """
    one_json() takes all the JSON files in the base path and return their union in a python list.
    """
    data = []

    files = os.listdir(c.SCN_JSON_PATH)

    for curr_file in files:
        with open(c.SCN_JSON_PATH + curr_file, "r") as file:
            for line in file:
                data.append(json.loads(line))

    return data
