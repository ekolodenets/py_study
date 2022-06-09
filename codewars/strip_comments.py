'''
Complete the solution so that it strips all text that follows any of a set of comment markers passed in.
Any whitespace at the end of the line should also be stripped out.

result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
'''

def strip_comments(strng, markers):
    lst = strng.split('\n')
    for i in range(len(lst)):
        for y in range(len(lst[i])):
            if lst[i][y] in markers:
                lst[i] = lst[i].split(lst[i][y])[0].rstrip()
                break
    return '\n'.join(lst)



assert strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!']), 'apples, pears\ngrapes\nbananas'
assert strip_comments('a #b\nc\nd $e f g', ['#', '$']), 'a\nc\nd'
assert strip_comments(' a #b\nc\nd $e f g', ['#', '$']), ' a\nc\nd'
