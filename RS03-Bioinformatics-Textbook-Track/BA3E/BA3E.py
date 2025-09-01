# --------------------------------------------------
# File Name : BA3E.py
# Problem   : Construct the De Bruijn Graph of a Collection of k-mers
# Author    : Worralop Srichainont
# Date      : 2025-08-20
# --------------------------------------------------

import os

# Directory Configurations
PROBLEM_DIR = os.path.dirname(os.path.abspath(__file__))
TESTCASE = os.path.join(PROBLEM_DIR, "src", "testcase.txt")
SRC_FILE = os.path.join(PROBLEM_DIR, "src", "rosalind_ba3e.txt")
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

# Initialize the adjacency list
adjacency_list = {}

# Construct the adjacency list for each patterns
with open(SOURCES[selection]) as file:
    for line in file:
        # Extract prefix and suffix for current pattern
        pattern = line.strip()
        prefix = pattern[:-1]
        suffix = pattern[1:]

        # Add the edge to the adjacency list
        if prefix not in adjacency_list:
            adjacency_list[prefix] = []
        adjacency_list[prefix].append(suffix)

# Output the adjacency list
with open(ANS_FILE, "w", encoding="utf-8") as ans_file:
    for from_pattern, to_patterns in sorted(adjacency_list.items()):
        ans_file.write(f"{from_pattern} -> {','.join(sorted(to_patterns))}\n")
