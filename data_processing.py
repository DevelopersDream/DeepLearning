import utils as u


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


def data_proc_cleaning() -> list:

    """" load data from the data folder, process and clean it. Then return a list of documents for fine-tuning"""

    data = u.one_json()

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
