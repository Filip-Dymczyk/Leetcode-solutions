from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        dont_wants = 0
        while len(students) and dont_wants < len(students):
            p = students.pop(0)
            if p == sandwiches[0]:
                sandwiches.pop(0)
                dont_wants = 0
            else:
                students.append(p)
                dont_wants += 1
        return len(students)
