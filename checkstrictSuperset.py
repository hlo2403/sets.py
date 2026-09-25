a=set(input().split())
t=int(input())
is_strict=True
for _ in range(t):
    sets=set(input().split())
    if not(a>sets):
        is_strict=False
        break
                
print(is_strict)
         