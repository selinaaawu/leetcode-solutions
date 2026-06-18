class Solution:
    def isValid(self, s: str) -> bool:

        # append open bracket to stack
        # pop matching closing bracket or invalid string
        parentheses_map = {')':'(', ']':'[', '}':'{'}
        stack = []

        for char in s:
            print(char)
            if char in parentheses_map.values():
                stack.append(char)
            else:
                # make sure to check stack not empty before popping
                if stack and stack[-1] == parentheses_map[char]:
                    stack.pop()
                else:
                    return False

        # make sure to check stack empty at end
        return True if not stack else False
        