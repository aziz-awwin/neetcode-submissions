"""
i think i didn't use 2 pointers it's O(n) at least
i check if the char is alpha before create the new valid string
then delete spaces
then compare the inverse with string origin
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalpha() or char.isdigit())
        s_without_space = s.replace(" ","") 
        if s_without_space[::-1].lower() == s_without_space.lower() :
            return True
        else :
            return False    

        