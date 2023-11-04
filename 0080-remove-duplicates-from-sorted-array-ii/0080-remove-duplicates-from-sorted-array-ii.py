class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        repetition = False # number of repetition
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
                repetition = False # when the value at r doesn't equal to the value at l, means find a new value, means another round of calculating the number of repetition starts
            elif nums[r] == nums[r - 1] and repetition == False:
                nums[l] = nums[r]
                l += 1
                repetition = True 
        return l
    