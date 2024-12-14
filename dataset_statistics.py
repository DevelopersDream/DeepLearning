def compute_init_wiki_stats(data: list) -> dict:
    """
    compute statistics for the initial dataset from Wikipedia

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


def compute_init_books_stats(data: list) -> dict:

    dataset_statistics = {}
    dataset_statistics["initial_books"] = len(data)
    dataset_statistics["initial_textWords_average"] = sum(
        len(book.split()) for book in data
    ) / len(data)
    dataset_statistics["initial_maxWords_num"] = max(len(book.split()) for book in data)
    dataset_statistics["initial_minWords_num"] = min(len(book.split()) for book in data)
    dataset_statistics["initial_textParagraphs_average"] = sum(
        len(book.split(". ")) for book in data
    ) / len(data)
    dataset_statistics["initial_maxParagraphs_num"] = max(
        len(book.split(". ")) for book in data
    )
    dataset_statistics["initial_minParagraphs_num"] = min(
        len(book.split(". ")) for book in data
    )

    return dataset_statistics


def compute_final_documents_stats(doc_list: list, dataset_statistics: dict ={}, dataset_name: str ="") -> dict:
    """
    compute statistics for the processed dataset

    """
    dataset_statistics["final_documents"] = len(doc_list)
    dataset_statistics["final_textWords_average"] = sum(
        len(elem.split()) for elem in doc_list
    ) / len(doc_list)
    dataset_statistics["final_text_maxWordsNum"] = max(
        len(elem.split()) for elem in doc_list
    )
    dataset_statistics["final_text_unigrams"] = sum(
        1 for elem in doc_list if elem.count(" ") == 0
    )
    dataset_statistics["final_text_bigrams"] = sum(
        1 for elem in doc_list if elem.count(" ") == 1
    )
    dataset_statistics["final_text_trigrams"] = sum(
        1 for elem in doc_list if elem.count(" ") == 2
    )
    dataset_statistics["final_text_longer_tengrams"] = sum(
        1 for elem in doc_list if elem.count(" ") > 9
    )

    print(f"Statistics for the dataset {dataset_name}")
    for key, value in dataset_statistics.items():
        print(f"{key.capitalize()} : {value}")

    return dataset_statistics
