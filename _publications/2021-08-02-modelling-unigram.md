---
title: "Modeling the Unigram Distribution"
collection: publications
authors: "Irene Nikkarinen, Tiago Pimentel, Damián Blasi, Ryan Cotterell"
permalink: /publication/2021-08-02-modelling-unigram
excerpt: 'This paper is about '
date: 2021-08-02
venue: 'Findings of the Association for Computational Linguistics'
citation: 'Nikkarinen I, Pimentel T, Blasi D, Cotterell R. Modeling the Unigram Distribution. In: Findings of the Association for Computational Linguistics: ACL-IJCNLP, 2021 June.'
---

The unigram distribution is the non-contextual probability of finding a specific word form in a corpus. While of central importance to the study of language, it is commonly approximated by each word's sample frequency in the corpus. This approach, being highly dependent on sample size, assigns zero probability to any out-of-vocabulary (oov) word form. As a result, it produces negatively biased probabilities for any oov word form, while positively biased probabilities to in-corpus words. In this work, we argue in favor of properly modeling the unigram distribution -- claiming it should be a central task in natural language processing. With this in mind, we present a novel model for estimating it in a language (a neuralization of Goldwater et al.'s (2011) model) and show it produces much better estimates across a diverse set of 7 languages than the naïve use of neural character-level language models.


```
@inproceedings{nikkarinen-etal-2021-modeling,
    title = "Modeling the Unigram Distribution",
    author = "Nikkarinen, Irene  and
      Pimentel, Tiago  and
      Blasi, Dami{\'a}n  and
      Cotterell, Ryan",
    booktitle = "Findings of the Association for Computational Linguistics: ACL-IJCNLP 2021",
    month = aug,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.findings-acl.326",
    doi = "10.18653/v1/2021.findings-acl.326",
    pages = "3721--3729",
}
```