---
title: "Causal Estimation of Tokenisation Bias "
collection: publications
authors: "Pietro Lesci, Clara Meister, Thomas Hofmann, Andreas Vlachos, <b>Tiago Pimentel</b>  "
permalink: /publication/2025-07-02-lesci-etal-2025-causal
date: 2025-07-02
venue: 'Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)'
paperurl: 'https://aclanthology.org/2025.acl-long.1374/'
citation: 'Pietro Lesci, Clara Meister, Thomas Hofmann, Andreas Vlachos, and Tiago Pimentel. 2025. Causal Estimation of Tokenisation Bias. In Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 28325–28340, Vienna, Austria. Association for Computational Linguistics.'
---

<a href='https://aclanthology.org/2025.acl-long.1374/'>Find paper here</a>

Modern language models are typically trained over subword sequences, but ultimately define probabilities over character-strings. Ideally, the choice of the tokeniser—which maps character-strings to subwords—should not affect the probability assigned to the underlying character-string; in practice, it does. We define this mismatch as **tokenisation bias**. In this work, we quantify one particular type of tokenisation bias: the effect of including or not a subword (e.g., ⟨ hello ⟩) in a tokeniser’s vocabulary on the probability a trained model assigns to the corresponding characters (i.e., “hello”). Estimating this effect is challenging because each model is trained with only one tokeniser. We address this by framing tokenisation bias as a causal effect and estimating it using the regression discontinuity design. Specifically, we exploit the fact that tokenisation algorithms rank subwords and add the first K to a tokeniser’s vocabulary, where K is an arbitrary cutoff point. As such, we can estimate a causal effect by comparing similar subwords around this cutoff. Experimentally, we find that tokenisation consistently affects models’ outputs across scales, vocabularies, and tokenisers. Notably, a subword’s presence in a small model’s vocabulary may increase its characters’ probability by up to 17 times, highlighting tokenisation as a key design choice in language modelling. 

```
@inproceedings{lesci-etal-2025-causal,
    author = {
        Pietro Lesci and
        Clara Meister and
        Thomas Hofmann and
        Andreas Vlachos and
        Tiago Pimentel  
    },
    booktitle = {Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
    title = {Causal Estimation of Tokenisation Bias },
    year = {2025},
    url = {https://aclanthology.org/2025.acl-long.1374/},
    pages = {},
}
```