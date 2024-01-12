class Solution:
    def halvesAreAlike(self, s):
        ch = list(s)
        left, right = 0, len(ch) - 1

        lcount, rcount = 0, 0
        vowels = set('aeiouAEIOU')

        while left < right:
            lcount += 1 if ch[left] in vowels else 0
            rcount += 1 if ch[right] in vowels else 0
            left += 1
            right -= 1

        return lcount == rcount

        
