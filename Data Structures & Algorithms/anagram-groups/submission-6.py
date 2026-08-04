class Solution:
    def groupAnagrams(self, strings: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for string in strings:
            sorted_string = ''.join(sorted(string))
            groups[sorted_string].append(string)
        
        return list(groups.values())