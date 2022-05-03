# numbers not float
# only - or +

x = "10 + 25 - 12 + 20- 1 + 3 -3"
j = x.replace('+', ' ').replace('-', ' ').split()
k = x
for i in j:
    k = k.replace(i, ' ')
k = k.split()
n = [int(i) for i in j]
p = n[0]
for i in range(len(k)):
    if k[i] == '+':
        p += n[i + 1]
    elif k[i] == '-':
        p -= n[i + 1]
print(p)