class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Binary search for the row
        rowLeft, rowRight = 0, len(matrix) - 1
        while (rowLeft < rowRight):
            rowMid = rowLeft + (rowRight - rowLeft) // 2
            if matrix[rowMid][0] == target: return True
            if matrix[rowMid][0] < target <= matrix[rowMid][-1]:
                rowLeft = rowMid
                break
            elif target > matrix[rowMid][0]:
                rowLeft = rowMid + 1
            else:
                rowRight = rowMid - 1

        # I've got to be smarter about my rows
        l, r = 0, len(matrix[0]) - 1
        print(rowLeft)
        while l < r:
            mid = l + (r - l) // 2
            if matrix[rowLeft][mid] == target:
                return True
            if matrix[rowLeft][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return True if matrix[rowLeft][r] == target else False


