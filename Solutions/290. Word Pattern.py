class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split()
        if len(s_list) != len(pattern):
            return False
        map_p_to_w = {}
        map_w_to_p = {}
        for p, w in zip(pattern, s_list):
            if p not in map_p_to_w:
                if w not in map_w_to_p:
                    map_p_to_w[p] = w
                    map_w_to_p[w] = p
                else:
                    return False
            else:
                if map_p_to_w[p] != w:
                    return False
        return True
