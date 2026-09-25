set1=int(input())
arr1=set(map(int,input().split()))
set2=int(input())
arr2=set(map(int,input().split()))

result = set()

for i in arr1: 
    if i in arr2:
        result.add(i)

print(len(result))