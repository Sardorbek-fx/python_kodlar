n = int(input("Son kiriting: "))

for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0:
            print(0, end=" ")
        else:
            print(1, end=" ")
    print()
