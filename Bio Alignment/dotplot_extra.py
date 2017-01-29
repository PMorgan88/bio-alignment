#!/usr/bin/env python3.5
from collections import defaultdict
import sys

def dotMatrix(seqDict,k):
    """Creates Matrix of blank spaces of length (n,m), being sequence 1 and 2,
    then looks for runs of matches of a length k or greater before assigning . to matrix."""
    nrows = seqDict['seq1']
    ncols = seqDict['seq2']
    labelCount = 0
    alignCount = 0
    c = 0
    score = 0
    Matrix = [[' ' for x in nrows] for y in ncols]
    
    for i in range(len(ncols)):
        for j in range(len(nrows)):
            while nrows[j-c] == ncols[i-c]:
                score += 1
                c += 1
                if score >= k:
                    Matrix[i][j] = '.'
            c = 0
            score = 0
            

    """Creates labels for axis"""
    for i in ncols:
        Matrix[labelCount].insert(0,i)
        labelCount += 1
    nrows = ' '+nrows
    Matrix.insert(0,nrows)

    return Matrix

"""Sequences assigned from input to default dictionary"""
f = open(sys.argv[1],'r')
k = eval(sys.argv[2])
list = defaultdict(str)
name = ''
for line in f:
    if line.startswith('>'):
        name = line[1:-1]
        continue
    list[name]+=line.strip()
    
print('\n'.join([' '.join(row) for row in dotMatrix(list,k)]))

