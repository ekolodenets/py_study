'''

    1
   232
  34543
 4567654
567898765


'''

max_n = 5
start = 1
space = max_n - 1

for i in range(1, max_n*2+1, 2):
    print(
        ' ' * space + ''.join([str(j) for j in range(start, i) if start != 1])
        + str(i)
        + ''.join(reversed([str(j) for j in range(start, i) if start != 1]))
            )
    space -= 1
    start += 1
