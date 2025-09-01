# --------------------------------------------------
# File Name : INI5.py
# Problem   : Working with Files
# Author    : Worralop Srichainont
# Date      : 2025-08-27
# --------------------------------------------------

import os

# Directory Configurations
PROBLEM_DIR = os.path.dirname(os.path.abspath(__file__))
TESTCASE = os.path.join(PROBLEM_DIR, "src", "testcase.txt")
SRC_FILE = os.path.join(PROBLEM_DIR, "src", "rosalind_ini5.txt")
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

# Input text on even lines (1-based) from a file.
even_lines = []
with open(SOURCES[selection]) as file:
    for idx, line in enumerate(file):
        if (idx + 1) % 2 == 0:
            even_lines.append(line.strip())

# Output the even lines
output_str = "\n".join(even_lines)
with open(ANS_FILE, "w", encoding="utf-8") as ans_file:
    ans_file.write(output_str)
