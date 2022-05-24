x, y = input(f'Input 2 numbers: ').split()

xn = int(x)
matrix = []
while xn != 0:
    temp = []
    y = int(y)
    inp = input(f'Input {y} times * or .')
    for i in inp[:y]:
        temp.append(i)
    matrix.append(temp)
    xn -= 1

bombs_coord = []
for i in matrix:
    inx_x = matrix.index(i)
    for y in range(len(i)):
        if i[y] == '.':
            i[y] = 0
        else:
            bombs_coord.append([inx_x, y])

def seek(*args):
    temp = []
    xt = [-1, 0, 1]
    yt = [-1, 0, 1]
    for i in args:
        for x in xt:
            for y in yt:
                if i != [i[0] + x, i[1] + y] and [i[0] + x, i[1] + y] not in bombs_coord and i[0] + x >= 0 and i[1] + y >= 0:
                    temp.append([i[0] + x, i[1] + y])
    return temp


def bombs_around(list):
    l = []
    for _ in list:
        l.extend(seek(_))
    l.sort()
    return l

def make_dic(a):
    d = {}
    for i in a:
        if str(i) in d:
            d[str(i)] += 1
        else:
            d[str(i)] = 1
    return d

what = make_dic(bombs_around(bombs_coord))

for i in matrix:
    inx_x = matrix.index(i)
    for y in range(len(i)):
        if str([inx_x, y]) in what:
            i[y] = str(what[str([inx_x, y])])
        else:
            if i[y] != '*':
                i[y] = '0'

for i in matrix:
    print(''.join(i))