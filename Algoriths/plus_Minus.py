#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    array_len = len(arr)
    pos =0
    neg = 0
    zero = 0
    for elem in arr:
        if elem > 0:
            pos +=1
        if elem < 0:
            neg +=1
        if elem == 0:
            zero += 1
    pos = round(pos/array_len,6)
    neg = round(neg/array_len,6)
    zero = round(zero/array_len,6)
    print(pos)
    print(neg)
    print(zero)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
