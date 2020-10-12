---
title: "Speakers Fill Lexical Semantic Gaps with Context"
collection: publications
authors: "Tiago Pimentel, Rowan Hall Maudslay, Damián Blasi, and Ryan Cotterell"
permalink: /publication/2020-11-16-speakers-fill-lexical-gaps
excerpt: 'This paper is about '
date: 2020-11-16
venue: 'Empirical Methods in Natural Language Processing (EMNLP)'
paperurl: 'https://arxiv.org/abs/2010.02172'
citation: 'Pimentel T, Hall Maudslay R, Blasi D, Cotterell R. Speakers Fill Lexical Semantic Gaps with Context. In: Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP), 2020 Nov.'
---

Lexical ambiguity is widespread in language, allowing for the reuse of economical word forms and therefore making language more efficient. If ambiguous words cannot be disambiguated from context, however, this gain in efficiency might make language less clear---resulting in frequent miscommunication. For a language to be clear and efficiently encoded, we posit that the lexical ambiguity of a word type should correlate with how much information context provides about it, on average. To investigate whether this is the case, we operationalise the lexical ambiguity of a word as the entropy of meanings it can take, and provide two ways to estimate this---one which requires human annotation (using WordNet), and one which does not (using BERT), making it readily applicable to a large number of languages. We validate these measures by showing that, on six high-resource languages, there are significant Pearson correlations between our BERT-based estimate of ambiguity and the number of synonyms a word has in WordNet (e.g. ρ=0.40 in English). We then test our main hypothesis---that a word's lexical ambiguity should negatively correlate with its contextual uncertainty---and find significant correlations on all 18 typologically diverse languages we analyse. This suggests that, in the presence of ambiguity, speakers compensate by making contexts more informative.

```
@inproceedings{pimentel2020speakers,
    title = "Speakers Fill Lexical Semantic Gaps with Context",
    author = "Pimentel, Tiago and
    Hall Maudslay, Rowan and
    Blasi, Damián and
    Cotterell, Ryan",
    booktitle = "Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)",
    year = "2020",
    publisher = "Association for Computational Linguistics",
}
```