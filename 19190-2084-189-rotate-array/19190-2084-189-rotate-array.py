class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # method one: cannot pass the test which has astronomical numbers
        # while k > 0:
        #     item_for_move = nums.pop()
        #     nums[:] = [item_for_move] + [value for value in nums]
        #     k -= 1

        # method two: 
        # Technically k can be any number which is bigger than the length of the nums, meaning it's repeating the rotation
        k = k % len(nums)

        nums.reverse() 
        part_one = nums[:k]
        part_two = nums[k:]
        part_one.reverse()
        part_two.reverse()
        nums[:] = part_one + part_two