# Solution 

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c] == ".":
                    continue

                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r // 3, c // 3)]):
                    return False

                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
                print(rows)

        return True

# Time Complexity of Solution - O(n^2)
# Space Complexity of Solution - O(n^2)
