class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        stack = []
        for num in nums:
            if not stack or num > stack[-1]:
                stack.append(num)
                continue
            res = len(stack) - 1
            l, r = 0, res
            while l <= r:
                p = (l + r) // 2
                if stack[p] >= num:
                    res = p
                    r = p - 1
                else:
                    l = p + 1
            stack[res] = num
        return len(stack)
