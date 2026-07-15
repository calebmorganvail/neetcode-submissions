class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        h_map = {'{': '}', '[': ']', '(': ')'}

        for char in s:
            if char in h_map:
                stack.append(char)
            else:
                if not stack:
                    return False
                if char != h_map[stack[-1]]:
                    return False
                stack.pop()

        return len(stack) == 0



        