class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
#         make a set to make sure it is unique 
#         loop the list 
# for 100, if there is 100 - 1, pass 
# no 100 -1, start counting the squence ( squence += 1 ), looking for 100 + 1
# if 100 + 1 exist, squence += 1 

        numsSet = set(nums)
        highest_count = 0
        for num in nums:
            
            sequence_count = 0 
            if (num - 1) not in numsSet:
                sequence_count += 1
                while num + 1 in numsSet: 
                    sequence_count += 1
                    num = num + 1 
                if sequence_count > highest_count: 
                    highest_count = sequence_count
        return highest_count
            