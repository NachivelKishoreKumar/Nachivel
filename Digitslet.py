str1=input("Enter string:")
Digits=0
Letters=0
for i in str1:
      if(i.isdigit()):
            Digits=Digits+1
      Letters=Letters+1
print("The number of digits is:")
print(Digits)
print("The number of Letters is:")
print(Letters)
