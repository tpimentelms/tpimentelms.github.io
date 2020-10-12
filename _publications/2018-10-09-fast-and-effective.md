---
title: "Fast and effective neural networks for translating natural language into denotations"
collection: publications
authors: "Tiago Pimentel, Juliano Viana, Adriano Veloso, and Nivio Ziviani"
permalink: /publication/2018-10-09-fast-and-effective
excerpt: 'This paper is about '
date: 2018-10-09
venue: 'String Processing and Information Retrieval (SPIRE)'
paperurl: 'https://link.springer.com/chapter/10.1007/978-3-030-00479-8_27'
citation: 'Pimentel T, Viana J, Veloso A, Ziviani N. Fast and effective neural networks for translating natural language into denotations. In: International Symposium on String Processing and Information Retrieval, 2018 Oct 9 (pp. 334-347). Springer, Cham.'
---

In this paper we study the semantic parsing problem of mapping natural language utterances into machine interpretable meaning representations. We consider a text-to-denotation application scenario in which a user interacts with a non-human assistant by entering a question, which is then translated into a logical structured query and the result of running this query is finally returned as response to the user. We propose encoder-decoder models that are trained end-to-end using the input questions and the corresponding logical structured queries. In order to ensure fast response times, our models do not condition the target string generation on previously generated tokens. We evaluate our models on real data obtained from a conversational banking chat service, and we show that conditionally-independent translation models offer similar accuracy numbers when compared with sophisticate translation models and present one order of magnitude faster response times.

```
@InProceedings{pimentel2018fast,
  author="Pimentel, Tiago
    and Viana, Juliano
    and Veloso, Adriano
    and Ziviani, Nivio",
  editor="Gagie, Travis
    and Moffat, Alistair
    and Navarro, Gonzalo
    and Cuadros-Vargas, Ernesto",
  title="Fast and Effective Neural Networks for Translating Natural Language into Denotations",
  booktitle="String Processing and Information Retrieval",
  year="2018",
  publisher="Springer International Publishing",
  address="Cham",
  pages="334--347",
  isbn="978-3-030-00479-8"
}
```