import utils as u
import constants as c
import dataset_statistics as dstat
import plots as p
import os, string, re

def wiki_data_processing() -> list:

    """" load data in the form of JSON documents from the data folder, process and clean it. Then return a list of documents for fine-tuning"""

    dataset_name = 'Wikipedia'

    data = u.one_json(c.SCN_WIKIPEDIA_PATH)

    # not sicilian and only number documents
    discard_ids = {"1", "5604", "5605"} 

    data = [d for d in data if d.get("id") not in discard_ids]

    dataset_statistics = dstat.compute_init_wiki_stats(data)

    doc_list = []

    for elem in data:

        doc_list.append([elem["title"].lower()]) 

        if elem["text"] != "":

            # 512 tokens is the chosen max length
            if elem["text"].count(" ") < 512:
                # a different document for every /n
                doc_list.append(elem["text"].lower().split("\n"))
            else:
                # a different document for every dot
                doc_list.append(elem["text"].lower().split("."))

    doc_list = [item.capitalize() for sublist in doc_list for item in sublist]

    del data

    dataset_statistics = dstat.compute_final_documents_stats(doc_list = doc_list,dataset_statistics = dataset_statistics, dataset_name=dataset_name)

    p.token_distribution(doc_list, dataset_name)

    return doc_list

def books_data_processing() -> list:

    """" load books in TXT format, remove all the characters besides punctuaction and alphanumerics, format
    them in paragraphs and return them into a list of strings"""

    dataset_name = "books"
    data = []

    files = os.listdir(c.SCN_BOOKS_PATH)

    for file in files:

        # vangelo special case index
        if file[:7] == "Vangelo":
            vangelo_pos = len(data)

        with open(c.SCN_BOOKS_PATH + file, "r", encoding="utf-8", errors="replace") as file:
            data.append(file.read())   

    dataset_statistics = dstat.compute_init_books_stats(data)

    characters_to_keep = string.punctuation + " \n«»"

    #characters that will be removed
    for char in "}{)(=][_~-/*@\^|+<>":

        characters_to_keep = characters_to_keep.replace(char, "")

    # Vangelo special case
    if vangelo_pos is not None:

        vangelo_text = data[vangelo_pos]

        # remove numbers
        vangelo_text = "".join(char for char in vangelo_text if not char.isnumeric())

        # each paragraph is divided by "CAP. " in this book
        vangelo_text = vangelo_text.replace("CAP.", "ENDPARAGRAPH")

        data[vangelo_pos] = vangelo_text

    clean_data = []
    doc_list = []

    for input_string in data:

        # keep only selected characters and alphanumerics
        clean_data.append("".join(char for char in input_string if char in characters_to_keep or char.isalnum()))

        # substitute \n character with blank spaces.
        clean_data[-1] = clean_data[-1].replace("\n"," ")

        # remove multiple blank spaces
        clean_data[-1] = re.sub(r"\s{2,}", " ", clean_data[-1])

        # divide the books in paragraphs after each dot, excluding multiple subsequent dots
        clean_data[-1] = clean_data[-1].replace(". ", ".ENDPARAGRAPH")

        # split in paragraphs
        doc_list.append(clean_data[-1].split("ENDPARAGRAPH"))

    del data, clean_data

    new_doc_list = []

    for book in doc_list:
        for paragraph in book:

            # at least 4 characters
            if len(paragraph) > 3:

                if paragraph[0] == " ":
                    new_doc_list.append(paragraph[1:].capitalize())
                else:
                    new_doc_list.append(paragraph.capitalize())

    del doc_list

    dataset_statistics = dstat.compute_final_documents_stats(doc_list = new_doc_list, dataset_statistics = dataset_statistics, dataset_name=dataset_name)

    p.token_distribution(new_doc_list, dataset_name)

    return new_doc_list

def full_data_processing() -> list:

    data = wiki_data_processing()

    data.extend(books_data_processing())

    p.token_distribution(data,"full data")

    dstat.compute_final_documents_stats(data,dataset_name='"full data"')

    return data
