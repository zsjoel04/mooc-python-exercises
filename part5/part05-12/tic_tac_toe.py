def play_turn(game_board: list, x: int, y: int, piece: str):
    if x > 2 or y > 2:
        return False
    if x < 0 or y < 0:
        return False
    row = game_board[y]
    if row[x] == "O" or row[x] == "X":
        return False
    row[x] = piece
    if piece == "O" or piece == "X":
        return True
    





if __name__ == "__main__":
    game_board = [['', 'X', ''], ['X', 'O', ''], ['', '', '']]
    print(play_turn(game_board,  3, 0, "X"))
    print(game_board)