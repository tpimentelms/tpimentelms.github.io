---
title: "A Bayesian Framework for Information-Theoretic Probing"
collection: publications
authors: "Tiago Pimentel, Ryan Cotterell"
permalink: /publication/2021-11-10-bayesian-information-theory
excerpt: 'This paper is about '
date: 2021-11-10
venue: 'Empirical Methods in Natural Language Processing (EMNLP)'
citation: "Pimentel T, Cotterell R. A Bayesian Framework for Information-Theoretic Probing. In: Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing (EMNLP), 2021 November."
---


Pimentel et al. (2020) recently analysed probing from an information-theoretic perspective. They argue that probing should be seen as approximating a mutual information. This led to the rather unintuitive conclusion that representations encode exactly the same information about a target task as the original sentences. The mutual information, however, assumes the true probability distribution of a pair of random variables is known, leading to unintuitive results in settings where it is not. This paper proposes a new framework to measure what we term Bayesian mutual information, which analyses information from the perspective of Bayesian agents -- allowing for more intuitive findings in scenarios with finite data. For instance, under Bayesian MI we have that data can add information, processing can help, and information can hurt, which makes it more intuitive for machine learning applications. Finally, we apply our framework to probing where we believe Bayesian mutual information naturally operationalises ease of extraction by explicitly limiting the available background knowledge to solve a task.



```
@inproceedings{pimentel-etal-2021-homophony,
    title = "A Bayesian Framework for Information-Theoretic Probing",
    author = "Pimentel, Tiago  and
      Cotterell, Ryan",
    booktitle = "Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing (EMNLP)",
    month = nov,
    year = "2021",
    publisher = "Association for Computational Linguistics",
    url = "https://arxiv.org/abs/2109.03853",
}
```