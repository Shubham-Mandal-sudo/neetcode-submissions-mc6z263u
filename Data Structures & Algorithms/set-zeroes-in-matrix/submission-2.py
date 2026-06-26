class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        column = set()
        row = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    row.add(i)
                    column.add(j)

        for i in row:
            matrix[i][::] = [0,]*(len(matrix[i]))
        for i in range(len(matrix)):    
            for j in column:
                matrix[i][j] = 0

        
        