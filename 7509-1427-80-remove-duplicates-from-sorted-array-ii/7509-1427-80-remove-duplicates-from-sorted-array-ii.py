class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        # allow two duplicates, first 2 items will never be changed
        p = 2

        # Handle action starts from index 2
        for i in range(2, len(nums)):
            # must compare with nums[p-2], not nums[i-2]
            if nums[i] != nums[p - 2]:
                nums[p] = nums[i]
                p += 1
            
        return p