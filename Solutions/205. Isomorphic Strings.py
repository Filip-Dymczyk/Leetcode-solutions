class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s_t = dict()
        map_t_s = dict()
        i = 0

        while i < len(s):

            if s[i] in map_s_t:
                if map_s_t[s[i]] != t[i]:
                    return False
            else:
                map_s_t[s[i]] = t[i]

            if t[i] in map_t_s:
                if map_t_s[t[i]] != s[i]:
                    return False
            else:
                map_t_s[t[i]] = s[i]
            i += 1
        return True
