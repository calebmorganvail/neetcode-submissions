class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = [char.lower() for char in s if char.isalnum()]
        s2 = [char.lower() for char in s if char.isalnum()]
        for char in s1:
            if s1.pop() != s2.pop(0):
                return False
        
        return True

        