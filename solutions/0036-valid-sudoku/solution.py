class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(0,9):
            for c in range(0,9):
                val = board[r][c]

                if board[r][c] == '.':
                    continue
                
                b = (r // 3) * 3 + (c // 3)

                if val in rows[r]:
                    return False
                if val in columns[c]:
                    return False
                if val in boxes[b]:
                    return False

                rows[r].add(val)
                columns[c].add(val)
                boxes[b].add(val)

        return True
