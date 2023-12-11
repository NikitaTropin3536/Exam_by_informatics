f = open('task_27\\third_block\\27-B_2.txt')
n = int(f.readline())
data = [int(k) for k in f]

max_number = 0

for i in range(0, n):
    for j in range(i + 1, n):
        d = data[i] * data[j]
        if d > max_number and d % 14 == 0:
            max_number = d
print(max_number)
