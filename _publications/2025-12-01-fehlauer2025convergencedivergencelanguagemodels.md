---
title: "Convergence and Divergence of Language Models under Different Random Seeds"
collection: publications
authors: "Finlay Fehlauer, Kyle Mahowald, <b>Tiago Pimentel</b>"
permalink: /publication/2025-12-01-fehlauer2025convergencedivergencelanguagemodels
date: 2025-12-01
venue: 'Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing '
paperurl: 'https://arxiv.org/abs/2509.26643'
citation: 'Finlay Fehlauer, Kyle Mahowald, Tiago Pimentel. 2025. Convergence and Divergence of Language Models under Different Random Seeds. EMNLP'
---

<a href='https://arxiv.org/abs/2509.26643'>Find paper here</a>

In this paper, we investigate the convergence of language models (LMs) trained under different random seeds, measuring convergence as the expected per-token Kullback--Leibler (KL) divergence across seeds. By comparing LM convergence as a function of model size and training checkpoint, we identify a four-phase convergence pattern: (i) an initial uniform phase, (ii) a sharp-convergence phase, (iii) a sharp-divergence phase, and (iv) a slow-reconvergence phase. Further, we observe that larger models reconverge faster in later training stages, while smaller models never actually reconverge; these results suggest that a certain model size may be necessary to learn stable distributions. Restricting our analysis to specific token frequencies or part-of-speech (PoS) tags further reveals that convergence is uneven across linguistic categories: frequent tokens and function words converge faster and more reliably than their counterparts (infrequent tokens and content words). Overall, our findings highlight factors that influence the stability of the learned distributions in model training.

```
@inproceedings{fehlauer2025convergencedivergencelanguagemodels,
    author = {
        Finlay Fehlauer and
        Kyle Mahowald and
        Tiago Pimentel
    },
    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing },
    title = {Convergence and Divergence of Language Models under Different Random Seeds},
    year = {2025},
    url = {https://arxiv.org/abs/2509.26643},
    pages = {},
}
```