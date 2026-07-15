class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """The correct thing to use in this problem is a dict, becuase we want to keep track 
        of the values and there indexes, specificially so we can check if the values add 
        to the target, but also to return the indexes of those values."""

        _dict = {}

        for i, num in enumerate(nums):

            r = target - num
            if r in _dict:
                return [_dict[r], i]

            _dict[num] = i