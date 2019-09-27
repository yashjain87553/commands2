#!/bin/python3

import math
import os
import random
import re
import sys
def addedge(adj,u,v):
    adj[u].append(v)
    adj[v].append(u)
def dfsutil(adj,visited,sn,ans):
    num=0
    temp=0
    visited[sn]=True
    for i in range(len(adj[sn])):
        if(visited[adj[sn][i]]==False):
            temp=dfsutil(adj,visited,adj[sn][i],ans)
            if(temp%2):
                num+=temp
            else:
                ans[0]+=1
    return num+1

def dfs(adj,sn,n):
    visited=[False] * n
    ans=[0]
    dfsutil(adj,visited,sn,ans)
    return ans[0];

# Complete the evenForest function below.
def evenForest(t_nodes, t_edges, t_from, t_to):
    adj=[[] for i in range(t_nodes)]
    for j in range(t_edges):
        addedge(adj,t_from[j]-1,t_to[j]-1)
    ans=dfs(adj,0,t_nodes)
    return ans
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t_nodes, t_edges = map(int, input().rstrip().split())

    t_from = [0] * t_edges
    t_to = [0] * t_edges

    for i in range(t_edges):
        t_from[i], t_to[i] = map(int, input().rstrip().split())

    res = evenForest(t_nodes, t_edges, t_from, t_to)

    fptr.write(str(res) + '\n')

    fptr.close()
