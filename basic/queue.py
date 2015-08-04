#!/usr/local/bin/python3

# Implementing the Queue

# Queue Class


class Queue:


    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        return self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


p = Queue()

p.enqueue("Hi")
p.enqueue("there")
print(p.dequeue())
print(p.dequeue())