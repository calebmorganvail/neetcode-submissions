class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''Produces the list of numbers that are the product of all numbers excluding the number
        at index i.
        
        Args:
            nums: The list of numbers to calculate the products list from.
        
        Returns:
            A list of numbers containing the products.
        
        Time Complexity:
            O(n) where n is the length of the list of numbers passed to the function.

        Space Complexity:
            O(n) where n is the length of the list of numbers passed to the function.
        '''


        result = [1] * len(nums) 

        prefix = 1  
        for i in range(len(nums)):
            result[i] *= prefix
            prefix = prefix * nums[i] 

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix = postfix * nums[i]
        
        return result

