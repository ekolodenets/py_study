def fact(n):
    start = 1
    for i in range(1, n + 1):
        start *= i
        yield start

for i in fact(5):
    print(i, end=' ')