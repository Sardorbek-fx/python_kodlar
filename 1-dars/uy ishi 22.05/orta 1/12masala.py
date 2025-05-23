son = input("Butun sonni kiriting: ")

bor = False 

for i in range(len(son) - 1):
    if son[i] == son[i+1]:
        bor = True
        break

if bor:
    print("Bor.")
else:
    print("Yo'q.")
