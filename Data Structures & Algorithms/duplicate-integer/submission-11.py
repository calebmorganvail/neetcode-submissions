class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """Determines weather the list that is being passed
        contains a duplicate number or not.

        Args: 
            nums: An integer list containing the values to check for 
                  duplicates.

        Returns:
            A boolean value, True if the the list contains a duplicate,
            and False if the list does not.

        Time Complexity:
            O(n), where n is the length of the input list.

        Space Complexity:
            O(n), because a set of the potentially length n is created.
        """

        _set = set()
        for num in nums: # O(n)
            if num in _set: # O(1)
                return True
            _set.add(num)
        
        return False