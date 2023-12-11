f = open("task_27\\first_block\\27-B_demo.txt")
n = int(f.readline())

max_sum = 0
razn = []

for s in f:
    a, b = map(int, s.split())
    max_sum += min(a, b)
    d = abs(a - b)
    if d % 3 != 0:
        razn.append(d)

if max_sum % 3 != 0:
    print(max_sum)
else:
    print(max_sum - max(razn))
