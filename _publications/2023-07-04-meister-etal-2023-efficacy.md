---
title: "On the Efficacy of Sampling Adapters"
collection: publications
authors: "Clara Meister, **Tiago Pimentel**, Luca Malagutti, Ethan Wilcox, Ryan Cotterell"
permalink: /publication/2023-07-04-meister-etal-2023-efficacy
date: 2023-07-04
venue: 'Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)'
paperurl: 'https://aclanthology.org/2023.acl-long.80/'
citation: 'Clara Meister, Tiago Pimentel, Luca Malagutti, Ethan Wilcox, and Ryan Cotterell. 2023. On the Efficacy of Sampling Adapters. In Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 1437–1455, Toronto, Canada. Association for Computational Linguistics.'
---

<a href='https://aclanthology.org/2023.acl-long.80/'>Find paper here</a>

Sampling-based decoding strategies are widely employed for generating text from probabilistic models, yet standard ancestral sampling often results in text that is degenerate or incoherent. To alleviate this issue, various modifications to a model’s sampling distribution, such as top-p or top-k sampling, have been introduced and are now ubiquitously used in language generation systems. We propose a unified framework for understanding these techniques, which we term sampling adapters. Sampling adapters often lead to qualitatively better text, which raises the question: From a formal perspective, how are they changing the token-level distributions of language generation models? And why do these local changes lead to higher-quality text? We argue that the shift they enforce can be viewed as a trade-off between precision and recall: while the model loses its ability to produce certain strings, its precision rate on desirable text increases. While this trade-off is not reflected in standard metrics of distribution quality (such as perplexity), we find that several precision-emphasizing measures indeed indicate that sampling adapters can lead to probability distributions more aligned with the true distribution. Further, these measures correlate with higher sequence-level quality scores, specifically, Mauve.

```
@inproceedings{meister-etal-2023-efficacy,
    author = {
        Clara Meister and
        Tiago Pimentel and
        Luca Malagutti and
        Ethan Wilcox and
        Ryan Cotterell
    },
    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
    title = {On the Efficacy of Sampling Adapters},
    year = {2023},
    url = {https://aclanthology.org/2023.acl-long.80/},
    pages = {1437--1455},
}
```