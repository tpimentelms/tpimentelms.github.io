---
title: "What About the Precedent: An Information-Theoretic Analysis of Common Law"
collection: publications
authors: "Josef Valvoda, <b>Tiago Pimentel</b>, Niklas Stoehr, Ryan Cotterell, Simone Teufel"
permalink: /publication/2021-06-04-precedent
date: 2021-06-04
venue: 'Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)'
paperurl: 'https://aclanthology.org/2021.naacl-main.181/'
citation: 'Josef Valvoda, Tiago Pimentel, Niklas Stoehr, Ryan Cotterell, Simone Teufel. 2021. What About the Precedent: An Information-Theoretic Analysis of Common Law. North American Chapter of the Association for Computational Linguistics.'
---

<a href='https://aclanthology.org/2021.naacl-main.181/'>Find paper here</a>

In common law, the outcome of a new case is determined mostly by precedent cases, rather than by existing statutes. However, how exactly does the precedent influence the outcome of a new case? Answering this question is crucial for guaranteeing fair and consistent judicial decision-making. We are the first to approach this question computationally by comparing two longstanding jurisprudential views; Halsbury&apos;s, who believes that the arguments of the precedent are the main determinant of the outcome, and Goodhart&apos;s, who believes that what matters most is the precedent&apos;s facts.  We base our study on the corpus of legal cases from the European Court of Human Rights (ECtHR), which allows us to access not only the case itself, but also cases cited in the judges&apos; arguments (i.e. the precedent cases). Taking an information-theoretic view, and modelling the question as a case outcome classification task, we find that the precedent&apos;s arguments share 0.38 nats of information with the case&apos;s outcome, whereas precedent&apos;s facts only share $0.18$ nats of information (i.e., $58$\% less); suggesting Halsbury&apos;s view may be more accurate in this specific court. We found however in a qualitative analysis that there are specific statues where Goodhart&apos;s view dominates, and present some evidence these are the ones where the legal concept at hand is less straightforward.

```
@inproceedings{valvoda-etal-2021-precedent,
    author = {
        Josef Valvoda and
        Tiago Pimentel and
        Niklas Stoehr and
        Ryan Cotterell and
        Simone Teufel
    },
    booktitle = {Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},
    title = {What About the Precedent: An Information-Theoretic Analysis of Common Law},
    year = {2021},
    doi = {10.18653/v1/2021.naacl-main.181},
    url = {https://aclanthology.org/2021.naacl-main.181/},
    pages = {2275--2288},
}
```