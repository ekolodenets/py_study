'''
input: amount of bricks given to a child
output: maximum number of complete rows possible to build
1
3
6
10
'''

def bricks(n):
    b_level = levels = 0
    counter = 1
    while True:
        s = sum([_ for _ in range(1, counter + 1)])
        if b_level + s > n:
            return levels
        b_level += s
        levels += 1
        counter += 1


print(bricks(20))