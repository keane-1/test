stars = 1

bintang = int(input())

for i in range(1, bintang+1):
    space = bintang-1
    print(space*" " + stars*"*")
    bintang -=1
    stars += 1