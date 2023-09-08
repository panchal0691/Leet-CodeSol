# Maximum Gap
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n= len(nums)
        if n<2: return 0
        lo,hi = min(nums),max(nums)
        B = defaultdict(list)
        for num in nums:
            if num==hi:
                ind = n-1
            else:
                ind = (abs(lo-num)*(n-1))//(hi-lo)
            B[ind].append(num)


        buckets =[]

        for i in range(n):
            if B[i]:
                buckets.append((min(B[i]),max(B[i])))

        output =0
        for i in range(1,len(buckets)):
            output = max(output,abs(buckets[i-1][-1]-buckets[i][0]))

        return output
        
