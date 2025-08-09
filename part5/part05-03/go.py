def who_won(game_board: list):      # [[a], [b], [c]]
    player_1 = 0
    result_1 = 1
    player_2 = 0
    result_2 = 2
    result_3 = 0
    for row in game_board:
        for square in row:
            if square == 1:
                player_1 += 1
            elif square == 2:
                player_2 += 1
    if player_2 > player_1:
        return result_2
    elif player_2 < player_1:
        return result_1
    else:
        return result_3
            

if __name__ == "__main__":
    lista = [[1, 2, 1], [0, 0, 1], [2, 1, 0]]
    print(who_won(lista))