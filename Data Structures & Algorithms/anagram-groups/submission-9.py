class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        _dict = defaultdict(list)
        for string in strs:
            sorted_str = "".join(sorted(string))
            _dict[sorted_str].append(string)
        
        result = []

        for value in _dict.values():
            result.append(value)
        
        return result
