str1=str(input("enter the string"))
str2=''
ls=list(str1)
print(ls)
if ls[0]=='i'and ls[1]=='s':
    print(str1)
else:
    ls.insert(0,'i')
    ls.insert(1,'s')
    for x in ls:
        str2+=x
    print(str2)
