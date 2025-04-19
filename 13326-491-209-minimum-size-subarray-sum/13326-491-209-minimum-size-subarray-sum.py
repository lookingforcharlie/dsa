class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # using two pointers and sliding window
        n = len(nums)
        # Initialize the minimal 
        min_length = n + 1
        # the moving pointer of the beginning of the sliding window
        left = 0
        current_sum = 0
         
        # for idx, num in enumerate(nums):
        # right is the end pointer of the sliding window
        # right and left start at the same point
        for right in range(n): 
            current_sum += nums[right]

            while current_sum >= target: 
                min_length = min(min_length, right - left + 1)
                # tricky part: left pointer will be incremented, previous correspondent value at left pointer need to be deleted
                current_sum -= nums[left]
                left += 1

        return 0 if min_length == n + 1 else min_length
            
    