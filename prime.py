j=0
n=int(input())
for i in range(1,n):
    if(n%i==0):
        j=j+1
if (j==2):
    print("prime")
else:
    print("not prime")
