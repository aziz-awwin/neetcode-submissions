class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # this version use the division operation
        o = []
        zeroes_index = []
        pro = 1
        for i in range(len(nums)) :
                if nums[i] != 0 :
                   pro = pro*nums[i]
                else :
                   zeroes_index.append(i)

        if len(zeroes_index) == 0 :
                for i in range(len(nums)) :
                        o.append(int(pro/nums[i]))
        elif len(zeroes_index) > 1 :  
                o = [0]*len(nums)
        else :
                o = [0]*len(nums)
                o[zeroes_index[0]] = pro
        return o



        