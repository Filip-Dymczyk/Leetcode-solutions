class Solution:
    def intToRoman(self, num: int) -> str:
        map_roman_to_int = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
        roman = ""
        base = 1
        numeral = 1

        while num > 0:
            rest = num % 10
            num //= 10

            if rest != 0:
                if rest == 4 or rest == 9:
                    roman += map_roman_to_int[(base + rest) * numeral]
                    roman += map_roman_to_int[numeral]
                else:
                    while rest > 0:
                        if rest in map_roman_to_int:
                            roman += map_roman_to_int[base * rest * numeral]
                            rest -= rest
                        else:
                            roman += map_roman_to_int[base * numeral]
                            rest -= base
            numeral *= 10

        return roman[::-1]
