A majority element is defined as an element that appears more than N // 3 times in the list
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        N = len(nums)
        
        INF = 10 **20 
        current1 = INF
        delta1 = 0
        current2 = INF
        delta2 =0

        for x in nums:
            if current1 == x:
                delta1 +=1
            elif current2 == x:
                delta2 +=1
            elif delta1 == 0:
                current1 = x
                delta1 += 1
            elif delta2 == 0:
                current2 =x
                delta2 +=1
            else:
                delta1 -=1
                delta2 -=1
        ans = []
        for x in [current1, current2]:
            count = nums.count(x)
            if count > N //3:
                ans.append(x)
        return ans
        
