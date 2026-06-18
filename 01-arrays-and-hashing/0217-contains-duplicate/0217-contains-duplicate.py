class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # return true if value appears more than once
        # return false if otherwise

        # set length: compare length of array w length of set of array
        # time: O(n), space: O(n)
        return len(nums) != len(set(nums))

        # set: store seen element in set
        # time: O(n), space: O(n)
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

        # brute force: check every element & if seen return true
        # time: O(n^2), space: O(1)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
