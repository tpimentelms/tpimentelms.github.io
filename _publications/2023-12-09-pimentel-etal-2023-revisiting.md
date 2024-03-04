---
title: "Revisiting the Optimality of Word Lengths"
collection: publications
authors: "<b>Tiago Pimentel</b>, Ethan G. Wilcox, Clara Meister, Kyle Mahowald, Ryan Cotterell"
permalink: /publication/2023-12-09-pimentel-etal-2023-revisiting
date: 2023-12-09
venue: 'Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing'
paperurl: 'https://aclanthology.org/2023.emnlp-main.137/'
citation: 'Tiago Pimentel, Clara Meister, Ethan G. Wilcox, Kyle Mahowald, and Ryan Cotterell. 2023. Revisiting the Optimality of Word Lengths. In Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing, pages 2240–2255, Singapore. Association for Computational Linguistics.'
highlights: 'Won an <b>outstanding paper award</b> in the Linguistic Theories, Cognitive Modeling, and Psycholinguistics track'
---

<a href='https://aclanthology.org/2023.emnlp-main.137/'>Find paper here</a>

Zipf (1935) posited that wordforms are optimized to minimize utterances’ communicative costs. Under the assumption that cost is given by an utterance’s length, he supported this claim by showing that words’ lengths are inversely correlated with their frequencies. Communicative cost, however, can be operationalized in different ways. Piantadosi et al. (2011) claim that cost should be measured as the distance between an utterance’s information rate and channel capacity, which we dub the channel capacity hypothesis (CCH) here. Following this logic, they then proposed that a word’s length should be proportional to the expected value of its surprisal (negative log-probability in context). In this work, we show that Piantadosi et al.’s derivation does not minimize CCH’s cost, but rather a lower bound, which we term CCH-lower. We propose a novel derivation, suggesting an improved way to minimize CCH’s cost. Under this method, we find that a language’s word lengths should instead be proportional to the surprisal’s expectation plus its variance-to-mean ratio. Experimentally, we compare these three communicative cost functions: Zipf’s, CCH-lower , and CCH. Across 13 languages and several experimental settings, we find that length is better predicted by frequency than either of the other hypotheses. In fact, when surprisal’s expectation, or expectation plus variance-to-mean ratio, is estimated using better language models, it leads to worse word length predictions. We take these results as evidence that Zipf’s longstanding hypothesis holds. 

```
@inproceedings{pimentel-etal-2023-revisiting,
    author = {
        Tiago Pimentel and
        Ethan G. Wilcox and
        Clara Meister and
        Kyle Mahowald and
        Ryan Cotterell
    },
    booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},
    title = {Revisiting the Optimality of Word Lengths},
    year = {2023},
    doi = {10.18653/v1/2023.emnlp-main.137},
    url = {https://aclanthology.org/2023.emnlp-main.137/},
    pages = {2240–2255},
}
```