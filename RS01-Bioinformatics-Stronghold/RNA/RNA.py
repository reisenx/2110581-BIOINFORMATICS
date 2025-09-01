# --------------------------------------------------
# File Name : 02-RNA.py
# Problem   : Transcribing DNA into RNA
# Author    : Worralop Srichainont
# Date      : 2025-08-11
# --------------------------------------------------

import os

# Directory Configurations
PROBLEM_DIR = os.path.dirname(os.path.abspath(__file__))
TESTCASE = os.path.join(PROBLEM_DIR, "src", "testcase.txt")
SRC_FILE = os.path.join(PROBLEM_DIR, "src", "rosalind_rna.txt")
ANS_FILE = os.path.join(PROBLEM_DIR, "src", "answer.txt")

SOURCES = (TESTCASE, SRC_FILE)

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

# Replace 'T' with 'U' to convert DNA to RNA
rna = dna.replace("T", "U")

# Output the RNA sequence
with open(ANS_FILE, "w", encoding="utf-8") as ans_file:
    ans_file.write(rna)
