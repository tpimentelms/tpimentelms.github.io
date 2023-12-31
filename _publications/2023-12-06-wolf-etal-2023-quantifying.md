---
title: "uantifying the redundancy between prosody and text"
collection: publications
authors: "Lukas Wolf, <b>Tiago Pimentel</b>, Evelina Fedorenko, Ryan Cotterell, Alex Warstadt, Ethan Wilcox, Tamar Regev"
permalink: /publication/2023-12-06-wolf-etal-2023-quantifying
date: 2023-12-06
venue: 'Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing'
paperurl: 'https://aclanthology.org/2023.emnlp-main.606/'
citation: 'Lukas Wolf, Tiago Pimentel, Evelina Fedorenko, Ryan Cotterell, Alex Warstadt, Ethan Wilcox, and Tamar Regev. 2023. Quantifying the redundancy between prosody and text. In Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing, pages 9765–9784, Singapore. Association for Computational Linguistics.'
---

<a href='https://aclanthology.org/2023.emnlp-main.606/'>Find paper here</a>

Prosody—the suprasegmental component of speech, including pitch, loudness, and tempo—carries critical aspects of meaning. However, the relationship between the information conveyed by prosody vs. by the words themselves remains poorly understood. We use large language models (LLMs) to estimate how much information is redundant between prosody and the words themselves. Using a large spoken corpus of English audiobooks, we extract prosodic features aligned to individual words and test how well they can be predicted from LLM embeddings, compared to non-contextual word embeddings. We find a high degree of redundancy between the information carried by the words and prosodic information across several prosodic features, including intensity, duration, pauses, and pitch contours. Furthermore, a word’s prosodic information is redundant with both the word itself and the context preceding as well as following it. Still, we observe that prosodic features can not be fully predicted from text, suggesting that prosody carries information above and beyond the words. Along with this paper, we release a general-purpose data processing pipeline for quantifying the relationship between linguistic information and extra-linguistic features. 

```
@inproceedings{wolf-etal-2023-quantifying,
    author = {
        Lukas Wolf and
        Tiago Pimentel and
        Evelina Fedorenko and
        Ryan Cotterell and
        Alex Warstadt and
        Ethan Wilcox and
        Tamar Regev
    },
    booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},
    title = {uantifying the redundancy between prosody and text},
    year = {2023},
    doi = {10.18653/v1/2023.emnlp-main.606},
    url = {https://aclanthology.org/2023.emnlp-main.606/},
    pages = {9765–9784},
}
```