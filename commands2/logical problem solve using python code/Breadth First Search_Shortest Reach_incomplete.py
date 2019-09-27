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
# Complete the bfs function below.
def bfsutil(s,adj,visited,distance):
    q = queue.Queue()
    visited[s]=True
    q.put(s)
    while(not q.empty()):
        u=q.queue[0]
        q.get()
        i=0
        while i != len(adj[u]):
            if(not visited[adj[u][i]]):
                visited[adj[u][i]]=True
                q.put(adj[u][i])
                distance[adj[u][i]]+=1
            i+=1
    return distance



def bfsnew(adj,n,s):
    visited = [False] * n
    distance = [0] * n
    distance=bfsutil(s,adj,visited,distance)
    return distance
def bfs(n, m, edges, s):
    adj=[[] for i in range (n)]
    for j in range (m):
        addedge(adj,edges[j][0]-1,edges[j][1]-1)
    print(adj)
    distance=bfsnew(adj,n,(s-1))
    result=[]
    for i in range(len(distance)):
        if(i==(s-1)):
            continue
        elif distance[i]==0:
            result.append(-1)
        else :
            result.append(distance[i]*6)

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
