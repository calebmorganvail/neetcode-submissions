class Solution:


    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''Determins the output list of values where each value in the list is the
        product of all numbers in nums excluding nums[output_list[i]]
        
        Args: 
            nums: The list of numbers to calculate products from.

        Returns: 
            The list of products at each index in nums excluding nums[output_list[i]]
        
        Time Complexity: 
            O(n) where n is the length of nums.

        Space Complexity:
            O(1).
        '''

        result = [1] * len(nums)

        prefix = 1

        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        suffix = 1 
        for i in reversed(range(len(nums))):
            result[i] *= suffix
            suffix *= nums[i]
    

        return result
        

        
        

    

    
        
