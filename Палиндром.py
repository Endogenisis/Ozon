n=int(input())
l = list(map(int, str(n)))
d=l[::-1]
m=0
while n <= 10**13:
    if len(l) <= 1:
        n+=1
        m+=1
        l = list(map(int, str(n)))
        d=l[::-1]
    elif l != d:
        n+=1
        m+=1
        l = list(map(int, str(n)))
        d=l[::-1]
    else: break
print(m)