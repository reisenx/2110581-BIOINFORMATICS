# --------------------------------------------------
# File Name : capitalize_motif.py
# Problem   : Assignment 6 (Motif Search)
# Authors   : Worralop Srichainont
#           : Suvijak Jintanaphan
#           : Thara Waranuset
# Date      : 2025-08-28
# --------------------------------------------------


import os

# Directory Configurations
PROBLEM_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_FILE = os.path.join(PROBLEM_DIR, "src", "dna_sequences.txt")
GENERATED_FILE = os.path.join(PROBLEM_DIR, "src", "generate.txt")
ANS_FILE = os.path.join(PROBLEM_DIR, "src", "answer.txt")


# Capitalize motif on each DNA sequence
def get_capitalize_motifs(dna_sequences, best_motifs):
    capitalized_motifs = []
    for i in range(len(dna_sequences)):
        idx = dna_sequences[i].find(best_motifs[i])
        if idx != -1:
            capitalized_motifs.append(
                dna_sequences[i][:idx]
                + best_motifs[i].upper()
                + dna_sequences[i][idx + len(best_motifs[i]) :]
            )
    return capitalized_motifs


# Main function
def main():
    # Input all DNA sequence into a list
    dna_sequences = []
    with open(SRC_FILE) as file:
        for line in file:
            if line.startswith(">"):
                continue
            dna_sequences.append(line.strip())

    # Get all generated motifs from the generate file
    generated_motif = []
    with open(GENERATED_FILE) as file:
        for line in file:
            if line.startswith(">"):
                continue
            generated_motif.append(line.strip().lower())

    # Output capitalized motifs to a file
    capitalized_motifs = get_capitalize_motifs(dna_sequences, generated_motif)
    with open(ANS_FILE, "w", encoding="utf-8") as ans_file:
        for i, item in enumerate(capitalized_motifs):
            ans_file.write(f">test{i + 1}\n")
            ans_file.write(item + "\n")


# Run the main function
main()
