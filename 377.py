class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        has_cache = [False] * (target+1)
        cache = [None] * (target+1)

        def count(target):
            if target < 0:
                return 0
            if target == 0:
                return 1
            if has_cache[target]:
                return cache[target]

            total = 0

            for x in nums:
                if (target -x) >=0:
                    total += count(target - x)


            has_cache[target] = True
            cache[target] = total
            return total

        return count(target)
    
