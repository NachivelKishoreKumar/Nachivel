try:
    a=5
    if a>6:
        b=a/a-7
        print("value of b:",b)
except(ZeroDivisionerror, Nameerror):
    print("\n error occured and handled")