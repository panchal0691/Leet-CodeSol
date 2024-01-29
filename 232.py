class MyQueue:

    def __init__(self):
        self.first =[]
        self.second =[]

    def push(self, x: int) -> None:
        while self.first:
            self.second.append(self.first.pop())
        self.first.append(x)
        while self.second:
            self.first.append(self.second.pop())
    def pop(self) -> int:
        return self.first.pop()

    def peek(self) -> int:
        return self.first[-1]    
    
    def empty(self) -> bool:
        if len(self.first)==0:
            return True
        return False
