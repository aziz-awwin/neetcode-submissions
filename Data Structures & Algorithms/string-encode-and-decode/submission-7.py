class Solution:
    # the idea is to choose non-ascii delemiter

    def encode(self, strs: List[str]) -> str:
        o_s = ""
        for i in range(len(strs)) :
                if i == 0 :
                    o_s = str(len(strs[i]))+"#"+strs[i]
                else :
                    o_s = o_s + str(len(strs[i]))+"#"+strs[i] 
        return o_s                 

            
    def decode(self, o_s: str) -> List[str]:
        o = []
        end = 0
        i = 0
        while i < len(o_s) :
            i += 1    
            print("start", i)    
            if o_s[i] == "#" :
                print(i)
                walking = int(o_s[end:i])
                begin = i + 1
                end = begin + walking
                o.append(o_s[begin:end])
                i = end
                print("end", i)

        return o           
