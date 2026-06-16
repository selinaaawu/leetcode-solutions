class Solution:
    def maxArea(self, height: List[int]) -> int:

        # TWO POINTERS | time: O(n), space: O(1)
        # move pointer from smaller bar to maximize area
        max_area = 0

        left, right = 0, len(height) - 1
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, area)

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return max_area
        