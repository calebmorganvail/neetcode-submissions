class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        _s = set()
        for num in nums:
            if num in _s:
                print(_s)
                return True
            _s.add(num)
        print(_s)
        return False
