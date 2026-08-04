class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res = []

        # nums = [1,2,2,3,3,3]
        for num in nums:
            freq[num] = freq.get(num, 0) + 1 # {"1": 1, "2": 2, ...}

        sorted_freq_desc = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
        print(sorted_freq_desc)
        
        for key, value in sorted_freq_desc.items():
            if k == 0:
                continue
            res.append(key)
            k = k - 1

        return res
                