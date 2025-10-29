---
title: "Local and Global Decoding in Text Generation"
collection: publications
authors: "Daniel Gareev, Thomas Hofmann, Ezhilmathi Krishnasamy, <b>Tiago Pimentel</b>  "
permalink: /publication/2024-11-03-gareev-etal-2024-local
date: 2024-11-03
venue: 'Findings of the Association for Computational Linguistics: EMNLP 2024 '
paperurl: 'https://aclanthology.org/2024.findings-emnlp.854/'
citation: 'Daniel Gareev, Thomas Hofmann, Ezhilmathi Krishnasamy, Tiago Pimentel '
---

<a href='https://aclanthology.org/2024.findings-emnlp.854/'>Find paper here</a>

Text generation, a component in applications such as dialogue systems, relies heavily on decoding algorithms that sample strings from a language model distribution. Traditional methods like top-k and top-𝜋 decoding locally normalise the model’s output, which can significantly distort the original distribution. In this paper, we investigate the effects of such distortions by introducing globally-normalised versions of these decoding methods. Further, we propose an independent Metropolis-Hastings (IMH) algorithm to approximate sampling from these globally-normalised distributions without explicitly computing them. Our empirical analyses compare the performance of local and global decoding across two algorithms (top-k and top-𝜋) with various hyperparameters, using the Pythia language models. Results show that in most configuration, global decoding performs worse than the local decoding versions of the same algorithms, despite preserving the distribution’s integrity. Our results thus suggest that distortion might be an important feature of local decoding algorithms. 

```
@inproceedings{gareev-etal-2024-local,
    author = {
        Daniel Gareev and
        Thomas Hofmann and
        Ezhilmathi Krishnasamy and
        Tiago Pimentel  
    },
    booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2024 },
    title = {Local and Global Decoding in Text Generation},
    year = {2024},
    url = {https://aclanthology.org/2024.findings-emnlp.854/},
    pages = {},
}
```