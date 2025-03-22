class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums[:] = [item for item in nums if item != val]
        k = len(nums)
        return k