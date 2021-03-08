from time import sleep

def print_board(board):
    for row in board:
        for pos, col in enumerate(row):
            if pos == len(row) - 1:
                print(col)
                continue
            print(col, end = ' | ')
        print()

def win_check():
    print('FIXME: Win_check')

def is_valid(input_list):
    if board[int(input_list[0])][int(input_list[1])] != ' ':
        player_input = input('Invalid move: Pick a number (1-9) or 0 to quit\n')
        player_move(player_input)
    return True

def player_move(player_input):
    player_input = move_dict[player_input]
    input_list = player_input.split()
    is_valid(input_list)
    board[int(input_list[0])][int(input_list[1])] = 'X'
    print_board(board)
    win_check()

def comp_move():
    print('FIXME: AI move (comp_move())')
    sleep(1)
    print_board(board)
    win_check()

board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

move_dict = {
    '1': '0 0',
    '2': '0 1',
    '3': '0 2',
    '4': '1 0',
    '5': '1 1',
    '6': '1 2',
    '7': '2 0',
    '8': '2 1',
    '9': '2 2'
}


player_input = input('TIC TAC TOE! Pick a number (1-9)\n')
while player_input != '0':
    player_move(player_input)
    sleep(1)
    comp_move()
    player_input = input('Pick a number (1-9) or 0 to quit\n')

