class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        ## BINARY SEARCH | time: O(log(m*n)), space: O(1)
        # flatten matrix into sorted array, binary search 0 to rows*cols-1
        # map m to matrix w row = m //cols, col = m % cols
        rows, cols = len(matrix), len(matrix[0])

        l, r = 0, rows * cols - 1
        while l <= r:
            mid = l + (r - l) // 2
            row, col = mid // cols, mid % cols
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False
        