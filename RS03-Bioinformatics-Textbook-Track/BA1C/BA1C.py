# --------------------------------------------------
# File Name : BA1C.py
# Problem   : Find the Reverse Complement of a String
# Author    : Worralop Srichainont
# Date      : 2025-08-20
# --------------------------------------------------

import os

# Directory Configurations
PROBLEM_DIR = os.path.dirname(os.path.abspath(__file__))
TESTCASE = os.path.join(PROBLEM_DIR, "src", "testcase.txt")
SRC_FILE = os.path.join(PROBLEM_DIR, "src", "rosalind_ba1c.txt")
ANS_FILE = os.path.join(PROBLEM_DIR, "src", "answer.txt")

SOURCES = (TESTCASE, SRC_FILE)

# Initialize the DNA complement mapping
DNA_COMPLEMENT = {
    "A": "T",
    "T": "A",
    "C": "G",
    "G": "C",
}

# Prompt user to select source file
print("========================================")
print("Current Problem:", os.path.basename(__file__))
print("========== SELECT SOURCE FILE ==========")
print("0 for test file")
print("1 for actual source file")
selection = int(input("Enter your choice (0 or 1): ").strip())
print("========================================")

# Extract DNA sequence from file
dna = ""
with open(SOURCES[selection]) as file:
    for line in file:
        dna += line.strip()

# Generate the reverse complement of the DNA sequence
complemented_dna = []
for nucleotide in dna[::-1]:
    complemented_dna.append(DNA_COMPLEMENT[nucleotide])

# Output the reverse complement sequence
with open(ANS_FILE, "w", encoding="utf-8") as ans_file:
    ans_file.write("".join(complemented_dna))
