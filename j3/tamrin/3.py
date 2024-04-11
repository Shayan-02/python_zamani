c = 57

for i in range(5):
    num= int(input(f"enter a number{i+1}: "))
    if num>c:
        print("bigger")
    elif num<c:
        print("smaller")
    else:
        print("correct")
        for i in range (1, 6):
            print("good job")
            if i == 3:
                break
        break


print("done")