import array as arr
total=0
a=arr.array('i',[95,97,91,93,99])
for i in range (0,len(a)):
    total=total+a[i]
    
average=total/len(a)
print(total)
print(average)
    