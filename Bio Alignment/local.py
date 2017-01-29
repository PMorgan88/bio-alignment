#!/usr/bin/env python3.5
from collections import defaultdict
import sys

def scoreMatrix(seqDict):
    """Creates matrix and fills with smith-waterman algorithm using the transition/transversion matrix provided.
    Returns the max scoring value found in matrix"""
    nrows = seqDict['seq1']
    ncols = seqDict['seq2']
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


"""Sequences assigned from input to default dictionary"""
f = open("dotplot-example.fa",'r')
list = defaultdict(str)
name = ''
for line in f:
    if line.startswith('>'):
        name = line[1:-1]
        continue
    list[name]+=line.strip()

print("Your score is: ",scoreMatrix(list))

##"""Debugging"""
##labelCount = 1
##nrows = list['seq1']
##ncols = list['seq2']
##for i in ncols:
##    matrixFinal[labelCount].insert(0,i)
##    labelCount += 1
##matrixFinal[0].insert(0,' ')
##nrows = '  '+nrows
##matrixFinal.insert(0,['   '+i for i in nrows])
##print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
##      for row in matrixFinal]))
