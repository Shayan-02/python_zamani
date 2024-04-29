import random

# internal function
a = "hello world"
print(len(a))

# external function
# 1
print(random.randint(1, 10))

# 2
lst = [324, 34234, 34324]
print(type(lst))

# 3 self:
def sums(a, b):
    return a + b
print(sums(1, 2))