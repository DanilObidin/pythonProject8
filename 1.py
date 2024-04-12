m = 0
while True:
    n = int(input())
    if n == -1:
        break
    if n > m:
        m = n
print(m)
