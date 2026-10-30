class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        running_total = 1 
        prefix = []
        suffix = []
        o = []
        prefix.append(running_total)
        for i in range(1,n) :
                running_total = running_total*nums[i-1]
                prefix.append(running_total)

        running_total = 1
        o.append(prefix[n - 1])



        for i in range(n -  2  ,-1 ,-1 ) :
                running_total = running_total * nums[i + 1]
                o.append(prefix[i]*running_total)


        o.reverse()   

        return o
       

      



           











        