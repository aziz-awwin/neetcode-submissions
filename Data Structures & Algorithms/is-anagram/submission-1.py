class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set_0 = set(s)
        set_1 = set(t)
        if (set_0 == set_1) :
            for c in set_0 :
                if s.count(c) != t.count(c) :
                    return False
            return True
        else :
            return False            


        