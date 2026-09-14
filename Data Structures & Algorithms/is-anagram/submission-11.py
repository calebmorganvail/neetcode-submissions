class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        _set = set()

        _set.add("".join(sorted(s)))

        if "".join(sorted(t)) in _set:
            return True
        
        return False

        