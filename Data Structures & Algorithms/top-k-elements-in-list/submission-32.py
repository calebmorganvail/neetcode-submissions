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
        
        print(dict_)

        for i in range(l, -1, -1 ):
            #print(i)
            if t == 0:
                break
            if dict_.get(i) != None:
                #print(dict_[i])
                r += dict_[i]
                t -= 1
        
        print(r)
        
        return r[:k]

            
    
            
            
        
      



                

  



        


