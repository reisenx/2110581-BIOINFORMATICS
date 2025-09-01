# --------------------------------------------------
# File Name : BA3G.py
# Problem   : Find an Eulerian Path in a Graph
# Author    : Worralop Srichainont
# Date      : 2025-08-20
# --------------------------------------------------

import os

# Directory Configurations
PROBLEM_DIR = os.path.dirname(os.path.abspath(__file__))
TESTCASE = os.path.join(PROBLEM_DIR, "src", "testcase.txt")
SRC_FILE = os.path.join(PROBLEM_DIR, "src", "rosalind_ba3g.txt")
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

# Initialize adjacency list, start node, and end node
adjacency_list = {}
start_node = ""
end_node = ""
path = []

# Read adjacency list from the file
with open(SOURCES[selection]) as file:
    for line in file:
        # Extract node and its adjacent nodes
        node, raw_adjacent = line.strip().split(" -> ")
        adjacent = raw_adjacent.strip().split(",")

        # Initialize nodes in adjacency list
        if node not in adjacency_list:
            adjacency_list[node] = {"in": [], "out": []}

        # Update node's out-degree
        adjacency_list[node]["out"] = adjacent

        for adj_node in adjacent:
            # Initialize nodes in adjacency list
            if adj_node not in adjacency_list:
                adjacency_list[adj_node] = {"in": [], "out": []}

            # Update node's in-degree
            adjacency_list[adj_node]["in"].append(node)

# Determine the start and end node
for node, degrees in adjacency_list.items():
    if len(degrees["out"]) - len(degrees["in"]) == 1:
        start_node = node
    elif len(degrees["in"]) - len(degrees["out"]) == 1:
        end_node = node

# Using Hierholzer's Algorithm to find the Eulerian Path
stack = [start_node]
while stack:
    # Get the current node
    current_node = stack[-1]

    # If the current node has outgoing edges
    if adjacency_list[current_node]["out"]:
        # Add one of the adjacent nodes to the stack, and remove it from the adjacency list
        stack.append(adjacency_list[current_node]["out"].pop())

    # If the current node has no outgoing edges
    else:
        # Add the current node to the path, and remove it from the stack
        path.append(stack.pop())

# Reverse the path to get the correct order
path.reverse()

# Output the Eulerian Path
with open(ANS_FILE, "w", encoding="utf-8") as ans_file:
    ans_file.write("->".join(path))
