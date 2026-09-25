m = int(input())                # size of set A
a = set(map(int, input().split()))

n = int(input())                # size of set B
b = set(map(int, input().split()))

# Symmetric difference
result = sorted(a.symmetric_difference(b))

# Print each element on a new line
for num in result:
    print(num)
