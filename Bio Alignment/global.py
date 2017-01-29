#!/usr/bin/env python3.5
from collections import defaultdict
import sys

def scoreMatrix(seqDict):
    """Matrix created and filled with needleman algorithm, before returning
    Matrix(n,m) score"""
    nrows = seqDict['seq1']
    ncols = seqDict['seq2']
    score = 0
    Matrix = [[0 for x in range(len(nrows)+1)] for y in range(len(ncols)+1)]

    i = 1
    while i < len(ncols)+1:
        Matrix[i][0] = Matrix[i-1][0] - 1
        i += 1
    i = 1
    while i < len(nrows)+1:
        Matrix[0][i] = Matrix[0][i-1] - 1
        i += 1

    for i in range(len(ncols)+1)[1:]:
        for j in range(len(nrows)+1)[1:]:
            if ncols[i-1] == nrows[j-1]:
                score = 1
            else:
                score = -1
            maxF = [Matrix[i-1][j-1] + score]
            maxF.append(Matrix[i][j-1] - 1)
            maxF.append(Matrix[i-1][j] - 1)
            Matrix[i][j] = max(maxF)
            
    score = Matrix[len(ncols)][len(nrows)]
    return score

"""Sequences assigned from input to default dictionary"""
f = open(sys.argv[1],'r')
list = defaultdict(str)
name = ''
for line in f:
    if line.startswith('>'):
        name = line[1:-1]
        continue
    list[name]+=line.strip()

print('Your score is: ',scoreMatrix(list))
