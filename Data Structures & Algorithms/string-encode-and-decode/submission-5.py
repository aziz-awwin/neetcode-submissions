class Solution:
    # the idea is to choose non-ascii delemiter
    separator = "-->"
    def encode(self, strs: List[str]) -> str:
        # separator = "-->"
        if strs == [] :
            return self.separator + self.separator
        elif strs == [""] :  
            return ""
        else :
            return self.separator.join(strs)
        

    def decode(self, s: str) -> List[str]:
        # separator = "-->"
        if s == "" :
            return [""]
        elif s == self.separator + self.separator :
            return []
        
        else :  
            return s.split(self.separator)
