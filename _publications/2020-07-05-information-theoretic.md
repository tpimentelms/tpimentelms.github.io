---
title: "Information-Theoretic Probing for Linguistic Structure"
collection: publications
authors: "<b>Tiago Pimentel</b>, Josef Valvoda, Rowan Hall Maudslay, Ran Zmigrod, Adina Williams, Ryan Cotterell"
permalink: /publication/2020-07-05-information-theoretic
date: 2020-07-05
venue: 'Association for Computational Linguistics (ACL)'
paperurl: 'https://aclanthology.org/2020.acl-main.420/'
citation: 'Tiago Pimentel, Josef Valvoda, Rowan Hall Maudslay, Ran Zmigrod, Adina Williams, Ryan Cotterell. 2020. Information-Theoretic Probing for Linguistic Structure. Association for Computational Linguistics (ACL).'
---

<a href='https://aclanthology.org/2020.acl-main.420/'>Find paper here</a>

The success of neural networks on a diverse set of NLP tasks has led researchers to question how much these networks actually &apos;&apos;know&apos;&apos; about natural language. Probes are a natural way of assessing this. When probing, a researcher chooses a linguistic task and trains a supervised model to predict annotations in that linguistic task from the network&apos;s learned representations. If the probe does well, the researcher may conclude that the representations encode knowledge related to the task. A commonly held belief is that using simpler models as probes is better; the logic is that simpler models will identify linguistic structure, but not learn the task itself. We propose an information-theoretic operationalization of probing as estimating mutual information that contradicts this received wisdom: one should always select the highest performing probe one can, even if it is more complex, since it will result in a tighter estimate, and thus reveal more of the linguistic information inherent in the representation. The experimental portion of our paper focuses on empirically estimating the mutual information between a linguistic property and BERT, comparing these estimates to several baselines. We evaluate on a set of ten typologically diverse languages often underrepresented in NLP research---plus English---totalling eleven languages. Our implementation is available in https://github.com/rycolab/info-theoretic-probing.

```
@inproceedings{pimentel2020information,
    author = {
        Tiago Pimentel and
        Josef Valvoda and
        Rowan Hall Maudslay and
        Ran Zmigrod and
        Adina Williams and
        Ryan Cotterell
    },
    booktitle = {Association for Computational Linguistics (ACL)},
    title = {Information-Theoretic Probing for Linguistic Structure},
    year = {2020},
    doi = {10.18653/v1/2020.acl-main.420},
    url = {https://aclanthology.org/2020.acl-main.420/},
    pages = {4609--4622},
}
```