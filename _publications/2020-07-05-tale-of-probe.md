---
title: "A Tale of a Probe and a Parser"
collection: publications
authors: "Rowan Hall Maudslay, Josef Valvoda, <b>Tiago Pimentel</b>, Adina Williams, Ryan Cotterell"
permalink: /publication/2020-07-05-tale-of-probe
date: 2020-07-05
venue: 'Association for Computational Linguistics (ACL)'
paperurl: 'https://aclanthology.org/2020.acl-main.659/'
citation: 'Rowan Hall Maudslay, Josef Valvoda, Tiago Pimentel, Adina Williams, Ryan Cotterell. 2020. A Tale of a Probe and a Parser. Association for Computational Linguistics (ACL).'
---

<a href='https://aclanthology.org/2020.acl-main.659/'>Find paper here</a>

Measuring what linguistic information is encoded in neural models of language has become popular in NLP. Researchers approach this enterprise by training &apos;&apos;probes&apos;&apos;---supervised models designed to extract linguistic structure from another model&apos;s output. One such probe is the structural probe (Hewitt and Manning, 2019), designed to quantify the extent to which syntactic information is encoded in contextualised word representations. The structural probe has a novel design, unattested in the parsing literature, the precise benefit of which is not immediately obvious. To explore whether syntactic probes would do better to make use of existing techniques, we compare the structural probe to a more traditional parser with an identical lightweight parameterisation. The parser outperforms structural probe on UUAS in seven of nine analysed languages, often by a substantial amount (e.g. by 11.1 points in English). Under a second less common metric, however, there is the opposite trend---the structural probe outperforms the parser. This begs the question: which metric should we prefer?

```
@inproceedings{hall-maudslay-etal-2020-tale,
    author = {
        Rowan Hall Maudslay and
        Josef Valvoda and
        Tiago Pimentel and
        Adina Williams and
        Ryan Cotterell
    },
    booktitle = {Association for Computational Linguistics (ACL)},
    title = {A Tale of a Probe and a Parser},
    year = {2020},
    doi = {10.18653/v1/2020.acl-main.659},
    url = {https://aclanthology.org/2020.acl-main.659/},
    pages = {7389--7395},
}
```