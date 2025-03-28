class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        # maxReach is the best (largest) index you can get to from any of the positions you’ve encountered up to that point
        maxReach = 0

        # don't need to compute a jump from the last index
        # you can reach the last index, not to jump from it
        for i in range(len(nums) -1):
            # when i is greater than maxReach, it means it won't be able to jump to this index
            if i > maxReach: 
                return False

            if i + nums[i] > maxReach:
                maxReach = i + nums[i]
            
            if maxReach >= len(nums) - 1:
                return True
        
        # handle situation as [1,0,0]
        # Reach index 1, but can't reach index 2
        return False

