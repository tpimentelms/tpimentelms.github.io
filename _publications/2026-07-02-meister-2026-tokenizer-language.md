---
title: "What Language is This? Ask Your Tokenizer"
collection: publications
authors: "Clara Meister, Ahmetcan Yavuz, Pietro Lesci, <b>Tiago Pimentel</b>"
permalink: /publication/2026-07-02-meister-2026-tokenizer-language
date: 2026-07-02
venue: 'International Conference on Machine Learning (ICML)'
paperurl: 'https://arxiv.org/abs/2602.17655'
citation: 'Clara Meister, Ahmetcan Yavuz, Pietro Lesci, Tiago Pimentel. 2026. What Language is This? Ask Your Tokenizer. International Conference on Machine Learning (ICML).'
---

<a href='https://arxiv.org/abs/2602.17655'>Find paper here</a>

Language Identification (LID) is an important component of many multilingual natural language processing pipelines, where it facilitates corpus curation, training data analysis, and cross-lingual evaluation of large language models. Despite near-perfect performance on high-resource languages, existing systems remain brittle in low-resource and closely related language settings. We introduce UniLID, a simple and efficient LID method based on the UnigramLM tokenization algorithm, leveraging its probabilistic framing, parameter estimation technique and inference strategy. In short, we learn language-conditional unigram distributions over a shared tokenizer vocabulary but treat segmentation as a language-specific phenomenon. Our formulation is data- and compute-efficient, supports incremental addition of new languages without retraining existing models, and can naturally be integrated into existing language model tokenization pipelines. Empirical evaluations against widely used baselines, including fastText, GlotLID, and CLD3, show that UniLID achieves competitive performance on standard benchmarks, substantially improves sample efficiency in low-resource settings - surpassing 70% accuracy with as few as five labeled samples per language - and delivers large gains on fine-grained dialect identification.

```
@inproceedings{meister2026language,
    author = {
        Clara Meister and
        Ahmetcan Yavuz and
        Pietro Lesci and
        Tiago Pimentel
    },
    booktitle = {International Conference on Machine Learning (ICML)},
    title = {What Language is This? Ask Your Tokenizer},
    year = {2026},
    url = {https://arxiv.org/abs/2602.17655},
    pages = {},
}
```