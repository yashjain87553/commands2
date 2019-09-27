class node:
    def __init__(self,data=None):
        self.data=data
        self.left=None
        self.right=None
    
    def insertnode(self,data=None):
        if self.data!=None:
            if self.data > data:
                if self.left==None:
                    self.left=node(data)
                else :
                    self.left.insertnode(data)
            else :
                if self.right==None:
                    self.right=node(data)
                else :
                    self.right.insertnode(data)
        else :
            self.data=data

    def printtree(self):
        if self.left!=None:
            self.left.printtree()
        print(self.data)
        if self.right!=None:
            self.right.printtree()

    def deletenode(self,deldata=None):
        if self.data==None:
            printf("Invalid Data")
            return
        if deldata < self.data:
            self.left=self.left.deletenode(deldata)
        elif deldata > self.data:
            self.right=self.right.deletenode(deldata)
        else:
            if self.left is None:
                temp=self.right
                self=None
                return temp
            elif self.right is None:
                temp=self.left
                self=None
                return temp
            currentnode=self
            while(currentnode.left is not None):
                currentnode=currentnode.left
            self.data=currentnode.data
            self.right=deletenode(self.right,currentnode.data)
        return self

root=node()
print("enter no of element in tree")
n=int(input())
for i in range (n):
    print("enter data")
    x=int(input())
    root.insertnode(x)
print("tree for is ")
root.printtree()
print("enter data to delete node , enter 0 to exit")
dn=int(input())
root.deletenode(dn)
print("tree after delete ")
root.printtree()


