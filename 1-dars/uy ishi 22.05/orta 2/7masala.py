n = int(input("Son kiriting: "))

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print() 
