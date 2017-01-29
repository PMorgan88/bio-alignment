#!/usr/bin/env python3.5
from collections import defaultdict
import sys

def score(seqDict):
    """Loops through sequences comparing letters and assigning the appropriate score,
    ""and returns the total"""
    nrows = seqDict['seq1']
    ncols = seqDict['seq2']
    score = 0
    
    for i in range(len(ncols)):
        if nrows[i] == ncols[i]:
            score += 1
        else:
            score -= 1
            
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
    
print ("Your score is: ",score(list))

