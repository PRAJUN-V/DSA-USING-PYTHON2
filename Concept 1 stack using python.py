"""
In python stack can be implemented using two methods
1. using list
2. using packages

push and pop are the most are the important operations on stack
append method is used for push operation
pop method is used for pop operation

boolean form of an empty list is False
that is
a = []
print(bool(a)) -> False


"""
class stack:
    def __init__(self):
        self.stack = []

    def stackAppend(self, data):
        self.stack.append(data)

    def stackPop(self):
        if not self.stack:
            print('stack is empty')

        else:
            poppedElement = self.stack.pop()
            return poppedElement
    def printStack(self):
        print(self.stack)


