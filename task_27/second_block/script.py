f = open("task_27\\second_block\\27-B_1.txt")
n = int(f.readline())

max_sum = 0
razn = []

for s in f:
    a, b = map(int, s.split())
    max_sum += max(a, b)
    d = abs(a - b)
    if d % 5 != 0:
        razn.append(d)

if max_sum % 5 != 0:
    print(max_sum)
else:
    print(max_sum - min(razn))
