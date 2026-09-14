class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        _dict = defaultdict(int) 

        for i, num in enumerate(nums):

            r = target - num

            if r in _dict:
                return [_dict[r], i]

            _dict[num] = i