class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        n = len(s)
        
        to_remove = set()
        st = []
        
        for i in range(n):
            if s[i] == '(':  
                st.append(i)
            elif s[i] == ')':
                if not st:  
                    to_remove.add(i)
                else:
                    st.pop()  
       
        while st:
            to_remove.add(st.pop())
        
        result = ''
        
        for i in range(n):
            if i not in to_remove:
                result += s[i]
        
        return result
