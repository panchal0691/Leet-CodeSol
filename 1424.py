class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        arr = []
        for x,row in enumerate(nums):
            for y, v in enumerate(row):
                if x+y >=len(arr):
                    arr.append([])
                arr[x+y].append(v)

        ans = []
        for row in arr:
            ans.extend(reversed(row))
        return ans
        
