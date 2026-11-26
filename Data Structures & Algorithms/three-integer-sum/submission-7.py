'''
final answer :

Idea:
Sort the list, then for each number, find two other numbers
that add up to its opposite (using two pointers, left and right).

Tips I learned:

1. Start left at i + 1
   Only look at numbers after i. Each triplet is then found once.

2. Skip repeated numbers
   Because the list is sorted, equal numbers sit next to each other.
   - If nums[i] equals nums[i - 1], skip it.
   - After a match, skip a repeated left or right value.
   This is faster than searching the answer list.

3. Always move both pointers after a match
   Keep left += 1 and right -= 1 outside the duplicate check.
   If they are inside, the loop can get stuck forever.

4. Optional speedups
   - Stop when nums[i] > 0 (three positive numbers can't add to 0).
   - Use range(n - 2), since i needs two numbers after it.

Time: O(n²)
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        o = []
        # [-4, -1, -1, 0, 1, 2]

        for i in range(n) :
            if (i != 0 and  nums[i] == nums[i-1]) :
                continue
            if nums[i] > 0:
                break    
            target = -nums[i]
            right = n - 1
            left = i + 1

            while(right > left) :

                if (nums[right] + nums[left] > target) :
                    
                    right -= 1

                elif (nums[right] + nums[left] < target) :
                    
                    left += 1 

                else :
                    if (
                        (left - 1 == i or nums[left] != nums[left - 1])
                        and (right + 1 == n or nums[right] != nums[right + 1])
                    ):
                        o.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1       

        return o            

                    

                  





        