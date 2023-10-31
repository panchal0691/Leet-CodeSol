class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        ans = []
        prev = 0
        for x in pref:
            ans.append(prev ^ x)
            prev = x
        return ans
        
