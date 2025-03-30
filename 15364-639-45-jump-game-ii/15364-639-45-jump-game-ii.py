class Solution:
    def jump(self, nums: List[int]) -> int:
        # We start with 0 because we haven't made any jumps yet.
        jumps = 0
        # current range we can reach with the current number of jumps
        current_end = 0
        # the farthest we can reach with the next jump
        farthest = 0

        # We only need to iterate through the array until the second-to-last element
        # because once we reach or pass the last element, we're done.
        for i in range(len(nums) - 1):
            # Update the farthest we can reach from the current index
            farthest = max(farthest, i + nums[i])

            # If we've reached the end of the current jump range,
            # it's time to make a jump.
            if i == current_end:
                jumps += 1
                current_end = farthest
        return jumps