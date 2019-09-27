# Enter your code here. Read input from STDIN. Print output to STDOUT
class stack_i:
    def __init__(self):
        self.stack=[]
    def add(self,data=None):
        self.stack.append(data)
    def remove(self):
        self.stack.pop()
    def max_l(self):
        max_ele=0
        for i in range (len(self.stack)):
            if max_ele < self.stack[i]:
                max_ele=self.stack[i]
        print(int(max_ele))    


stack=stack_i()
operation=int(input())
for i in range (operation):
    str_o=input()
    str_1=str_o.split()
    if int(str_1[0])==1:
        stack.add(float(str_1[1]))
    elif int(str_1[0])==2:
        stack.remove()
    else:
        stack.max_l()