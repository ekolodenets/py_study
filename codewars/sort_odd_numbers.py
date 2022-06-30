'''
sort only odd numbers
'''

def sort_array(source_array):
    even = ()
    odd = []
    for i, v in enumerate(source_array):
        if v % 2 == 0:
            even += (i, v),
        else:
            odd.append(v)
    odd.sort()
    for i in range(len(even)):
        odd.insert(even[i][0], even[i][1])
    return odd


assert sort_array([5, 3, 2, 8, 1, 4]), [1, 3, 2, 8, 5, 4]
assert sort_array([5, 3, 1, 8, 0]), [1, 3, 5, 8, 0]
