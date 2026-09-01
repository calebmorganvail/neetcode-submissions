class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """Determines weather or not there are two values in the list 
        that sum to the target value.

        Args:
            numbers:
                The list of numbers to look through. 
            target:
                The target value to sum too.
        
        Returns:
            The indices - 1-indexed - of two numbers, such that they add up to a given 
            target number and index1 < index2.

        Time Complexity:
            O(n), where n is the length of the input list.

        Space Complexity:
            O(n), where n is the length of the input list - becuase we create a set
            that, in the worst case will be the length of the input list.
        """

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

             