#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'performOperations' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. 2D_INTEGER_ARRAY operations
#

def performOperations(arr, operations):
    # Write your code here
    import copy

    new_arr = []
    for operation in operations:
        index_start = operation[0]
        index_end = operation[1] + 1


        if index_end == (len(arr) - 1)  and index_start == 0:
            new_arr = list(reversed(arr[index_start:index_end]))
        else:
            new_arr = arr[0:index_start] + list(reversed(arr[index_start:index_end])) + arr[index_end:]

        arr = copy.deepcopy(new_arr)

    return new_arr


if __name__ == '__main__':
    arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    operations = [(0, 9), (4,5), (3,6), (2,7), (1,8), (0,9)]
    result = performOperations(arr, operations)
    print(result)