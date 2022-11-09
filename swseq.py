import sys
import operator
import pandas as pd
import matplotlib.pyplot as plt
from numpy import unravel_index
import numpy as np

def smith_waterman(sequence_a, sequence_b, match, mismatch, gap):
    matrix = []

    N = len(sequence_a) + 1
    M = len(sequence_b) + 1

    # STEP 1: CONSTRUCTING AND FILLING THE GRID
    # initialization with zeros
    matrix = [[0] * N for _ in range(M)]

    # initialize first row and coloumn
    for i in range(M):
        matrix[i][0] = 0
    for i in range(N):
        matrix[0][i] = 0

    # initialize the tree dictionary, which will keep the paths from nodes
    tree = {}
    for i in range(1, M):
        tree.setdefault((i, 0), [(i - 1, 0)])
    for i in range(1, N):
        tree.setdefault((0, i), [(0, i - 1)])

    # fill the numbers of each element
    for i in range(1, M):
        for j in range(1, N):

            diagonal = 0
            if sequence_a[j - 1] == sequence_b[i - 1]:
                diagonal += match
            else:
                diagonal += mismatch

            diagonal += matrix[i - 1][j - 1]

            # Getting values of neighbours
            left = matrix[i][j - 1] + gap
            up = matrix[i - 1][j] + gap
            matrix[i][j] = max(diagonal, up, left) if max(diagonal, up, left) > 0 else 0

            # Getting indices of neighbours
            left_id = (i, j - 1)
            up_id = (i - 1, j)
            diagonal_id = (i - 1, j - 1)
            indices = [diagonal_id, up_id, left_id]

            # Getting maximum indices
            max_indices = []
            values = [diagonal, up, left]
            for k in range(len(values)):
                if matrix[i][j] == values[k]:
                    max_indices.append(indices[k])

            tree.setdefault((i, j), max_indices)

    # Step 2: GET THE POSSIBLE ALIGNMENTS, AND TRACE BACK TO THE FIRST ELEMENT.

    # queue variable represent a path that can be taken from bottom right to top left cell
    # queues variable represent all optimal paths
    # tree is traversed in depth-first recursive manner
    def traverse(tree, node, queue, queues):
        if matrix[node[0]][node[1]] == 0:
            queues.append(list(queue))
            queue.clear()
            return
        for nodes in tree[node]:
            old_queue = list(queue)
            queue.append(nodes)
            traverse(tree, nodes, queue, queues)
            queue = old_queue
    x = np.array(matrix)
    y = unravel_index(x.argmax(), x.shape)
    queues = []
    traverse(tree, (y[0], y[1]), [], queues)
    for queue in queues:
        queue.insert(0, (y[0], y[1]))

    # STEP 3: FROM ARROWS TO STRING (DETERMINE GAP POSITIONS)
    optimal = []

    for queue in queues:
        seq_a = []
        seq_b = []
        ind_a = y[1]
        ind_b = y[0]
        for index in range(len(queue)):
            if index == len(queue) - 1:
                optimal.append([seq_a, seq_b])
                break
            move = tuple(map(operator.sub, queue[index], queue[index + 1]))
            if move == (1, 1):
                seq_a.insert(0, sequence_a[ind_a - 1])
                seq_b.insert(0, sequence_b[ind_b - 1])
                ind_a -= 1
                ind_b -= 1
            if move == (0, 1):
                seq_a.insert(0, sequence_a[ind_a - 1])
                seq_b.insert(0, "-")
                ind_a -= 1
            if move == (1, 0):
                seq_a.insert(0, "-")
                seq_b.insert(0, sequence_b[ind_b - 1])
                ind_b -= 1

    original_stdout = sys.stdout  # Save a reference to the original standard output

    # print alignments
    with open('filename.txt', 'w') as f:
        sys.stdout = f  # Change the standard output to the file we created.
        print("There are " + str(len(optimal)) + " Optimal Alignments:")
        for item in optimal:
            print(' '.join(item[0]))
            print(' '.join(item[1]))
            print("-----------------------------------")
        sys.stdout = original_stdout  # Reset the standard output to its original value

    


# MAIN
# parameters
match = 2
mismatch = 0
gap = -1
sequence_a = "GACCCGTTATGCTCGAGTTCGGTCAGTGCGTCATTGCAAGTAGTCGATTGCTTTCTCAATCTCCGAGCGATTTAGCGTGACAGCCCCAGGGAACCCATAA"
sequence_b = "GTTTAATTTTGTATGGCAAGGTACTCCCGATCTTAATGAATGGCCGGAAGTGGTACGGACGCAATAT"

smith_waterman(sequence_a, sequence_b, match, mismatch, gap)