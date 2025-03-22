# import heapq

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # we can't use nums1 = nums1[:m] + nums2, because it assigns a new array to nums1, didn't update the original one
        # we can't use nums1.sort(), because .sort() sort the list in place, and don't return anything
        # sorted() return a new sorted list and doesn't modify the orignal list
        nums1[:] = sorted(nums1[:m] + nums2)