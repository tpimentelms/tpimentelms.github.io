---
title: "Naturalistic Causal Probing for Morpho-Syntax"
collection: publications
authors: "Afra Amini, **Tiago Pimentel**, Clara Meister, Ryan Cotterell"
permalink: /publication/2023-02-02-amini-etal-2023-naturalistic
date: 2023-02-02
venue: 'Transactions of the Association for Computational Linguistics, Volume 11'
paperurl: 'https://aclanthology.org/2023.tacl-1.23/'
citation: 'Afra Amini, Tiago Pimentel, Clara Meister, and Ryan Cotterell. 2023. Naturalistic Causal Probing for Morpho-Syntax. Transactions of the Association for Computational Linguistics, 11:384–403.'
---

<a href='https://aclanthology.org/2023.tacl-1.23/'>Find paper here</a>

Probing has become a go-to methodology for interpreting and analyzing deep neural models in natural language processing. However, there is still a lack of understanding of the limitations and weaknesses of various types of probes. In this work, we suggest a strategy for input-level intervention on naturalistic sentences. Using our approach, we intervene on the morpho-syntactic features of a sentence, while keeping the rest of the sentence unchanged. Such an intervention allows us to causally probe pre-trained models. We apply our naturalistic causal probing framework to analyze the effects of grammatical gender and number on contextualized representations extracted from three pre-trained models in Spanish, the multilingual versions of BERT, RoBERTa, and GPT-2. Our experiments suggest that naturalistic interventions lead to stable estimates of the causal effects of various linguistic properties. Moreover, our experiments demonstrate the importance of naturalistic causal probing when analyzing pre-trained models. https://github.com/rycolab/naturalistic-causal-probing

```
@article{amini-etal-2023-naturalistic,
    author = {
        Afra Amini and
        Tiago Pimentel and
        Clara Meister and
        Ryan Cotterell
    },
    article = {Transactions of the Association for Computational Linguistics, Volume 11},
    title = {Naturalistic Causal Probing for Morpho-Syntax},
    year = {2023},
    volume = {11},
    doi = {10.1162/tacl_a_00554},
    url = {https://aclanthology.org/2023.tacl-1.23/},
    pages = {384--403},
}
```