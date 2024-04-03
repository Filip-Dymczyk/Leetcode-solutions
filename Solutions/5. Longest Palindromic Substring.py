class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) < 2:
            return s

        longest_palindrome = ""

        # Let's map all occurrences of letters onto their id's in the string:
        map_letter_to_idx = dict()

        # Let's gather letter information into the dictionary:
        for idx, elem in enumerate(s):
            if elem not in map_letter_to_idx:
                map_letter_to_idx[elem] = [idx]
            else:
                map_letter_to_idx[elem].append(idx)

        # Let's map through letters and get corresponding ids array:
        for letter in map_letter_to_idx:
            idx_array = map_letter_to_idx[letter]
            curr_palindrome = ""

            # If there's more than 1 element in the array:
            if len(idx_array) > 1:
                # Iterate through array with two pointers - beginning and end of substring:
                for i in range(len(idx_array)):
                    # We check from the furthest index to the right - possibility for the longest palindrome on the
                    # longest substring:
                    for j in range(len(idx_array) - 1, i, -1):
                        left = idx_array[i]
                        right = idx_array[j]
                        string = s[left:right + 1]

                        # Is string is equal to its reverse:
                        if string == string[::-1]:
                            # We found longest palindrome for selected beginning:
                            curr_palindrome = string
                            break

                    # Check for swap possibility:
                    if len(curr_palindrome) > len(longest_palindrome):
                        longest_palindrome = curr_palindrome

            # if we have 1 element in the array - letter occurred only once in the string:
            elif len(idx_array) == 1:

                # Get the palindrome as the letter itself:
                curr_palindrome = s[idx_array[0]]

                # Check for swap possibility:
                if len(curr_palindrome) > len(longest_palindrome):
                    longest_palindrome = curr_palindrome

        return longest_palindrome
