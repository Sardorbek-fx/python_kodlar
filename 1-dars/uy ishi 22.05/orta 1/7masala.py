A = int(input("A ni kiriting: "))
B = int(input("B ni kiriting: "))

for son in range(A, B + 1):
    if son % 2 == 0:
        print(-son)
    else:
        print(son)
