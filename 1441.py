class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        prev = 1
        for x in target:
            while prev != x:
                ans.append("Push")
                ans.append("Pop")
                prev +=1
            ans.append("Push")
            prev +=1
        return ans
        
