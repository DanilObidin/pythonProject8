n = int(input())
for a in range(2, n+1):
    f = 1
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            f = 0
    if f and a > 1:
        print(a)
