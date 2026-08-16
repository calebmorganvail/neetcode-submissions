class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''Determines if two values within the list add to the target.

        Args:
            nums: The list of integer values.
            target: The target value to sum too.

        Returns: 
            The list of indexes, if any, from the nums list that sum to the target.
        
        Time Complexity:
            O(n) where n is the number of values in the list.

        Space Complexity: 
            O(n) where n is the number of values in the list.
        '''

        _dict: dict[int, int] = defaultdict(int)

        # O(n)
        for i, num in enumerate(nums):
            r: int = target - num
            if r in _dict:
                return [_dict[r], i]

            _dict[num] = i