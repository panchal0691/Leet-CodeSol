class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse = True)
        s.sort(reverse = True)
        count = 0
        gi = si = 0
        while gi < len(g) and si < len(s):
            if g[gi]  > s[si]:
                gi +=1
                continue

            gi +=1
            si +=1
            count +=1
        return count

        
