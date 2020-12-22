
    #!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'countGroups' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY related as parameter.
#

from collections import deque
def countGroups(related):
    # Write your code here
    M = [list(map(int,list(x))) for x in related]
    print(M)
    answer = 0
    seen = [0] * len(M)
    queue = deque()
    for i in range(len(M)):
        if seen[i] == 0:
            queue.append(i)
            while queue:
                search = queue.pop()
                seen[search] = 1
                for j in range(len(M)):
                    if(M[search][j] == 1 and seen[j] == 0):
                        queue.append(j)
            answer+=1
    return answer
