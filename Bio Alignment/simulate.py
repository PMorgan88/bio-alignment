#!/usr/bin/env python3.5
import random
import matplotlib.pyplot as plt
import numpy as np

def scoreMatrix(seq1,seq2):
    """Fills matrix using local sequence alignment algorithm smith-waterman, and returns
    the max score given to an alignment"""
    nrows = seq1
    ncols = seq2
    score = 0
    mValue = 0
    Matrix = [[0 for x in range(len(nrows)+1)] for y in range(len(ncols)+1)]

    i = 1
    while i < len(ncols)+1:
        Matrix[i][0] = 0
        i += 1
    i = 1
    while i < len(nrows)+1:
        Matrix[0][i] = 0
        i += 1
    for i in range(len(ncols)+1)[1:]:
        for j in range(len(nrows)+1)[1:]:
            if ncols[i-1] == nrows[j-1]:
                score = 4
            elif (ncols[i-1] == 'A' and nrows[j-1] == 'G') or (ncols[i-1] == 'G' and nrows[j-1] == 'A'):
                score = -1
            elif (ncols[i-1] == 'C' and nrows[j-1] == 'T') or (ncols[i-1] == 'T' and nrows[j-1] == 'C'):
                score = -1
            else:
                score = -5
            maxF = [Matrix[i-1][j-1] + score]
            maxF.append(Matrix[i][j-1] - 5)
            maxF.append(Matrix[i-1][j] - 5)
            maxF.append(0)
            maxF = max(maxF)
            Matrix[i][j] = maxF
            if maxF > mValue:
                mValue = maxF
    return mValue


"""Loop creating and assigning pairwise sequence scores from scoreMatrix"""
i = 0
seq1 = ''
seq2 = ''
scoreList = []
while i < 100000:
    seq1 = [random.choice('AGCT') for x in range(100)]
    seq2 = [random.choice('AGCT') for x in range(100)]
    i += 1
    scoreList.append(scoreMatrix(seq1,seq2))
scoreList = np.array(scoreList)

"""Plot creation"""
plt.hist(scoreList,50, range=[10,110], facecolor='gray', align='mid')
plt.title("Occurences of Local Alignment Scores from 100,000 Random Length 100 Pairwise DNA sequences") 
plt.ylabel('Number of Occurences')
plt.xlabel('Local Alignment Scores')
plt.show()
