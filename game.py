import random
t = {2: 38, 7: 14, 8: 31, 15: 26, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 78: 98, 87: 94,
     16: 6, 49: 11, 62: 19, 46: 25, 74: 53, 64: 60, 89: 68, 95: 75, 99: 80, 92: 88}

print(t.keys())
l = [1, 2, 3, 4, 5, 6, 7]
# for i in l:
#     if i in x:
#         print(f'{i} -> {x[i]}')
x = random.randint(1, 6)
if x not in t:
    print(x)
else:
    print(f'{x} -> {t[x]}')
