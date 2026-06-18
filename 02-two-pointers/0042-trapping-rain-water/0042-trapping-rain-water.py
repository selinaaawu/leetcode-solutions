class Solution:
    def trap(self, height: List[int]) -> int:

        # TWO POINTERS | time: O(n), space: O(1)
        # move shorter wall, update if higher wall, calculate water trapped
        # [ 0 1 0 2 1 0 1 3 2 1 2 1]
        #   L                     R     leftMax = 0, rightMax = 1
        #     L                   R     leftMax = 1, rightMax = 1, result += 1 - 1
        #       L                 R     leftMax = 1, rightMax = 1, result += 1 - 0
        #         L               R     leftMax = 2, rightMax = 1, result += 2 - 2
        #         L             R       leftMax = 2, rightMax = 2, result += 2 - 2
        #           L           R       leftMax = 2, rightMax = 2, result += 2 - 1
        #             L         R       leftMax = 2, rightMax = 2, result += 2 - 0
        #               L       R       leftMax = 2, rightMax = 2, result += 2 - 1
        #                 L     R       leftMax = 3, rightMax = 2, result += 3 - 3
        #                 L   R         leftMax = 3, rightMax = 2, result += 2 - 1
        #                 L R           leftMax = 3, rightMax = 2, result += 2 - 2
        n = len(height)
        result = 0
        
        leftMax, rightMax = height[0], height[n - 1]
        left, right = 0, n - 1
        while left < right:
            if height[left] <= height[right]:
                left += 1
                leftMax = max(leftMax, height[left])
                result += leftMax - height[left]
                
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                result += rightMax - height[right]
                
                
        return result

        # PREFIX & SUFFIX ARRAYS | time: O(n), space: O(n)
        n = len(height)

        # array of tallest bar from start to i
        leftMax = [0] * n
        leftMax[0] = height[0]
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])

        # array of tallest bar from end to i
        rightMax = [0] * n
        rightMax[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])
        
        # find water stored
        result = 0
        for i in range(n):
            result += min(leftMax[i], rightMax[i]) - height[i]
        return result


        # BRUTE FORCE | time: O(n^2), space: O(1)
        # calculate max water to left (0 to i) and right (i + 1 to n)
        # of current bar to find water stored
        result = 0
        for i in range(len(height)):
            leftMax = rightMax = height[i]

            for j in range(i):
                leftMax = max(leftMax, height[j])
            for j in range(i + 1, len(height)):
                rightMax = max(rightMax, height[j])
            result += min(leftMax, rightMax) - height[i]
        return result
        