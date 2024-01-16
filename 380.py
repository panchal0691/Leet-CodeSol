class RandomizedSet:

    def __init__(self):
        self.vec = []
        self.mp = {}

        

    def insert(self, val: int) -> bool:
        if val in self.mp:
            return False

        self.vec.append(val)
        self.mp[val] = len(self.vec) - 1
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.mp:
            return False

        idx = self.mp[val]
        temp = self.vec[-1]
        self.vec[-1] = val
        self.vec[idx] = temp
        self.mp[temp] = idx
        self.vec.pop()
        del self.mp[val]
        return True
        

    def getRandom(self) -> int:
        idx = random.randint(0, len(self.vec) - 1)
        return self.vec[idx]
