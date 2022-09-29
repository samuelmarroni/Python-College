def contaLeds(n):
    leds = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    n = str(n)
    l = 0
    for d in str(n):
        l += leds[int(d)]
    return l

N = int(input())
for i in range(N):
    V = int(input())
    print(f"{contaLeds(V)} leds")
