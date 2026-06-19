---
title: "A Bayesian Framework for Information-Theoretic Probing"
collection: publications
authors: "<b>Tiago Pimentel</b>, Ryan Cotterell"
permalink: /publication/2021-11-10-bayesian-information-theory
date: 2021-11-10
venue: 'Conference on Empirical Methods in Natural Language Processing (EMNLP)'
paperurl: 'https://aclanthology.org/2021.emnlp-main.229/'
citation: 'Tiago Pimentel, Ryan Cotterell. 2021. A Bayesian Framework for Information-Theoretic Probing. Empirical Methods in Natural Language Processing (EMNLP).'
---

<a href='https://aclanthology.org/2021.emnlp-main.229/'>Find paper here</a>

Pimentel et al. (2020) recently analysed probing from an information-theoretic perspective. They argue that probing should be seen as approximating a mutual information. This led to the rather unintuitive conclusion that representations encode exactly the same information about a target task as the original sentences. The mutual information, however, assumes the true probability distribution of a pair of random variables is known, leading to unintuitive results in settings where it is not. This paper proposes a new framework to measure what we term Bayesian mutual information, which analyses information from the perspective of Bayesian agents -- allowing for more intuitive findings in scenarios with finite data. For instance, under Bayesian MI we have that data can add information, processing can help, and information can hurt, which makes it more intuitive for machine learning applications. Finally, we apply our framework to probing where we believe Bayesian mutual information naturally operationalises ease of extraction by explicitly limiting the available background knowledge to solve a task.

```
@inproceedings{pimentel-etal-2021-bayesian,
    author = {
        Tiago Pimentel and
        Ryan Cotterell
    },
    booktitle = {Conference on Empirical Methods in Natural Language Processing (EMNLP)},
    title = {A Bayesian Framework for Information-Theoretic Probing},
    year = {2021},
    doi = {10.18653/v1/2021.emnlp-main.229},
    url = {https://aclanthology.org/2021.emnlp-main.229/},
    pages = {2869--2887},
}
```