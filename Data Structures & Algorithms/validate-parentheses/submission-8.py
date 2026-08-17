class Solution:
    def isValid(self, s: str) -> bool:
        '''Determins if the string contains valid parentheses.

        Args: 
            s: The string to scan for valid parentheses.
        
        Returns: 
            A boolean, true if the string s contains valid parentheses, flase otherwise.
        
        Time Complexity: 
            O(n), where n is a char in s.
        
        Space Complexity:
            O(n), where n is a char in s.
        '''

        stack = []
        h_map = {'{': '}', '[': ']', '(': ')'}

        for char in s: # O(n)
            if char in h_map:
                stack.append(char)
            else:
                if not stack:
                    return False
                if char != h_map[stack[-1]]:
                    return False
                stack.pop(-1)
        
        return len(stack) == 0