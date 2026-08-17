class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Determines the k most frequent elements in nums.

        Args:
            nums: A list of integers.
            k: The number of most frequent elements to return.

        Returns:
            A list containing the k most frequent integers.

        Time Complexity:
            O(n log n), where n is the number of elements in nums.

        Space Complexity:
            O(n), where n is the number of elements in nums.
        """

        freq = {}
        res = []

        # Count the frequency of each number.
        # O(n) time, where n is the number of elements in nums.
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Sort the numbers by frequency from highest to lowest.
        # O(n log n) time in the worst case.
        sorted_freq = sorted(
            freq.items(),
            key=lambda item: item[1],
            reverse=True
        )

        # Take the first k numbers with the highest frequencies.
        # O(k) time.
        for key, value in sorted_freq:
            if k == 0:
                break

            res.append(key)
            k -= 1

        return res