class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        

        _set = set(nums)
        longest = 0
        for num in nums:
            count = 0
            if num - 1 not in _set:
                while num + count in _set:
                    count += 1
                
                longest = max(count, longest)
        return longest