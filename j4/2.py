a = "Lorem ipsum dolor sit amet."

i = 0 # از 0 شروع میشود
while True:
    if i == 100:
        break
    if i == 10:
        i = i + 5
        continue
    else:
        print(i)
        i = i + 1 # i را اضافه میکند

print("**********************************")
for ali in range(0, 100):
        if ali == 100:
            break
        if ali == 10:
            print("ali")
            continue
        else:
            print(ali)# i را اضافه میکند

j = 0
while j < 100:
    print(j)
    j += 1