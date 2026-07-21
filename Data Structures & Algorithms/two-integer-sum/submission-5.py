class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        inum = {}

        for i, num in enumerate(nums):
            remainder = target - num
            if remainder in inum:
                return [inum[remainder], i]
            inum[num] = i
        