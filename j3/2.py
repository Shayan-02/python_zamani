math = int(input("math: "))
physics = int(input("physics: "))
chemistry = int(input("chemistry: "))
arabi = int(input("arabi: "))
avg = (math + physics + chemistry + arabi) / 4

if (
    math < 20
    and math > 0
    and physics < 20
    and physics > 0
    and chemistry > 20
    and chemistry > 0
    and arabi < 20
    and arabi > 0
):
    if avg >= 16:
        print("average is {} grade A".format(avg))
    if avg >= 12 and avg < 16:
        print("average is {} grade B".format(avg))
    if avg >= 10 and avg < 12:
        print("average is {} grade C".format(avg))
    if avg >= 0 and avg < 10:
        print("average is {} grade D ==> fail".format(avg))
    if avg not in range(0, 20):
        print("wrong")

