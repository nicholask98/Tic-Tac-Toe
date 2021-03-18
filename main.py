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

def main():
    board_size = int(input('Enter a number for gameboard size:\n'))
    print_board(board_size)
    
if __name__ == '__main__':
    main()

