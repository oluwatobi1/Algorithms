#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'doesCircleExist' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY commands as parameter.
#

def doesCircleExist(commands):
    # Write your code here
    out =[]
    store = {"G":0, "L":0, "R":0}
    for each in commands:
        if 'G' in each:
            for letter in each:
                store[letter]+=1
            
            V = (store["R"]-store["L"])
            if V%2!=0:
                out.append('YES')
            else:
                out.append("NO")
            store = {"G":0, "L":0, "R":0}
        else:
            out.append('YES')
    return out

    

if __name__ == '__main__':



    