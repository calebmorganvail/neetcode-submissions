class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """This function determines if there are duplicate numbers in a a list
        
        Args:
            nums: List[int], the list of numbers that is being passed.
        
        Returns: True if there are duplicates in the list, and False if there are none.

        Time Complexity: O(n) where n is the number of items in the list.
        """
        hash_set = set()
        for num in nums:
            if num in hash_set:
                return True
            hash_set.add(num)
        return False


                
             
