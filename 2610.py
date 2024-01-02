class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        f = collections.Counter(nums)

        ans = []
        for k,v in f.items():
            for i in range(v):
                if i >= len(ans):
                    ans.append([])
                ans[i].append(k)

        return ans
        
