import utils as u
import constants as c
import os, string, re

def compute_init_dataset_stats(data: list) -> dict:
    """
    compute statistics for the initial dataset

    """
    dataset_statistics = {}
    dataset_statistics["initial_documents"] = len(data) * 2  # 1 title and 1 text
    dataset_statistics["initial_textWords_average"] = sum(
        len(elem["text"].split()) for elem in data
    ) / len(data)
    dataset_statistics["initial_text_maxWordsNum"] = max(
        len(elem["text"].split()) for elem in data
    )
    dataset_statistics["initial_text_nullPerc"] = (
        sum(1 for d in data if len(d.get("text", "")) == 0) * 100 / len(data)
    )
    dataset_statistics["initial_titleWords_average"] = sum(
        len(elem["title"].split()) for elem in data
    ) / len(data)
    dataset_statistics["initial_title_maxWordsNum"] = max(
        len(elem["title"].split()) for elem in data
    )
    dataset_statistics["initial_title_nullPerc"] = (
        sum(1 for d in data if len(d.get("title", "")) == 0) * 100 / len(data)
    )
    return dataset_statistics

def compute_final_dataset_stats(dataset_statistics: list, doc_list: list) -> list:
    """
    compute statistics for the processed dataset

    """
    dataset_statistics["final_documents"] = len(doc_list)
    dataset_statistics["final_textWords_average"] = sum(len(elem.split()) for elem in doc_list) / len(doc_list)
    dataset_statistics["final_text_maxWordsNum"] = max(len(elem.split()) for elem in doc_list)
    dataset_statistics["final_text_unigrams"] = sum(1 for elem in doc_list if elem.count(" ") == 0)
    dataset_statistics["final_text_bigrams"] = sum(1 for elem in doc_list if elem.count(" ") == 1)
    dataset_statistics["final_text_trigrams"] = sum(1 for elem in doc_list if elem.count(" ") == 2)
    dataset_statistics["final_text_longer_tengrams"] = sum(1 for elem in doc_list if elem.count(" ") >9)

    return dataset_statistics


def wiki_data_processing() -> list:

    """" load data from the data folder, process and clean it. Then return a list of documents for fine-tuning"""

    data = u.one_json(c.SCN_JSON_PATH)

    discard_ids = {"1", "5604", "5605"} #not sicilian and only number documents

    data = [d for d in data if d.get("id") not in discard_ids]

    dataset_statistics = compute_init_dataset_stats(data)

    doc_list = []

    for elem in data: #data pre-processing and cleaning

        doc_list.append([elem["title"].lower()])  # no /n in titles, converting the single string in a list

        if elem["text"] != "":

            if elem["text"].count(" ") < 512: # 512 tokens
                doc_list.append(elem["text"].lower().split("\n")) # a different document for every /n
            else:
                doc_list.append(elem["text"].lower().split(".")) # a different document for every .

    doc_list = [item for sublist in doc_list for item in sublist] #list of lists -> list

    del data

    dataset_statistics = compute_final_dataset_stats(dataset_statistics, doc_list)

    print(dataset_statistics)

    return doc_list


def books_data_processing() -> list:

    data = []

    files = os.listdir(c.SCN_BOOKS_PATH)

    for file in files:

        # vangelo special case index
        if file[:7] == "Vangelo":
            vangelo_pos = len(data)

        with open(c.SCN_BOOKS_PATH + file, "r", encoding="utf-8", errors="replace") as file:
            data.append(file.read())   

    characters_to_keep = string.punctuation + " \n«»"

    for char in "}{)(=][_~-/*@\^|+":

        characters_to_keep = characters_to_keep.replace(char, "") #the characters to keep

    # Vangelo special case
    if vangelo_pos is not None:

        vangelo_text = data[vangelo_pos]

        # remove numbers
        vangelo_text = "".join(char for char in vangelo_text if not char.isnumeric())

        # each paragtraph is divided by "CAP. " in this book
        vangelo_text = vangelo_text.replace("CAP.", "ENDPARAGRAPH")

        data[vangelo_pos] = vangelo_text

    clean_data = []

    for input_string in data:

        # keep only selected characters and alphanumerics
        clean_data.append("".join(char for char in input_string if char in characters_to_keep or char.isalnum()))

        # remove multiple blank spaces
        clean_data[-1] = " ".join(clean_data[-1].split(" "))

        # remove eventual initial blank space in each line.
        clean_data[-1] = "\n".join(line.lstrip() for line in clean_data[-1].splitlines())

        # divide the books in paragraphs or meaningful sentences
        clean_data[-1] = re.sub(r"\n{2,}", "ENDPARAGRAPH", clean_data[-1])

    return clean_data
