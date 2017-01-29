#!/usr/bin/env python3.5
from collections import defaultdict
import sys

def dotMatrix(seqDict):
    """Creates Matrix of blank spaces of length (n,m), being sequence 1 and 2,
    then looks for matches before assigning . to matrix."""
    nrows = seqDict['seq1']
    ncols = seqDict['seq2']
    labelCount = 0
    Matrix = [[' ' for x in nrows] for y in ncols]
    
    for i in range(len(ncols)):
        for j in range(len(nrows)):
            if nrows[j] == ncols[i]:
                Matrix[i][j] = '.'

    """Creates labels for axis"""
    for i in ncols:
        Matrix[labelCount].insert(0,i)
        labelCount += 1
    nrows = ' '+nrows
    Matrix.insert(0,nrows)

    return Matrix

"""Sequences assigned from input to default dictionary"""
f = open(sys.argv[1],'r')
list = defaultdict(str)
name = ''
for line in f:
    if line.startswith('>'):
        name = line[1:-1]
        continue
    list[name]+=line.strip()
    
print ('\n'.join([' '.join(row) for row in dotMatrix(list)]))

