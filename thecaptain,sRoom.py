k = int(input())

numbers = list(map(int,input().split()))

freq = {}

for num in numbers:

    if num in freq:

        freq[num] += 1
    else:
        freq[num] = 1