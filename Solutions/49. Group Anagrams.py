from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Map sorted word to its index in the res array:
        d = dict()
        res = []
        idx = 0
        for word in strs:
            s_word = ''.join(sorted(word))
            if s_word not in d:
                res.append([word])
                d[s_word] = idx
                idx += 1
            else:
                curr_idx = d[s_word]
                res[curr_idx].append(word)
        return res
