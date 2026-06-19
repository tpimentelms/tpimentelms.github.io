---
title: "Operationalising the Superficial Alignment Hypothesis via Task Complexity"
collection: publications
authors: "Tomás Vergara-Browne, Darshan Patil, Ivan Titov, Siva Reddy, <b>Tiago Pimentel</b>*, Marius Mosbach*"
permalink: /publication/2026-07-02-vergarabrowne-2026-superficial
date: 2026-07-02
venue: 'International Conference on Machine Learning (ICML)'
paperurl: 'https://arxiv.org/abs/2602.15829'
citation: 'Tomás Vergara-Browne, Darshan Patil, Ivan Titov, Siva Reddy, Tiago Pimentel, Marius Mosbach. 2026. Operationalising the Superficial Alignment Hypothesis via Task Complexity. International Conference on Machine Learning (ICML).'
---

<a href='https://arxiv.org/abs/2602.15829'>Find paper here</a>

The superficial alignment hypothesis (SAH) posits that large language models learn most of their knowledge during pre-training, and that post-training merely surfaces this knowledge. The SAH, however, lacks a precise definition, which has led to (i) different and seemingly orthogonal arguments supporting it, and (ii) important critiques to it. We propose a new metric called task complexity: the length of the shortest program that achieves a target performance on a task. In this framework, the SAH simply claims that pre-trained models drastically reduce the complexity of achieving high performance on many tasks. Our definition unifies prior arguments supporting the SAH, interpreting them as different strategies to find such short programs. Experimentally, we estimate the task complexity of mathematical reasoning, machine translation, and instruction following; we then show that these complexities can be remarkably low when conditioned on a pre-trained model. Further, we find that pre-training enables access to strong performances on our tasks, but it can require programs of gigabytes of length to access them. Post-training, on the other hand, collapses the complexity of reaching this same performance by several orders of magnitude. Overall, our results highlight that task adaptation often requires surprisingly little information -- often just a few kilobytes.

```
@inproceedings{vergarabrowne2026superficial,
    author = {
        Tomás Vergara-Browne and
        Darshan Patil and
        Ivan Titov and
        Siva Reddy and
        Tiago Pimentel and
        Marius Mosbach
    },
    booktitle = {International Conference on Machine Learning (ICML)},
    title = {Operationalising the Superficial Alignment Hypothesis via Task Complexity},
    year = {2026},
    url = {https://arxiv.org/abs/2602.15829},
    pages = {},
}
```