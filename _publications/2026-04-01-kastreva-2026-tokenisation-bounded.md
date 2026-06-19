---
title: "Tokenisation over Bounded Alphabets is Hard"
collection: publications
authors: "Violeta Kastreva, Philip Whittington, Dennis Komm, <b>Tiago Pimentel</b>"
permalink: /publication/2026-04-01-kastreva-2026-tokenisation-bounded
date: 2026-04-01
venue: 'International Conference on Learning Representations (ICLR)'
paperurl: 'https://arxiv.org/abs/2511.15709'
citation: 'Violeta Kastreva, Philip Whittington, Dennis Komm, Tiago Pimentel. 2026. Tokenisation over Bounded Alphabets is Hard. International Conference on Learning Representations (ICLR).'
---

<a href='https://arxiv.org/abs/2511.15709'>Find paper here</a>

Recent works have shown that tokenisation is NP-complete. However, these works assume tokenisation is applied to inputs with unboundedly large alphabets -- an unrealistic assumption, given that in practice tokenisers operate over fixed-size alphabets, such as bytes or Unicode characters. We close this gap by analysing tokenisation over bounded $n$-ary alphabets, considering two natural variants: bottom-up tokenisation and direct tokenisation, where we must, respectively, select a sequence of merge operations or a vocabulary whose application optimally compresses a dataset. First, we note that proving hardness results for an $n$-ary alphabet proves the same results for alphabets of any larger size. We then prove that even with binary alphabets, both variants are not only NP-complete, but admit no polynomial-time approximation scheme (unless P=NP). We further show that direct tokenisation remains NP-complete even when applied to unary alphabets. While unary alphabets may not be practically useful, this result establishes that the computational intractability of tokenisation is not an artifact of large alphabets or complex constructions, but a fundamental barrier. Overall, our results explain why practical algorithms such as BPE and UnigramLM are heuristic, and points toward approximation algorithms being an important path going forward for tokenisation research.

```
@inproceedings{kastreva2026bounded,
    author = {
        Violeta Kastreva and
        Philip Whittington and
        Dennis Komm and
        Tiago Pimentel
    },
    booktitle = {International Conference on Learning Representations (ICLR)},
    title = {Tokenisation over Bounded Alphabets is Hard},
    year = {2026},
    url = {https://arxiv.org/abs/2511.15709},
    pages = {},
}
```