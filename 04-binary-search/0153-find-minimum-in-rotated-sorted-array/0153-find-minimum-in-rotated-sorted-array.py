class Solution:
    def findMin(self, nums: List[int]) -> int:
        ## BINARY SEARCH | time: O(logn), space: O(1)
        # rotated sorted array, find minimum element
        # check if mid element is rotated or not rotated
        # if rotated, mid > r, check right side, l = m + 1
        # if not rotated mid < r, check left side, r = m
        # return l
        
        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2

            # if not rotated, mid <= rightmost element
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
                
        return nums[l]
        