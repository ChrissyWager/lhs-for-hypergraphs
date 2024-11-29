# lhs-for-hypergraphs
Investigation into the possibilities of using Locality Sensitive Hashing schemes to aid in the partition of hypergraphs.

A shortlist consisting of the following LHS schemes was chosen for comparison:
- Densifying One Permutation Hashing (of the MinHash family)
- ProbMinHash (3a specifically) (also of the MinHash family)
- SimHash (of the family that uses Cosine Similarity)
- Random Projections LSH (also of the family that uses Cosine Similarity)
- P-Stable LSH (using Euclidean Distance)
- Original Locality Sensitive Hashing (bit-wise, using Hamming Distance)

## Current Status
Implementations of the various schemes, and datasets for testing, have been collected and tested across numerous projects to form a basis for this project.

## Next Steps
Will establish uniformity inside the code to ease comparison of aspects such as runtime, as well as edit the code so as to output similarity values for comparison across the schemes and to facilitate the tuning of hyperparameters common across all schemes (such as parameter K for the number of hash functions or random projections).
Will also add a more generalized pre-processing step for hgf files to ease testing later on.

