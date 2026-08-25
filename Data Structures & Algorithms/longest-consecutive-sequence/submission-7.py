class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        # print(nums)

        if len(nums) == 0:
            return 0
        count = 1
        longest = 1
        for i in range(len(nums)):
            if i != len(nums) - 1:
                j = i + 1
            else:
                break

            dif = nums[j] - nums[i]

            if dif == 0:
                continue

            if dif == 1:
                count += 1
            else:
                count = 1
        
            longest = max(longest, count)

        return longest


