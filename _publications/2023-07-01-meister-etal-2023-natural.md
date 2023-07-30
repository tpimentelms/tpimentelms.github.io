---
title: "A Natural Bias for Language Generation Models"
collection: publications
authors: "Clara Meister, Wojciech Stokowiec, <b>Tiago Pimentel</b>, Lei Yu, Laura Rimell, Adhiguna Kuncoro"
permalink: /publication/2023-07-01-meister-etal-2023-natural
date: 2023-07-01
venue: 'Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)'
paperurl: 'https://aclanthology.org/2023.acl-short.22/'
citation: 'Clara Meister, Wojciech Stokowiec, Tiago Pimentel, Lei Yu, Laura Rimell, and Adhiguna Kuncoro. 2023. A Natural Bias for Language Generation Models. In Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers), pages 243–255, Toronto, Canada. Association for Computational Linguistics.'
---

<a href='https://aclanthology.org/2023.acl-short.22/'>Find paper here</a>

After just a few hundred training updates, a standard probabilistic model for language generation has likely not yet learnt many semantic or syntactic rules of natural language, making it difficult to estimate the probability distribution over next tokens. Yet around this point, these models have identified a simple, loss-minimising behaviour: to output the unigram distribution of the target training corpus. The use of such a heuristic raises the question: Can we initialise our models with this behaviour and save precious compute resources and model capacity? Here we show that we can effectively endow standard neural language generation models with a separate module that reflects unigram frequency statistics as prior knowledge, simply by initialising the bias term in a model’s final linear layer with the log-unigram distribution. We use neural machine translation as a test bed for this simple technique and observe that it: (i) improves learning efficiency; (ii) achieves better overall performance; and perhaps most importantly (iii) appears to disentangle strong frequency effects by encouraging the model to specialise in non-frequency-related aspects of language.

```
@inproceedings{meister-etal-2023-natural,
    author = {
        Clara Meister and
        Wojciech Stokowiec and
        Tiago Pimentel and
        Lei Yu and
        Laura Rimell and
        Adhiguna Kuncoro
    },
    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},
    title = {A Natural Bias for Language Generation Models},
    year = {2023},
    url = {https://aclanthology.org/2023.acl-short.22/},
    pages = {243--255},
}
```