class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        _dict = defaultdict(int)
        _s = "".join(sorted(s))
        _t = "".join(sorted(t))
        _dict[_s] += 1
        _dict[_t] += 1

        if _dict[_s] > 1:
            return True
        return False
        