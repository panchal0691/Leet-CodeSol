from sortedcontainers import SortedList
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        N = len(nums)
        INF = 10**20
        prefix = [INF]

        for x in nums:
            prefix.append(min(prefix[-1],x))

        sl = SortedList()
        for x in nums[::-1]:
            prefix.pop()
            index = sl.bisect_left(x)

            if 0<= index -1 < len(sl):
                two = sl[index -1]

                if two > prefix[-1]:
                    return True
            sl.add(x)

        return False
        
