class Solution:
    def getLeftMax(self, height, n):
        leftMax = [0] * n
        leftMax[0] = height[0]
        for i in range(1, n):
            leftMax[i] = max(leftMax[i-1], height[i])
        return leftMax
    
    def getRightMax(self, height, n):
        rightMax = [0] * n
        rightMax[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            rightMax[i] = max(rightMax[i+1], height[i])
        return rightMax
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 1 or n == 0:
            return 0
        leftMax = self.getLeftMax(height, n)
        rightMax = self.getRightMax(height, n)
        water = 0
        for i in range(n):
            water += min(leftMax[i], rightMax[i]) - height[i]
        return water
        
