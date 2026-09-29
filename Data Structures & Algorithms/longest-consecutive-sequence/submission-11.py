class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        n_set = set(nums)

        l = 0

        for n in n_set:
            
            if n - 1 not in n_set:
                c = 0
                while n + c in n_set:
                    c += 1
                l = max(c, l)
        return l

