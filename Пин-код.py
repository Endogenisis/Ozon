n=str(input())
l=[]
l.append(int(n))
l.append(int(n[0]+n[2]+n[1]))
l.append(int(n[1]+n[0]+n[2]))
l.append(int(n[1]+n[2]+n[0]))
l.append(int(n[2]+n[0]+n[1]))
l.append(int(n[2]+n[1]+n[0]))
l.sort()
for x in l:
    print(x)