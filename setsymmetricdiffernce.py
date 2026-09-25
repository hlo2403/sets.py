e = int(input())
e_stud = set(map(int, input().split()))
f = int(input())
f_stud = set(map(int, input().split()))

eng_fren_only = e_stud.symmetric_difference(f_stud)

print(len(eng_fren_only))