fruits = ["apple", "banana", "cherry"]

cars = ["Ford", "BMW", "Volvo"]

for i in cars:
    fruits.append(i)

# fruits.append(cars)

print(fruits[3][1])

fruits.extend(cars)
print(fruits)

lst2 = fruits.copy()
print(lst2)

