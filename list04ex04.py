from random import randint

L = []
for i in range(20):
    L.append(randint(1, 50))
print(L)

num = int(input("Digite um valor: "))
d = L.count(num)
while d != 0:
    if num in L:
        L.remove(num)
    d -= 1
print(L)
