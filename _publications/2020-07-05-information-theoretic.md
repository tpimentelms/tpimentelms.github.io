---
title: "Information-Theoretic Probing for Linguistic Structure"
collection: publications
authors: "Tiago Pimentel, Josef Valvoda, Rowan Hall Maudslay, Ran Zmigrod, Adina Williams, and Ryan Cotterell"
permalink: /publication/2020-07-05-
excerpt: 'This paper is about '
date: 2020-07-05
venue: 'Association for Computational Linguistics (ACL)'
paperurl: 'https://www.aclweb.org/anthology/2020.acl-main.420/'
citation: 'Pimentel T, Valvoda J, Maudslay RH, Zmigrod R, Williams A, Cotterell R. Information-theoretic probing for linguistic structure. In: Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics, 2020 Jul (pp. 4609-4622).'
---

The success of neural networks on a diverse set of NLP tasks has led researchers to question how much these networks actually ''know'' about natural language. Probes are a natural way of assessing this. When probing, a researcher chooses a linguistic task and trains a supervised model to predict annotations in that linguistic task from the network's learned representations. If the probe does well, the researcher may conclude that the representations encode knowledge related to the task. A commonly held belief is that using simpler models as probes is better; the logic is that simpler models will identify linguistic structure, but not learn the task itself. We propose an information-theoretic operationalization of probing as estimating mutual information that contradicts this received wisdom: one should always select the highest performing probe one can, even if it is more complex, since it will result in a tighter estimate, and thus reveal more of the linguistic information inherent in the representation. The experimental portion of our paper focuses on empirically estimating the mutual information between a linguistic property and BERT, comparing these estimates to several baselines. We evaluate on a set of ten typologically diverse languages often underrepresented in NLP research---plus English---totalling eleven languages. Our implementation is available in https://github.com/rycolab/info-theoretic-probing.


```
@inproceedings{pimentel2020information,
    title = "Information-Theoretic Probing for Linguistic Structure",
    author = "Pimentel, Tiago  and
      Valvoda, Josef  and
      Hall Maudslay, Rowan  and
      Zmigrod, Ran  and
      Williams, Adina  and
      Cotterell, Ryan",
    booktitle = "Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics",
    month = jul,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.acl-main.420",
    doi = "10.18653/v1/2020.acl-main.420",
    pages = "4609--4622",
}
```