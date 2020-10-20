---
title: "Predicting Declension Class from Form and Meaning"
collection: publications
authors: "Adina Williams, Tiago Pimentel, Hagen Blix, Arya D. McCarthy, Eleanor Chodroff, and Ryan Cotterell"
permalink: /publication/2020-07-05-
excerpt: 'This paper is about '
date: 2020-07-05
venue: 'Association for Computational Linguistics (ACL)'
paperurl: 'https://www.aclweb.org/anthology/2020.acl-main.597/'
citation: 'Williams A, Pimentel T, McCarthy AD, Blix H, Chodroff E, Cotterell R. Predicting Declension Class from Form and Meaning. In: Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics, 2020 Jul (pp. 6682-6695).'
---

The noun lexica of many natural languages are divided into several declension classes with characteristic morphological properties. Class membership is far from deterministic, but the phonological form of a noun and/or its meaning can often provide imperfect clues. Here, we investigate the strength of those clues. More specifically, we operationalize this by measuring how much information, in bits, we can glean about declension class from knowing the form and/or meaning of nouns. We know that form and meaning are often also indicative of grammatical gender---which, as we quantitatively verify, can itself share information with declension class---so we also control for gender. We find for two Indo-European languages (Czech and German) that form and meaning respectively share significant amounts of information with class (and contribute additional information above and beyond gender). The three-way interaction between class, form, and meaning (given gender) is also significant. Our study is important for two reasons: First, we introduce a new method that provides additional quantitative support for a classic linguistic finding that form and meaning are relevant for the classification of nouns into declensions. Secondly, we show not only that individual declensions classes vary in the strength of their clues within a language, but also that these variations themselves vary across languages.

```
@inproceedings{williams2020predicting,
    title = "Predicting Declension Class from Form and Meaning",
    author = "Williams, Adina  and
      Pimentel, Tiago  and
      Blix, Hagen  and
      McCarthy, Arya D.  and
      Chodroff, Eleanor  and
      Cotterell, Ryan",
    booktitle = "Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics",
    month = jul,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.acl-main.597",
    doi = "10.18653/v1/2020.acl-main.597",
    pages = "6682--6695",
}
```