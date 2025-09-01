# --------------------------------------------------
# File Name : BA3C.py
# Problem   : Construct the Overlap Graph of a Collection of k-mers
# Author    : Worralop Srichainont
# Date      : 2025-08-20
# --------------------------------------------------

import os

# Directory Configurations
PROBLEM_DIR = os.path.dirname(os.path.abspath(__file__))
TESTCASE = os.path.join(PROBLEM_DIR, "src", "testcase.txt")
SRC_FILE = os.path.join(PROBLEM_DIR, "src", "rosalind_ba3c.txt")
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

# Initialize nucleotide pattern and adjacency list
patterns = []
adjacency_list = {}

# Input nucleotide patterns
with open(SOURCES[selection]) as file:
    patterns = [line.strip() for line in file]

# Construct the adjacency list of the graph
for from_pattern in patterns:
    # Initialize the adjacency list for current pattern
    current_adjacent = []

    # Check if there are any overlapped pattern
    for to_pattern in patterns:
        if from_pattern == to_pattern:
            continue
        if from_pattern[1:] == to_pattern[:-1]:
            current_adjacent.append(to_pattern)

    # If there are any adjacent pattern, store them in a dictionary
    if current_adjacent:
        adjacency_list[from_pattern] = current_adjacent

# Output the adjacency list
with open(ANS_FILE, "w", encoding="utf-8") as ans_file:
    for from_pattern, to_patterns in sorted(adjacency_list.items()):
        ans_file.write(f"{from_pattern} -> {' '.join(sorted(to_patterns))}\n")
