#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict 

#
# Complete the 'kruskals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts WEIGHTED_INTEGER_GRAPH g as parameter.
#

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i]. The weight of the edge is <name>_weight[i].
#
#
class graph:
    def __init__(self,vertices):
        self.V=vertices
        self.graph=[]
    def addedge(self,u,v,w):
        self.graph.append([u,v,w])
    def find(self,parent,i):
        if parent[i]==i:
            return i
        return self.find(parent,parent[i])
    def union(self, parent, rank, x, y): 
        xroot = self.find(parent, x) 
        yroot = self.find(parent, y) 
  
        # Attach smaller rank tree under root of  
        # high rank tree (Union by Rank) 
        if rank[xroot] < rank[yroot]: 
            parent[xroot] = yroot 
        elif rank[xroot] > rank[yroot]: 
            parent[yroot] = xroot 
  
        # If ranks are same, then make one as root  
        # and increment its rank by one 
        else : 
            parent[yroot] = xroot 
            rank[xroot] += 1
    def kruskal(self):
        result=[]
        i=0
        e=0
        self.graph =  sorted(self.graph,key=lambda item: item[2])
        parent=[]
        rank=[]
        for k in range(self.V):
            parent.append(k)
            rank.append(0)
        while e < self.V -1 :
            u,v,w=self.graph[i]
            i+=1
            x=self.find(parent,u)
            y=self.find(parent,v)
            if x != y: 
                e = e + 1     
                result.append([u,v,w]) 
                self.union(parent, rank, x, y)
        return result
        
def kruskals(g_nodes, g_from, g_to, g_weight):
    g=graph(g_nodes)
    for i in range (len(g_from)):
        g.addedge(g_from[i]-1,g_to[i]-1,g_weight[i])
    result=g.kruskal()
    wight=0
    for u,v,w in result:
        wight+=w
    return wight


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g_nodes, g_edges = map(int, input().rstrip().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges

    for i in range(g_edges):
        g_from[i], g_to[i], g_weight[i] = map(int, input().rstrip().split())

    res = kruskals(g_nodes, g_from, g_to, g_weight)
    fptr.write(str(res))
    # Write your code here.

    fptr.close()
