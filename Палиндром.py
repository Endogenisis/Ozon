n=int(input())
m=n
l = str(n)
d=l[::-1]
while n <= 10**13:
    if l != d:
        n+=1
        l = str(n)
        d=l[::-1]
    else: break
print(n-m)