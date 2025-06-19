def is_in_check(board):
    size = len(board)

    king_pos = None
    for i in range(size):
        for j in range(size):
            if board[i][j] == 'K':
                king_pos = (i, j)
                break
        if king_pos:
            break

    if not king_pos:
        print("Fail") 
        return

    ki, kj = king_pos

    directions = {
        'rook': [(-1,0), (1,0), (0,-1), (0,1)],
        'bishop': [(-1,-1), (-1,1), (1,-1), (1,1)],
        'queen': [(-1,0), (1,0), (0,-1), (0,1), (-1,-1), (-1,1), (1,-1), (1,1)]
    }

    for dx, dy in [(-1, -1), (-1, 1)]:  # Pawn เดินทแยงลง
        ni, nj = ki + dx, kj + dy
        if 0 <= ni < size and 0 <= nj < size and board[ni][nj] == 'P':
            print("Success")
            return

    for dx, dy in directions['rook']:
        x, y = ki + dx, kj + dy
        while 0 <= x < size and 0 <= y < size:
            if board[x][y] != '.':
                if board[x][y] in ('R', 'Q'):
                    print("Success")
                    return
                break
            x += dx
            y += dy

    for dx, dy in directions['bishop']:
        x, y = ki + dx, kj + dy
        while 0 <= x < size and 0 <= y < size:
            if board[x][y] != '.':
                if board[x][y] in ('B', 'Q'):
                    print("Success")
                    return
                break
            x += dx
            y += dy

    print("Fail")
