class Solution:
    def maximumValueSum(self, nums, k, edges):
        sum_val = 0
        count = 0
        min_nukasan = float('inf')
        
        for num in nums:
            if (num ^ k) > num:
                count += 1
                sum_val += (num ^ k)
            else:
                sum_val += num

            min_nukasan = min(min_nukasan, abs(num - (num ^ k)))
        
        if count % 2 == 0:
            return sum_val
        
        return sum_val - min_nukasan
