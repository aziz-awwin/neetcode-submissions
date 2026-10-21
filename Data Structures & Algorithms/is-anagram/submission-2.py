class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t_1 = "".join(sorted(s))
        t_2 = "".join(sorted(t))
        if t_1 == t_2 :
            return True
        else :
            return False    
            


        