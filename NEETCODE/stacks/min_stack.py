class MinStack:
    def __init__(self):
        self.stack = []
        self.stack_min = []
    
    def push(self, val:int) -> None:
        self.stack.append(val)
        val = min(val, self.stack_min[-1] if self.stack_min else val)
        self.stack_min.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.stack_min.pop()
    
    def top(self) -> int:
        return self.stack[-1]
    
    def get_min(self) -> int:
        return self.stack[-1] # return minimum element in constant time 


if __name__ == "__main__":
    obj = MinStack()
    # obj.push(val)
    # obj.pop()
    # param_3 = obj.top()
    # param_4 = obj.getMin()