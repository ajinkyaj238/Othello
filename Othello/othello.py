"""
Ajinkya Joshi
Othello in python
"""

def constant_chars(calledint):
    if calledint == 1:
        return '-'
    elif calledint == 2:
        return 'X'
    elif calledint == 3:
        return 'O'
    elif calledint == 4:
        return '\n'
    elif calledint == 5:
        return '  '
    elif calledint == 6:
        return '?'

def score_counterX(game_hashmap):
    score = 0
    for lst in game_hashmap.values():
        for value in lst:
            if value == constant_chars(2):
                score += 1
    return score

def score_counterO(game_hashmap):
    score = 0
    for lst in game_hashmap.values():
        for value in lst:
            if value == constant_chars(3):
                score += 1
    return score

def printer(game_hashmap):
    printer_job = ''
    printer_job += f'\'X\' score: {score_counterX(game_hashmap)}'
    printer_job += (constant_chars(5))
    printer_job += f'\'O\' score: {score_counterO(game_hashmap)}'
    printer_job += constant_chars(4)
    for lst in game_hashmap.values():
        for value in lst:
            printer_job += str(value)
            printer_job += constant_chars(5)  # is a space '  '
        printer_job += constant_chars(4)
    return printer_job

def starting_board(func_rowcol):
    """prints the starting board"""
    #eliminates attempts to make an odd board grid
    if func_rowcol % 2 == 1:  
        return 'The board grid size has to be an even number!'
    #calls the constant chars function to get the apropriate characters. This part of the function also finds the first 4 positions in the matrix where the black and the while disks have to be placed at
    game_hashmap = {row: value_lst for row, value_lst in range(func_rowcol, func_rowcol)}
    pos = func_rowcol//2 
    for i in range(func_rowcol):
        if i == (pos-1):
            different_row = [constant_chars(1)] * func_rowcol
            different_row[pos-1], different_row[pos] =  constant_chars(2), constant_chars(3)
            game_hashmap[i] = different_row
        elif i == (pos):
            different_row = [constant_chars(1)] * func_rowcol
            different_row[pos-1], different_row[pos] = constant_chars(3), constant_chars(2)
            game_hashmap[i] = different_row
        else:
            game_hashmap[i] = [constant_chars(1)] * func_rowcol
    return printer(game_hashmap), game_hashmap  # the function sends all its information to the printer function in order to print make the board suited to be printed

def xmove(dx, dy, game_hashmap):
    #column is the dy, row is dx. dy is the key, dx is the value in the list
    dx_lst_change = game_hashmap[dy]
    dx_lst_change[dx] = constant_chars(2)
    game_hashmap[dy] = dx_lst_change
    return printer(game_hashmap), game_hashmap

def omove(dx, dy, game_hashmap):
    #column is the dy, row is dx. dy is the key, dx is the value in the list
    dx_lst_change = game_hashmap[dy]
    dx_lst_change[dx] = constant_chars(3)
    game_hashmap[dy] = dx_lst_change
    return printer(game_hashmap), game_hashmap           

def index_exists(matrix, row, col):
    try:
        matrix[row][col]
        return True
    except IndexError:
        return False

def single_index_exist(lst, ind):
    try:
        lst[ind]
        return True
    except IndexError:
        return False

def recursive_position_finder(i, row, char_to_find, char_against):
    j = single_index_exist(row, i)
    if j is True and row[i] == constant_chars(1):  # if an empty space is present
        return row_finder(i)
    elif j is True and row[i] == char_against:  # if a rival element is present, recursively search to find the next index
        return recursive_position_finder(i+1, row, char_to_find, char_against)
    elif j is True and row[i] == constant_chars(6):  # if ? is present
        return row_finder(False)
    elif j is False:  # if the index does not exist
        return row_finder(False)
    
def row_finder(row, char_to_find, char_against):  # works for X and O
    for i in range(len(row)):
        if row[i] == char_to_find:
            if single_index_exist(row, i+1) is True and row[i+1] == char_against:  #eliminates the opportunity to have XX or OO
                index_of_end = recursive_position_finder(i+1, row, char_to_find, char_against)
                if index_of_end is False:
                    continue
                else:
                    row[index_of_end] = constant_chars(6)
    return(row)

def move_finder(game_hashmap, char_for, char_against):
    
    game_matrix = [row for row in game_hashmap.values()]
    for row in range(len(game_matrix)):
        for col in range(len(game_matrix[row])):
            if game_matrix[row][col] == char_for:
                
                right = col + 1
                if index_exists(game_matrix, row, right) is True and game_matrix[row][right] == char_against:
                    game_matrix[row] = row_finder(game_matrix[row], char_for, char_against)
                
                left = col - 1
                if index_exists(game_matrix, row, left) is True and game_matrix[row][left] == char_against:
                    changed_row = game_matrix[row]
                    changed_row.reverse()
                    changed_row = row_finder(changed_row, char_for, char_against)
                    changed_row.reverse()
                    game_matrix[row] = changed_row
                 
                up = row + 1
                if index_exists(game_matrix, up, col) is True and game_matrix[up][left] == char_against:
                    column_lst = [game_matrix[col_extraction][col] for col_extraction in range(len(game_matrix))]
                    column_lst = row_finder(column_lst, char_for, char_against)
                    for column_lst_col in range(len(game_matrix)):
                        game_matrix[column_lst_col][col] = column_lst[column_lst_col]
                
                down = row - 1
                if index_exists(game_matrix, down, col) is True and game_matrix[down][col] == char_against:
                    column_lst.reverse()
                    column_lst = row_finder(column_lst, char_for, char_against)
                    column_lst.reverse()
                    for column_lst_col in range(len(game_matrix)):
                        game_matrix[column_lst_col][col] = column_lst[column_lst_col]
                





                    













        


def Omovefinder(game_hashmap):   

"""game initialization"""
rowcol = int(input('What grid would you like your game to be: '))
board_print, game_hashmap = starting_board(rowcol)
print(board_print)

"""Game Loop"""
gameend = False
while gameend == False:

    board_print, game_hashmap = Xmovefinder(game_hashmap)
    moveX_validity = 0
    while moveX_validity == 0:  # move input code for X
        print('X turn: ')
        dymove_X = int(input('Enter row: ')) - 1
        dxmove_X = int(input('Enter column: ')) - 1
        if dymove_X > rowcol - 1  or dxmove_X > rowcol - 1:
            print('Invalid row/column input, try again')
        else:
            moveX_validity += 1
    board_print, game_hashmap = xmove(dxmove_X, dymove_X, game_hashmap)
    print(board_print)

    moveY_validity = 0
    while moveY_validity == 0:  # move input code for O
        print('O turn: ')
        dymove_O = int(input('Enter row: ')) - 1
        dxmove_O = int(input('Enter column: ')) - 1
        if dymove_O > rowcol - 1 or dxmove_O > rowcol - 1:
            print('Invalid row/column input, try again')
        else:
            moveY_validity += 1
    board_print, game_hashmap = omove(dxmove_O, dymove_O, game_hashmap)
    print(board_print)

