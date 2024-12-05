import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

def token_distribution(data):

    """ plot the distribution of the documents per number of tokens (5 token bins)"""

    word_counts = [len(s.split()) for s in data]

    max_words = max(word_counts)
    bin_edges = np.arange(0, max_words + 5, 5)

    hist, bins = np.histogram(word_counts, bins=bin_edges)

    plt.bar(bins[:-1], hist, width=5, edgecolor="black", align="edge")
    plt.xlabel("Number of tokens per String")
    plt.ylabel("Number of documents")
    plt.title("Distribution of tokens per documents")
    plt.show()
