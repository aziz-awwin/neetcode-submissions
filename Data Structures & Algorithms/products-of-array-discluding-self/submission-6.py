class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        o = []
        array_1 = []
        array_2 = []
        n = len(nums)
        array_1.append(nums[0]) 
        array_2.append(nums[n - 1]) 
        new_size = n - 1

        for i in range(1 , n - 1) :
                array_1.append(array_1[i - 1]*nums[i])
                array_2.append(array_2[i - 1]*nums[n - i - 1])  

        for i in range(0 , n) :
                if i == 0 :
                    o.append(array_2[new_size - 1])

                elif i == n-1 :
                    o.append(array_1[new_size - 1])

                else :

                    o.append(array_1[i - 1] * array_2[new_size - (i+1)])
        return o    











        