class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        N = len(arr)
        candidates = [arr[N //4], arr[2*N//4],arr[3*N//4]]

        def count(x):
            first = bisect.bisect_left(arr, x)
            last = bisect.bisect_right(arr, x) -1

            return last - first +1

        for x in candidates:
            if count(x)* 4 > N:
                return x
        assert(False)
