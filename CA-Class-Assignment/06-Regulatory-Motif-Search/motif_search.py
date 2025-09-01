# --------------------------------------------------
# File Name : motif_search.py
# Problem   : Assignment 06 - Regulatory Motif Search
# Authors   : 1. Worralop Srichainont
#           : 2. Suvijak Jintanaphan
#           : 3. Thara Waranuset
# Date      : 2025-08-28
# --------------------------------------------------

import os
import random

# Directory Configurations
PROBLEM_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_FILE = os.path.join(PROBLEM_DIR, "src", "dna_sequences.txt")
ANS_FILE = os.path.join(PROBLEM_DIR, "src", "answer.txt")

# Motif Length Configuration
NUCLEOTIDES = ("a", "c", "g", "t")
MOTIF_LENGTH = 10


# Get all substring motifs from a single DNA sequence
def get_all_motifs_from_dna(dna_sequence):
    motifs = []
    for i in range(len(dna_sequence) - MOTIF_LENGTH + 1):
        motifs.append(dna_sequence[i : i + MOTIF_LENGTH])
    return motifs


# Get random motifs from all DNA sequence
def get_random_motifs_from_all_dna(dna_sequences):
    random_motifs = []
    for dna in dna_sequences:
        random_motifs.append(random.choice(get_all_motifs_from_dna(dna)))
    return random_motifs


# Calculate profile matrix of selected motifs
def get_profile_matrix(motifs):
    # Initialize profile matrix with pseudo-count
    profile = {
        "a": [1.0] * MOTIF_LENGTH,
        "c": [1.0] * MOTIF_LENGTH,
        "g": [1.0] * MOTIF_LENGTH,
        "t": [1.0] * MOTIF_LENGTH,
    }

    # Count nucleotide occurrences in each position
    for motif in motifs:
        for i, nucleotide in enumerate(motif):
            profile[nucleotide][i] += 1

    # Calculate profile probabilities
    for nucleotide, frequencies in profile.items():
        for i in range(MOTIF_LENGTH):
            frequencies[i] /= len(motifs) + 4

    # Return the profile matrix
    return profile


# Calculate score of selected motifs
def get_score(motifs):
    # Initialize count matrix of each nucleotide
    nucleotide_count = {
        "a": [0] * MOTIF_LENGTH,
        "c": [0] * MOTIF_LENGTH,
        "g": [0] * MOTIF_LENGTH,
        "t": [0] * MOTIF_LENGTH,
    }

    # Count nucleotide occurrences in each position
    for motif in motifs:
        for i, nucleotide in enumerate(motif):
            nucleotide_count[nucleotide][i] += 1

    # Calculate score which is the sum of all unpopular nucleotides count
    score = 0
    for i in range(MOTIF_LENGTH):
        total_count = sum(nucleotide_count[nucleotide][i] for nucleotide in NUCLEOTIDES)
        max_count = max(nucleotide_count[nucleotide][i] for nucleotide in NUCLEOTIDES)
        score += total_count - max_count

    # Return a score
    return score


# Get motif probability of a single motif
def get_motif_probability_from_profile(motif, profile):
    # Initialize probability
    probability = 1.0

    # Multiply profile probabilities of current motif and position
    for i, nucleotide in enumerate(motif):
        probability *= profile[nucleotide][i]

    # Return a probability of a motif
    return probability


# Get the best motif in a list of motifs
def get_best_motif_from_profile(motifs, profile):
    best_motif = None
    best_score = 0.0

    for motif in motifs:
        score = get_motif_probability_from_profile(motif, profile)
        if score > best_score:
            best_score = score
            best_motif = motif

    return best_motif


# Get all best motif from all DNA sequences
def get_all_best_motifs_from_all_dna(dna_sequences, profile):
    best_motifs = []

    for dna_sequence in dna_sequences:
        motifs = get_all_motifs_from_dna(dna_sequence)
        best_motif = get_best_motif_from_profile(motifs, profile)
        best_motifs.append(best_motif)

    return best_motifs


def get_randomized_motif_search(dna_sequences):
    # Randomly select a k-mer from each DNA sequence
    best_motifs = get_random_motifs_from_all_dna(dna_sequences)

    # Iterate until convergence
    while True:
        # Get the profile matrix of the current motifs
        profile = get_profile_matrix(best_motifs)

        # Get the best motifs from all DNA sequences according to the profile
        current_best_motifs = get_all_best_motifs_from_all_dna(dna_sequences, profile)

        # Compare score of motifs. If the current motifs are better, update the best motifs
        if get_score(current_best_motifs) < get_score(best_motifs):
            best_motifs = current_best_motifs
        else:
            break

    # Return the best motifs
    return best_motifs


# Main function
def main():
    # Input all DNA sequence into a list
    dna_sequences = []
    with open(SRC_FILE) as file:
        for line in file:
            if line.startswith(">"):
                continue
            dna_sequences.append(line.strip())

    # Get the best motifs from the DNA sequences by using randomized motif search
    best_motifs = get_randomized_motif_search(dna_sequences)
    capitalized_motifs = [seq.upper() for seq in best_motifs]

    # Output best motifs to a file
    with open(ANS_FILE, "w", encoding="utf-8") as ans_file:
        for i, item in enumerate(capitalized_motifs):
            ans_file.write(f">test{i + 1}\n")
            ans_file.write(item + "\n")


# Run the main function
main()
