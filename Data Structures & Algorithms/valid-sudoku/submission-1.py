class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9

        for i in range(9):
            for j in range(9):

                if board[i][j] == ".":
                    continue

                val = int(board[i][j]) - 1
                box_num = (i // 3) + (3 * (j // 3))

                if rows[i] & (1 << val):
                    return False
                if cols[j] & (1 << val):
                    return False
                if boxes[box_num] & (1 << val):
                    return False
                
                rows[i] |= (1 << val)
                cols[j] |= (1 << val)
                boxes[box_num] |= (1 << val)
        
        return True


        