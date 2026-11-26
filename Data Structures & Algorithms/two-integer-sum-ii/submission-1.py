'''
We keep two pointers, one at the start and the other at the end of the array. If the sum of the numbers at the two pointers is greater than the target, decrement the right pointer, else increment the left pointer. Repeat this process until you find a valid pair.

the issues you did :
1/  - pay attention instead of right > left you did the inverse
2/  - instead of increment you deincrment
3/  - right =- 1 assigns -1; decrementing is right -= 1. Likewise, left =+ 1 assigns 1; incrementing is left += 1.
''' 

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        right = n - 1
        left = 0 

        while (right > left ) :

            if (numbers[right] + numbers[left] < target ) :
                left = left + 1

            elif  (numbers[right] + numbers[left] > target ) : 
                right = right - 1
            
            else :
                break    
        print("right", right)
        print("left", left)
        return [left + 1 , right + 1]        



        