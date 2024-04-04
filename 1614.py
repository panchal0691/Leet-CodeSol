class Solution:
    def maxDepth(self, s: str) -> int:
        result = 0
        stack = []
        
        for ch in s:
            if ch == '(':
                stack.append(ch)
            elif ch == ')':
                stack.pop()
                
            result = max(result, len(stack))
        
        return result
        
