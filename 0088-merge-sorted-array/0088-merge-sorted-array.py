class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ptr1 = m - 1  # Pointer for nums1
        ptr2 = n - 1  # Pointer for nums2
        merged_ptr = m + n - 1  # Pointer for the merged array

        while ptr1 >= 0 and ptr2 >= 0:
            if nums1[ptr1] > nums2[ptr2]:
                nums1[merged_ptr] = nums1[ptr1]
                ptr1 -= 1
            else:
                nums1[merged_ptr] = nums2[ptr2]
                ptr2 -= 1
            merged_ptr -= 1

        # If there are remaining elements in nums2, copy them to nums1
        nums1[:ptr2 + 1] = nums2[:ptr2 + 1]