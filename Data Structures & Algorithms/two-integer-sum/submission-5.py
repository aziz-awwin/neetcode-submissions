class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        o = []
        hashmap = {}
        for index,value in enumerate(nums) :
            hashmap[value] = index

        for index , value in enumerate(nums) :
            if target - value in hashmap and index != hashmap[target - value] :
                o.append(index)     
                o.append(hashmap[target - value])
                break
        return o       




        