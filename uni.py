def uniq(ls):
    k=0
    for x in ls:
        if ls.count(x)>1:
            k=k+1
    if k==0:
        print("unique")
    else:
        print("not unique")
uniq([1,2,3,1])
uniq([1,2,3,4])
