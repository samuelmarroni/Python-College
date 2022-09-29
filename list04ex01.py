from random import randint

L = []
for i in range(10):
    L.append(randint(1, 50))
x = randint(1, 10)

print(f"Lista: {L}\n O número {x} aparece {L.count(x)}")
