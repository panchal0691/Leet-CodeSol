class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = [c for c in s if c.lower() in 'aeiou']
        vowels_sorted = sorted(vowels, reverse=True)

        result = []
        for char in s:
            if char.lower() in 'aeiou':
                result.append(vowels_sorted.pop())
            else:
                result.append(char)

        return ''.join(result)
    
        
