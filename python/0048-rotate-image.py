class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # Swap all i and j
        for row in range(n):
            for col in range(row,n):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

        # Then reverse all rows
        for row in matrix:
            row.reverse()

