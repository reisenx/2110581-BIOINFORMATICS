# --------------------------------------------------
# File Name : INI2.py
# Problem   : Variables and Some Arithmetic
# Author    : Worralop Srichainont
# Date      : 2025-08-27
# --------------------------------------------------

import os

# Directory Configurations
PROBLEM_DIR = os.path.dirname(os.path.abspath(__file__))
TESTCASE = os.path.join(PROBLEM_DIR, "src", "testcase.txt")
SRC_FILE = os.path.join(PROBLEM_DIR, "src", "rosalind_ini2.txt")
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

# Input right triangle whose legs have lengths a and b from a file.
a, b = 0, 0
with open(SOURCES[selection]) as file:
    a, b = [int(num) for num in file.readline().strip().split()]

# Output the square of the hypotenuse of the right triangle
with open(ANS_FILE, "w", encoding="utf-8") as ans_file:
    ans_file.write(str(a**2 + b**2))
