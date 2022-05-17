from numpy import *

a = array([['Mon', 18, 20, 22, 17], ['Tue', 11, 18, 21, 18],
           ['Wed', 15, 21, 20, 19], ['Thu', 11, 20, 22, 21],
           ['Fri', 18, 17, 23, 22], ['Sat', 12, 22, 20, 18],
           ['Sun', 13, 15, 19, 16]])

# Split output 7 rows and 5 columns
m = reshape(a, (7, 5))
# print(m)

#  Adding a new row
m_r = append(m, [['Avg', 12, 15, 13, 11]], 0)
# print(m_r)

# Adding a new column
m_c = insert(m, [5], [[1], [2], [3], [4], [5], [6], [7]], 1)
# print(m_c)

# Deleting a row
m = delete(m, [2], 0)
# print(m)

# Deleting a column
dc = delete(m, [2], 1)
# print(dc)

m[3] = ['Thu', 0, 0, 0, 0]
print(m)
