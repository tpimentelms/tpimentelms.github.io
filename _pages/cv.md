---
layout: prose
title: "CV"
permalink: /cv/
description: "Curriculum vitae — Tiago Pimentel."
redirect_from:
  - /resume
---

# CV

A short version is below; the [full CV is available as a PDF]({{ '/files/cv.pdf' | relative_url }}).

## Education

- **University of Cambridge** — Ph.D. in Computer Science, 2019–2023. Advisors: Simone Teufel & Ryan Cotterell. Gates Cambridge Scholar; Facebook Fellow.
- **Universidade Federal de Minas Gerais (UFMG)** — M.S. in Computer Science, 2016–2018. Advisors: Adriano Veloso & Nivio Ziviani.
- **Universidade de Brasília (UnB)** — B.E. in Mechatronics Engineering, 2009–2014. Advisor: Carla Koike. Valedictorian (highest GPA in class).
- **Washington University in St. Louis** — Non-degree in Computer Science, 2012–2013. Brazil Scientific Mobility Program scholar.

## Experience

- **Postdoctoral Researcher, ETH Zürich** — 2023–present. Machine learning interpretability and natural language generation.
- **Research Intern, Google** — 2022. How metaphors are encoded in language models.
- **Research Intern, Google** — 2021. Upside-down reinforcement learning for recommendation systems.
- **Data Scientist, Kunumi** — 2018–2019. Active anomaly detection; conversational agents; led deep-learning & NLP reading groups.
- **Adjunct Lecturer, IESB** — 2018–2019. Taught Unsupervised Learning and Reinforcement Learning (AI postgraduate specialisation).
- **Voluntary Teacher, EduBot** — 2014–2015. Computer science and robotics for under-resourced public-school students.

## Publications

<div class="pubs">
{% assign cvpubs = site.publications | sort: "date" | reverse %}
{% for pub in cvpubs %}{% include pub-entry.html pub=pub %}{% endfor %}
</div>
