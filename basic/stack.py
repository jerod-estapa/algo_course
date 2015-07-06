#!usr/local/bin/python3

# Implementing the Stack

# Stack Class

class Stack:


    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(items) - 1]

    def size(self):
        return len(self.items)

# Reverse-string function

def revstring(mystr):
    s = Stack()
    for ch in mystr:
        s.push(ch)
    revstr = ''
    while not s.is_empty():
        revstr += s.pop()

    return revstr


print(revstring('Hume'))
print(revstring('Spinoza'))
print(revstring('Camus'))
print(revstring('Russell'))
