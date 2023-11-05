class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        N = len(arr)
        k = min(N -1 , k)
        current = arr[0]
        streak = 0

        for i in range(1,2 *N):
            x = arr[i %N]
            if current > x:
                streak +=1
            else:
                current = x
                streak =1
            if streak == k:
                return current
        assert(False)
        return -1
        
