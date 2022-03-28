n=int(input())
m=0
l = list(map(int, str(n)))
d=l[::-1]
while len(l) <= 1:
    n+=1
    m+=1
    l = list(map(int, str(n)))
    d=l[::-1]
while n <= 10**13:
    if l != d:
        n+=1
        m+=1
        l = list(map(int, str(n)))
        d=l[::-1]
    else: break
print(m)