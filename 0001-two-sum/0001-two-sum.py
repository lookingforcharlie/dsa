class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_and_index = {}
        for index, num in enumerate(nums):
            num_for_search = target - num
            if num_for_search in num_and_index: 
                return [index, num_and_index[num_for_search]]
            num_and_index[num] = index