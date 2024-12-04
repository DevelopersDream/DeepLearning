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


def compute_init_dataset_stats(data: list) -> dict:
    """
    compute statistics for the initial dataset

    """
    dataset_statistics = {}
    dataset_statistics["initial_documents"] = len(data)*2 #1 title and 1 text
    dataset_statistics["initial_textWords_average"] = sum(len(elem["text"].split()) for elem in data) / len(data)
    dataset_statistics["initial_text_maxWordsNum"] = max(len(elem["text"].split()) for elem in data)
    dataset_statistics["initial_text_nullPerc"] = sum(1 for d in data if len(d.get("text", "")) == 0)*100 / len(data)
    dataset_statistics["initial_titleWords_average"] = sum(len(elem["title"].split()) for elem in data) / len(data)
    dataset_statistics["initial_title_maxWordsNum"] = max(len(elem["title"].split()) for elem in data)
    dataset_statistics["initial_title_nullPerc"] = sum(1 for d in data if len(d.get("title", "")) == 0)*100 / len(data)
    return dataset_statistics


def compute_final_dataset_stats(dataset_statistics: list, doc_list: list) -> list:
    """
    compute statistics for the initial dataset

    """
    dataset_statistics["final_documents"] = len(doc_list)
    dataset_statistics["final_textWords_average"] = sum(len(elem.split()) for elem in doc_list) / len(doc_list)
    dataset_statistics["final_text_maxWordsNum"] = max(len(elem.split()) for elem in doc_list)

    return dataset_statistics
