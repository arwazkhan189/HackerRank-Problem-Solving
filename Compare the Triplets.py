#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    res=[]
    a1=0
    b1=0
    for i in range (3):
        if (a[i]>b[i]):
            a1+=1
        elif (a[i]==b[i]):
            pass
        else:
            b1+=1
    res.append(a1)
    res.append(b1)
    return (res)
            


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
