# If 2 inputed coords the same color say 'Yes', otherwise say 'No'
l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

def chess(a, b):
    return 'Yes' if ((l.index(a[0]) + 1) % 2 == int(a[1]) % 2) == ((l.index(b[0]) + 1) % 2 == int(b[1]) % 2) else 'No'


assert chess("a1", "b2") == 'Yes'
assert chess("f5", "c3") == 'No'
assert chess("f4", "g7") == 'Yes'
assert chess("h3", "e3") == 'No'
