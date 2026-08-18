import random

class Solution:
    def __init__(self):
        self.mapping: dict[int, str] = defaultdict(str)
        self.sample: list[int] = []


    def gen_sample(self, strs: List[str]):
        n: int = len(strs)
        self.sample = random.sample(range(0, n), n)
        

    def encode(self, strs: List[str]) -> str:
        self.gen_sample(strs)

        for i, string in enumerate(strs):
            rnd_num: int = self.sample[i]
            self.mapping[rnd_num] = string
        return '-'.join(str(k) for k in self.mapping.keys())


    def decode(self, s: str) -> List[str]:
        result = []
        if len(s) == 0:
            return result
        for num in s.split("-"):
            num = int(num)
            mapped_str: str = self.mapping[num]
            result.append(mapped_str)
        return result
        


