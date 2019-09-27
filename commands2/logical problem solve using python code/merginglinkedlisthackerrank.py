#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):
    list3=SinglyLinkedList()
    list1start=head1
    list2start=head2
    if list1start ==None and list2start==None:
        return list3.head
    elif list1start ==None and list2start!=None:
        list3.head=list2start
        return list3.head
    elif list1start !=None and list2start==None:
        list3.head=list1start
        return list3.head
    else :
        while (list1start !=None and list2start!=None) :
            if list1start.data <= list2start.data :
                num = list1start.data
                list1start=list1start.next
                list3.insert_node(num)
            elif list1start.data > list2start.data :
                num = list2start.data
                list2start=list2start.next
                list3.insert_node(num)
        if list1start == None :
            while list2start !=None:
                num = list2start.data
                list2start=list2start.next
                list3.insert_node(num)
        elif list2start == None :
            while list1start !=None:
                num = list1start.data
                list1start=list1start.next
                list3.insert_node(num)
    return list3.head



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)
            
        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        llist3 = mergeLists(llist1.head, llist2.head)

        print_singly_linked_list(llist3, ' ', fptr)
        fptr.write('\n')

    fptr.close()
