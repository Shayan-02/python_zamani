firstName = input("enter your first name: ")
lastName = input("enter your last name: ")
math = int(input("math: "))
physics = int(input("physics: "))
chemistry = int(input("chemistry: "))
geography = int(input("geography: "))
avg = (math + physics + chemistry + geography) / 4

if math > 20 or math < 0 or physics > 20 or physics < 0 or chemistry > 20 or chemistry < 0 or geography > 20 or geography < 0:
    print("false number")
elif avg >= 16:
    print("average is {} grade A".format(firstName, lastName, avg))
elif avg >= 12 and avg < 16:
    print(f"{firstName} {lastName} average is {avg} grade B")
elif avg >= 10 and avg < 12:
    print(firstName, lastName, "average is", avg, "grade C".format(firstName, lastName, avg))
elif avg >= 0 and avg < 10:
    print("{} {} average is {} grade D ==> fail".format(firstName, lastName, avg))
elif avg not in range (0, 20):
    print("wrong")
# else:
#     print("wrong average")
