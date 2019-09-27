class Node_ex:
	def __init__(self,data=None):
		self.data = data
		self.nextnode = None
class linklist_ex:
	
	def __init__(self):
		self.head = None
		
	def addnode(self,data=None):
		node=Node_ex(data)
		if self.head==None:
			self.head=node
		else :
			start=self.head
			temp=start
			while temp.nextnode!=None:
				temp=temp.nextnode
			temp.nextnode=node

	def printlist(self) :   
		head=self.head
		if head==None:
			print("List is empty")
		else :
			currentnode=head
			while True:
				if currentnode.nextnode==None:
					print(currentnode.data)
					break
				else:
					print(currentnode.data)
					currentnode = currentnode.nextnode
	def merge_list(self,list1=None,list2=None):
		list1start=list1.head
		list2start=list2.head
		if list1start ==None and list2start==None:
			return
		elif list1start ==None and list2start!=None:
			self.head=list2start
		elif list1start !=None and list2start==None:
			self.head=list1start
		else :
			while (list1start !=None and list2start!=None) :
				if list1start.data <= list2start.data :
					num = list1start.data
					list1start=list1start.nextnode
					self.addnode(num)
				elif list1start.data > list2start.data :
					num = list2start.data
					list2start=list2start.nextnode
					self.addnode(num)
			if list1start == None :
				while list2start !=None:
					num = list2start.data
					list2start=list2start.nextnode
					self.addnode(num)
			elif list2start == None :
				while list1start !=None:
					num = list1start.data
					list1start=list1start.nextnode
					self.addnode(num)
			else :
				return




i=0
print("enter number of element in your first list")
num1=int(input())
list1 = linklist_ex()
while i<num1:
	print("enter data ")
	num = int(input())
	list1.addnode(num)
	i=i+1
print("enter number of element in your second list")
num2=int(input())
list2 = linklist_ex()
i=0
while i<num2:
	print("enter data ")
	num = int(input())
	list2.addnode(num)
	i=i+1
print("list 1")
list1.printlist()
print("list 2")
list2.printlist()
merge_list=linklist_ex()
merge_list.merge_list(list1,list2)
print("result")
merge_list.printlist()




