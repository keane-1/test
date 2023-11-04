total = 1
num = int(input())
num += 1

# for i in range(num-1):
#     if i == 0:
#         total = num
#     total *= num-1-i

# print(total)

for i in range(1, num):
    total *= i
print(total)

# def add(a, b):
#     return (a + b)

# def mult(x):
#     return x * x

# def minus_ten(number):
#     return number - 10

# print(minus_ten(add(mult(2), 6)))