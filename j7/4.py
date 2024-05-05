i = 1

while i <= 10:
    if i == 5:
        i = 7
        continue
    if i == 9:
        print("game over")
        break
    print(i)
    i = i + 1