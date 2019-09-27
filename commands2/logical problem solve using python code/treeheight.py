class Node:

    def __init__(self,data=None):
        self.data=data
        self.left=None
        self.right=None

    def insert(self,data=None):
        if self.data!=None:
            if self.data > data:
                if self.left==None:
                    self.left=Node(data)
                else :
                    self.left.insert(data)
            else :
                if self.right==None:
                    self.right=Node(data)
                else :
                    self.right.insert(data)  
        else :
            self.data=data

    def printtree(self):
        if self.left!=None:
            self.left.printtree()
        print(self.data)
        if self.right!=None:
            self.right.printtree()

    def treeheight(self,height=None):
        if self.left!=None:
            leftheight=self.left.treeheight(height+1)
        else :
            leftheight=height;
        if self.right!=None:
            rightheight=self.right.treeheight(height+1)
        else :
            rightheight=height;
        if leftheight > rightheight:
            return leftheight
        else :
            return rightheight
        



print("Enter number of element in your tree")
n=int(input())
root=Node()
for i in range (n):
    print("enter data")
    x=int(input())
    root.insert(x)
print("formed tree is")
root.printtree()
print("Height of tree is")
height=root.treeheight(0)
print(height)