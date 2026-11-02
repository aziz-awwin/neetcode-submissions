class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        start : int
        end : int 
        start = 0
        end = 0
        len_ = 1
        duplicates = 0
        value = 0

        nums.sort()
        if len(nums) == 0 :
                len_ = 0
        print("nums", nums)
        for i in range(1,len(nums)) :
                if nums[i] == nums[i-1]+1 :
                        end = i
                
                        value = end - start + 1  -  duplicates 

                elif    nums[i] == nums[i-1] :
                        duplicates += 1
                
                        continue

                else :  
                        start = i 
                        end = i 
                        duplicates = 0
                        len_ = max(value,len_)

        len_ = max(value,len_)
        print(len_)

        return len_        




        