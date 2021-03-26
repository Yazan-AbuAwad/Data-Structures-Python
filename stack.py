# stack data structure based on python list

class stack:
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def view(self):
        return self.items

    def is_empty(self):
        return self.items == []


s= stack()
s.push(5)
s.push(6)

print(s.view())

s.pop()

print(s.view())