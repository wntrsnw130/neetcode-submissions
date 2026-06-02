class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        sqrs = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                current_val = board[r][c]

                if (current_val in rows[r] or
                    current_val in cols[c] or
                    current_val in sqrs[(r // 3, c // 3)]):
                    return False
                
                rows[r].add(current_val)
                cols[c].add(current_val)
                sqrs[(r // 3, c // 3)].add(current_val)
            
        return True
