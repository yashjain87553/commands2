#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumMoves function below.
def minimumMoves(n,grid, sX, fX , sY, fY, gX, gY,count,direction):
    flag=0
    if direction == 'n' :
        count=count + 1
        flag=1 
        
    count1=0
    count2=0
    if 1+fX < n-1 and grid[1+fX][fY] != 'X' :
        if flag==1:
            count1=minimumMoves(n,grid,sX,fX+1,sY, fY, gX, gY,count,'x')
        elif direction == 'x':
            count1=minimumMoves(n,grid,sX,fX+1,sY, fY, gX, gY,count,'x')
        else:
            count1=minimumMoves(n,grid,sX,fX+1,sY, fY, gX, gY,count+1,'x')
    elif grid[1+fX][fY] == 'X':
        count1= False
    elif (1+fX) == n-1 :
        count1= count+1

    
    if 1+fY < n-1 and grid[fX][fY+1] != 'X' :
        if flag==1 :
            count2=minimumMoves(n,grid,sX,fX,sY, fY+1, gX, gY,count,'y')
        elif direction == 'y':
            count2=minimumMoves(n,grid,sX,fX,sY, fY+1, gX, gY,count,'y')
        else:
            count2=minimumMoves(n,grid,sX,fX,sY, fY+1, gX, gY,count+1,'y')
    elif grid[fX][fY+1] == 'X' :
        count2 = False
    elif (1+fY) == n-1 :
        count2 = count+1
    if count1==False and count2==False:
           return False
    elif count1==False:
        return count2
    elif count2==False :
        return count1
    elif count1 < count2:
        return count1
    else:
        return count2
         

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    startXStartY = input().split()

    startX = int(startXStartY[0])

    startY = int(startXStartY[1])

    goalX = int(startXStartY[2])

    goalY = int(startXStartY[3])

    result = minimumMoves(n,grid, startX,startX, startY,startY, goalX, goalY,0,'n')

    fptr.write(str(result) + '\n')

    fptr.close()
