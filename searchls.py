def check(ls,search):
    for x in ls:
        if x==search:
            print('True')
            break
    else:
        print('false')
check([1,5,8,3],3)
check([1,5,8,3],-1)
            
