# Solution

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        top, bottom = 0, rows - 1
        while top <= bottom:
            mid = (top + bottom) // 2
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bottom = mid - 1
            else: 
                break
        
        if not (top <= bottom):
            return False

        row = (top + bottom) // 2
        low, high = 0, cols - 1

        while low <= high:
            mid = (low + high) // 2

            if target > matrix[row][mid]:
                low = mid + 1
            elif target < matrix[row][mid]:
                high = mid - 1
            else:
                return True
        return False

  # Time Complexity of Solution - O(logn + logm)
  # Space Complexity of Solution - O(1)
