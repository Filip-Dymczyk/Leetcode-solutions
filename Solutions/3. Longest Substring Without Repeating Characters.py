class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # Edge case:
        if len(s) < 2:
            return len(s)

        # Current length - before transitioning to another window:
        curr_length = 0

        # Result length:
        max_length = 0

        # Left window edge:
        i = 0

        # Right window edge:
        j = 1

        # Set to check if an elem has already been seen throughout substring:
        seen = set()

        while i < len(s) and j < len(s):
            # if we haven't seen left window edge - we mark it and increment current length:
            if s[i] not in seen:
                seen.add(s[i])
                curr_length += 1

            # If we haven't seen right window edge - mark it, move it and increment length:
            if s[j] not in seen:
                seen.add(s[j])
                j += 1
                curr_length += 1
            # Else:
            else:
                # Remove left edge elem from set (substring) - we need to resolve conflict within the substring and move the i:
                seen.remove(s[i])
                i += 1

                # Check if we need to swap:
                max_length = max(max_length, curr_length)

                # Decrement curr_length - moving the edge:
                curr_length -= 1

                # if the idx's equal up - move j:
                if i == j:
                    j += 1

        # If we haven't made the last swap:
        max_length = max(curr_length, max_length)
        return max_length
