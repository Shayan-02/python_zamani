lst = [1, 2, 3, 4 , 5]
lst2 = [8, 9, 10]
lst.append(6)
lst.append(7)
# lst.append(lst2)
for i in lst2:
    lst.append(i)

print(lst)

if len(lst) == 7:
    print("7")
elif len(lst) == 6:
    print("6")
else:
    print("else")
