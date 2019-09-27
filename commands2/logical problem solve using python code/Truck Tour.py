#!/bin/python3

import os
import sys

#
# Complete the truckTour function below.
#
def truckTour(petrolpumps,n):
    for i in range(n):
        index=i
        pa=petrolpumps[i][0]
        npd=petrolpumps[i][1]
        if pa>=npd:
            pa=pa-npd
            for j in range (i+1,n):
                pa=petrolpumps[j][0]+pa
                npd=petrolpumps[j][1]
                if pa>npd:
                    pa=pa-npd
                    continue
                else :
                    break
            if j==n-1 and i!=0:
                for k in range (0,i):
                    pa=petrolpumps[k][0]+pa
                    npd=petrolpumps[k][1]
                    if pa>=npd:
                        pa=pa-npd
                        continue
                    else:
                        break
                if k==i-1:
                    return index
            elif i==0 and j==n-1:
                return index
        else :
            continue

    return -1  
    #
    # Write your code here.
    #

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps,n)

    fptr.write(str(result) + '\n')

    fptr.close()