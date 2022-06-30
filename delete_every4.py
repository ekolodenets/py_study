'''
delete every 4 in list
[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] ->
[1,2,3,5,6,7,9,10,11,13,14,15,17,18,19]
'''

import time




def del_every_four(lst):
    idx = 3
    for i in range(len(lst)//4):
        del lst[idx]
        idx += 3
    return lst

def del_every_four_(b):
    del b[3::4]
    return b

x = list(range(1, 100000))
y = list(range(1, 100000))

# start = time.perf_counter()
# del_every_four(x)
# print(time.perf_counter() - start)

start = time.perf_counter()
del_every_four_(y)
print(time.perf_counter() - start)
