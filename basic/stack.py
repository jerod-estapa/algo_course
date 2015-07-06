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


def revstring(mystr):
    s = Stack()
    char = [c for line in s for c in line if c is not " "]



if __name__ == '__main__':
    revstring(raw_input('?'))
