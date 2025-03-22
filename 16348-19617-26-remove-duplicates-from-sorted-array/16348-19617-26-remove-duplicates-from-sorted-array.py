class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # we are using two pointers, one for the place to insertion, one loop through the array
        p = 1 # pointer starts from the index 1, because index 0 always stay there
        for index, value in enumerate(nums):
            # action starts from index 1, no action for index 0 whatsoever
            if index > 0 and index <= len(nums):
                # if value is different from the value on previous index, means it's first time we see this value, and we are going to insert it
                if value != nums[index - 1]:
                    nums[p] = value
                    p += 1
        return p