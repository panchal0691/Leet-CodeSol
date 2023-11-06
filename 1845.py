from sortedcontainers import SortedList
class SeatManager:

    def __init__(self, n: int):
        self.available = SortedList()
        self.N = n

        for i in range(1, n +1):
            self.available.add(i)

        

    def reserve(self) -> int:
        x = self.available[0]
        self.available.remove(x)
        return x
        

    def unreserve(self, seatNumber: int) -> None:
        self.available.add(seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
