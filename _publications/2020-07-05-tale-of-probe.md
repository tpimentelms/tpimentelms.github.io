---
title: "A Tale of a Probe and a Parser"
collection: publications
authors: "Rowan Hall Maudslay, Josef Valvoda, Tiago Pimentel, Adina Williams, and Ryan Cotterell"
permalink: /publication/2020-07-05-
excerpt: 'This paper is about '
date: 2020-07-06
venue: 'Association for Computational Linguistics (ACL)'
paperurl: 'https://www.aclweb.org/anthology/2020.acl-main.659/'
citation: 'Hall Maudslay R, Valvoda J, Pimentel T, Williams A, Cotterell R. A Tale of a Probe and a Parser. In: Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics, 2020 Jul (pp. 7389-7395).'
---

Measuring what linguistic information is encoded in neural models of language has become popular in NLP. Researchers approach this enterprise by training ''probes''---supervised models designed to extract linguistic structure from another model's output. One such probe is the structural probe (Hewitt and Manning, 2019), designed to quantify the extent to which syntactic information is encoded in contextualised word representations. The structural probe has a novel design, unattested in the parsing literature, the precise benefit of which is not immediately obvious. To explore whether syntactic probes would do better to make use of existing techniques, we compare the structural probe to a more traditional parser with an identical lightweight parameterisation. The parser outperforms structural probe on UUAS in seven of nine analysed languages, often by a substantial amount (e.g. by 11.1 points in English). Under a second less common metric, however, there is the opposite trend---the structural probe outperforms the parser. This begs the question: which metric should we prefer?

```
@inproceedings{hall-maudslay-etal-2020-tale,
    title = "A Tale of a Probe and a Parser",
    author = "Hall Maudslay, Rowan  and
      Valvoda, Josef  and
      Pimentel, Tiago  and
      Williams, Adina  and
      Cotterell, Ryan",
    booktitle = "Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics",
    month = jul,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.acl-main.659",
    doi = "10.18653/v1/2020.acl-main.659",
    pages = "7389--7395",
}
```