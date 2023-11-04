a = 0
b = 1

num = int(input())
for i in range(num):
    if i == 0:
        print("0", end = " ")
    elif i == 1:
        print("1", end = " ")
    elif i >= 2:
        print(a+b, end = " ")
        c = a
        a = b
        b = c + b