n=int(input())
m=n
l = list(map(int, str(n)))
d=l[::-1]
while n <= 10**13:
    if l != d:
        n+=1
        l = list(map(int, str(n)))
        d=l[::-1]
    else: break
print(n-m)