class MinStack:

    def __init__(self):
        self.stack=[]
        self.mstack=[]
        self.minval=float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.mstack:
            self.mstack.append(val)
        else:
            currentmin=self.mstack[-1]
            self.mstack.append(min(currentmin,val))



    def pop(self) -> None: 
        self.stack.pop()
        self.mstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        
        return self.mstack[-1]
        
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()