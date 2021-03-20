def horizontals(board_size):
    for hor in range(board_size):
        print(' ---', end = '')
    print(' ')
    return 

def verticals(board_size):
    for ver in range(board_size):
        print('|   ', end = '')
    print('|')
    return -1

def print_board(board_size):
    for cell in range(board_size):
        horizontals(board_size)
        verticals(board_size)
    horizontals(board_size)

def vert_win(current_moves, win): # checks for vertical win by either player
    winner = 0
    for move in range(len(current_moves[0])):
        if current_moves[0][move] != 0:
            if current_moves[0][move] == current_moves[1][move] and current_moves[0][move] == current_moves[2][move]: 
                win = True
                winner = current_moves[0][move]
    return win, winner

def hori_win(current_moves, win):
    winner = 0
    for row in range(len(current_moves[0])): # checks for horizontal win by either player
        current_row = current_moves[row]
        if current_row[0] != 0:
            if current_row[0] == current_row[1] and current_row[0] == current_row[2]: 
                win = True
                winner = current_row[0]
    return win, winner

def diag_win(current_moves, win): # checks for diagonal win by either player
    winner = 0
    if current_moves[0][0] != 0:
        if current_moves[0][0] == current_moves[1][1] and current_moves[0][0] == current_moves[2][2]:
            win = True
            winner = current_moves[1][1]
        elif current_moves[0][2] == current_moves[1][1] and current_moves[0][2] == current_moves[2][0]:
            win = True
            winner = current_moves[1][1]
    return win, winner

def win_check(current_moves):
    win = False
    win, winner = vert_win(current_moves, win)
    if win == False:
        win, winner = hori_win(current_moves, win)
    if win == False:
        win, winner = diag_win(current_moves, win)
    return win, winner

def main():
    board_size = int(input('Enter a number for gameboard size:\n'))
    print_board(board_size)
    current_moves = [[1, 2, 1], #Sample board for testing
                     [0, 2, 1],
                     [2, 2, 1]]
    win, winner = win_check(current_moves)
    if win:
        print('Winner: Player ' + str(winner))



if __name__ == '__main__':
    main()

