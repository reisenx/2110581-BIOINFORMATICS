# Assignment 6: Regulatory Motif Search

# Problem Description Part I

This problem requires you to identify a common motif within a set of biological
sequences and then visualize the consensus of that motif. You will use a
motif-finding algorithm to discover the pattern and then generate a sequence
logo to represent the motif's profile.

Apply one of the following algorithm to identify the most likely recurring motif
across all the provided sequences.

-   Randomized Motif Search with Pseudo-count

-   Gibbs Sampling with Pseudo-count

## Input

You will be given an input file containing a collection of DNA sequences, each
in FASTA format.

```
>test1
acaaccatatatagtagccactgaat
>test2
ccaccccatatatagtagtgcgggtggtg
>test3
ccataaatagataggcagactgtcgctgt
>test4
gtaaacataccataaatagga
...more
```

## Output

Create an output file that is a copy of the original input file, but with one
modification: for each sequence, the identified motif must be converted to
uppercase letters, while the rest of the sequence remains in its original case.

```
>test1
acaaCCATATATAGtagccactgaat
>test2
ccaccCCATATATAGtagtgcgggtggtg
>test3
CCATAAATAGataggcagactgtcgctgt
>test4
gtaaacataCCATAAATAGga
...more
```

---

# Problem Description Part II

Upload motif DNA sequences to WebLogo (https://weblogo.berkeley.edu/logo.cgi) to
generate a sequence logo.

Example sequences data for sequence logo generation.

```
>test1
CCATATATAG
>test2
CCATATATAG
>test3
CCATAAATAG
>test4
CCATAAATAG
...more
```
