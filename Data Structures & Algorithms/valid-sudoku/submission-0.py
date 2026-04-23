class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        temp = [set() for _ in range(9)]
        for i in range(9):
            temp_ver = set()
            temp_hor = set()
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in temp_hor:
                        return False
                    else:
                        temp_hor.add(board[i][j])
                    if board[i][j] in temp[(i//3*3)+(j//3)]:
                        return False
                    else:
                        temp[(i//3*3)+(j//3)].add(board[i][j])
                if board[j][i] != '.':
                    if board[j][i] in temp_ver:
                        return False
                    else:
                        temp_ver.add(board[j][i])
        return True
                
