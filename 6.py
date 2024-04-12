n = int(input())
b = "*"
for i in range(1, n+1):
    c = " "*(n-i)
    print(c+b)
    b += "*"