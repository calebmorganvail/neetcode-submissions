class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''Determines duplicates in a given array of integers.
        
        Args: 
            nums: The list of integers to look through for duplicates
        
        Returns:
            A boolean, true if there are duplicates in the list, and false otherwise.
        
        Time Complexity:
            O(n): Where n is the number of values in nums.

        Space Complexity:
            O(n): Where n is the number of values in nums and nums is the space needed in memory.

        '''

        _set = set()

        for num in nums:
            
            if num in _set:
                return True
            
            _set.add(num)

        return False