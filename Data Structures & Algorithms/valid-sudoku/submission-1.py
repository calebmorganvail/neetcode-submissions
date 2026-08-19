class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        


        # First Box 
        box_idxs = [(0,0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
        # First Row
        row_idxs = [(0,0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8)]
        # First Col
        col_idxs = [(0,0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0)]

        box_check = set()
        row_check = set()
        col_check = set()
        
        for idx in box_idxs:
            print(board[idx[0]][idx[1]])
            
            num = board[idx[0]][idx[1]]
            if num != ".":
                if int(num) > 9 or int(num) < 1:
                    return False
            if num != "." and num in box_check:
               return False
            box_check.add(num)
        
        for idx in row_idxs:
            print(board[idx[0]][idx[1]])
            
            num = board[idx[0]][idx[1]]
            if num != ".":
                if int(num) > 9 or int(num) < 1:
                    return False
            if num != "." and num in row_check:
               return False
            row_check.add(num)
        
        for idx in col_idxs:
            print(board[idx[0]][idx[1]])
            
            num = board[idx[0]][idx[1]]
            if num != ".":
                if int(num) > 9 or int(num) < 1:
                    return False
            if num != "." and num in col_check:
               return False
            col_check.add(num)


        # 2 Box 
        box_idxs = [(0,3), (0, 4), (0, 5), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5)]
        # 2 Row
        row_idxs = [(1,0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8)]
        # 2 Col
        col_idxs = [(0,1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1)]

        box_check = set()
        row_check = set()
        col_check = set()
        
        for idx in box_idxs:
            print(board[idx[0]][idx[1]])
            
            num = board[idx[0]][idx[1]]
            if num != ".":
                if int(num) > 9 or int(num) < 1:
                    return False
            if num != "." and num in box_check:
               return False
            box_check.add(num)
        
        for idx in row_idxs:
            print(board[idx[0]][idx[1]])
            
            num = board[idx[0]][idx[1]]
            if num != ".":
                if int(num) > 9 or int(num) < 1:
                    return False
            if num != "." and num in row_check:
               return False
            row_check.add(num)
        
        for idx in col_idxs:
            print(board[idx[0]][idx[1]])
            
            num = board[idx[0]][idx[1]]
            if num != ".":
                if int(num) > 9 or int(num) < 1:
                    return False
            if num != "." and num in col_check:
               return False
            col_check.add(num)

        
        # 3 Box 
        box_idxs = [(0,6), (0, 7), (0, 8), (1, 6), (1, 7), (1, 8), (2, 6), (2, 7), (2, 8)]
        # 3 Row
        row_idxs = [(2,0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8)]
        # 3 Col
        col_idxs = [(0,2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2)]

        box_check = set()
        row_check = set()
        col_check = set()
        
        for idx in box_idxs:
            # print(board[idx[0]][idx[1]])
            
            num = board[idx[0]][idx[1]]
            if num != ".":
                if int(num) > 9 or int(num) < 1:
                    return False
            if num != "." and num in box_check:
               return False
            box_check.add(num)
        
        for idx in row_idxs:
            print(board[idx[0]][idx[1]])
            
            num = board[idx[0]][idx[1]]
            if num != ".":
                if int(num) > 9 or int(num) < 1:
                    return False
            if num != "." and num in row_check:
               return False
            row_check.add(num)
        
        for idx in col_idxs:
            print(board[idx[0]][idx[1]])
            
            num = board[idx[0]][idx[1]]
            if num != ".":
                if int(num) > 9 or int(num) < 1:
                    return False
            if num != "." and num in col_check:
               return False
            col_check.add(num)


        # 4 Box 
        box_idxs = [(3,0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2)]
        # 4 Row
        row_idxs = [(3,0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8)]
        # 4 Col
        col_idxs = [(0,3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (8, 3)]

        box_check = set()
        row_check = set()
        col_check = set()
        
        for idx in box_idxs:
            print(board[idx[0]][idx[1]])
            
            num = board[idx[0]][idx[1]]
            if num != ".":
                if int(num) > 9 or int(num) < 1:
                    return False
            if num != "." and num in box_check:
               return False
            box_check.add(num)
        
        for idx in row_idxs:
            print(board[idx[0]][idx[1]])
            
            num = board[idx[0]][idx[1]]
            if num != ".":
                if int(num) > 9 or int(num) < 1:
                    return False
            if num != "." and num in row_check:
               return False
            row_check.add(num)
        
        for idx in col_idxs:
            print(board[idx[0]][idx[1]])
            
            num = board[idx[0]][idx[1]]
            if num != ".":
                if int(num) > 9 or int(num) < 1:
                    return False
            if num != "." and num in col_check:
               return False
            col_check.add(num)

        
        # 5 Box 
        box_idxs = [(3,3), (3, 4), (3, 5), (4, 3), (4, 4), (4, 5), (5, 3), (5, 4), (5, 5)]
        # 5 Row
        row_idxs = [(4,0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8)]
        # 5 Col
        col_idxs = [(0,4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4), (8, 4)]

        box_check = set()
        row_check = set()
        col_check = set()
        
        for idx in box_idxs:
            print(board[idx[0]][idx[1]])
            
            num = board[idx[0]][idx[1]]
            if num != ".":
                if int(num) > 9 or int(num) < 1:
                    return False
            if num != "." and num in box_check:
               return False
            box_check.add(num)
        
        for idx in row_idxs:
            print(board[idx[0]][idx[1]])
            
            num = board[idx[0]][idx[1]]
            if num != ".":
                if int(num) > 9 or int(num) < 1:
                    return False
            if num != "." and num in row_check:
               return False
            row_check.add(num)
        
        for idx in col_idxs:
            print(board[idx[0]][idx[1]])
            
            num = board[idx[0]][idx[1]]
            if num != ".":
                if int(num) > 9 or int(num) < 1:
                    return False
            if num != "." and num in col_check:
               return False
            col_check.add(num)

        # 6 Box 
        box_idxs = [(3,6), (3, 7), (3, 8), (4, 6), (4, 7), (4, 8), (5, 6), (5, 7), (5, 8)]
        # 6 Row
        row_idxs = [(5,0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8)]
        # 6 Col
        col_idxs = [(0,5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (8, 5)]

        box_check = set()
        row_check = set()
        col_check = set()
        
        for idx in box_idxs:
            print(board[idx[0]][idx[1]])
            
            num = board[idx[0]][idx[1]]
            if num != ".":
                if int(num) > 9 or int(num) < 1:
                    return False
            if num != "." and num in box_check:
               return False
            box_check.add(num)
        
        for idx in row_idxs:
            print(board[idx[0]][idx[1]])
            
            num = board[idx[0]][idx[1]]
            if num != ".":
                if int(num) > 9 or int(num) < 1:
                    return False
            if num != "." and num in row_check:
               return False
            row_check.add(num)
        
        for idx in col_idxs:
            print(board[idx[0]][idx[1]])
            
            num = board[idx[0]][idx[1]]
            if num != ".":
                if int(num) > 9 or int(num) < 1:
                    return False
            if num != "." and num in col_check:
               return False
            col_check.add(num)

        # 7 Box 
        box_idxs = [(6,0), (6, 1), (6, 2), (7, 0), (7, 1), (7, 2), (8, 0), (8, 1), (8, 2)]
        # 7 Row
        row_idxs = [(6,0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8)]
        # 7 Col
        col_idxs = [(0,6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6), (8, 6)]

        box_check = set()
        row_check = set()
        col_check = set()
        
        for idx in box_idxs:
            print(board[idx[0]][idx[1]])
            
            num = board[idx[0]][idx[1]]
            if num != ".":
                if int(num) > 9 or int(num) < 1:
                    return False
            if num != "." and num in box_check:
               return False
            box_check.add(num)
        
        for idx in row_idxs:
            print(board[idx[0]][idx[1]])
            
            num = board[idx[0]][idx[1]]
            if num != ".":
                if int(num) > 9 or int(num) < 1:
                    return False
            if num != "." and num in row_check:
               return False
            row_check.add(num)
        
        for idx in col_idxs:
            print(board[idx[0]][idx[1]])
            
            num = board[idx[0]][idx[1]]
            if num != ".":
                if int(num) > 9 or int(num) < 1:
                    return False
            if num != "." and num in col_check:
               return False
            col_check.add(num)

        # 8 Box 
        box_idxs = [(6,3), (6, 4), (6, 5), (7, 3), (7, 4), (7, 5), (8, 3), (8, 4), (8, 5)]
        # 8 Row
        row_idxs = [(7,0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8)]
        # 8 Col
        col_idxs = [(0,7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (8, 7)]

        box_check = set()
        row_check = set()
        col_check = set()
        
        for idx in box_idxs:
            print(board[idx[0]][idx[1]])
            
            num = board[idx[0]][idx[1]]
            if num != ".":
                if int(num) > 9 or int(num) < 1:
                    return False
            if num != "." and num in box_check:
               return False
            box_check.add(num)
        
        for idx in row_idxs:
            print(board[idx[0]][idx[1]])
            
            num = board[idx[0]][idx[1]]
            if num != ".":
                if int(num) > 9 or int(num) < 1:
                    return False
            if num != "." and num in row_check:
               return False
            row_check.add(num)
        
        for idx in col_idxs:
            print(board[idx[0]][idx[1]])
            
            num = board[idx[0]][idx[1]]
            if num != ".":
                if int(num) > 9 or int(num) < 1:
                    return False
            if num != "." and num in col_check:
               return False
            col_check.add(num)

        # 9 Box 
        box_idxs = [(6,6), (6, 7), (6, 8), (7, 6), (7, 7), (7, 8), (8, 6), (8, 7), (8, 8)]
        # 9 Row
        row_idxs = [(8,0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8)]
        # 9 Col
        col_idxs = [(0,8), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8)]

        box_check = set()
        row_check = set()
        col_check = set()
        
        for idx in box_idxs:
            print(board[idx[0]][idx[1]])
            
            num = board[idx[0]][idx[1]]
            if num != ".":
                if int(num) > 9 or int(num) < 1:
                    return False
            if num != "." and num in box_check:
               return False
            box_check.add(num)
        
        for idx in row_idxs:
            print(board[idx[0]][idx[1]])
            
            num = board[idx[0]][idx[1]]
            if num != ".":
                if int(num) > 9 or int(num) < 1:
                    return False
            if num != "." and num in row_check:
               return False
            row_check.add(num)
        
        for idx in col_idxs:
            print(board[idx[0]][idx[1]])
            
            num = board[idx[0]][idx[1]]
            if num != ".":
                if int(num) > 9 or int(num) < 1:
                    return False
            if num != "." and num in col_check:
               return False
            col_check.add(num)
        return True

        
