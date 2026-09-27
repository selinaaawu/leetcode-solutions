class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:

        # FIXED SLIDING WINDOW | time: O(n)
        # calculate sum for current range (up to not including k)
        currSum = sum(nums[:k])                 # O(k)
        maxSum = currSum

        # move fixed window, update current sum, update max sum
        for right in range(k, len(nums)):           # O(n)
            currSum += nums[right] - nums[right - k]
            maxSum = max(currSum, maxSum)
        
        # return average
        return maxSum / k
