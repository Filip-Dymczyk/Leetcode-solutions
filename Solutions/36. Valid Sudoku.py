from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        set_cube1 = set()
        set_cube2 = set()
        set_cube3 = set()
        sets_cols = [set() for _ in range(9)]

        for row in range(0, len(board)):
            if row % 3 == 0:
                set_cube1 = set()
                set_cube2 = set()
                set_cube3 = set()
            set_row = set()
            for col in range(0, len(board[0])):
                if board[row][col] not in [",", "."]:
                    if board[row][col] in sets_cols[col]:
                        print(1)
                        return False
                    else:
                        sets_cols[col].add(board[row][col])
                    if board[row][col] in set_row:
                        print(2)
                        return False
                    else:
                        set_row.add(board[row][col])
                        if col < 3:
                            if board[row][col] in set_cube1:
                                print(3, row, col, set_cube1)
                                return False
                            else:
                                set_cube1.add(board[row][col])
                        elif col < 6:
                            if board[row][col] in set_cube2:
                                print(4)
                                return False
                            else:
                                set_cube2.add(board[row][col])
                        else:
                            if board[row][col] in set_cube3:
                                print(5)
                                return False
                            else:
                                set_cube3.add(board[row][col])
        return True
