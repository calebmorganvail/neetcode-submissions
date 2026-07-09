class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for r, num in enumerate(nums):
            remainder = target - num
            if remainder in nums and nums.index(remainder) != r:
                i, j = nums.index(remainder), r
        return [i, j]
            
        