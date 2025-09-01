# --------------------------------------------------
# File Name : BA9J.py
# Problem   : Reconstruct a String from its Burrows-Wheeler Transform
# Author    : Worralop Srichainont
# Date      : 2025-08-27
# --------------------------------------------------

import os

# Directory Configurations
PROBLEM_DIR = os.path.dirname(os.path.abspath(__file__))
TESTCASE = os.path.join(PROBLEM_DIR, "src", "testcase.txt")
SRC_FILE = os.path.join(PROBLEM_DIR, "src", "rosalind_ba9j.txt")
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

# Input the Burrows-Wheeler Transform string.
with open(SOURCES[selection]) as file:
    bwt = file.readline().strip()

# Reconstruct the original string from the Burrows-Wheeler Transform.
decrypted_string = sorted(list(bwt))
for i in range(len(bwt) - 1):
    # Insert the each character from the BWT into the decrypted string
    for j in range(len(bwt)):
        decrypted_string[j] = bwt[j] + decrypted_string[j]

    # Sort the decrypted string on each iteration
    decrypted_string.sort()

# Output the reconstructed string
ans = f"{decrypted_string[0].lstrip('$')}$"
with open(ANS_FILE, "w", encoding="utf-8") as ans_file:
    ans_file.write(ans)
