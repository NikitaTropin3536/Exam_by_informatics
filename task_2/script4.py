from functions import equivalence

print("w z y x")
for w in range(0, 2):
    for z in range(0, 2):
        for y in range(0, 2):
            for x in range(0, 2):
                f = (x and (not y)) or equivalence(y, z) or (not w)
                if f == 0:
                    print(f'{w} {z} {y} {x}')
