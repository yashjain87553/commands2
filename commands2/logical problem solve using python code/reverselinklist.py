class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class linklist:
    def __init__(self):
        self.head=None
    def add(self,data=None):
        newnode=node(data)
        if self.head==None:
            self.head=newnode
            return
        else:
            start=self.head
            while start.next!=None:
                start=start.next
            start.next=newnode
    def display(self):
        if self.head==None:
            print("list in empty")
        else:
            start=self.head
            while start!=None:
                print(start.data)
                start=start.next
    def reverse(self):
        if self.head==None:
            return
        else:
            pn=None
            while self.head.next!=None:
                cn=self.head
                self.head=cn.next
                cn.next=pn
                pn=cn
            self.head.next=pn

list1=linklist()
print("enter the no of element in your linklist")
count=int(input())
for i in range (count):
    data=int(input())
    list1.add(data)
print("enter list is ")
list1.display()
list1.reverse()
print("after reverse list  ")
list1.display()