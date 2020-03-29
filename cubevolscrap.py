T=int(input())
N=[]
for i in range(T):
    N.append(int(input()))
for j in range(len(N)):
    if(N[i])==1:
        print("1")
    if(N[i]>=2):
        print((N[i]**3)-(N[i]-2)**3)
