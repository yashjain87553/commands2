#!/bin/python3

import os
import sys
import math

#
# Complete the movingTiles function below.
#
def movingTiles(l, s1, s2, queries):
    x = [None] * len(queries)
    for i in queries:
        d1=math.sqrt(i)
        d2=math.sqrt(l*l)
        d=d2-d1
        print(d)
        t=d/(s2-s1)
        t=round(t, 4)
        print(t)
        x.append(t)#!/bin/python3

import os
import sys
import math

#
# Complete the movingTiles function below.
#
def movingTiles(l, s1, s2, queries):
    x = [None] * len(queries)
    for i in queries:
        d1=math.sqrt(i)
        print(d1)
        d2=((l) * math.sqrt(2))
        print(d2)
        d=d2-d1
        t=d/(s2-s1)
        t=round(t, 4)
        print(t)
        x.append(t)
    return x
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lS1S2 = input().split()

    l = int(lS1S2[0])

    s1 = int(lS1S2[1])

    s2 = int(lS1S2[2])

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = movingTiles(l, s1, s2, queries)

    

    fptr.close()

    return x
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lS1S2 = input().split()

    l = int(lS1S2[0])

    s1 = int(lS1S2[1])

    s2 = int(lS1S2[2])

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = movingTiles(l, s1, s2, queries)

    

    fptr.close()
