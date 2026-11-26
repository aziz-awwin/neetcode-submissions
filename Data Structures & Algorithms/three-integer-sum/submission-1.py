'''
we have the solution just the same idea as before and loop over the array 
the O is O(n2)
doing this part like to avoid duplication
                    tmp = [nums[right],nums[left], nums[i]]
                    tmp.sort()
                    if tmp not in o :
                        o.append(tmp) 
                    left += 1
                    right -= 1
i m not sure if there is another way
to skip the same number as we are in
nums[0] + nums[1] + nums[2] =  0 ==> 
nums[0] + nums[1]  =  -nums[2]
--------------------------
the same solution but a little takes  time
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        o = []
        # [-4, -1, -1, 0, 1, 2]

        for i in range(n) :
            target = -nums[i]
            right = n - 1
            left = 0

            while(right > left) :
                if (right == i) :
                    right -= 1
                    continue


                if (left == i) :
                    left += 1
                    continue


                if (nums[right] + nums[left] > target) :
                    
                    right -= 1

                elif (nums[right] + nums[left] < target) :
                    
                    left += 1 

                else :
                    tmp = [nums[right],nums[left], nums[i]]
                    tmp.sort()
                    if tmp not in o :
                        o.append(tmp) 
                    left += 1
                    right -= 1

        return o            

                    

                  





        