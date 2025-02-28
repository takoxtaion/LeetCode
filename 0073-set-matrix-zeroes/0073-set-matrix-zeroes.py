class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        zero_positions = []
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_positions.append((i, j))

        for row, col in zero_positions:
            for j in range(cols):
                matrix[row][j] = 0
            for i in range(rows):
                matrix[i][col] = 0
