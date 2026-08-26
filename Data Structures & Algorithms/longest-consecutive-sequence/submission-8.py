class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """Calculate the longest consecutive sequence in the number list passed.
        
        Args: 
            nums: The list of numbers to find the longest consecutive sequence in.
        
        Returns: 
            An integer value representing the length of the longest consecutive sequence.
        
        Time Complexity:
            O(n) where n is the number of values in the nums list.

        Space Complexity:
            O(n)
        """

        _set = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in _set:
                count = 0
                while num + count in _set:
                    count += 1
                longest = max(count, longest)
        return longest
