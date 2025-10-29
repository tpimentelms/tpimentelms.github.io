---
title: "The Role of Language Imbalance in Cross-lingual Generalisation: Insights from Cloned Language Experiments "
collection: publications
authors: "Anton Schäfer, Shauli Ravfogel, Thomas Hofmann, <b>Tiago Pimentel</b>*, Imanol Schlag* "
permalink: /publication/2024-07-01-schafer2024rolelanguageimbalancecrosslingual
date: 2024-07-01
venue: 'arXiv'
paperurl: 'https://arxiv.org/abs/2404.07982'
citation: 'Anton Schäfer, Shauli Ravfogel, Thomas Hofmann, Tiago Pimentel*, Imanol Schlag*. 2024. The Role of Language Imbalance in Cross-lingual Generalisation: Insights from Cloned Language Experiments. arXiv &quot; '
---

<a href='https://arxiv.org/abs/2404.07982'>Find paper here</a>

Multilinguality is crucial for extending recent advancements in language modelling to diverse linguistic communities. To maintain high performance while representing multiple languages, multilingual models ideally align representations, allowing what is learned in one language to generalise to others. Prior research has emphasised the importance of parallel data and shared vocabulary elements as key factors for such alignment. In this study, we investigate an unintuitive novel driver of cross-lingual generalisation: language imbalance. In controlled experiments on perfectly equivalent cloned languages, we observe that the existence of a predominant language during training boosts the performance of less frequent languages and leads to stronger alignment of model representations across languages. Furthermore, we find that this trend is amplified with scale: with large enough models or long enough training, we observe that bilingual training data with a 90/10 language split yields better performance on both languages than a balanced 50/50 split. Building on these insights, we design training schemes that can improve performance in all cloned languages, even without altering the training data. As we extend our analysis to real languages, we find that infrequent languages still benefit from frequent ones, yet whether language imbalance causes cross-lingual generalisation there is not conclusive.

```
@inproceedings{schäfer2024rolelanguageimbalancecrosslingual,
    author = {
        Anton Schäfer and
        Shauli Ravfogel and
        Thomas Hofmann and
        Tiago Pimentel* and
        Imanol Schlag* 
    },
    booktitle = {arXiv},
    title = {The Role of Language Imbalance in Cross-lingual Generalisation: Insights from Cloned Language Experiments },
    year = {2024},
    url = {https://arxiv.org/abs/2404.07982},
    pages = {},
}
```