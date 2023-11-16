class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        N = len(nums)
        s = set(int(x,2) for x in nums)

        def pad(x,N):
            K = len(x)
            return ("0" * (N - K)) + x
        for x in range(1 << N):
            if x not in s:
                return pad(bin(x)[2:], N)
        return "0"* N
        
