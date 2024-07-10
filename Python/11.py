class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxArea = 0

        while left < right:
            currentArea = min(height[left], height[right]) * (right - left) #calculate the area
            maxArea = max(maxArea, currentArea) #update the maxArea

            if height[left] < height[right]: #Move the pointer with the smaller height
                left += 1
            else:
                right -= 1

        return maxArea