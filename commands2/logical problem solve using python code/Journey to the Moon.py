#!/bin/python3

import math
import os
import random
import re
import sys
import queue
def addedge(adj,u,v):
    adj[u].append(v)
    adj[v].append(u)

def bfsutil(u,adj,visited):
    q = queue.Queue()
    visited[u] = True
    q.put(u)
    num=1
    while(not q.empty()):
        u = q.queue[0]
        q.get()
        i = 0
        while i != len(adj[u]): 
            if (not visited[adj[u][i]]): 
                    visited[adj[u][i]] = True
                    q.put(adj[u][i])
                    num=num+1 
            i += 1
    return num
def bfs(adj,m):
    visited=[False] * m
    test=[]
    for u in range (m):
        if visited[u]==False :
           num=bfsutil(u,adj,visited)
           test.append(num)
    return test
# Complete the journeyToMoon function below.
def journeyToMoon(m, astronaut,p):
    adj = [[] for i in range(m)]
    for j in range (p):
        addedge(adj,astronaut[j][0],astronaut[j][1])
    test=bfs(adj,m)
    term =1
    result=0
    for i in range(len(test)):
        if i==0:
            continue
        elif i==1:
            result=test[i]*test[0]
            term=test[i]+test[0]
        else:
            result +=term*test[i]
            term +=test[i]
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    np = input().split()

    n = int(np[0])

    p = int(np[1])

    astronaut = []

    for _ in range(p):
        astronaut.append(list(map(int, input().rstrip().split())))

    result = journeyToMoon(n, astronaut,p)

    fptr.write(str(result) + '\n')

    fptr.close()