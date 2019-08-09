class node:
    def __init__(self,x):
        self.data=x
        self.addrs=0
ob1=node(19)
ob2=node(49)
ob3=node(18)
ob4=node(27)
ob5=node(24)

ob3.addrs=ob1
ob1.addrs=ob5
ob5.addrs=ob4
ob4.addrs=ob2
temp=ob3
while(temp):
    print(temp.data,"=>",end=' ')
    temp=temp.addrs