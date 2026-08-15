class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for row in range (9):
            for col in range (9):
                cell = board[row][col]
                if cell == '.':
                    continue
                if cell in rows[row]:
                    return False
                else:
                    rows[row].add(cell)
                if cell in cols[col]:
                    return False
                else:
                    cols[col].add(cell)

                box_index = row//3 * 3 + col//3

                if cell in boxes[box_index]:
                    return False
                else:
                    boxes[box_index].add(cell)
                
        return True
                
        
        
        