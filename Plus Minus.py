#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    l=len(arr)
    p=0
    n=0
    o=0
    for i in arr:
        if (i>0):
            p+=1
        elif (i<0):
            n+=1
        else:
            o+=1
    print('{:.6}'.format(p/l))
    print('{:.6}'.format(n/l))
    print('{:.6}'.format(o/l))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
