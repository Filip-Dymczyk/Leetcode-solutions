from typing import List
import heapq


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:

        max_heap = []
        for p, t in classes:
            profit = ((p + 1) / (t + 1)) - (p / t)
            max_heap.append((-profit, p, t))
        heapq.heapify(max_heap)

        while extraStudents > 0:
            _, p, t = heapq.heappop(max_heap)
            new_profit = ((p + 2) / (t + 2)) - ((p + 1) / (t + 1))
            heapq.heappush(max_heap, (-new_profit, p + 1, t + 1))
            extraStudents -= 1

        ratio_sum = 0
        for _, pass_count, total in max_heap:
            ratio_sum += pass_count / total

        return ratio_sum / len(classes)
