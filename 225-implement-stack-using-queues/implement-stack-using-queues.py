class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        

    def push(self, x: int) -> None:
        self.q2.append(x)
        
        while self.q1:
            self.q2.append(self.q1.popleft())   #move all elements from q1 to q2
        self.q1, self.q2 = self.q2, self.q1 #swap q1 and q2
        
    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]   #front element of q1, top of stack
        
    def empty(self) -> bool:
        return not self.q1       


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()