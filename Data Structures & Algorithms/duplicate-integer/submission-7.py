class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """Pattern matching. 1. What is the data struct, what is the algo."""

        # Contains duplicate requires that we look and check if there are duplicates in a list
        # Choosing the correct data structure: hashing removes duplicates by defualy.
        # The options are set() which just contains keys, and dict {} with key value pairs

        _set = set()

        for num in nums: 
            if num in _set:
                return True
            _set.add(num)
        
        return False