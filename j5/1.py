a = "Lorem ipsum dolor sit amet."
print(len(a))

lst = []
print(lst)
lst.append(a)

print(lst)

lst2 = list(a)
print(lst2)

lst3 = []
for i in a:
    lst3.append(i)
print(lst3)