'''
nPascal
nPascal(0) # should be []
nPascal(5) # should be [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

'''

def nPascal(n):
    x = [[1], [1, 1]]
    if n == 0:
        return []
    elif n == 1:
        return [1]
    else:
        for i in range(2, n):
            x.append([1] + [x[i - 1][j] + x[i - 1][j + 1] for j in range(i-1)] + [1])
        return x





# print(nPascal(0))
print(nPascal(1))
print(nPascal(2))
print(nPascal(3))
# print(nPascal(4))
# print(nPascal(5))
# print(nPascal(10))
# assert nPascal(3) == [[1], [1, 1], [1, 2, 1]]
# assert nPascal(4) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
# assert nPascal(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
# assert nPascal(6) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
# assert nPascal(7) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1]]
# assert nPascal(8) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1], [1, 7, 21, 35, 35, 21, 7, 1]]
