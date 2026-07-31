class Solution:
    def groupAnagrams(self, words: List[str]) -> List[List[str]]:
        # The key insight to this problem is the fact that we want to sort the
        # given list of words based on if they share the exacy same set of characters. 
        # SO, the idea is to 'create' a key by sorting the char in a given word.

        # Python normally requires that a dict needs to be checked before adding a new key if the
        # key exists in the dict already. To simplify we can use a 'defaultdict()' and pass
        # 'list' -> defaultdict(list), so the check is done automatically, and if the key
        # does not exist then it will get added and a list created. ex:

        # result = defaultdict(list) -> " { "aet": [...], ... } 

        result = defaultdict(list)
        for word in words:

            # This preforms two operations. sorted(word) returns an array of the 
            # sorted words: ['a','e','t'], so they need to be joined together.
            sorted_word = ''.join(sorted(word))
            
            # Add the word to the dictionary
            result[sorted_word].append(word)
    

        # Return only the list of the values of the dict
        return list(result.values())