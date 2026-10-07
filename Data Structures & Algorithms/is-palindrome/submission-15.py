class Solution:
    def isPalindrome(self, s: str) -> bool:

        char = []
        for character in s:
            if character.isalnum():
                char.append(character.lower().strip())
        
        rev_idx = len(char) - 1
     
        flag = True

        for i in range(len(char)):
            if char[rev_idx] != char[i]:
                flag = False
            rev_idx -= 1
        return flag