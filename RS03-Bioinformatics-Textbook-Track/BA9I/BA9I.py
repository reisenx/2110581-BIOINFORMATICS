# --------------------------------------------------
# File Name : BA9I.py
# Problem   : Construct the Burrows-Wheeler Transform of a String
# Author    : Worralop Srichainont
# Date      : 2025-08-27
# --------------------------------------------------

import os

# Directory Configurations
PROBLEM_DIR = os.path.dirname(os.path.abspath(__file__))
TESTCASE = os.path.join(PROBLEM_DIR, "src", "testcase.txt")
SRC_FILE = os.path.join(PROBLEM_DIR, "src", "rosalind_ba9i.txt")
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

# Input the initial string.
with open(SOURCES[selection]) as file:
    initial_string = file.readline().strip()

# Generate all cyclically shifted strings and sort alphabetically.
shifted_strings = []
for i in range(len(initial_string)):
    shifted_strings.append(initial_string[i:] + initial_string[:i])
shifted_strings.sort()

# Output the Burrows-Wheeler Transform
bwt = "".join(s[-1] for s in shifted_strings)
with open(ANS_FILE, "w", encoding="utf-8") as ans_file:
    ans_file.write(bwt)
