class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        N = len(nums)
        best = [-1]*N
        best[k] = nums[k]

        index = k-1
        while index >=0:
            best[index] = min(best[index +1], nums[index])
            index -=1

        index = k +1
        while index < N:
            best[index] = min(best[index -1], nums[index])
            index +=1
        ans =0
        left = right =k
        current = best[k]
        while True:
            current = min(best[left] , best[right])
            ans = max(ans, (right - left +1)* current)
            if left == 0 and right == N-1:
                break
            if left ==0:
                right +=1
            elif right == N-1:
                left -=1
            elif best[left -1] > best[right +1]:
                left -=1
            else:
                right +=1
        return ans


        
