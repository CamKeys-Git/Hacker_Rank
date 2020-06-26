#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
  total1 = arr[0][0]
  lst = []
  for x in arr:
    for num in x:
      lst.append(num)
  counter = 0    
  for i in range(len(arr)-1):
     counter += len(arr)+1
     total1 += lst[counter]

  total2 = 0
  counter2 = 0    
  for i in range(len(arr)):
     counter2 += len(arr)-1
     total2 += lst[counter2]

  return abs(total1 - total2)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
