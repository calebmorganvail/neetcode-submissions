class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        t = k

        _dict = defaultdict(int)

        r = []

        l = len(nums)

        dict_ = defaultdict(list)

        for num in nums:
            _dict[num] += 1
        
        for key, val in _dict.items():
            dict_[val].append(key)

        for i in range(l, -1, -1):
            if t == 0:
                break
            if dict_.get(i) != None:
                r += dict_[i]
                t -= 1
        
        return r[:k]

            
    
            
            
        
      



                

  



        


