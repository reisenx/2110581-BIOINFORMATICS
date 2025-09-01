# --------------------------------------------------
# File Name : PROT.py
# Problem   : Translating RNA into Protein
# Author    : Worralop Srichainont
# Date      : 2025-08-11
# --------------------------------------------------

import os

# Directory Configurations
PROBLEM_DIR = os.path.dirname(os.path.abspath(__file__))
TESTCASE = os.path.join(PROBLEM_DIR, "src", "testcase.txt")
SRC_FILE = os.path.join(PROBLEM_DIR, "src", "rosalind_prot.txt")
ANS_FILE = os.path.join(PROBLEM_DIR, "src", "answer.txt")

SOURCES = (TESTCASE, SRC_FILE)

# Initialize the RNA codon table
CODON_TABLE = {
    "U": {
        "U": {"U": "F", "C": "F", "A": "L", "G": "L"},
        "C": {"U": "S", "C": "S", "A": "S", "G": "S"},
        "A": {"U": "Y", "C": "Y", "A": "-", "G": "-"},
        "G": {"U": "C", "C": "C", "A": "-", "G": "W"},
    },
    "C": {
        "U": {"U": "L", "C": "L", "A": "L", "G": "L"},
        "C": {"U": "P", "C": "P", "A": "P", "G": "P"},
        "A": {"U": "H", "C": "H", "A": "Q", "G": "Q"},
        "G": {"U": "R", "C": "R", "A": "R", "G": "R"},
    },
    "A": {
        "U": {"U": "I", "C": "I", "A": "I", "G": "M"},
        "C": {"U": "T", "C": "T", "A": "T", "G": "T"},
        "A": {"U": "N", "C": "N", "A": "K", "G": "K"},
        "G": {"U": "S", "C": "S", "A": "R", "G": "R"},
    },
    "G": {
        "U": {"U": "V", "C": "V", "A": "V", "G": "V"},
        "C": {"U": "A", "C": "A", "A": "A", "G": "A"},
        "A": {"U": "D", "C": "D", "A": "E", "G": "E"},
        "G": {"U": "G", "C": "G", "A": "G", "G": "G"},
    },
}

# Prompt user to select source file
print("========================================")
print("Current Problem:", os.path.basename(__file__))
print("========== SELECT SOURCE FILE ==========")
print("0 for test file")
print("1 for actual source file")
selection = int(input("Enter your choice (0 or 1): ").strip())
print("========================================")

# Extract RNA sequence from file
rna = ""
with open(SOURCES[selection]) as file:
    for line in file:
        rna += line.strip()

# Translate RNA to Protein
proteins = []
for idx in range(0, len(rna), 3):
    # Extract current codon from RNA
    codon = rna[idx : idx + 3]
    if len(codon) == 3:
        # Translate codon to amino acid
        amino_acid = CODON_TABLE[codon[0]][codon[1]][codon[2]]

        # If the amino acid is a stop codon, break the loop
        if amino_acid == "-":
            break

        # Append the amino acid to the protein list
        proteins.append(amino_acid)

# Output the protein sequence
protein_sequence = "".join(proteins)
with open(ANS_FILE, "w", encoding="utf-8") as ans_file:
    ans_file.write(protein_sequence)
