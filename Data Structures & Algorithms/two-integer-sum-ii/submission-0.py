class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        
        
        
        Returns:
            The indices - 1-indexed - of two numbers, such that they add up to a given 
            target number and index1 < index2.
        
        
        
        """

        # ex: [1,2,3,4], target = 3

        output = []

        seen = defaultdict(int)

     
        for i, number in enumerate(numbers):
            rem = target - number
            
            if rem in seen:
                output.append(seen[rem] + 1)
                output.append(i + 1)
                break
            seen[number] = i

        return output

             