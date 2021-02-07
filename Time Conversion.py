#!/bin/python3
import os
import sys

def timeConversion(s):
    ns=''
    if s[8:]=='AM'and s[:2]=='12':
        ns+=('00'+s[2:8])
    elif s[8:]=='PM' and s[:2]!='12':
        ns+=str(int(s[:2])+12)+(s[2:8])
    else:
        ns+=(s[:8])

    return (ns)

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
