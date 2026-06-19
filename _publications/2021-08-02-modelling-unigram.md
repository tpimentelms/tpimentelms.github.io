---
title: "Modeling the Unigram Distribution"
collection: publications
authors: "Irene Nikkarinen, <b>Tiago Pimentel</b>, Damián Blasi, Ryan Cotterell"
permalink: /publication/2021-08-02-modelling-unigram
date: 2021-08-02
venue: 'Findings of the Association for Computational Linguistics (ACL)'
paperurl: 'https://aclanthology.org/2021.findings-acl.326/'
citation: 'Irene Nikkarinen, Tiago Pimentel, Damián Blasi, Ryan Cotterell. 2021. Modeling the Unigram Distribution. Findings of the Association for Computational Linguistics.'
---

<a href='https://aclanthology.org/2021.findings-acl.326/'>Find paper here</a>

The unigram distribution is the non-contextual probability of finding a specific word form in a corpus. While of central importance to the study of language, it is commonly approximated by each word&apos;s sample frequency in the corpus. This approach, being highly dependent on sample size, assigns zero probability to any out-of-vocabulary (oov) word form. As a result, it produces negatively biased probabilities for any oov word form, while positively biased probabilities to in-corpus words. In this work, we argue in favor of properly modeling the unigram distribution -- claiming it should be a central task in natural language processing. With this in mind, we present a novel model for estimating it in a language (a neuralization of Goldwater et al.&apos;s (2011) model) and show it produces much better estimates across a diverse set of 7 languages than the naïve use of neural character-level language models.

```
@inproceedings{nikkarinen-etal-2021-modeling,
    author = {
        Irene Nikkarinen and
        Tiago Pimentel and
        Damián Blasi and
        Ryan Cotterell
    },
    booktitle = {Findings of the Association for Computational Linguistics (ACL)},
    title = {Modeling the Unigram Distribution},
    year = {2021},
    doi = {10.18653/v1/2021.findings-acl.326},
    url = {https://aclanthology.org/2021.findings-acl.326/},
    pages = {3721--3729},
}
```