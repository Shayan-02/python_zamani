fruits = ["apple", "banana", "cherry"]

cars = ["Ford", "BMW", "Volvo"]

for i in cars:
    fruits.append(i)

print(fruits)

fruits.extend(cars)
print(fruits)

lst2 = fruits.copy()
print(lst2)

