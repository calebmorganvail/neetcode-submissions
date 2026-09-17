class Solution:
    def __init__(self):
        self.mapping = defaultdict(str)
    
    def encode(self, strs: List[str]) -> str:

        l = len(strs)

        for i in range(l):
            self.mapping[i] = strs[i]

        r = []

        for key in self.mapping.keys():
            r.append(str(key))
            r.append("_")

        return "".join(r)
    

    def decode(self, s: str) -> List[str]:
        r = []
      
        s = s.split('_')
        s.pop(-1)
     
        for key in s:
            val = self.mapping.get(int(key))
            if val != None:
                r.append(val)
        return r
