s1 = 20
s2 = 15
s3 = 17

print(s1)
print(s2)
print(s3)
print("------------------------")

s = [20, 15, 17, 18, 20, 19, 12, "alireza mohammadi", 19, 20, 12, 15]

try:
    for i in s:
        if i == int(i):
            print(i, end=" ")
except:
    print("false")
finally:
    print("done")

print("new app")