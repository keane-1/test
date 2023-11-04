table_size = int(input())

for i in range(1, table_size*table_size+1):
    if i % table_size == 0:
        print(i)
    else:
        print(i, end = " ")