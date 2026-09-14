class Solution:
    def groupAnagrams(self, strings: List[str]) -> List[List[str]]:
        
        
        _dict = defaultdict(list[str])


        for string in strings:
            
            _dict["".join(sorted(string))].append(string)

        
        return list(_dict.values())
