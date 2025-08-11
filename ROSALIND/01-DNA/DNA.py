# --------------------------------------------------
# File Name : DNA.py
# Problem   : Counting DNA Nucleotides
# Author    : Worralop Srichainont
# Date      : 2025-08-11
# --------------------------------------------------

import os

# Directory Configurations
SRC_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DIR = os.path.join(SRC_DIR, "src", "testcase.txt")
DIR = os.path.join(SRC_DIR, "src", "rosalind_dna.txt")

# Initialize Nucleotide Count Dictionary
NUCLEOTIDE_COUNT = {"A": 0, "C": 0, "G": 0, "T": 0}

# Open the DNA file and count nucleotides
with open(DIR) as file:
    for line in file:
        for char in line.strip():
            NUCLEOTIDE_COUNT[char] += 1

# Output the nucleotide counts
print(*(NUCLEOTIDE_COUNT.values()))
