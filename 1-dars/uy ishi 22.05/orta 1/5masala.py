N = int(input("N soninini kiritng "))  
M = int(input("M soninini kiritng "))  
K = int(input("K soninini kiritng "))  
Fibonachchi = []
a = 0
b = 1

for i in range(0, M):
    Fibonachchi.append(a)
    a, b = b, a + b


Javob = Fibonachchi[N:M][:K]
print("Natija:", Javob)