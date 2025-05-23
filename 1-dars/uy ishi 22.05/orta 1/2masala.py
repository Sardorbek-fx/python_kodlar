N = int(input("N ni kiriting: "))
M = int(input("M ni kiriting: "))
K = int(input("K ni kiriting: "))

juft_sonlar = []

for son in range(N, M + 1):
    if son % 2 == 0:
        juft_sonlar.append(son)

juft_sonlar = juft_sonlar[:K]

yigindi = sum(juft_sonlar)

print("Juft sonlar:", juft_sonlar)
print("Yig'indi:", yigindi)
