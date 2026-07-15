class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """An anagram is a word that contains the same letters in a differnt order.
        The correct data structure to use in this case is a dict, becuase we can 
        keep track of the letters and there counts {letter: count, ...}
        then we can compare one dict to another and return based on if the dicts match.
        """

        s_dict = {}
        t_dict = {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            s_dict[s[i]] = s_dict.get(s[i], 0) + 1 
            t_dict[t[i]] = t_dict.get(t[i], 0) + 1
        
        return s_dict == t_dict
