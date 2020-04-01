def pro(n):
    if(n==3):
        return 2
    max_pro = 0
    if(n%3==0):
        max_pro=pow(3,int(n/3))
        return max_pro
    if(n%3==1):
        max_pro=4*pow(3,int(n/3)-1)
        return max_pro
    if(n%3==2):
        max_pro=6*pow(3,int(n/3)-1)
        return max_pro
n=int(input())
a=pro(n)
print(a)
