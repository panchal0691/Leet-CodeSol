class Solution:
    def longestPalindrome(self, s: str) -> int:
        st = set()
        result = 0
        
        for ch in s:
            if ch in st:
                st.remove(ch)
                result += 2
            else:
                st.add(ch)
        
        if st:
            result += 1
        
        return result
