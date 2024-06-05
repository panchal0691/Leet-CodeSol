class Solution:
    def fillCountArray(self, word, count):
        for ch in word:
            count[ord(ch) - ord('a')] += 1

    def commonChars(self, words):
        result = []
        
        n = len(words)
        
        count = [0] * 26
        
        self.fillCountArray(words[0], count)

        for i in range(1, n):
            temp = [0] * 26
            
            self.fillCountArray(words[i], temp)

            for j in range(26):
                if count[j] != temp[j]:
                    count[j] = min(count[j], temp[j])
            
        for i in range(26):
            if count[i] != 0:
                result.extend([chr(i + ord('a'))] * count[i])
        
        return result

# Example usage:
# sol = Solution()
# print(sol.commonChars(["bella", "label", "roller"]))
