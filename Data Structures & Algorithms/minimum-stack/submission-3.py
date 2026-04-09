class MinStack:
    def __init__(self):
        self.stack = list()
        self.pos = -1

    def push(self, val: int) -> None:
        self.pos = self.pos + 1
        self.stack.insert(self.pos,val)

    def pop(self) -> None:
        self.pos = self.pos - 1
        
    def top(self) -> int:
        return self.stack[self.pos]

    def getMin(self) -> int:
        return min(self.stack[0:self.pos+1])
