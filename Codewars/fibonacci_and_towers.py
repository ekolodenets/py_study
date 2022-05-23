# fibonachi
n = 5
#
F = [1] * (n + 1)
for i in range(2, n + 1):
    F[i] = F[i - 2] + F[i - 1]
print(F[n])

# fibonachi2
# def fib(n):
#     a = 0
#     b = 1
#     for _ in range(n):
#         a, b = b, a + b
#     return a
# print(fib(4))

# factorial
# n = 1
# s = 1
# for i in range(1, n):
#     s += s * i
#
# print(s)

# Ханойские башни
# def move(n, start, finish):
#     if n > 0:
#         temp = 6 - start - finish # Вспомогательный колышек
#         move(n - 1, start, temp)
#         print("Перенести диск", n, "со стержня", start, "на стержень", finish)
#         move(n - 1, temp, finish)
#
# move(3, 1, 3)