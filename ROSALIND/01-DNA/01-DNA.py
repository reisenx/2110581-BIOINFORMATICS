# --------------------------------------------------
# File Name : 01-DNA.py
# Problem   : Counting DNA Nucleotides
# Author    : Worralop Srichainont
# Date      : 2025-08-11
# --------------------------------------------------

import os

# Directory Configurations
PROBLEM_DIR = os.path.dirname(os.path.abspath(__file__))
TESTCASE = os.path.join(PROBLEM_DIR, "src", "testcase.txt")
SRC_FILE = os.path.join(PROBLEM_DIR, "src", "rosalind_dna.txt")
ANS_FILE = os.path.join(PROBLEM_DIR, "src", "answer.txt")

# Initialize Nucleotide Count Dictionary
NUCLEOTIDE_COUNT = {"A": 0, "C": 0, "G": 0, "T": 0}

# Open the DNA file and count nucleotides
with open(SRC_FILE) as file:
    for line in file:
        for char in line.strip():
            NUCLEOTIDE_COUNT[char] += 1

# Construct the result string
result = ""
for _, count in NUCLEOTIDE_COUNT.items():
    result += f"{count} "
result = result.strip()

# Output the nucleotide counts
with open(ANS_FILE, "w", encoding="utf-8") as ans_file:
    ans_file.write(result)
