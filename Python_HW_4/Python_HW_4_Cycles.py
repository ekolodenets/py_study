#   1
count = 0
range_count = 10
for_count = 0
run = True

#   2
while run:
    print('Hello Cycle')

#   3
while run:
    print('Step =', count)
    count += 1


#   4
while count < range_count:
    print('Step =', count)
    count += 1

#   5
while count < range_count:
    print('Step =', count)
    count += 1
    if count == 3:
        print('Step =', count, 'If body')

#   6
while run:
    print('Step =', count)
    count += 1
    if count == range_count:
        print('STOP', count)
        break

#   7
for item in range(for_count, range_count):
    print('Step =', item)


#   8
for item in range(30):
    print('Step =', item)
    if item == 5:
        print('Item =', item)
    if item == 10:
        print('Item =', item)
    if item < 4:
        print('Item <', item)
    if item > 27:
        print('Item >=', item)

#   9
for item in range(range_count+1):
    print('Step =', item)
    if item == 7:
        inner_count = 0
        print('-- inner_count =', inner_count)
        for inner_item in range(item):
            print('-------- Inner_Step =', inner_item)
            if inner_item == 5:
                inner_count = inner_item
        print('-- inner_count =', inner_count)

#   10
for item in range(20):
    print('Step =', item)
    if 7 < item < 12:
        print('If_item =', item)
        continue
print('End_iteration =', item)
