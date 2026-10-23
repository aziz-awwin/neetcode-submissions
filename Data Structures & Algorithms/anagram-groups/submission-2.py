class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        o = []
        hashs = {}

        for str_ in strs :
            hash_key = self.buildarray(str_)
            if hash_key in hashs :
               hashs[hash_key].append(str_)          
            else :
               hashs[hash_key] = [str_]   
        for hash_key in hashs :
            o.append(hashs[hash_key])  
        return o        

    def buildarray(self, str_ : str) -> tuple[int] :
        a_caracter = [0]*26
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        for ctr in str_ : 
            index = alphabets.find(ctr)
            a_caracter[index] += 1
        return tuple(a_caracter)     





    

    
        