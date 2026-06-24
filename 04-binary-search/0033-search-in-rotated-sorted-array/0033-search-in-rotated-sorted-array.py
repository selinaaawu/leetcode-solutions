class Solution:
    def search(self, nums: List[int], target: int) -> int:

        ## BINARY SEARCH
        # rotated sorted array, find specific element
        # compare nums[mid] > nums[r] to see if rotated or not
        # if mid > r, part of rotated half
        #   if target == mid, return mid
        #   if mid < target, search right, l = mid + 1
        #   if mid > target
        #       if r >= target, search right, l = mid + 1
        #       if r < target, search left, r = mid - 1
        # if mid < r, part of sorted half
        #   if target == mid, return mid
        #   if mid < target, 
        #       if r >= target, search right, l = mid + 1
        #       if r < target, search left, r = mid - 1
        #   if mid > target, search left, r = mid - 1

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2
            
            # found match
            if nums[mid] == target:
                return mid
            # part of rotated half
            elif nums[mid] > nums[r]:
                if nums[mid] < target or nums[r] >= target:
                    l = mid + 1
                else:
                    r = mid - 1
            # part of sorted half
            else:
                if nums[mid] > target or nums[r] < target:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1
        