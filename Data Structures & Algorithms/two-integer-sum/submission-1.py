class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute force O(n^2)
        # for r, num in enumerate(nums):
        #     remainder = target - num
        #     if remainder in nums and nums.index(remainder) != r:
        #         i, j = nums.index(remainder), r
        # return [i, j]
        
        seen = set()

        for r, num in enumerate(nums):
            remainder = target - num
            if remainder in seen:
                i = nums.index(remainder)
                j = r
            seen.add(num)
        return [i, j]
        