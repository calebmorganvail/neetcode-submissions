class Solution:
    def groupAnagrams(self, strings: List[str]) -> List[List[str]]:
        result = defaultdict(list) # {'key': [...]}

        for string in strings:
            orderd = ''.join(sorted(string)) # "hat" -> ['a', 'h', 't'] -> "aht"
            result[orderd].append(string)
        
        return list(result.values())

