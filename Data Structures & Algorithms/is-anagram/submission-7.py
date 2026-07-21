class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        

        _s = {}
        _t = {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            _s[s[i]] = _s.get(s[i], 0) + 1
            _t[t[i]] = _t.get(t[i], 0) + 1
        return _s == _t