class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """An anagram is a word that makes another word with the same letters as the
        original word.
        """

        if len(t) != len(s):
            return False

        _s = {}
        _t = {}

        for i in range(len(s)):
            _s[s[i]] = _s.get(s[i], 0) + 1
            _t[t[i]] = _t.get(t[i], 0) + 1

        return _s == _t


        