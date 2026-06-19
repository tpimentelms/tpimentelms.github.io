---
title: "Predicting Declension Class from Form and Meaning"
collection: publications
authors: "Adina Williams, <b>Tiago Pimentel</b>, Hagen Blix, Arya D. McCarthy, Eleanor Chodroff, Ryan Cotterell"
permalink: /publication/2020-07-05-predicting-declension
date: 2020-07-05
venue: 'Annual Meeting of the Association for Computational Linguistics (ACL)'
paperurl: 'https://aclanthology.org/2020.acl-main.597/'
citation: 'Adina Williams, Tiago Pimentel, Hagen Blix, Arya D. McCarthy, Eleanor Chodroff, Ryan Cotterell. 2020. Predicting Declension Class from Form and Meaning. Association for Computational Linguistics (ACL).'
---

<a href='https://aclanthology.org/2020.acl-main.597/'>Find paper here</a>

The noun lexica of many natural languages are divided into several declension classes with characteristic morphological properties. Class membership is far from deterministic, but the phonological form of a noun and/or its meaning can often provide imperfect clues. Here, we investigate the strength of those clues. More specifically, we operationalize this by measuring how much information, in bits, we can glean about declension class from knowing the form and/or meaning of nouns. We know that form and meaning are often also indicative of grammatical gender---which, as we quantitatively verify, can itself share information with declension class---so we also control for gender. We find for two Indo-European languages (Czech and German) that form and meaning respectively share significant amounts of information with class (and contribute additional information above and beyond gender). The three-way interaction between class, form, and meaning (given gender) is also significant. Our study is important for two reasons: First, we introduce a new method that provides additional quantitative support for a classic linguistic finding that form and meaning are relevant for the classification of nouns into declensions. Secondly, we show not only that individual declensions classes vary in the strength of their clues within a language, but also that these variations themselves vary across languages.

```
@inproceedings{williams2020predicting,
    author = {
        Adina Williams and
        Tiago Pimentel and
        Hagen Blix and
        Arya D. McCarthy and
        Eleanor Chodroff and
        Ryan Cotterell
    },
    booktitle = {Annual Meeting of the Association for Computational Linguistics (ACL)},
    title = {Predicting Declension Class from Form and Meaning},
    year = {2020},
    doi = {10.18653/v1/2020.acl-main.597},
    url = {https://aclanthology.org/2020.acl-main.597/},
    pages = {6682--6695},
}
```