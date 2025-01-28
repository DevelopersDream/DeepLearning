# SiciLLaMa: a fine-tuned version of LLaMa for the Sicilian language
This repository contains the code for SiciLLaMa, a Sicilian fine-tuned version of [unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit](https://huggingface.co/unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit) using [low-rank adaptation (LoRA)](https://arxiv.org/pdf/2106.09685).</br>
Llama-3.1-8B-Instruct-bnb-4bit is the baseline model for this study, the aim is to create an LLM capable of understanding and generating text in the Sicilian language.</br>
At first, a detailed description of the code and the process is presented, then some quantitative and qualitative results.


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
- 3 kinds of datasets were generated, each of them split into **train (85%)** and **test (15%)**:
  - **"full"** dataset, the original samples.
  - **"partial"** dataset, a version with fewer uni-grams and bi-grams (20% kept), and tri-grams (40% kept)
  - **"reduced"** dataset, a version with no uni-grams and bi-grams, and fewer tri-grams (40% kept)

### Phase 3: Fine-tuning
#### The fine-tuning phase has been conducted on Google Colab, to use the free available GPU.
- **fine-tuning.ipynb** contained in the project's folder "colab files/fine-tuning", produces a fine-tuned version of the baseline model.
- depending on the chosen parameters is possible to generate a different fine-tuned model (r_lora, target modules, train dataset)

### Phase 4: Evaluation
#### The evaluation phase has been conducted on Google Colab, to use the free available GPU.
- **evaluation.ipynb** contained in the project's folder "colab files/evaluation", evaluates all the saved models and produces a log file with perplexities.
- additional code is available at the end to evaluate also the baseline model.

### Bonus: Demo
It is possible to run a demo of the best-fine-tuned model using the **Test-model.ipynb** in the project's folder "colab files/try-model/" on Google Drive.
The best model is available at this [Google Drive URL](https://drive.google.com/drive/folders/1OWJidhynEyP_gSemAKMHDvdxEiVmyvmj?usp=sharing).

## Results
best fine-tuned model with a perplexity of ... is ... </br>
worst fine-tuned model with a perplexity of ... is ... </br>
base-line model on X dataset with a perplexity of ... </br>

Comment on results: ... </br>

Qualitative results

---

Question: something? </br>
**Best Model Answer**: some answer </br>
**Baseline Model answer**: some answer </br>

---

Quantitive results

| Model name | Perplexity | Test set |
|----------|----------|----------|
| Row 1    | Data 1   | Data 2   |
| Row 2    | Data 3   | Data 4   |
| Row 3    | Data 5   | Data 6   |
| Row 4    | Data 7   | Data 8   |
| Row 5    | Data 9   | Data 10  |
| Row 6    | Data 11  | Data 12  |
| Row 7    | Data 13  | Data 14  |
| Row 8    | Data 15  | Data 16  |
| Row 9    | Data 17  | Data 18  |
| Row 10   | Data 19  | Data 20  |
| Row 11   | Data 21  | Data 22  |
| Row 12   | Data 23  | Data 24  |
| Row 13   | Data 25  | Data 26  |
| Row 14   | Data 27  | Data 28  |
| Row 15   | Data 29  | Data 30  |
| Row 16   | Data 31  | Data 32  |


Deploy the model to production.

Monitor and update the system as needed.

il modello migliore è su [Google Drive](https://drive.google.com/drive/folders/1OWJidhynEyP_gSemAKMHDvdxEiVmyvmj?usp=drive_link)
