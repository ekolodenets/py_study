def parse_int(string):
    d = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,
         'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17,
         'eighteen': 18, 'nineteen': 19, 'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50, 'sixty': 60,
         'seventy': 70, 'eighty': 80, 'ninety': 90, 'hundred': 100, 'thousand': 1000, 'million': 1000000}
    s = []
    for i in string.split():
        if i in d:
            s.append(d[i])
        if '-' in i:
            i = i.split('-')
            s.append(d[i[0]] + d[i[1]])
    # print(s)
    for i, x in enumerate(s):
        if x == 100:
            del s[i]
            s[i-1] *= 100
        if x == 1000:
            del s[i]
            s[i-1] *= 1000
        if x == 1000000:
            del s[i]
            s[i-1] *= 1000000
    # print(s)
    if sum(s) > 1000:
        if s[0] < 1000:
            s[0] *= 1000
            if s[1] == 1000:
                del s[1]
                return sum(s)
            return sum(s)
    return sum(s)




print(parse_int("seven hundred thousand"), 700000)
print(parse_int("two hundred thousand three"), 200003)
print(parse_int("five hundred thousand three hundred"), 500300)


print(parse_int("six hundred sixty-six thousand six hundred sixty-six"), 666666)
print(parse_int("two hundred three thousand"), 203000)
print(parse_int("eight hundred eighty-eight thousand eight hundred and eighty-eight"), 888888)



print(parse_int("two hundred forty-six"))
print(parse_int("one hundred"), 100)
print(parse_int("one hundred sixty-nine"), 169)
print(parse_int("one hundred and one"), 101)
print(parse_int("one thousand three hundred and thirty-seven"), 1337)
print(parse_int("ten thousand"), 10000)
print(parse_int("twenty-six thousand three hundred and fifty-nine"), 26359)
print(parse_int("thirty-five thousand"), 35000)
print(parse_int("ninety-nine thousand nine hundred and ninety-nine"), 99999)
print(parse_int("six hundred sixty-six thousand six hundred sixty-six"), 666666)
print(parse_int("seven hundred five thousand"), 705000)
print(parse_int("one million"), 1000000)


# assert parse_int("one") == 1
# assert parse_int("twenty") == 20
# assert parse_int("two hundred forty-six") == 246