class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        running_total = 1 
        prefix = []
        suffix = []
        o = []
        prefix.append(running_total)
        for i in range(1,len(nums)) :
                running_total = running_total*nums[i-1]
                prefix.append(running_total)

        running_total = 1
        suffix.append(running_total)


        for i in range(len(nums) -  2  ,-1 ,-1 ) :
                running_total = running_total*nums[i + 1]
                suffix.append(running_total) 

        suffix.reverse()   

        for i in range(0,len(nums)) :
                o.append(suffix[i]*prefix[i])

        return o        

      



           











        