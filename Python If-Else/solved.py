"""
    Task:
        A single line containing a postive integer, n
    Constraints:
        1 <= n <= 100
    Output Format:
        PrintWeird if the number is weird; otherwise, print Not Weird
    
    Sample Input:
        3
    Sample Output:
        Weird
    Explanation 0:
        n = 3
        n is odd and odd numbers are weird, so we print Weird.
    Sample Input 1:
        24
    Sample Output 1:
        Not Weird
    Explanation 1:
        n = 24
        n > 20 and n is even, so it isn't weird. Thus, we print Not Weird.
"""

import math
import os
import random
import re
import sys


def solution(input):
    if input % 2 == 1 or (input > 5 and input < 21):
        return "Weird"
    else:
        return "Not Weird"

if __name__ == '__main__':
    n = int(input().strip())
    print(solution(n))
