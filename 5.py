n = int(input())
e = 0
for i in range(1, n):
    k = 0
    for j in range(1, i):
        if i % j == 0:
            k += j
    if k == i:
        e += 1
print(e)

