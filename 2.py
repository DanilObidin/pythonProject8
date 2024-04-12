m = 0
k = 0
while True:
    n = int(input())
    if n == -1:
        break
    if n > m:
        m = n
        k += 1
print(k)