A = int(input("A ni kiriting: "))
B = int(input("B ni kiriting: "))

soni = 0
qolgan = A

while qolgan >= B:
    qolgan = qolgan - B
    soni += 1

print(f"A kesmada {soni} ta B bor")
print(f"Bo'sh qismi {qolgan}")
