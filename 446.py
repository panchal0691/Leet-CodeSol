from collections import defaultdict

class Solution:
    def numberOfArithmeticSlices(self, nums):
        ans = 0
        length = len(nums)
        map = [defaultdict(int) for _ in range(length)]

        for i in range(length):
            for j in range(i):
                diff = nums[j] - nums[i]
                if diff <= -2147483648 or diff > 2147483647:
                    continue

                n2 = map[i][diff]
                n1 = map[j][diff]
                ans += n1
                freq = n1 + n2 + 1
                map[i][diff] = freq

        return ans
