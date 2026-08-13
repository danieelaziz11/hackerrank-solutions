
import math
import os
import random
import re
import sys

#
# Complete the 'maxPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY skillLevel
#  2. INTEGER minDiff
#
def maxPairs(skillLevel, minDiff):
    skillLevel.sort()

    count = 0
    i = 0
    j = (len(skillLevel) + 1) // 2

    while i < len(skillLevel) // 2 and j < len(skillLevel):
        if skillLevel[j] - skillLevel[i] >= minDiff:
            count += 1
            i += 1
            j += 1
        else:
            j += 1

    return count
    
if __name__ == '__main__':

    skillLevel_count = int(input().strip())

    skillLevel = []

    for _ in range(skillLevel_count):
        skillLevel_item = int(input().strip())
        skillLevel.append(skillLevel_item)

    minDiff = int(input().strip())

    result = maxPairs(skillLevel, minDiff)
    
    print (result)
