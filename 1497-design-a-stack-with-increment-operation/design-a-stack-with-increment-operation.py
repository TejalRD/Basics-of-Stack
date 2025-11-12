class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []
        self.inc = [0] * maxSize        

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)
        
    def pop(self) -> int:
        if not self.stack:
            return -1
        i = len(self.stack) -1
        x = self.stack.pop() + self.inc[i]        
        if i>0:
            self.inc[i-1] += self.inc[i]
        self.inc[i] =0
        return x

    def increment(self, k: int, val: int) -> None:
        if not self.stack:
            return
        i = min(k, len(self.stack)) -1
        self.inc[i] +=val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)