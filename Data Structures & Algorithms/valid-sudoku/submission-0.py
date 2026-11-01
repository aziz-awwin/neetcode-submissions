class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        ## first check 
        for l in board :
            if self.checklist( l) == False :
                return False

        ## check the boxes
        positions = [
            (0, 0), (0, 3), (0, 6),
            (3, 0), (3, 3), (3, 6),
            (6, 0), (6, 3), (6, 6)
        ]
        
        l_p = []
        for i,j in positions :
                for k in range(i , i + 3):
                    for p in range (j  , j + 3) :
                        l_p.append(board[k][p])
                
                if self.checklist(l_p) == False :
                    return False 
                l_p = []    



        ## check the columns 
        for l in [ list(l) for l in zip(*board)] :
             if self.checklist( l) == False :
                return False

        return True        
            

    def checklist(self , board_list) :
        if (len(set(board_list)) < (9 - board_list.count(".")) + 1) and set(board_list) != {"1","2","3","4","5","6","7","8","9"} :
              return False 

        return True  

                    

        

        