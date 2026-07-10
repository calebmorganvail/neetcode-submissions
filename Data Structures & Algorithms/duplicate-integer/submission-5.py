class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """The contains duplicate problem requires that the function 
        returns a bool indicating weather or not the list of numbers 
        contains and duplicate numbers. 
        """
        
        # Brute force solution O(n^2)
        # for i, x in enumerate(nums):
        #     for j, y in enumerate(nums): 
        #         if x == y and i != j: 
        #             return True
        # return False

        # Faster solution using a set O(n)
        # _set = set()
        # for num in nums:
        #     if num in _set:
        #         return True 
        #     _set.add(num)
        # return False

        # Another solution using sets O(n)
        return len(set(nums)) < len(nums)



