class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # Result str:
        res = ""

        # ASCII code indicating beggining of A - Z (65 - 90):
        asc_left = 65

        while columnNumber:
            # Scale currently procesed value so that it will have letter corresponding - A-Z (0 - 25):
            columnNumber -= 1

            # Get the current number and change columnNumber:
            num = columnNumber % 26
            columnNumber //= 26

            # Add to res:
            res += chr(asc_left + num)

        # Invert:
        return res[::-1]
