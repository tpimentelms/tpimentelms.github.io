---
title: "What About the Precedent: An Information-Theoretic Analysis of Common Law"
collection: publications
authors: "Josef Valvoda, Tiago Pimentel, Niklas Stoehr, Ryan Cotterell, and Simone Teufel"
permalink: /publication/2021-06-04-precedent
excerpt: 'This paper is about '
date: 2021-06-04
venue: 'North American Chapter of the Association for Computational Linguistics'
citation: 'Valvoda J, Pimentel T, Stoehr N, Cotterell R, Teufel S. What About the Precedent: An Information-Theoretic Analysis of Common Law. In: Proceedings of the 2021 Conference of the North {A}merican Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers), 2021 June.'
---


In common law, the outcome of a new case is determined mostly by precedent cases, rather than by existing statutes. However, how exactly does the precedent influence the outcome of a new case? Answering this question is crucial for guaranteeing fair and consistent judicial decision-making. We are the first to approach this question computationally by comparing two longstanding jurisprudential views; Halsbury's, who believes that the arguments of the precedent are the main determinant of the outcome, and Goodhart's, who believes that what matters most is the precedent's facts.  We base our study on the corpus of legal cases from the European Court of Human Rights (ECtHR), which allows us to access not only the case itself, but also cases cited in the judges' arguments (i.e. the precedent cases). Taking an information-theoretic view, and modelling the question as a case outcome classification task, we find that the precedent's arguments share 0.38 nats of information with the case's outcome, whereas precedent's facts only share $0.18$ nats of information (i.e., $58$\% less); suggesting Halsbury's view may be more accurate in this specific court. We found however in a qualitative analysis that there are specific statues where Goodhart's view dominates, and present some evidence these are the ones where the legal concept at hand is less straightforward.

```
@inproceedings{valvoda-etal-2021-precedent,
    title = "What About the Precedent: {A}n Information-Theoretic Analysis of Common Law",
    author = "Valvoda, Josef and
      Pimentel, Tiago  and
      Stoehr, Niklas and
      Cotterell, Ryan and
      Teufel, Simone",
    booktitle = "Proceedings of the 2021 Conference of the North {A}merican Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers)",
    month = jun,
    year = "2021",
    address = "Virtual",
    publisher = "Association for Computational Linguistics",
}
```