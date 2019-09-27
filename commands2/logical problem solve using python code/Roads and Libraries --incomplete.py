#!/bin/python3
import queue
import math
import os
import random
import re
import sys

def addedge(adj,u,v):
    adj[u].append(v)
def bfsutil(u,adj,visited):
    print(visited)
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
def bfs(adj,m,c_lib,c_road):
    cost=0;
    visited=[False] * m
    for u in range (m):
        if visited[u]==False :
           num=bfsutil(u,adj,visited)
           if num==1:
               cost+=c_road+c_lib
           else:
               cost+=c_road*(num-1)+c_lib
    return cost
# Complete the roadsAndLibraries function below.
def roadsAndLibraries(n, c_lib, c_road, cities,m):
    if c_lib<=c_road:
        return c_lib*(n)
    else:          
        adj = [[] for i in range(m)]
        for j in range (m):
            addedge(adj,cities[j][0]-1,cities[j][1]-1)
        cost=bfs(adj,m,c_lib,c_road)
        return cost


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nmC_libC_road = input().split()

        n = int(nmC_libC_road[0])

        m = int(nmC_libC_road[1])

        c_lib = int(nmC_libC_road[2])

        c_road = int(nmC_libC_road[3])

        cities = []

        for i in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities,m)
        if q_itr<q-1:
            fptr.write(str(result) + '\n')
        else :
            fptr.write(str(result))


    fptr.close()
