import itertools,string
def possible_ways(toss):
    a = itertools.product('HT', repeat = toss)
    k=list(a)
    Output = [''.join(temp) for temp in k]
    l=len(Output)
#print(Output)    #possible outcome
    if toss>2:
        for i in range(0,l):
            if 'TTT' in Output[i]:
                 l-=1
        print(l)

n=int(input("Enter the number toss: "))
possible_ways(n)
