import numpy as np
import matplotlib.pyplot as plt
import constants as c
import os

def token_distribution(data:list, data_name:str):

    """ plot the distribution of the documents per number of tokens (5 token bins)"""

    data_name = " for " + data_name

    word_counts = [len(s.split()) for s in data]

    max_words = max(word_counts)
    bin_edges = np.arange(0, max_words + 5, 5)

    hist, bins = np.histogram(word_counts, bins=bin_edges)

    plt.figure()
    plt.bar(bins[:-1], hist, width=5, edgecolor="black", align="edge")
    plt.xlabel("Number of tokens per String")
    plt.ylabel("Number of documents")
    plt.title(f"Distribution of tokens per documents{data_name}")
    plt.savefig(os.path.join(c.IMAGES_PATH, data_name[5:] + " token distribution"))
    plt.close()