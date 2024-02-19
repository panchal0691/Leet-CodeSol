class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        key = S.replace("-", "").upper()
        
        # 6u5F3Z2E9W
        
        formatted = []
        
        i = len(key)-K
        while i >= 0:
            formatted.append(key[i:i+K])
            i -= K
            
        if i != -K:
            formatted.append(key[:i + K])
        
        formatted = formatted[::-1]
        
        return "-".join(formatted)
        
        
