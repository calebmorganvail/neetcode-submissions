class Solution:
    def isPalindrome(self, s: str) -> bool:

        forward = []
        backward = []

        for char in s:
            
            if char != " " and char.isalnum():
                forward.append(char.lower())
                backward.append(char.lower())
        backward.reverse()
        flag = True
        for i in range(len(forward)):
            
            let_f = forward.pop()
            let_b = backward.pop()
            if let_f != let_b:
                flag = False
        
        return flag

        