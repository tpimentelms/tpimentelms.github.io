---
title: "How to Compute the Probability of a Word "
collection: publications
authors: "<b>Tiago Pimentel</b>, Clara Meister  "
permalink: /publication/2024-11-01-pimentel-meister-2024-compute
date: 2024-11-01
venue: 'Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing '
paperurl: 'https://aclanthology.org/2024.emnlp-main.1020/'
citation: 'Tiago Pimentel and Clara Meister. 2024. How to Compute the Probability of a Word. In Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing, pages 18358–18375, Miami, Florida, USA. Association for Computational Linguistics.'
---

<a href='https://aclanthology.org/2024.emnlp-main.1020/'>Find paper here</a>

Language models (LMs) estimate a probability distribution over strings in a natural language; these distributions are crucial for computing perplexity and surprisal in linguistics research. While we are usually concerned with measuring these values for words, most LMs operate over subwords. Despite seemingly straightforward, accurately computing probabilities over one unit given probabilities over the other requires care. Indeed, we show here that many recent linguistic studies have been incorrectly computing these values. This paper derives the correct methods for computing word probabilities, highlighting issues when relying on language models that use beginning-of-word (bow)-marking tokenisers, e.g., the GPT family. Empirically, we show that correcting the widespread bug in probability computations affects measured outcomes in sentence comprehension and lexical optimisation analyses.

```
@inproceedings{pimentel-meister-2024-compute,
    author = {
        Tiago Pimentel and
        Clara Meister  
    },
    booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing },
    title = {How to Compute the Probability of a Word },
    year = {2024},
    url = {https://aclanthology.org/2024.emnlp-main.1020/},
    pages = {},
}
```