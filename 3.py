w = []
s = 0
while True:
    n = int(input())
    w.append(n)
    if n == 0:
        break
    s += n
    ave = s/len(w)
print(ave)