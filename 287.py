class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        N = len(nums)

        left = 1
        right = N
        def good(low, high):

            count = 0
            for x in nums:
                if low <= x <= high:
                    count +=1
            return  count > (high - low +1)

        while left < right:

            mid = (left +  right)//2

            if good(left, mid):
                 right = mid

            else:
                 left = mid +1
        return left
