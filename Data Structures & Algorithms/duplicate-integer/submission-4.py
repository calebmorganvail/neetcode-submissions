class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """Determines weather the list of integers contains a duplicate number.

        Args: nums as a list of integers.

        Returns: A True boolean if the list contains a duplicate and a false if it does not.

        Time Complexity: O(n), where n is the number of elements in the list.

        Space Complexity: O(n), where n is the number of elements in the list.
        """
        _set = set()
        for num in nums:
            if num in _set:
                return True
            _set.add(num)
        return False
        