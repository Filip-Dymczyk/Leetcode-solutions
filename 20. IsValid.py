class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) > 1:
            # Initialize stack.
            stack = [s[0]]
            for bracket in s[1:]:
                # If opening bracket - add to stack:
                if bracket in ["(", "[", "{"]:
                    stack.append(bracket)
                # If there is still something in stack:
                elif stack:
                    # Check if closing bracket has a corresponding opening one:
                    if (bracket == ")" and stack[-1] == "(") or (bracket == "}" and stack[-1] == "{") or \
                            (bracket == "]" and stack[-1] == "["):
                        # Pop a corresponding opening one:
                        stack.pop(-1)
                    else:
                        # If the closing bracket doesn't have a corresponding one:
                        return False
                # If stack is empty and next bracket is a closing one:
                else:
                    # We won't have a matching opening bracket:
                    return False
            # If stack is empty - we return True:
            return not stack
            # If string has only 1 element or is empty:
        return False
    