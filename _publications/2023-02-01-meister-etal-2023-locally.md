---
title: "Locally Typical Sampling"
collection: publications
authors: "Clara Meister, Tiago Pimentel, Gian Wiher, Ryan Cotterell"
permalink: /publication/2023-02-01-meister-etal-2023-locally
date: 2023-02-01
venue: 'Transactions of the Association for Computational Linguistics, Volume 11'
paperurl: 'https://aclanthology.org/2023.tacl-1.7/'
citation: 'Clara Meister, Tiago Pimentel, Gian Wiher, and Ryan Cotterell. 2023. Locally Typical Sampling. Transactions of the Association for Computational Linguistics, 11:102–121.'
---

<a href='https://aclanthology.org/2023.tacl-1.7/'>Find paper here</a>

Today’s probabilistic language generators fall short when it comes to producing coherent and fluent text despite the fact that the underlying models perform well under standard metrics (e.g., perplexity). This discrepancy has puzzled the language generation community for the last few years. In this work, we posit that the abstraction of natural language generation as a discrete stochastic process—which allows for an information-theoretic analysis—can provide new insights into the behavior of probabilistic language generators, for example, why high-probability texts can be dull or repetitive. Humans use language as a means of communicating information, aiming to do so in a simultaneously efficient and error-minimizing manner; in fact, psycholinguistics research suggests humans choose each word in a string with this subconscious goal in mind. We formally define the set of strings that meet this criterion: Those for which each word has an information content close to the expected information content, namely, the conditional entropy of our model. We then propose a simple and efficient procedure for enforcing this criterion when generating from probabilistic models, which we call locally typical sampling. Automatic and human evaluations show that, in comparison to nucleus and top-k sampling, locally typical sampling offers competitive performance (in both abstractive summarization and story generation) in terms of quality while consistently reducing degenerate repetitions.

```
@article{meister-etal-2023-locally,
    author = {
        Clara Meister and
        Tiago Pimentel and
        Gian Wiher and
        Ryan Cotterell
    },
    article = {Transactions of the Association for Computational Linguistics, Volume 11},
    title = {Locally Typical Sampling},
    year = {2023},
    volume = {11},
    doi = {10.1162/tacl_a_00536},
    url = {https://aclanthology.org/2023.tacl-1.7/},
    pages = {102--121},
}
```