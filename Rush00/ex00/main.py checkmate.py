def is_king_in_check(board):
    size = len(board)
    directions = {
        'R': [(1, 0), (-1, 0), (0, 1), (0, -1)],
        'B': [(1, 1), (1, -1), (-1, 1), (-1, -1)],
        'Q': [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    }

    def find_king():
        for i in range(size):
            for j in range(size):
                if board[i][j] == 'K':
                    return i, j
        return None

    king_pos = find_king()
    if not king_pos:
        return  # No King found, undefined behavior

    king_x, king_y = king_pos

    # Check for Pawn threats (assuming enemy pawns move from top to bottom)
    for dx, dy in [(-1, -1), (-1, 1)]:
        x, y = king_x + dx, king_y + dy
        if 0 <= x < size and 0 <= y < size and board[x][y] == 'P':
            print("Success")
            return

    # Check for Rook, Bishop, Queen
    for piece, dirs in directions.items():
        for dx, dy in dirs:
            x, y = king_x + dx, king_y + dy
            while 0 <= x < size and 0 <= y < size:
                if board[x][y] == '.':
                    x += dx
                    y += dy
                    continue
                if board[x][y] == piece or (piece == 'Q' and board[x][y] == 'Q'):
                    print("Success")
                    return
                else:
                    break

    print("Fail")
