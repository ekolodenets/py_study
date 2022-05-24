'''
Next bigger number with the same digits
Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging its digits. For example:
12 ==> 21
513 ==> 531
2017 ==> 2071

If the digits can't be rearranged to form a bigger number, return -1

9 ==> -1
111 ==> -1
531 ==> -1



'''



import itertools

def next_bigger(n):
    if len(set(str(n))) <= 1:
        return -1
    elif len(str(n)) > 5:
        n_list = tuple(str(n))
        t = len(n_list)-1
        timer = 0
        for i in reversed(n_list):
            if int(i) >= timer:
                timer = int(i)
                t -= 1
            else:
                break
        if t == -1:
            return -1
        first, second, s_int = n_list[:t], n_list[t:], int(''.join(n_list[t:]))
        print(first, second, s_int)
        x = list(map(int, (''.join(i) for i in list(itertools.permutations(second)))))
        temp = tuple()
        for i in set(x):
            if i > s_int:
                temp += (i, )
        x = str(sorted(temp)[0])
        return int(''.join(first) + x)
    else:
        x = list(map(int, (''.join(i) for i in list(itertools.permutations(str(n))))))
        if max(x) <= n:
            return -1
        temp = []
        for i in set(x):
            if i > n:
                temp += (i, )
        x = sorted(temp)[0]
        return x


# def next_bigger(n):
#     s = list(str(n))
#     for i in range(len(s)-2,-1,-1):
#         if s[i] < s[i+1]:
#             t = s[i:]                               # t is the smallest list that should be increased
#             m = min(filter(lambda x: x>t[0], t))    # m is the smallest number that is bigger than t[0]
#             t.remove(m)                             # remove m from t
#             t.sort()                                # sort t
#             s[i:] = [m] + t                         # replace old slice with the next bigger one
#             return int("".join(s))
#     return -1


# print(next_bigger(9876543210))
# print(next_bigger(9876543210))
# print(next_bigger(59884848459853))
print(next_bigger(848459853))
# print(next_bigger(51716565413093))
# assert next_bigger(59884848459853), 59884848483559
# assert next_bigger(51716565413093), 51716565413309
# assert next_bigger(12), 21
# assert next_bigger(513), 531
# assert next_bigger(2017), 2071
# assert next_bigger(414), 441
# assert next_bigger(144), 414
# assert next_bigger(1234567890), 1234567908
# assert next_bigger(9876543210), -1

