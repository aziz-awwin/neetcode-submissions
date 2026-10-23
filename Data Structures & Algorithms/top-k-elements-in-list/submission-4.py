class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       
        o = []
        hashs = {}
        for num in nums : 
                if num in hashs :
                   hashs[num] += 1
                else :
                   hashs[num] = 1

        sorted_d = dict(sorted(hashs.items(), key=lambda item: item[1], reverse=True))  


        for key in sorted_d :
                if ( k == 0) :
                   break 
                o.append(key)
                k -= 1
        return o        





        