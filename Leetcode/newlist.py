class Newlist(list):
    def __getitem__(self, key):
        if key == 0:
            raise IndexError
        elif key < 0:
            return super().__getitem__(key)
        return super().__getitem__(key - 1)


sl = [i for i in range(10)]
print(sl)
print(sl[1])

new = Newlist(sl)
print(new)
print(new[1])