class Solution:
    def groupAnagrams(self, words: List[str]) -> List[List[str]]:

        res = defaultdict(list)
        for s in words:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())
            


    