---
title: "On the Effect of (Near) Subword Duplication in Language Modelling"
collection: publications
authors: "Anton Schäfer, Thomas Hofmann, Imanol Schlag, <b>Tiago Pimentel</b>"
permalink: /publication/2024-06-01-schafer2024effect
date: 2024-06-01
venue: 'Findings of the Association for Computational Linguistics: ACL 2024'
paperurl: 'https://aclanthology.org/2024.findings-acl.571/'
citation: 'Anton Schäfer, Thomas Hofmann, Imanol Schlag, Tiago Pimentel. 2024. On the Effect of (Near) Subword Duplication in Language Modelling. In Findings of the Association for Computational Linguistics: ACL 2024'
---

<a href='https://aclanthology.org/2024.findings-acl.571/'>Find paper here</a>

Tokenisation is a core part of language models (LMs). It involves splitting a character sequence into subwords which are assigned arbitrary indices before being served to the LM. While typically lossless, however, this process may lead to less sample efficient LM training: as it removes character-level information, it could make it harder for LMs to generalise across similar subwords, such as now and Now. We refer to such subwords as near duplicates. In this paper, we study the impact of near duplicate subwords on LM training efficiency. First, we design an experiment that gives us an upper bound to how much we should expect a model to improve if we could perfectly generalise across near duplicates. We do this by duplicating each subword in our LM&apos;s vocabulary, creating perfectly equivalent classes of subwords. Experimentally, we find that LMs need roughly 17% more data when trained in a fully duplicated setting. Second, we investigate the impact of naturally occurring near duplicates on LMs. Here, we see that merging them considerably hurts LM performance. Therefore, although subword duplication negatively impacts LM training efficiency, naturally occurring near duplicates may not be as similar as anticipated, limiting the potential for performance improvements.

```
@inproceedings{schafer-etal-2024-effect,
    author = {
        Anton Schäfer and
        Thomas Hofmann and
        Imanol Schlag and
        Tiago Pimentel
    },
    booktitle = {Findings of the Association for Computational Linguistics: ACL 2024},
    title = {On the Effect of (Near) Subword Duplication in Language Modelling},
    year = {2024},
    url = {https://aclanthology.org/2024.findings-acl.571/},
    pages = {},
}
```