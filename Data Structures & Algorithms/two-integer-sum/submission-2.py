class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        o = []
        hashmap = {}
        for index in range(len(nums)) :
            hashmap[target - nums[index]] = index

        for index in range(len(nums)) :
            if nums[index] in hashmap and index != hashmap[nums[index]] :
                o.append(index)     
                o.append(hashmap[nums[index]])
                break
        return o        




        