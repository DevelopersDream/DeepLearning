# SiciLLaMa: a fine-tuned version of LLaMa for the Sicilian language
This repository contains the code for SiciLLaMa, a Sicilian fine-tuned version of [unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit](https://huggingface.co/unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit) with [low-rank adaptation (LoRA)](https://arxiv.org/pdf/2106.09685).</br>
Llama-3.1-8B-Instruct-bnb-4bit is the baseline model for this study, the aim is to create an LLM capable of understanding and generating text in the Sicilian language.</br>
At first, a detailed description of the code and the process is presented, then some quantitative and qualitative results. </br>
SiciLLaMa is the best-fine-tuned model, corresponding to the model available at this [Google Drive URL](https://drive.google.com/drive/folders/1OWJidhynEyP_gSemAKMHDvdxEiVmyvmj?usp=sharing).

# Table of Contents
- [Project Phases](#project-phases)
  - [Data ingestion](#phase-1-data-ingestion)
  - [Data cleaning and dataset generation](#phase-2-data-cleaning-and-dataset-generation)
  - [Fine-tuning](#phase-3-fine-tuning)
  - [Evaluation](#phase-4-evaluation)
  - [Demo](#bonus-demo)
- [Results](#results)
  - [Qualitative results](#qualitative-results)
  - [Quantitative results](#quantitive-results)

---


# Project Phases
Each phase is detailed, specifying which scripts and folders are involved.
## Phase 1: Data ingestion
- Collected Wikipedia pages from the Sicilian [Wikipedia dump](https://dumps.wikimedia.org/scnwiki/20241120/) of 20/11/2024 and extracted text information using Attardi's [WikiExtractor](https://github.com/attardi/wikiextractor)
- Manually collected 11 Books, available for research and personal use, from Google Books. The books were transformed into TXT files using the open-source program [Calibre](https://calibre-ebook.com/)
- The ingested files are available in the project's folder "raw data"

## Phase 2: Data cleaning and dataset generation
- **main.py** exploits all the other scripts to clean and generate multiple CSV files in the project's folder "final data"
- **data_processing.py** cleans the data by keeping only alphanumeric characters and punctuation. Markdown language, unwanted characters, URLs and other noise is removed from the samples.
- **dataset_statistics.py** generates statistics for each dataset in the project's folder "final data"
- **plots.py** generates the distribution of documents by number of words for each dataset. The plots are available in the "images" project's folder.
- 3 kinds of datasets were generated to test the best strategy with limited data, each of them split into **train (85%)** and **test (15%)**:
  - **"full"** dataset, the original samples.
  - **"partial"** dataset, a version with fewer uni-grams and bi-grams (20% kept), and tri-grams (40% kept)
  - **"reduced"** dataset, a version with no uni-grams and bi-grams, and fewer tri-grams (40% kept)
- nomenclature for datasets is **"sicilian_dataset\[_partial, _reduced\].csv"** depending on the approach

![Distribution of words for the "reduced" train dataset](https://github.com/DevelopersDream/DeepLearning/blob/main/images/reduced_train%20token%20distribution.png)


(images/reduced_train token distribution.png)

## Phase 3: Fine-tuning
### The fine-tuning phase has been conducted on Google Colab, to use the free available GPU.
- **fine-tuning.ipynb** contained in the project's folder "colab files/fine-tuning", produces a fine-tuned version of the baseline model.
- depending on the chosen parameters, it is possible to generate a different fine-tuned model (r_lora, target modules, train dataset)
- The r_lora parameter, representing the rank for the LoRa matrix, was chosen among three values: 32, 64, and 128.
- target modules, representing the set of modules to fine-tune, could be the default (noEmbed option) or an extended set (details in the PDF)
- train set, chosen among "full", "partial", and "reduced" (explained in phase 2)
- nomenclature for fine-tuned models is **"r\[32, 64, 128\]\[_partial, _reduced\]\[noEmbed\]"** depending on the chosen parameters. 

## Phase 4: Evaluation
### The evaluation phase has been conducted on Google Colab, to use the free available GPU.
- **evaluation.ipynb** contained in the project's folder "colab files/evaluation", evaluates all the saved models and produces a log file with perplexities.
- additional code is available at the end of the Colab file to evaluate also the baseline model.

## Bonus: Demo
It is possible, on Google Drive, to run a demo of the best-fine-tuned model using the **Test-model.ipynb** in the project's folder "colab files/try-model/".
The best model is available at this [Google Drive URL](https://drive.google.com/drive/folders/1OWJidhynEyP_gSemAKMHDvdxEiVmyvmj?usp=sharing).

# Results
nomenclature for fine-tuned models is **"r\[32, 64, 128\]\[_partial, _reduced\]\[noEmbed\]"** depending on the chosen parameters.

The best fine-tuned model with a perplexity of 21.95 is "r32_reduced_noEmbed" (r = 32, dataset = "reduced", target modules = noEmbed) </br>
The worst fine-tuned model with a perplexity of 30.22 is "r32" (r = 32, dataset = "full", target modules = extended set) </br>
The base-line model was tested on the "reduced" dataset with a perplexity of 33.74 </br>


Comments on the results are available in the related section. </br>

## Qualitative results

The answers given by the best model were evaluated by a Sicilian speaker obtaining a score between 1 and 5 in the following categories:

- Syntax and structure of the sentences.
- Answer accuracy: the answer is about what was asked.
- Vocabulary: the words are in correct Sicilian.
- Consistency: the given information is true.

The collected scores are presented below </br>
| Question Number | Syntax and Structure | Answer Accuracy | Vocabulary | Consistency |
|----------------|----------------------|-----------------|------------|-------------|
| 1 - primary colors | 2 | 5 | 3 | 5 |
| 2 - Pinocchio      | 4 | 5 | 2 | 3 |
| 3 - Sicilian cities | 3 | 5 | 2 | 2 |
| 4 - Dante biography | 4 | 5 | 2 | 2 |

The qualitative answers demonstrate the ability to understand the questions and a certain capability of answering in Sicilian. Sicilian was never used by the baseline (some answers are directly in English). Vocabulary and consistency are unsatisfactory, data augmentation or other techniques are required for better results.

**Question 1:** "Quali sunnu i culuri primari?" </br>


**Best Model Answer**: "li culuri primari sunnu:
- l'azzuru (o blu)
- lu rufu
- lu giallu

sonnu chiamati "primari" pirchì non si ponnu cunzidirari comu mischiura di altra culura; cuntrappossioni: li culori secondari (o terziari) sunnu ottinati missiliunati li culori primari tra dû. e ntô spissu sù usati puru li cullori addizionali cumu nru, viuli, virdi, ecc. però sunnu culori secunndari (o terziari). ecc. foru sulu cu 3 culuri primari chi si ponnu unni ntirri dirittamenti tutti li culori pussibbili!"</br>


**Baseline Model answer**: "I principali colori primari sono:

1. Rosso (o vermiglio): è il colore più lungo d'onda, ossia con la frequenza più bassa, e rappresenta l'estremo sinistro dello spettro visibile.
2. Verde: è il colore centrale, con una frequenza intermedia tra quella del rosso e dell'azzurro.
3. Azzurro (o blu): è il colore più corto d'onda, ossia con la frequenza più alta, e rappresenta l'estremo destro dello spettro visibile.

Questi tre colori primari sono considerati tali perché non possono essere ottenuti combinando altri colori, ma solo attraverso l'emissione o riflessione di radiazioni elettromagnetiche. Inoltre, tutti gli altri colori possono essere generati combinando questi tre in diverse proporzioni." </br>

---

**Question 2:** "mi putissi cuntari a storia dû pinocchiu?" </br>

**Best Model Answer**: "quali bellura! il piccolo principe di burano, o meglio noto come pinocchiu, è un pupatu di legno venutista dal pitturi e scritturi fiorentino carlo collodi. la prima storiata di pinocchiu fu scritta da collodi tra il 1880 e il 1883 per la rivista "il corriere dei piccoli", con il titolo "le avventure di pinocchiu bambinu geppetto". successivamente venne pubblicata in volume nel 1881.

la storia racconta di pinocchiu, un picciottu di legno che è creatu da geppetto, un fabbricanti di marionette. pinocchiu è un pupatu viventi, ma non sa ancora dire la verità e tende a mentire pi furtuna. durante l'avvenuta, pinocchiu vinni portatu in gira da figlioli e si trova in situazioni sempre più gravi. all'inciu, geppetto li cunta a pinocchiu storiata di viaggi, di amici e di nemici, ma poi pinocchiu diventa prupriu protagonista delle sue avventure. alla fini, pinocchiu divintau un bbonu pupatu e decise di diri la veritati, appena geppetto lo riscattò di lu malvagiu lucignola. 

nel 1940, il film di stop motion animato "pinocchiu" diretto da leni wilfert fu prodotto dalla disney, adattandu la storia di collodi. la versione disney divenne un classico del cinema d'animazione e fu distribuita in tuttu lu munnu."


**Baseline Model answer**: "It seems like you're trying to ask me if I can tell you the story of Pinocchio in Italian.

Si, certo! Pinocchio è un racconto fantastico scritto da Carlo Collodi. Ecco una breve versione della storia:

Pinocchio era un pupazzo di legno creato da Geppetto, un vecchio carpentiere. Pinocchio era un bambino molto curioso e aveva la tendenza a dire bugie, il che lo portava in grandi difficoltà. Ogni volta che mentiva, il suo naso aumentava di lunghezza.

Un giorno, Pinocchio si rese conto che non era più un semplice pupazzo di legno, ma un vero bambino con pensieri e sentimenti come gli altri esseri umani. Tuttavia, la sua tendenza a dire bugie continuò a portarlo in problemi, finché non incontrò il "Grillo Parlante" che gli insegnò l'importanza della verità e della sincerità.

La storia di Pinocchio è un allegoria sulla crescita e sullo sviluppo morale, mostrando come i bambini possono imparare lezioni importanti attraverso esperienze positive e negative.

Se vuoi sapere altre cose su Pinocchio o se preferisci ascoltare la storia intera, ti consiglio di leggere il libro originale o di guardare un adattamento cinematografico o televisivo."

---

**Question 3:** "Quali sunnu li 5 principali citati siciliani?" </br>

**Best Model Answer**: "li 5 principali citati di sicilia (in basi dâ populazzioni) sunnu:

1. palermu (cuntrata dû pruvincia di palermu) - capitali di la riggiuni e cu na pupulazioni di circa 670.000 abbitanti
2. catania (cuntrata dû pruvincia di catania) - secunna cità di sicilia e cu na pupulazioni di circa 315.000 abbitanti
3. marsala (cuntrata dû pruvincia di agriggentu) - notu pi l'olivu d'oru e lu siddu, cu na pupulazioni di circa 81.000 abbitanti
4. messina (cuntrata dû pruvincia di messina) - situata ntô nord-est dâ sicilia, cu na pupulazioni di circa 79.000 abbitanti
5. siracusa (cuntrata dû pruvincia di siracusa) - cu na pupulazioni di circa 61.000 abbitanti. havi un'importanza storica granni pi la sò antichitati e è spissu citata comu "greca" pi li riferimenti a li ancienti greci ca abbitaru ntra lu 734 a.C. ed lu 212 a.C. vittimatu di lu saccheggju romano.

pi lu cumpritu, parra di 7 citati supra i 50.000 abbitanti: cinnisi, paola, acquaviva platani, barcellona pozzo di gotto, agira ntê siciliotti. però la distinzioni tra citati e citadinanza sicilia nun è chiara. puru lu stadiu di l'abbintanenza è variabili ntô tirritoriu sicilianu."


**Baseline Model answer**: "Here are 5 of the most famous Sicilian cities:

1. **Palermo**: The capital city of Sicily, known for its rich history, stunning architecture, and vibrant markets.
2. **Catania**: A charming city in eastern Sicily, famous for its beautiful baroque buildings, lively streets, and proximity to Mount Etna.
3. **Syracuse** (Siracusa): An ancient Greek city with a rich history dating back over 2,700 years. It's home to impressive ruins, including the Greek Theater and the Roman Amphitheater.
4. **Taormina**: A picturesque hilltop town on the east coast of Sicily, known for its stunning views of the sea, ancient Greek theater, and charming streets lined with shops and restaurants.
5. **Agrigento**: A city in southern Sicily, famous for its magnificent Valley of the Temples, a vast archaeological site featuring some of the best-preserved ancient Greek ruins in the world.

These five cities offer a great taste of Sicily's rich history, culture, and natural beauty!"

---

**Question 4:** "Cu je Dante Alighieri? scrivi 'na biografia curta." </br>

**Best Model Answer**: "Dante alighieri (firenze, 1265 - ravenna, 1321) fu nu poeta e scritturi talianu dû mediuevu. era figghiu di una famigghia di banchari di firenze, ma nun si sparti la ricchezza a capitanari, pi cchì rifuggiò la sò vita ntô munastiriu da santa marija dâ fiorenza. li soi opiri cchiù noti sunnu "la divina commedia", lu "vulgari eloquentio" (un trattatu suprâ lingua taliana) e li "rimu latini". la "divina commedia" è nu cantu longu di 14 canti, ca cuntèni na stissa verra dû sò amuri ànima ntra li "inferni", "il pargulu" e "lu paradisu". fu traduttu in tuttu lu munnu e è canusciutu comu l'òpira cchiù granda dû mediuevu italianu. la so morti avvennu a ravenna, dunca a curneggiu tra lu 1320 e lu 1321. lu so cumparimentu veni storicizzatu ntra lu 1308-1317: pigghiò parti a la guerra ca si svignau tra lu duccatu dà repubblica di firenze e lu regnu di ravenna, arripunnu lu so patrimoni nta quistu puntu. a causa dî disputi chi li succedaru ntô ducatu, mori peggriu ntirviunatu da l'assidiu. la so targa fu mossa nta lu 1349; ufficialmenti riconisciuta, fu ricanuscita comu "patri dâ lingua taliana" â fini dû sèculu XIII. la sò pupulazziuna fu granni, e lu so nomu diveni simboli dâ cultura taliana."


**Baseline Model answer**: "Dante Alighieri (1265-1321) è stato un poeta e scrittore italiano, considerato uno dei massimi esponenti della letteratura italiana. Nacque a Firenze, in Italia, da una famiglia patrizia del quartiere di Santa Maria del Calcinaio.

Iniziò la sua carriera come poeta e cantore a corte del re Manfredi, ma presto si ritrovò coinvolto nella politica fiorentina, appoggiando la fazione nobile contro il potere imperiale. Dopo l'esilio dalla città nel 1302, Dante trascorse 19 anni all'estero, scrivendo alcune delle sue opere più importanti, tra cui la Divina Commedia, un poema epico che narra la storia di un viaggio attraverso gli inferni, il purgatorio e il paradiso.

La sua opera più famosa, la Divina Commedia, è considerata una delle maggiori creazioni della letteratura mondiale, conosciuta per la sua struttura complessa e la sua profonda riflessione sulla natura umana, la virtù, la moralità e la religione.

Dante morì nel 1321, probabilmente ad Avignone, in Francia, dove aveva trascorso i suoi ultimi anni di esilio. La sua tomba si trova nella Basilica di Santa Croce a Firenze, dove sono conservate molte delle sue opere originali. È ancora oggi considerato uno degli autori più grandi e influenti della storia della letteratura italiana."

---

## Quantitive results
Results are ordered by ascending perplexity (lower is better). It is possible to observe that, the **"reduced"** dataset with the default configuration **"noEmbed"** of target modules produced the best results. The rank doesn't make significant differences between the models, probably due to the scarcity of data: if having more trainable parameters for the fine-tuning doesn't increase the performance, it is possible to hypothesize that the representational power of the model with fewer parameters **(rank 32)** is capable of capturing the essence of the relationships between data, given their limited amount; so, more parameters are not needed here.</br>
The baseline model shows higher perplexity (33.74) compared to the best-fine-tuned model (21.95), indicating an **effective improved capacity** of predicting the next token in Sicilian by SiciLLaMa.

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
