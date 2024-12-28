import os, json, csv, random

import pandas as pd

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


def dict_to_csv(file_name: str,file_path: str, data: dict):

    """A function that saves data in the form of a python dictionary to a csv file"""

    with open(file_path + file_name + ".csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["Statistic", "Value"])

        for key, value in data.items():
            writer.writerow([key, value])


def list_to_csv(file_name: str,file_path: str,column_name: str,data: list):
    """ a function that shuffles and saves data in the form of a list of strings to a CSV file"""

    random.shuffle(data)

    data = [elem for elem in data]

    dict = {column_name : data}

    df = pd.DataFrame(dict)

    df.to_csv(file_path + file_name + ".csv", index=False, encoding="utf-8")
