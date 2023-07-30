---
title: "On the Intersection of Context-Free and Regular Languages"
collection: publications
authors: "Clemente Pasti, Andreas Opedal, <b>Tiago Pimentel</b>, Tim Vieira, Jason Eisner, Ryan Cotterell"
permalink: /publication/2023-05-01-pasti-etal-2023-intersection
date: 2023-05-01
venue: 'Proceedings of the 17th Conference of the European Chapter of the Association for Computational Linguistics'
paperurl: 'https://aclanthology.org/2023.eacl-main.52/'
citation: 'Clemente Pasti, Andreas Opedal, Tiago Pimentel, Tim Vieira, Jason Eisner, and Ryan Cotterell. 2023. On the Intersection of Context-Free and Regular Languages. In Proceedings of the 17th Conference of the European Chapter of the Association for Computational Linguistics, pages 737–749, Dubrovnik, Croatia. Association for Computational Linguistics.'
---

<a href='https://aclanthology.org/2023.eacl-main.52/'>Find paper here</a>

The Bar-Hillel construction is a classic result in formal language theory. It shows, by a simple construction, that the intersection of a context-free language and a regular language is itself context-free. In the construction, the regular language is specified by a finite-state automaton. However, neither the original construction (Bar-Hillel et al., 1961) nor its weighted extension (Nederhof and Satta, 2003) can handle finite-state automata with ε-arcs. While it is possible to remove ε-arcs from a finite-state automaton efficiently without modifying the language, such an operation modifies the automaton’s set of paths. We give a construction that generalizes the Bar- Hillel in the case the desired automaton has ε-arcs, and further prove that our generalized construction leads to a grammar that encodes the structure of both the input automaton and grammar while retaining the asymptotic size of the original construction.

```
@inproceedings{pasti-etal-2023-intersection,
    author = {
        Clemente Pasti and
        Andreas Opedal and
        Tiago Pimentel and
        Tim Vieira and
        Jason Eisner and
        Ryan Cotterell
    },
    booktitle = {Proceedings of the 17th Conference of the European Chapter of the Association for Computational Linguistics},
    title = {On the Intersection of Context-Free and Regular Languages},
    year = {2023},
    url = {https://aclanthology.org/2023.eacl-main.52/},
    pages = {737--749},
}
```