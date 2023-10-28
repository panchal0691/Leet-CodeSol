class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10 **9 +7
        current = [1] *5
        prev = current 

        for _ in range(1,n):
            current = [0] * 5
            current[0] = (prev[1] + prev[2] + prev[4]) % MOD
            current[1] = (prev[0] + prev[2] ) % MOD
            current[2] = (prev[1] + prev[3] ) % MOD
            current[3] = (prev[2]) % MOD
            current[4] = (prev[2] + prev[3]) % MOD

            prev = current 
        return sum(current) % MOD
        
