seta=int(input())
value1=set(map(int,input().split()))
setb=int(input())
value2=set(map(int,input().split()))
l=set()
for i in value1:
    l.add(i)
    for j in value2:
        l.add(j)
print(len(l))
