b = 2.7
f = 25
print(f + b)
print(b, f)
c = input("enter your name: ")
d = input("enter your lastname: ")
a = int(input("enter your age: "))

fullname = c + " " + d
print(c, d)
print(fullname)

print("your full name is:", c, d, "and your age is:", a)
print(f"your full name is: {c} {d} and your age is: {a}")
print("your full name is: {} {} and your age is: {}".format(c, d, a))

print(f"{a} + {b} = {a + b}")
print(f"{23 + 2.7 = :}")
print(a , "+", b, "=", a + b)