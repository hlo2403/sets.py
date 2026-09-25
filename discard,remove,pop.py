n = int(input())                # number of elements in the set
s = set(map(int, input().split()))  # read the set elements

c = int(input())                # number of commands
for _ in range(c):
    choice = input().split()    # read command
    cmd = choice[0]

    if cmd == "pop":
        if s:                   # avoid error if set is empty
            s.remove(min(s))
    elif cmd == "remove":
        x = int(choice[1])
        if x in s:              # avoid KeyError
            s.remove(x)
    elif cmd == "discard":
        x = int(choice[1])
        s.discard(x)

print(sum(s)) 