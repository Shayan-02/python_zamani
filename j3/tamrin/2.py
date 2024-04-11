f=int (input("enter your number: "))
b=int(input("enter your number: "))
c=int(input("enter your number: "))
if f >= 0 and b >= 0 and c >= 0 :
    if f == b and b == c:
        print("the numbers are equal", c)
    elif f >= b and f >= c :
        print("the biggest is: ",f)
    elif f >= c and c >= b:
        print("the biggest is: ",f)
    elif b >= f and f >= c:
        print("the biggest is: ",b)
    elif b >= c and c >= f:
        print("the biggest is: ",b)
    elif c >= b and b >= f:
        print("the biggest is: ",c)
    elif c >= f and f >= b:
        print("the biggest is: ",c)
else:
    print("wrong number...")