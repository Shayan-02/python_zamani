lst = [1, 2, 3, "ali", 10, 4, 5]
lst.pop()
print(lst)
lst.pop(1) # 1 index را پاک میکند
print(lst)
lst.remove(10) # 10 را پاک میکند
print(lst)
lst.remove("ali") # ali را پاک میکند
print(lst)
lst.clear()
print(lst)
del lst
print(lst)