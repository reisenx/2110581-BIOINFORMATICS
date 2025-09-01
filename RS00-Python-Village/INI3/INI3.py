# --------------------------------------------------
# File Name : INI3.py
# Problem   : Strings and Lists
# Author    : Worralop Srichainont
# Date      : 2025-08-27
# --------------------------------------------------

import os

# Directory Configurations
PROBLEM_DIR = os.path.dirname(os.path.abspath(__file__))
TESTCASE = os.path.join(PROBLEM_DIR, "src", "testcase.txt")
SRC_FILE = os.path.join(PROBLEM_DIR, "src", "rosalind_ini3.txt")
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

# Input original text and slice indices from a file.
text = ""
start_01, end_01, start_02, end_02 = 0, 0, 0, 0
with open(SOURCES[selection]) as file:
    text = file.readline().strip()
    start_01, end_01, start_02, end_02 = [
        int(num) for num in file.readline().strip().split()
    ]

# Output the formatted string
output_str = f"{text[start_01:end_01 + 1]} {text[start_02:end_02 + 1]}"
with open(ANS_FILE, "w", encoding="utf-8") as ans_file:
    ans_file.write(output_str)
