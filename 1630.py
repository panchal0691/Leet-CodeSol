class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        N = len(nums)
        Q = len(l)
        ans =[]
        for start, end in zip(l,r):
            ans.append(True)
            current = sorted(nums[start:end + 1])

            delta = current[1] - current[0]
            for i in range(1, len(current)):
                if current[i] - current[i -1] != delta:
                    ans[-1] =False
        return ans
        
