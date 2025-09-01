# Assignment 2: Read Mapping

# Problem Description

-   **Align Reads:** For each read from both reads1.fastq and reads2.fastq, find
    its correct starting position on the reference genome.

-   **Identify Variants:** Compare each aligned read to the corresponding
    segment of the reference genome. A position where the base in the read
    differs from the base in the reference is considered a variant.

-   **Generate Visualization:** Create a formatted output that displays the
    reference genome, all the aligned reads, and marks the variant positions
    according to the rules below.

## Input

**`reference.fastq`**

Contains a single, complete reference DNA sequence.

```
>reference_genome
GCAGCCCGTCTTCAATGTTGGAATGGGGGTACCTTCACCGCGCGAGGTTGATTCCTCCGGGTGCCCCCGGGCGCGGGCGGTGCGACAGCCGGACATCTCT
```

**`reads1.fastq`**

A collection of short DNA sequence fragments (reads).

```
>read_001
AATGTTGGAATGGGGGTACCTTCACCGCGCGAGGT
>read_002
TGGAATGGGGGTACCTTCACCGCGCGAGGTTGATT
>read_003
CCGTCTTCAATGCTGGAATGGGGGTACCTTCACCG
>read_004
GCAGCCCGTCTTCAATGCTGGAATGGGGGTACCTT
>read_005
CTTCAATGTTGGAATGGGGGTACCTTCACCGCGCG
```

**`reads2.fastq`**

A second collection of short DNA sequence fragments (reads).

```
>read_001
GGGTGCCCCCGGGCGCGGGCGGTGCGACAGCCGGA
>read_002
CCCCCGGGCGCGGGCGGTGCGACAGCCGGACATCT
>read_003
ATTCCTCCGGGTGCCCCCGGGCGCGGGCGGTGCTA
>read_004
GGTTGATTCCTCCGGGTGCCCCCGGGCGCGGGCGG
>read_005
CTCCGGGTGCCCCCGGGCGCGGGCGGTGCTACAGC
```

## Output

Your output must be formatted precisely as follows:

-   **First Line (Variant Header):** This line is used to mark variant
    locations. Place an asterisk (`*`) directly above each position in the
    reference genome where at least one of the aligned reads has a mismatch.

-   **Second Line (Reference Sequence):** Display the entire reference genome
    sequence.

-   **Subsequent Lines (Aligned Reads):**

    -   Display each read from both input files on its own line, positioned
        horizontally to match its alignment location against the reference
        sequence above it.

    -   If a base within an aligned read does not match the reference sequence,
        replace that base with a hyphen (`-`).

    -   Maintain the correct spatial alignment for all reads relative to the
        reference.

**Example Output**

```
                       *                                   *
ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFG-HIJKLMNOPQRSTUVWXYZ
ABCDEFGHIJKLMNOPQRSTUVWX           JKLMNOPQRSTUVWXYZABCDEF
  CDEFGHIJKLMNOPQRSTUVW-YZA            NOPQRSTUVWXYZABCDEFGHHI
     FGHIJKLMNOPQRSTUVW-YZABCD          OPQRSTUVWXYZABCDEFGHHIJKL
            MNOPQRSTUVWXYZABCDEFGHIJ          UVWXYZABCDEFG-HIJKLMNOPQR
                  STUVWXYZABCDEFGHIJKLMNO           ABCDEFG-HIJKLMNOPQRSTU
                   TUVWXYZABCDEFGHIJKLMNOPQRS          DEFGHHIJKLMNOPQRSTUVWX
```
