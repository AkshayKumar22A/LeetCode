class MinStack:

    def __init__(self):
        self.m = deque()
        self.stack = deque()

    def push(self, val: int) -> None:
        if len(self.m) == 0 or val <= self.m[-1]:
            self.m.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        if len(self.stack) == 0:
            return
        if self.stack[-1] == self.m[-1]:
            self.m.pop()
        return self.stack.pop()

    def top(self) -> int:
        if len(self.stack) == 0:
            return
        return self.stack[-1]

    def getMin(self) -> int:
        return self.m[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()