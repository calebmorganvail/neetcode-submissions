class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """Calculates the products of all the numbers at each position
        in the input array minus the position itself.

        Args: 
            nums: The list of numbers to calculate the product from.

        Returns:
            A list containing the product at each position in the input list, 
            where the product at a given location is the product of all the 
            numbers except the number at the current position.

        Time Complexity:

        Space Complexity:
        
        """ 

        leng = len(nums)
        result = [1] * leng 
        
        prefix = 1 
        for i in range(leng):
            result[i] = prefix 
            prefix *= nums[i] 

        postfix = 1
        for i in range(leng -1, -1, -1):
            result[i] *= postfix 
            postfix *= nums[i] 

        return result

            