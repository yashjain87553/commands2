#!/bin/python3

import os
import sys
import pprint

#
# Complete the maximumDraws function below.
#
#def maximumDraws(n):
    #return (n+1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    query_no = int(input())

    for itr_1 in range(query_no):
        str_1 = input()
        str_1 = str_1.split()
        x=int(str_1[0])
        y=int(str_1[1])
        matrix = [[ [0 for col in range(x)] for col in range(x)] for row in range(x)]
        for query_1 in range(y):
            query_type = input()
            query_type = query_type.split()
            if query_type[0] == 'UPDATE':
                a = int(query_type[1])
                b = int(query_type[2])
                c = int(query_type[3])
                matrix[a-1][b-1][c-1]=int(query_type[4])
            else:
                x1 = int(query_type[1])
                y1 = int(query_type[2])
                z1 = int(query_type[3])
                x2 = int(query_type[4])
                y2 = int(query_type[5])
                z2 = int(query_type[6])
                sum=0;
                for v_1 in range(x1-1,x2):
                    for v_2 in range(y1-1,y2):
                        for v_3 in range(z1-1,z2):                              
                            sum += matrix[v_1][v_2][v_3]
                result=sum;
                fptr.write(str(result) + '\n')

    fptr.close()
