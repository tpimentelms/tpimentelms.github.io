---
title: "Few-shot Fine-tuning vs. In-context Learning: A Fair Comparison and Evaluation"
collection: publications
authors: "Marius Mosbach, **Tiago Pimentel**, Shauli Ravfogel, Dietrich Klakow, Yanai Elazar"
permalink: /publication/2023-07-03-mosbach-etal-2023-shot
date: 2023-07-03
venue: 'Findings of the Association for Computational Linguistics: ACL 2023'
paperurl: 'https://aclanthology.org/2023.findings-acl.779/'
citation: 'Marius Mosbach, Tiago Pimentel, Shauli Ravfogel, Dietrich Klakow, and Yanai Elazar. 2023. Few-shot Fine-tuning vs. In-context Learning: A Fair Comparison and Evaluation. In Findings of the Association for Computational Linguistics: ACL 2023, pages 12284–12314, Toronto, Canada. Association for Computational Linguistics.'
---

<a href='https://aclanthology.org/2023.findings-acl.779/'>Find paper here</a>

Few-shot fine-tuning and in-context learning are two alternative strategies for task adaptation of pre-trained language models. Recently, in-context learning has gained popularity over fine-tuning due to its simplicity and improved out-of-domain generalization, and because extensive evidence shows that fine-tuned models pick up on spurious correlations.Unfortunately, previous comparisons of the two approaches were done using models of different sizes. This raises the question of whether the observed weaker out-of-domain generalization of fine-tuned models is an inherent property of fine-tuning or a limitation of the experimental setup. In this paper, we compare the generalization of few-shot fine-tuning and in-context learning to challenge datasets, while controlling for the models used, the number of examples, and the number of parameters, ranging from 125M to 30B. Our results show that fine-tuned language models can in fact generalize well out-of-domain. We find that both approaches generalize similarly; they exhibit large variation and depend on properties such as model size and the number of examples, highlighting that robust task adaptation remains a challenge.

```
@inproceedings{mosbach-etal-2023-shot,
    author = {
        Marius Mosbach and
        Tiago Pimentel and
        Shauli Ravfogel and
        Dietrich Klakow and
        Yanai Elazar
    },
    booktitle = {Findings of the Association for Computational Linguistics: ACL 2023},
    title = {Few-shot Fine-tuning vs. In-context Learning: A Fair Comparison and Evaluation},
    year = {2023},
    url = {https://aclanthology.org/2023.findings-acl.779/},
    pages = {12284--12314},
}
```