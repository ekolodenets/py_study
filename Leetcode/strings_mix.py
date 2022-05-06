'''
Given two strings s1 and s2, we want to visualize how different the two strings are. We will only take into account
the lowercase letters (a to z). First let us count the frequency of each lowercase letters in s1 and s2.

s1 = "A aaaa bb c"
s2 = "& aaa bbb c d"
||
s1 has 4 'a', 2 'b', 1 'c'
s2 has 3 'a', 3 'b', 1 'c', 1 'd'

In the result, substrings (a substring is for example 2:nnnnn or 1:hhh; it contains the prefix) will be in decreasing
order of their length and when they have the same length sorted in ascending lexicographic order (letters and digits -
more precisely sorted by codepoint); the different groups will be separated by '/'. See examples and "Example Tests".

s1 = "my&friend&Paul has heavy hats! &"
s2 = "my friend John has many many friends &"
mix(s1, s2) --> "2:nnnnn/1:aaaa/1:hhh/2:mmm/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"

s1 = "mmmmm m nnnnn y&friend&Paul has heavy hats! &"
s2 = "my frie n d Joh n has ma n y ma n y frie n ds n&"
mix(s1, s2) --> "1:mmmmmm/=:nnnnnn/1:aaaa/1:hhh/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"

s1="Are the kids at home? aaaaa fffff"
s2="Yes they are here! aaaaa fffff"
mix(s1, s2) --> "=:aaaaaa/2:eeeee/=:fffff/1:tt/2:rr/=:hh"

'''

import re
from collections import Counter

def grouper(iter, n):
    values = set(map(lambda x: x[n], iter))
    newlist = [[[y[0], y[1], y[2]] for y in iter if y[n] == x] for x in values]
    return newlist


def mix(s1, s2):
    ss1 = [i for i in Counter(re.findall(r'[a-z]', s1)).items() if i[1] > 1]
    ss2 = [i for i in Counter(re.findall(r'[a-z]', s2)).items() if i[1] > 1]
    identical = []

    for i in ss1[:]:    # deleting identical amount of the letter
        if i in ss2:
            identical.append((i + (3,)))
            ss1.remove(i)
            ss2.remove(i)

    temp = []
    for i in grouper(([i+(1,) for i in ss1]+[i+(2,) for i in ss2])+identical, 0):  # pick the biggest amount of the letter
        if len(i) > 1:
            i = sorted(i, key=lambda x: x[1], reverse=True)[0]
            temp.append(i)
        else:
            i = i[0]
            temp.append(i)

    half = []
    result = ''

    for i in reversed(grouper(temp, 1)):
        if len(i[0]) == 1:
            half.append(i[0])
            result += f'{i[0][2]}:{i[0][0]*i[0][1]}/'
        else:
            i = sorted(i, key=lambda x: x[2])
            for j in grouper(i, 2):
                if len(j) == 1:
                    half.append(j[0])
                    result += f'{j[0][2]}:{j[0][0]*j[0][1]}/'
                else:
                    j = sorted(j, key=lambda x: x[0])
                    result += f'{"/".join([f"{i[2]}:{i[0]*i[1]}" for i in sorted(j, key=lambda x: x[0])])}/'
                    half.extend(j)

    return "/".join([f'{i[2] if i[2] != 3 else "="}:{i[0]*i[1]}' for i in half]) if half else result



# print(mix("Are they here", "yes, they are here"))
# print('2:eeeee/2:yy/=:hh/=:rr')

# print(mix("Sadus:cpms>orqn3zecwGvnznSgacs","MynwdKizfd$lvse+gnbaGydxyXzayp"))
# print('2:yyyy/1:ccc/1:nnn/1:sss/2:ddd/=:aa/=:zz')

# print(mix("looping is fun but dangerous", "less dangerous than coding"))
# print('1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg')

# print(mix(" In many languages", " there's a pair of functions"))
# print('1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt')



print(mix("Lords of the Fallen", "gamekult"))
print('1:ee/1:ll/1:oo')

# assert mix("Are they here", "yes, they are here"), "2:eeeee/2:yy/=:hh/=:rr"
# assert mix("Sadus:cpms>orqn3zecwGvnznSgacs","MynwdKizfd$lvse+gnbaGydxyXzayp"), '2:yyyy/1:ccc/1:nnn/1:sss/2:ddd/=:aa/=:zz'
# assert mix("looping is fun but dangerous", "less dangerous than coding"), "1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg"
# assert mix(" In many languages", " there's a pair of functions"), "1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt"
# assert mix("Lords of the Fallen", "gamekult"), "1:ee/1:ll/1:oo"
# assert mix("codewars", "codewars"), ""    AssertionError
# assert mix("A generation must confront the looming ", "codewarrs"), "1:nnnnn/1:ooooo/1:tttt/1:eee/1:gg/1:ii/1:mm/=:rr"