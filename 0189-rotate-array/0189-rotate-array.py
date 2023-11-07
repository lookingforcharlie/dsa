class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # prevent list index (k) out of range
        k = k % len(nums)
        
        last_index = len(nums) - 1 
        nums.reverse()
        def helper(nums, start, end): 
            while start <= end: 
                temp_start = nums[start]
                nums[start] = nums[end]
                nums[end] = temp_start
                start += 1
                end -= 1
        
        # reverse range: 0, (k -1) 
        helper(nums, 0, k-1)
        
        # reverse range: k, last_index 
        helper(nums, k, last_index)
        
        
        
        
        
        
        
        
# My initial way, use a for loop inside a while loop
#         while k != 0: 
#             index_last_item = len(nums) - 1 
#             first = nums[index_last_item]
#             # Use a for loop to move items in list one step ahead except the first item 
#             for i in range(index_last_item, 0, -1): 
#                 nums[i] = nums[i - 1]
#             nums[0] = first

#             k -= 1 
    
        
        
