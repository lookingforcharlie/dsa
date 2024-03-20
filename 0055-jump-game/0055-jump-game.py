class Solution:
    def canJump(self, nums: List[int]) -> bool:
        index_of_goal  = len(nums) - 1 
        if any(item == 0 for item in nums):
            print("The list contains 0.")
            for i in range(index_of_goal - 1, -1, -1):
                if nums[i] >= index_of_goal - i:
                    index_of_goal = i
            if index_of_goal == 0: 
                return True
            elif index_of_goal > 0: 
                return False
        else:
            return True
        

    
# if list doesn't have 0, reture True 