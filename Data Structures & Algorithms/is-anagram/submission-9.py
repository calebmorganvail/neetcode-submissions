class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''Determines weather a string is an anagram of another string.
        
        Args: 
            s: The first string.
            t: The seccond string.

        Returns: 
            A boolean value if the strings s and t are anagrams of eachother.

        Time Complexity:
            O(n): Where n is a character in the string s.

        Space Complexity:
            O(n): Where n is a character in the string s.
        
        '''

        if len(s) != len(t):
            return False
        
        _s = defaultdict(int)
        _t = defaultdict(int)

        # O(n)
        for i in range(len(s)):
            _s[s[i]] += 1
            _t[t[i]] += 1

        # O(n)
        return _s == _t 


    