class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        N = len(arr)
        arr.sort()

        arr[0] = 1
        for i in range(1, N):
            arr[i] = min(arr[i -1] +1, arr[i])

        return arr[-1]
        
