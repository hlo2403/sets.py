num_a = int(input())
set_a = set(map(int, input().split()))
n = int(input())
commands = []
sets = []
for i in range(n):
    command = input().split()[0]
    commands.append(command)
    set1 = set(map(int, input().split()))
    sets.append(set1)
    #set_a.command(set1)
 
for ind, command in enumerate(commands):
    if command == 'intersection_update':
        set_a.intersection_update(sets[ind])
    elif command == 'update':
        set_a.update(sets[ind])
    elif command == 'symmetric_difference_update':
        set_a.symmetric_difference_update(sets[ind])
    elif command == 'difference_update':
        set_a.difference_update(sets[ind])
        
print(sum(set_a))