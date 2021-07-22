# creating a stack class with the following operations
#check length, Push, Pop, Check if empty, get top

class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass

class ArrayStack:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def push(self, k):
        self.data.append(k)

    def top(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self.data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self.data.pop()


S = ArrayStack()
S.push(2)
S.push(4)
S.push(6)

print(S.is_empty())
print(S.pop())