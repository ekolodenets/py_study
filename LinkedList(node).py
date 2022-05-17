class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def __str__(self):
        return f'{self.data = } -> {str(self.next)}'

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next = b
b.prev = a
b.next = c
c.prev = b
c.next = d
d.prev = c
d.next = e
e.prev = d

print(a)


'''
2 variant
'''

class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

    def __str__(self):
        n = self
        res = ''
        while (n):

            res += str(n.data) + ' -> '
            n = n.next
        return res

    def append(self, val):
        end = Node(val)
        n = self
        while (n.next):
            n = n.next
        n.next = end

ll = Node(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
print(ll)