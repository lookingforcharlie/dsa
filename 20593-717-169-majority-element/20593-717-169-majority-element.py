class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Create a dict to store the num and how many num appears as key and value
        dict = {}
        # Take advantage of list.setdefault()
        for num in nums:
            # Set the key if the key doesn't exist
            # Nice shortcut to ensure that a key exists
            dict.setdefault(num, 0)
            dict[num] += 1
            if dict[num] >= len(nums)/2:
                return num