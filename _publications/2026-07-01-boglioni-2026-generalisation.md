---
title: "Do Generalisation Results Generalise?"
collection: publications
authors: "Matteo Boglioni, Andrea Sgobbi, Gabriel Tavernini, Francesco Rita, Marius Mosbach, <b>Tiago Pimentel</b>"
permalink: /publication/2026-07-01-boglioni-2026-generalisation
date: 2026-07-01
venue: 'Findings of the Association for Computational Linguistics (ACL)'
paperurl: 'https://arxiv.org/abs/2512.07832'
citation: 'Matteo Boglioni, Andrea Sgobbi, Gabriel Tavernini, Francesco Rita, Marius Mosbach, Tiago Pimentel. 2026. Do Generalisation Results Generalise?. Findings of the Association for Computational Linguistics (ACL).'
---

<a href='https://arxiv.org/abs/2512.07832'>Find paper here</a>

A large language model&apos;s (LLM&apos;s) out-of-distribution (OOD) generalisation ability is crucial to its deployment. Previous work assessing LLMs&apos; generalisation performance, however, typically focuses on a single out-of-distribution dataset. This approach may fail to precisely evaluate the capabilities of the model, as the data shifts encountered once a model is deployed are much more diverse. In this work, we investigate whether OOD generalisation results generalise. More specifically, we evaluate a model&apos;s performance across multiple OOD testsets throughout a finetuning run; we then evaluate the partial correlation of performances across these testsets, regressing out in-domain performance. This allows us to assess how correlated are generalisation performances once in-domain performance is controlled for. Analysing OLMo2 and OPT, we observe no overarching trend in generalisation results: the existence of a positive or negative correlation between any two OOD testsets depends strongly on the specific choice of model analysed.

```
@inproceedings{boglioni2026generalise,
    author = {
        Matteo Boglioni and
        Andrea Sgobbi and
        Gabriel Tavernini and
        Francesco Rita and
        Marius Mosbach and
        Tiago Pimentel
    },
    booktitle = {Findings of the Association for Computational Linguistics (ACL)},
    title = {Do Generalisation Results Generalise?},
    year = {2026},
    url = {https://arxiv.org/abs/2512.07832},
    pages = {},
}
```