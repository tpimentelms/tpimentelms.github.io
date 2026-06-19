---
title: "Pareto Probing: Trading-Off Accuracy and Complexity"
collection: publications
authors: "<b>Tiago Pimentel</b>, Naomi Saphra, Adina Williams, Ryan Cotterell"
permalink: /publication/2020-11-16-pareto-probing
date: 2020-11-16
venue: 'Empirical Methods in Natural Language Processing (EMNLP)'
paperurl: 'https://arxiv.org/abs/2010.02180'
citation: 'Tiago Pimentel, Naomi Saphra, Adina Williams, Ryan Cotterell. 2020. Pareto Probing: Trading-Off Accuracy and Complexity. Empirical Methods in Natural Language Processing (EMNLP).'
---

<a href='https://arxiv.org/abs/2010.02180'>Find paper here</a>

The question of how to probe contextual word representations for linguistic structure in a way that is both principled and useful has seen significant attention recently in the NLP literature. In our contribution to this discussion, we argue for a probe metric that reflects the fundamental trade-off between probe complexity and performance: the Pareto hypervolume. To measure complexity, we present a number of parametric and non-parametric metrics. Our experiments using Pareto hypervolume as an evaluation metric show that probes often do not conform to our expectations---e.g., why should the non-contextual fastText representations encode more morpho-syntactic information than the contextual BERT representations? These results suggest that common, simplistic probing tasks, such as part-of-speech labeling and dependency arc labeling, are inadequate to evaluate the linguistic structure encoded in contextual word representations. This leads us to propose full dependency parsing as a probing task. In support of our suggestion that harder probing tasks are necessary, our experiments with dependency parsing reveal a wide gap in syntactic knowledge between contextual and non-contextual representations. Our code can be found at https://github.com/rycolab/pareto-probing.

```
@inproceedings{pimentel2020pareto,
    author = {
        Tiago Pimentel and
        Naomi Saphra and
        Adina Williams and
        Ryan Cotterell
    },
    booktitle = {Empirical Methods in Natural Language Processing (EMNLP)},
    title = {Pareto Probing: Trading-Off Accuracy and Complexity},
    year = {2020},
    doi = {10.18653/v1/2020.emnlp-main.254},
    url = {https://arxiv.org/abs/2010.02180},
    pages = {3138--3153},
}
```