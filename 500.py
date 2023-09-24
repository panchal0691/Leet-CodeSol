class Solution:
    
    def check(self, c, s):
        for i in s:
            if i == c:
                return True
        return False

    def findWords(self, words):
        mp = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        ans = []
        n = len(words)
        for i in range(n):
            for j in range(3):
                found = True
                for k in range(len(words[i])):
                    if not self.check(words[i][k].lower(), mp[j]):
                        found = False
                if found:
                    ans.append(words[i])
                    break
        return ans

        
