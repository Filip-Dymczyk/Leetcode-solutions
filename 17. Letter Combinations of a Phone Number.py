from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        n = len(digits)

        nr_to_str = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                     '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        if n == 1:
            return [''.join(letter) for letter in nr_to_str[digits[0]]]
        elif n == 2:
            word1 = nr_to_str[digits[0]]
            word2 = nr_to_str[digits[1]]
            return [''.join(letter1 + letter2) for letter1 in word1 for letter2 in word2]
        elif n == 3:
            word1 = nr_to_str[digits[0]]
            word2 = nr_to_str[digits[1]]
            word3 = nr_to_str[digits[2]]
            return [''.join(letter1 + letter2 + letter3) for letter1 in word1 for letter2 in word2 for letter3 in word3]

        word1 = nr_to_str[digits[0]]
        word2 = nr_to_str[digits[1]]
        word3 = nr_to_str[digits[2]]
        word4 = nr_to_str[digits[3]]
        return [''.join(letter1 + letter2 + letter3 + letter4) for letter1 in word1 for letter2 in word2
                for letter3 in word3 for letter4 in word4]
