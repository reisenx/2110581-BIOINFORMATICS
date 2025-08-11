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

SOURCES = (TESTCASE, SRC_FILE)

# Initialize Nucleotide Count Dictionary
NUCLEOTIDE_COUNT = {"A": 0, "C": 0, "G": 0, "T": 0}

# Prompt user to select source file
print("========================================")
print("Current Problem:", os.path.basename(__file__))
print("========== SELECT SOURCE FILE ==========")
print("0 for test file")
print("1 for actual source file")
selection = int(input("Enter your choice (0 or 1): ").strip())
print("========================================")

# Open the DNA file and count nucleotides
with open(SOURCES[selection]) as file:
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
