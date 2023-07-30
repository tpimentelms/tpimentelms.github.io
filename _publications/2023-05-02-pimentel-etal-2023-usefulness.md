---
title: "On the Usefulness of Embeddings, Clusters and Strings for Text Generation Evaluation"
collection: publications
authors: "Tiago Pimentel, Clara Meister, Ryan Cotterell"
permalink: /publication/2023-05-02-pimentel-etal-2023-usefulness
date: 2023-05-02
venue: 'The Eleventh International Conference on Learning Representations'
paperurl: 'https://openreview.net/forum?id=bvpkw7UIRdU'
citation: 'Tiago Pimentel, Clara Isabel Meister, and Ryan Cotterell. &quot;On the Usefulness of Embeddings, Clusters and Strings for Text Generation Evaluation.&quot; The Eleventh International Conference on Learning Representations. 2022.'
---

<a href='https://openreview.net/forum?id=bvpkw7UIRdU'>Find paper here</a>

A good automatic evaluation metric for language generation ideally correlates highly with human judgements of text quality.  Yet, there is a dearth of such metrics, which inhibits the rapid and efficient progress of language generators. One exception is  the recently proposed Mauve. In theory, Mauve measures an information-theoretic divergence between two probability distributions over strings: one representing the language generator under evaluation; the other representing the true natural language distribution. Mauve&apos;s authors argue that its success comes from the qualitative properties of their proposed divergence.  Yet in practice, as this divergence is uncomputable, Mauve approximates it by measuring the divergence between multinomial distributions over clusters instead, where cluster assignments are attained by grouping strings based on a pretrained language model&apos;s embeddings. As we show, however, this is not a tight approximation---in either theory or practice. This begs the question: why does Mauve work so well? In this work, we show that \mauve was right for the wrong reasons, and that its newly proposed divergence is not necessary for its high performance. In fact, classical divergences paired with its proposed cluster-based approximation may actually serve as better evaluation metrics. We finish the paper with a probing analysis; this analysis leads us to conclude that---by encoding syntactic- and coherence-level features of text, while ignoring surface-level features---such cluster-based approximations to string distributions may simply be better for evaluating state-of-the-art language generators.

```
@inproceedings{pimentel-etal-2023-usefulness,
    author = {
        Tiago Pimentel and
        Clara Meister and
        Ryan Cotterell
    },
    booktitle = {The Eleventh International Conference on Learning Representations},
    title = {On the Usefulness of Embeddings, Clusters and Strings for Text Generation Evaluation},
    year = {2023},
    url = {https://openreview.net/forum?id=bvpkw7UIRdU},
    pages = {},
}
```