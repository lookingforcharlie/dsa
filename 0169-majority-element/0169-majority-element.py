class Solution:
    def majorityElement(self, nums: List[int]) -> int:
         # Using Boyer-Moore Voting Algorithm 
        # The array has the majority of element which is greater that n/2 is the prerequisite of Boyer-Moore
        candidate = 0
        count = 0
        for value in nums:
            if count == 0: 
                candidate = value
                count += 1
            elif candidate == value: 
                count += 1
            elif value != candidate: 
                count -= 1 
        return candidate
            
        
        
        
        
        
        
        
        
   
        
        
# n = len(nums)
# return value will be the integer that appears more than n/2  

# Could you solve the problem in linear time and in O(1) space?
# meaning loop through the array
# don't create another array

# loop through the array, 
# count the appearance time for each value
# if the value > n/2 
# return the value 


# my code which doesn't solved in linear time
#     n = len(nums)
#         for value in nums: 
#             if nums.count(value) > n/2: 
#                 return value
        