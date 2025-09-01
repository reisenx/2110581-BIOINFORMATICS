# --------------------------------------------------
# File Name : BA2D.py
# Problem   : Implement GreedyMotifSearch
# Author    : Worralop Srichainont
# Date      : 2025-08-27
# --------------------------------------------------

import os

# Directory Configurations
PROBLEM_DIR = os.path.dirname(os.path.abspath(__file__))
TESTCASE = os.path.join(PROBLEM_DIR, "src", "testcase.txt")
SRC_FILE = os.path.join(PROBLEM_DIR, "src", "rosalind_ba2d.txt")
ANS_FILE = os.path.join(PROBLEM_DIR, "src", "answer.txt")

SOURCES = (TESTCASE, SRC_FILE)

# Nucleotide Configuration
NUCLEOTIDES = ("A", "C", "G", "T")


# Get all substring motifs from a single DNA sequence
def get_all_motifs_from_dna(dna_sequence, motif_length):
    motifs = []
    for i in range(len(dna_sequence) - motif_length + 1):
        motifs.append(dna_sequence[i : i + motif_length])
    return motifs


# Calculate profile matrix of selected motifs
def get_profile_matrix(motifs, motif_length):
    # Initialize profile matrix
    profile = {
        "A": [0.0] * motif_length,
        "C": [0.0] * motif_length,
        "G": [0.0] * motif_length,
        "T": [0.0] * motif_length,
    }

    # Count nucleotide occurrences in each position
    for motif in motifs:
        for i, nucleotide in enumerate(motif):
            profile[nucleotide][i] += 1

    # Calculate profile probabilities
    for nucleotide, frequencies in profile.items():
        for i in range(motif_length):
            frequencies[i] /= len(motifs)

    # Return the profile matrix
    return profile


# Calculate score of selected motifs
def get_score(motifs, motif_length):
    # Initialize count matrix of each nucleotide
    nucleotide_count = {
        "A": [0] * motif_length,
        "C": [0] * motif_length,
        "G": [0] * motif_length,
        "T": [0] * motif_length,
    }

    # Count nucleotide occurrences in each position
    for motif in motifs:
        for i, nucleotide in enumerate(motif):
            nucleotide_count[nucleotide][i] += 1

    # Calculate score which is the sum of all unpopular nucleotides count
    score = 0
    for i in range(motif_length):
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
    best_score = -1.0

    for motif in motifs:
        score = get_motif_probability_from_profile(motif, profile)
        if score > best_score:
            best_score = score
            best_motif = motif

    return best_motif


def greedy_motif_search(dna_sequences, motif_length):
    # Initialize best motifs and score
    best_motifs = []
    best_score = float("inf")

    # Iterate over all starting motifs
    starting_motifs = get_all_motifs_from_dna(dna_sequences[0], motif_length)
    for starting_motif in starting_motifs:
        # Initialize current motifs by the current starting motif
        current_motifs = [starting_motif]

        # Build remaining motifs using the profile matrix of the current starting motif
        for i in range(1, len(dna_sequences)):
            profile = get_profile_matrix(current_motifs, motif_length)
            motifs = get_all_motifs_from_dna(dna_sequences[i], motif_length)
            best_motif = get_best_motif_from_profile(motifs, profile)
            current_motifs.append(best_motif)

        # Calculate the score for the current set of motifs and update the best motifs if needed
        current_score = get_score(current_motifs, motif_length)
        if current_score < best_score:
            best_score = current_score
            best_motifs = current_motifs

    # Return the best motifs found
    return best_motifs


# Main function
def main():
    # Prompt user to select source file
    print("========================================")
    print("Current Problem:", os.path.basename(__file__))
    print("========== SELECT SOURCE FILE ==========")
    print("0 for test file")
    print("1 for actual source file")
    selection = int(input("Enter your choice (0 or 1): ").strip())
    print("========================================")

    # Input nucleotide patterns
    with open(SOURCES[selection]) as file:
        motif_length = int(file.readline().strip().split()[0])
        dna_sequences = [line.strip() for line in file]

    # Get the best motifs using greedy search
    best_motifs = greedy_motif_search(dna_sequences, motif_length)

    # Output the adjacency list
    output_str = "\n".join(best_motifs)
    with open(ANS_FILE, "w", encoding="utf-8") as ans_file:
        ans_file.write(output_str)


# Run the main function
main()
