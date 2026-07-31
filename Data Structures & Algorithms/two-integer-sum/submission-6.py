class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lib = defaultdict()

        for i, num in enumerate(nums):

            remainder = target - num
            if remainder in lib:
                return [lib[remainder], i]
            
            lib[num]= i 
        
        