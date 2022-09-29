from random import randint

L = []
for i in range(20):
    L.append(randint(1,50))
print(L)

d = max(L)
c = min(L)
media = sum(L) / len(L)

print(d, c, media)