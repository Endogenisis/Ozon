n=int(input())
m=n
l = str(n)
d=l[::-1]
while n <= 10**13:
    if l != l[::-1]:
        n+=1
        l = str(n)
    else: break
print(n-m)