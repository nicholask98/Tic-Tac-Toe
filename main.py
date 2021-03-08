board = [
    ['o', 'x', 'x'],
    ['x', 'o', 'o'],
    ['x', 'o', 'x']
]

player_input = input('TIC TAC TOE! Pick a number (1-9)\n')

for row in board:
    for pos, col in enumerate(row):
        if pos == len(row) - 1:
            print(col)
            continue
        print(col, end = ' | ')
    print()
