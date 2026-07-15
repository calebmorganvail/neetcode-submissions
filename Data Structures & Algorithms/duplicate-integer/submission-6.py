class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """The key insight with these problems is identifying the correct
        datastructures to use in solving the problems. I already know this problem
        belongs to the array and hash catagories, but should and will note where and why
        its the appropriate data structure to use.
        
        The iput is a list, and were meant to indicate weather or not the list contains
        duplicates. The indication that this is a hash problem is by knowing the properties of a
        hash table. A hash table does not allow duplicates, so we can iterativly add elements
        to a hash set and if it contains an item that is already in there we can return false.
        """

        _set = set()

        for num in nums:
            if num in _set:
                return True
            _set.add(num)
        return False

    