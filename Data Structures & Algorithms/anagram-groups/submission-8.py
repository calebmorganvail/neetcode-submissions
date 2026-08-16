class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''Groups the words in the list by anagrams.
        
        Args: 
            strs: The list of strings passed into the function.

        Returns:
            A list of lists where each inner list is a group of anagrams.
        
        Time Complexity:
            O(nklog(k)): Where n is the number of strings in the strs list, and k is the number of
                         characters in a given string.

        Space Complexity:
            O(nk): Where n is the number of strings in the strs list, and k is the number of
                   characters in a given string.
        '''

        _dict: dict[str, list[str]] = defaultdict(list)

        # O(n) where n is a string in strs.
        for string in strs:
            # O(klog(k)) where k is the len of the largest string.
            _dict[''.join(sorted(string))].append(string)
        
        # O(n) where n is a string in strs.
        return list(_dict.values())