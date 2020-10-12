---
title: "Efficient estimation of node representations in large graphs using linear contexts"
collection: publications
authors: "Tiago Pimentel, Rafael Castro, Adriano Veloso, and Nivio Ziviani"
permalink: /publication/2019-07-14-efficient-estimation
excerpt: 'This paper is about '
date: 2019-07-14
venue: 'International Joint Conference on Neural Networks (IJCNN)'
paperurl: 'https://ieeexplore.ieee.org/document/8852262'
citation: 'Pimentel T, Castro R, Veloso A, Ziviani N. Efficient estimation of node representations in large graphs using linear contexts. In: International Joint Conference on Neural Networks (IJCNN), 2019 Jul 14 (pp. 1-8). IEEE.'
---

Learning distributed representations in graphs has a rising interest in the neural network community. Recent works have proposed new methods for learning low dimensional embeddings of nodes and edges in graphs and networks. Several of these methods rely on the SkipGram algorithm to learn distributed representations, and they usually process a large number of multi-hop neighbors in order to produce the context from which node representations are learned. This is a limiting factor for these methods as graphs and networks keep growing in size. In this paper, we propose a simple alternate method which is as effective as previous methods, but being much faster at learning node representations. Our proposed method employs a restricted number of permutations over the immediate neighborhood of a node as context to generate its representation, thus avoiding long walks and large contexts while learning the representations. We present a thorough evaluation showing that our method outperforms state-of-the-art methods in six different datasets related to the problems of link prediction and node classification, being one to three orders of magnitude faster than baselines when generating node embeddings for very large graphs.

```
@INPROCEEDINGS{pimentel2019efficient,
  author={
    Tiago Pimentel and
    Rafael Castro and
    Adriano Veloso and
    Nivio Ziviani
  },
  booktitle={International Joint Conference on Neural Networks (IJCNN)},
  title={Efficient Estimation of Node Representations in Large Graphs using Linear Contexts},
  year={2019},
  volume={},
  number={},
  pages={1-8},
}
```