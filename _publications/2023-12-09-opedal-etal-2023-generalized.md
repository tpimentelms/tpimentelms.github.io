---
title: "An Exploration of Left-Corner Transformations"
collection: publications
authors: "Andreas Opedal, Eleftheria Tsipidi, <b>Tiago Pimentel</b>, Ryan Cotterell, Tim Vieira"
permalink: /publication/2023-12-09-opedal-etal-2023-generalized
date: 2023-12-09
venue: 'Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing'
paperurl: 'https://aclanthology.org/2023.emnlp-main.827/'
citation: 'Andreas Opedal, Eleftheria Tsipidi, Tiago Pimentel, Ryan Cotterell, and Tim Vieira. 2023. An Exploration of Left-Corner Transformations. In Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing, pages 13393–13427, Singapore. Association for Computational Linguistics.'
---

<a href='https://aclanthology.org/2023.emnlp-main.827/'>Find paper here</a>

The left-corner transformation (Rosenkrantz and Lewis, 1970) is used to remove left recursion from context-free grammars, which is an important step towards making the grammar parsable top-down with simple techniques. This paper generalizes prior left-corner transformations to support semiring-weighted production rules and to provide finer-grained control over which left corners may be moved. Our generalized left-corner transformation (GLCT) arose from unifying the left-corner transformation and speculation transformation (Eisner and Blatz, 2007), originally for logic programming. Our new transformation and speculation define equivalent weighted languages. Yet, their derivation trees are structurally different in an important way: GLCT replaces left recursion with right recursion, and speculation does not. We also provide several technical results regarding the formal relationships between the outputs of GLCT, speculation, and the original grammar. Lastly, we empirically investigate the efficiency of GLCT for left-recursion elimination from grammars of nine languages. Code: https://github.com/rycolab/left-corner

```
@inproceedings{opedal-etal-2023-generalized,
    author = {
        Andreas Opedal and
        Eleftheria Tsipidi and
        Tiago Pimentel and
        Ryan Cotterell and
        Tim Vieira
    },
    booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},
    title = {An Exploration of Left-Corner Transformations},
    year = {2023},
    doi = {10.18653/v1/2023.emnlp-main.827},
    url = {https://aclanthology.org/2023.emnlp-main.827/},
    pages = {13393–13427},
}
```