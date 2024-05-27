class Solution:
    def specialArray(self, nums):
        for i in range(1, 1001):
            count = 0
            for num in nums:
                if num >= i:
                    count += 1
            if i == count:
                return i
        return -1

class Solution2:
    @staticmethod
    def specialArray(nums):
        nums.sort()
        for i in range(1, nums[-1] + 1):
            ind = Solution2.binary_search(nums, i)
            if ind >= 0 and i == len(nums) - ind:
                return i
        return -1

    @staticmethod
    def binary_search(nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1

# Example usage
if __name__ == "__main__":
    print(Solution2.specialArray([3, 6, 7, 7, 0]))
