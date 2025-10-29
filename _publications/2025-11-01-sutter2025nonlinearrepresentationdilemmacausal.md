---
title: "The Non-Linear Representation Dilemma: Is Causal Abstraction Enough for Mechanistic Interpretability?"
collection: publications
authors: "Denis Sutter, Julian Minder, Thomas Hofmann, <b>Tiago Pimentel</b> "
permalink: /publication/2025-11-01-sutter2025nonlinearrepresentationdilemmacausal
date: 2025-11-01
venue: 'Advances in Neural Information Processing Systems'
paperurl: 'https://arxiv.org/abs/2507.08802'
citation: 'Denis Sutter, Julian Minder, Thomas Hofmann, Tiago Pimentel. 2025. The Non-Linear Representation Dilemma: Is Causal Abstraction Enough for Mechanistic Interpretability? NeurIPS'
---

<a href='https://arxiv.org/abs/2507.08802'>Find paper here</a>

The concept of causal abstraction got recently popularised to demystify the opaque decision-making processes of machine learning models; in short, a neural network can be abstracted as a higher-level algorithm if there exists a function which allows us to map between them. Notably, most interpretability papers implement these maps as linear functions, motivated by the linear representation hypothesis: the idea that features are encoded linearly in a model&apos;s representations. However, this linearity constraint is not required by the definition of causal abstraction. In this work, we critically examine the concept of causal abstraction by considering arbitrarily powerful alignment maps. In particular, we prove that under reasonable assumptions, any neural network can be mapped to any algorithm, rendering this unrestricted notion of causal abstraction trivial and uninformative. We complement these theoretical findings with empirical evidence, demonstrating that it is possible to perfectly map models to algorithms even when these models are incapable of solving the actual task; e.g., on an experiment using randomly initialised language models, our alignment maps reach 100% interchange-intervention accuracy on the indirect object identification task. This raises the non-linear representation dilemma: if we lift the linearity constraint imposed to alignment maps in causal abstraction analyses, we are left with no principled way to balance the inherent trade-off between these maps&apos; complexity and accuracy. Together, these results suggest an answer to our title&apos;s question: causal abstraction is not enough for mechanistic interpretability, as it becomes vacuous without assumptions about how models encode information. Studying the connection between this information-encoding assumption and causal abstraction should lead to exciting future work. 

```
@inproceedings{sutter2025nonlinearrepresentationdilemmacausal,
    author = {
        Denis Sutter and
        Julian Minder and
        Thomas Hofmann and
        Tiago Pimentel 
    },
    booktitle = {Advances in Neural Information Processing Systems},
    title = {The Non-Linear Representation Dilemma: Is Causal Abstraction Enough for Mechanistic Interpretability?},
    year = {2025},
    url = {https://arxiv.org/abs/2507.08802},
    pages = {},
}
```