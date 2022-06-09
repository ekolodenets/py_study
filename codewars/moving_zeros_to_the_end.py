def move_zeros(arr):
    zeros = []
    [(arr.remove(i), zeros.append(i)) for i in arr[:] if i == 0]
    return arr + zeros

print(move_zeros([1, 0, 1, 2, 0, 1, 3]))
# returns [1, 1, 2, 1, 3, 0, 0])
print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))
# returns [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
