# --------------------------------------------------
# File Name : INI4.py
# Problem   : Conditions and Loops
# Author    : Worralop Srichainont
# Date      : 2025-08-27
# --------------------------------------------------

import os

# Directory Configurations
PROBLEM_DIR = os.path.dirname(os.path.abspath(__file__))
TESTCASE = os.path.join(PROBLEM_DIR, "src", "testcase.txt")
SRC_FILE = os.path.join(PROBLEM_DIR, "src", "rosalind_ini4.txt")
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

# Input number range from a file.
start, end = 0, 0
with open(SOURCES[selection]) as file:
    start, end = [int(num) for num in file.readline().strip().split()]

# Calculate sum of all odd numbers in range start <= num <= end
ans = 0
for num in range(start, end + 1):
    if num % 2 == 1:
        ans += num

# Output the sum
with open(ANS_FILE, "w", encoding="utf-8") as ans_file:
    ans_file.write(str(ans))
