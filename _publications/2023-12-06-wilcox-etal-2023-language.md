---
title: "Language Model Quality Correlates with Psychometric Predictive Power in Multiple Languages"
collection: publications
authors: "Ethan G. Wilcox, Clara Meister, Ryan Cotterell, <b>Tiago Pimentel</b>"
permalink: /publication/2023-12-06-wilcox-etal-2023-language
date: 2023-12-06
venue: 'Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing'
paperurl: 'https://aclanthology.org/2023.emnlp-main.466/'
citation: 'Ethan Wilcox, Clara Meister, Ryan Cotterell, and Tiago Pimentel. 2023. Language Model Quality Correlates with Psychometric Predictive Power in Multiple Languages. In Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing, pages 7503–7511, Singapore. Association for Computational Linguistics.'
---

<a href='https://aclanthology.org/2023.emnlp-main.466/'>Find paper here</a>

Surprisal theory (Hale, 2001; Levy, 2008) posits that a word’s reading time is proportional to its surprisal (i.e., to its negative log probability given the proceeding context). Since we are unable to access a word’s ground-truth probability, surprisal theory has been empirically tested using surprisal estimates from language models (LMs). Under the premise that surprisal theory holds, we would expect that higher quality language models provide more powerful predictors of human reading behavior—a conjecture we dub the quality–power (QP) hypothesis. Unfortunately, empirical support for the QP hypothesis is mixed. Some studies in English have found correlations between LM quality and predictive power, but other studies using Japanese data, as well as using larger English LMs, find no such correlations. In this work, we conduct a systematic crosslinguistic assessment of the QP hypothesis. We train LMs from scratch on small- and medium-sized datasets from 13 languages (across five language families) and assess their ability to predict eye tracking data. We find correlations between LM quality and power in eleven of these thirteen languages, suggesting that, within the range of model classes and sizes tested, better language models are indeed better predictors of human language processing behaviors. 

```
@inproceedings{wilcox-etal-2023-language,
    author = {
        Ethan G. Wilcox and
        Clara Meister and
        Ryan Cotterell and
        Tiago Pimentel
    },
    booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},
    title = {Language Model Quality Correlates with Psychometric Predictive Power in Multiple Languages},
    year = {2023},
    doi = {10.18653/v1/2023.emnlp-main.466},
    url = {https://aclanthology.org/2023.emnlp-main.466/},
    pages = {7503–7511},
}
```