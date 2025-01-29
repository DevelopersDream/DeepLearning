# SiciLLaMa: a fine-tuned version of LLaMa for the Sicilian language
This repository contains the code for SiciLLaMa, a Sicilian fine-tuned version of [unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit](https://huggingface.co/unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit) using [low-rank adaptation (LoRA)](https://arxiv.org/pdf/2106.09685).</br>
Llama-3.1-8B-Instruct-bnb-4bit is the baseline model for this study, the aim is to create an LLM capable of understanding and generating text in the Sicilian language.</br>
At first, a detailed description of the code and the process is presented, then some quantitative and qualitative results.

[link](#results)
# Table of Contents
- [Project Phases](#project-phases)
  - [Data ingestion](#phase-1-data-ingestion)
  - [Data cleaning and dataset generation](#phase-2-data-cleaning-and-dataset-generation)
  - [Fine-tuning](#phase-3-fine-tuning)
  - [Evaluation](#phase-4-evaluation)
  - [Demo](#bonus-demo)
- [Results](#results)
  - [Qualitative results](#qualitative-results)
  - [Quantitative results](#quantitative-results)



## Project Phases
Each phase is detailed, specifying which scripts and folders are involved.
### Phase 1: Data ingestion
- Collected Wikipedia pages from the Sicilian [Wikipedia dump](https://dumps.wikimedia.org/scnwiki/20241120/) of 20/11/2024 and extracted text information using Attardi's [WikiExtractor](https://github.com/attardi/wikiextractor)
- Manually collected 11 Books, available for research and personal use, from Google Books. The books were transformed into TXT files using the open-source program [Calibre](https://calibre-ebook.com/)
- The ingested files are available in the project's folder "raw data"

### Phase 2: Data cleaning and dataset generation
- **main.py** exploits all the other scripts to clean and generate multiple CSV files in the project's folder "final data"
- **data_processing.py** cleans the data by keeping only alphanumeric characters and punctuation. Markdown language, unwanted characters, URLs and other noise is removed from the samples.
- **dataset_statistics.py** generates statistics for each dataset in the project's folder "final data"
- **plots.py** generates the distribution of documents by number of words for each dataset.
- 3 kinds of datasets were generated to test the best strategy with limited data, each of them split into **train (85%)** and **test (15%)**:
  - **"full"** dataset, the original samples.
  - **"partial"** dataset, a version with fewer uni-grams and bi-grams (20% kept), and tri-grams (40% kept)
  - **"reduced"** dataset, a version with no uni-grams and bi-grams, and fewer tri-grams (40% kept)

### Phase 3: Fine-tuning
#### The fine-tuning phase has been conducted on Google Colab, to use the free available GPU.
- **fine-tuning.ipynb** contained in the project's folder "colab files/fine-tuning", produces a fine-tuned version of the baseline model.
- depending on the chosen parameters, it is possible to generate a different fine-tuned model (r_lora, target modules, train dataset)
- The r_lora parameter, representing the rank for the LoRa matrix, was chosen among three values: 32, 64, and 128.
- target modules, representing the set of modules to fine-tune, could be the default or an extended set (details in the PDF)
- train set, chosen among "full", "partial", and "reduced" (explained in phase 2)

### Phase 4: Evaluation
#### The evaluation phase has been conducted on Google Colab, to use the free available GPU.
- **evaluation.ipynb** contained in the project's folder "colab files/evaluation", evaluates all the saved models and produces a log file with perplexities.
- additional code is available at the end of the Colab file to evaluate also the baseline model.

### Bonus: Demo
It is possible, on Google Drive, to run a demo of the best-fine-tuned model using the **Test-model.ipynb** in the project's folder "colab files/try-model/".
The best model is available at this [Google Drive URL](https://drive.google.com/drive/folders/1OWJidhynEyP_gSemAKMHDvdxEiVmyvmj?usp=sharing).

## Results
best fine-tuned model with a perplexity of ... is ... </br>
worst fine-tuned model with a perplexity of ... is ... </br>
base-line model on X dataset with a perplexity of ... </br>

Comment on results: ... </br>

### Qualitative results

---

Question: something? </br>
**Best Model Answer**: some answer </br>
**Baseline Model answer**: some answer </br>

---




### Quantitive results
Results are ordered by ascending perplexity (lower is better). It is possible to observe that, the **"reduced"** dataset with the default configuration **"noEmbed"** of target modules produced the best results. The rank doesn't make significant differences between the models, probably due to the scarcity of data: if having more trainable parameters for the fine-tuning doesn't increase the performance, it is possible to hypothesize that the representational power of the model with fewer parameters **(rank 32)** is capable of capturing the essence of the relationships between data, given their limited amount; so, more parameters are not needed here.</br>
The baseline model shows higher perplexity () than the best-fine-tuned model, indicating an **effective improved capacity** of predicting the next token in Sicilian by SiciLLaMa.

| Model name                             | Perplexity  | Test set  |
|----------------------------------------|---------|---------|
| **r32_reduced_noEmbed**                    | **21.95**   | **reduced** |
| r128_reduced_noEmbed                   | 22.00   | reduced |
| r64_reduced_noEmbed                    | 22.03   | reduced |
| r128_partial_noEmbed                   | 22.71   | partial |
| r64_partial_noEmbed                    | 22.76   | partial |
| r32_partial_noEmbed                    | 22.77   | partial |
| r128_noEmbed                           | 25.75   | full    |
| r32_noEmbed                            | 25.77   | full    |
| r64_noEmbed                            | 25.82   | full    |
| r32_partial                            | 26.41   | partial |
| r64_partial                            | 26.42   | partial |
| r64                                    | 30.16   | full    |
| r32                                    | 30.22   | full    |
| **unsloth/llama-3-8b-Instruct-bnb-4bit**   | **33.74**   | **reduced** |
| unsloth/llama-3-8b-Instruct-bnb-4bit   | 34.96   | partial |
| unsloth/llama-3-8b-Instruct-bnb-4bit   | 37.21   | full    |






Deploy the model to production.

Monitor and update the system as needed.

il modello migliore è su [Google Drive](https://drive.google.com/drive/folders/1OWJidhynEyP_gSemAKMHDvdxEiVmyvmj?usp=drive_link)
