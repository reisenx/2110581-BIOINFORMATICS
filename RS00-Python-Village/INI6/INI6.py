# --------------------------------------------------
# File Name : INI6.py
# Problem   : Dictionaries
# Author    : Worralop Srichainont
# Date      : 2025-08-27
# --------------------------------------------------

import os

# Directory Configurations
PROBLEM_DIR = os.path.dirname(os.path.abspath(__file__))
TESTCASE = os.path.join(PROBLEM_DIR, "src", "testcase.txt")
SRC_FILE = os.path.join(PROBLEM_DIR, "src", "rosalind_ini6.txt")
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

# Count the frequency of each word in the selected file.
word_count = {}
with open(SOURCES[selection]) as file:
    for line in file:
        for word in line.strip().split():
            word_count[word] = word_count.get(word, 0) + 1

# Output the word count
output_str = "\n".join(f"{word} {count}" for word, count in word_count.items())
with open(ANS_FILE, "w", encoding="utf-8") as ans_file:
    ans_file.write(output_str)
