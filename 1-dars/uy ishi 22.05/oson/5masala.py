yigindi = 0
son = int (input("son kiritng "))
for i in range(1, son):
    if son % i == 0:
        yigindi += i

if yigindi == son:
    print("Mukammal son")
else:
    print("Mukammal son emas")

