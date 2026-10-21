class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        o = []
        hashs = {}
        for str_  in strs :
            if self.labeling(str_) in hashs :
                hashs[self.labeling(str_)].append(str_)
            else :
                hashs[self.labeling(str_)] = [str_]
        for k  in  hashs :
            o.append(hashs[k])
        return o          

    def labeling(self, str_: str) -> str:
        return "".join(sorted(str_))     

    
        