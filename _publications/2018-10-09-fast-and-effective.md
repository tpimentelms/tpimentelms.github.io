---
title: "Fast and effective neural networks for translating natural language into denotations"
collection: publications
authors: "<b>Tiago Pimentel</b>, Juliano Viana, Adriano Veloso, Nivio Ziviani"
permalink: /publication/2018-10-09-fast-and-effective
date: 2018-10-09
venue: 'String Processing and Information Retrieval (SPIRE)'
paperurl: 'https://link.springer.com/chapter/10.1007/978-3-030-00479-8_27'
citation: 'Tiago Pimentel, Juliano Viana, Adriano Veloso, Nivio Ziviani. 2018. Fast and effective neural networks for translating natural language into denotations. String Processing and Information Retrieval (SPIRE).'
---

<a href='https://link.springer.com/chapter/10.1007/978-3-030-00479-8_27'>Find paper here</a>

In this paper we study the semantic parsing problem of mapping natural language utterances into machine interpretable meaning representations. We consider a text-to-denotation application scenario in which a user interacts with a non-human assistant by entering a question, which is then translated into a logical structured query and the result of running this query is finally returned as response to the user. We propose encoder-decoder models that are trained end-to-end using the input questions and the corresponding logical structured queries. In order to ensure fast response times, our models do not condition the target string generation on previously generated tokens. We evaluate our models on real data obtained from a conversational banking chat service, and we show that conditionally-independent translation models offer similar accuracy numbers when compared with sophisticate translation models and present one order of magnitude faster response times.

```
@inproceedings{pimentel2018fast,
    author = {
        Tiago Pimentel and
        Juliano Viana and
        Adriano Veloso and
        Nivio Ziviani
    },
    booktitle = {String Processing and Information Retrieval (SPIRE)},
    title = {Fast and effective neural networks for translating natural language into denotations},
    year = {2018},
    volume = {11147},
    doi = {10.1007/978-3-030-00479-8_27},
    url = {https://link.springer.com/chapter/10.1007/978-3-030-00479-8_27},
    pages = {334--347},
}
```