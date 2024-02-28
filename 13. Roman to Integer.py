class Solution:
    def romanToInt(self, s: str) -> int:
        map_roman_to_int = {'I': 1, 'V': 5, 'X': 10,
                            'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        if len(s) == 1:
            return map_roman_to_int[s]

        result = 0
        idx = 0
        while idx < len(s):
            if idx < len(s) - 1:
                if (s[idx] == 'I' and s[idx + 1] in ['V', 'X']) or (s[idx] == 'X' and s[idx + 1] in ['L', 'C']) \
                        or (s[idx] == 'C' and s[idx + 1] in ['D', 'M']):
                    result += map_roman_to_int[s[idx + 1]] - map_roman_to_int[s[idx]]
                    idx += 1
                else:
                    result += map_roman_to_int[s[idx]]
            else:
                result += map_roman_to_int[s[idx]]
            idx += 1
        return result
    