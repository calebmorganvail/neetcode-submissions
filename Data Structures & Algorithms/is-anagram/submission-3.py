class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """This function determines weather the strings make a valid anagram.
        
        An anagram is a string that contains the exact same characters as another string,
        but the order of the characters can be different.

        Args:
            s: the first string.
            t: the string to compare to s.

        Time Complexity: O(n + m), where n is the number of elements in s, and m is the number of elements in t.

        Space Complexity: O(1), since we have at most 26 different characters.
        """

        if len(s) != len(t): 
            return False
        
        s_dict = {}
        t_dict = {}

        for i in range(len(s)):
            s_dict[s[i]] = s_dict.get(s[i], 0) + 1
            t_dict[t[i]] = t_dict.get(t[i], 0) + 1

        return s_dict == t_dict
            
        