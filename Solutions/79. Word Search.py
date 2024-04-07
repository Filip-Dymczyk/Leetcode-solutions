from typing import List, Tuple, Set


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def rec_exist(elem: Tuple[int, int], word_idx: int, visited: Set[Tuple[int, int]]) -> bool:
            if word_idx == len(word):
                return True
            i, j = elem
            if i < 0 or i >= n or j < 0 or j >= m or word[word_idx] != board[i][j] or elem in visited:
                return False
            visited.add((i, j))
            neighs = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
            for neigh in neighs:
                if rec_exist(neigh, word_idx + 1, visited):
                    return True
            visited.remove((i, j))
            return False
        n, m = len(board), len(board[0])
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if rec_exist((i, j), 0, set()):
                        return True
        return False
