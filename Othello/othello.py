"""
Ajinkya Joshi
Othello in python
Functional Python script non-OOP
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

# to find if the index exits
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
    return game_hashmap  # the function sends all its information to the printer function in order to print make the board suited to be printed

def possible_move_remover(game_hashmap):
    for row in game_hashmap.keys():
        if constant_chars(6) in game_hashmap[row]:
            arb_row = game_hashmap[row]
            for col in range(len(arb_row)):
                if arb_row[col] == constant_chars(6):
                    arb_row[col] = constant_chars(1)
            game_hashmap[row] = arb_row

    return game_hashmap

def xmove(dx, dy, game_hashmap):
    #column is the dy, row is dx. dy is the key, dx is the value in the list
    dx_lst_change = game_hashmap[dy]
    dx_lst_change[dx] = constant_chars(2)
    game_hashmap[dy] = dx_lst_change
    return possible_move_remover(game_hashmap)
def omove(dx, dy, game_hashmap):
    #column is the dy, row is dx. dy is the key, dx is the value in the list
    dx_lst_change = game_hashmap[dy]
    dx_lst_change[dx] = constant_chars(3)
    game_hashmap[dy] = dx_lst_change
    return possible_move_remover(game_hashmap)        

# to find possible moves. 
def recursive_position_finder(i, row, char_to_find, char_against):
    j = single_index_exist(row, i)
    if j is True and row[i] == constant_chars(1):  # if an empty space is present
        return i
    elif j is True and row[i] == char_against:  # if a rival element is present, recursively search to find the next index
        return recursive_position_finder(i+1, row, char_to_find, char_against)
    elif j is True and row[i] == constant_chars(6):  # if ? is present
        return False
    elif j is True and row[i] == char_to_find: # eliminates senario where chartofind is X and board is XOX
        return False
    elif j is False:  # if the index does not exist
        return False
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

# to take and put back diagonally downwards row
def diag_getter(game_matrix, row, col):
    diag_row = []
    diag_row.append(game_matrix[row][col])

    for index in range(len(game_matrix)):
        if row == len(game_matrix) or col == len(game_matrix):
            diag_row.append(game_matrix[row][col])
            return diag_row
        
        diag_row.append(game_matrix[row + index][col + index])
def diag_putter(game_matrix, diag_row, arb_row, arb_col):
    for index in range(len(diag_row)):
        game_matrix[arb_row + index][arb_col + index] = diag_row[index]
    
    return game_matrix

# to take and put back diagonally upwards row
def diag2_getter(game_matrix, row, col):
    diag_row = []
    saved_row, saved_col = row, col
    
    for index in range(len(game_matrix)):
        if row == 0 or col == len(game_matrix):
            diag_row.append(game_matrix[row][col])
            return diag_row
        
        diag_row.append(game_matrix[row - index][col + index])
def diag2_putter(game_matrix, diag_row, arb_row, arb_col):
    for index in range(len(diag_row)):
        game_matrix[arb_row - index][arb_col + index] = diag_row[index]

    return game_matrix

# to find moves
def move_finder(game_hashmap, char_for, char_against):
    game_matrix = [row for row in game_hashmap.values()]
    for row in range(len(game_matrix)):
        for col in range(len(game_matrix[row])):
            if game_matrix[row][col] == char_for:

                # checking and placing rightwards of the piece
                right = col + 1
                if index_exists(game_matrix, row, right) is True and game_matrix[row][right] == char_against:
                    game_matrix[row] = row_finder(game_matrix[row], char_for, char_against)
                
                # checking and placing leftwards of the piece
                left = col - 1
                if index_exists(game_matrix, row, left) is True and game_matrix[row][left] == char_against:
                    changed_row = game_matrix[row]
                    changed_row.reverse()
                    changed_row = row_finder(changed_row, char_for, char_against)
                    changed_row.reverse()
                    game_matrix[row] = changed_row
                 
                # checking and placing upwards of the piece
                up = row + 1
                if index_exists(game_matrix, up, col) is True and game_matrix[up][col] == char_against:
                    column_lst = [game_matrix[col_extraction][col] for col_extraction in range(len(game_matrix))]
                    column_lst = row_finder(column_lst, char_for, char_against)
                    for column_lst_col in range(len(game_matrix)):
                        game_matrix[column_lst_col][col] = column_lst[column_lst_col]
                
                # checking and placing downwards of the piece
                down = row - 1
                if index_exists(game_matrix, down, col) is True and game_matrix[down][col] == char_against:
                    column_lst = [game_matrix[col_extraction][col] for col_extraction in range(len(game_matrix))]
                    column_lst.reverse()
                    column_lst = row_finder(column_lst, char_for, char_against)
                    column_lst.reverse()
                    for column_lst_col in range(len(game_matrix)):
                        game_matrix[column_lst_col][col] = column_lst[column_lst_col]
                
                # checking and placing diagonally dowards (topleft to the bottom right)
                if (index_exists(game_matrix, up, left) is True and game_matrix[up][left] == char_against) or (index_exists(game_matrix, down, right) is True and game_matrix[down][right] == char_against):
                    if row == col:
                        arb_row, arb_col = 0, 0
                    elif row > col:
                        arb_row = row - col
                        arb_col = col
                    elif row < col: 
                        arb_col = col - row
                        arb_row = row
                    
                    diag_row = diag_getter(game_matrix, arb_row, arb_col)
                    diag_row = row_finder(diag_row, char_for, char_against)
                    diag_row.reverse()
                    diag_row = row_finder(diag_row, char_for, char_against)
                    diag_row.reverse()
                    game_matrix = diag_putter(game_matrix, diag_row, arb_row, arb_col)
                
                # checking and placing diagonally upwards (bottomleft to the topright)
                if (index_exists(game_matrix, up, right) is True and game_matrix[up][right] == char_against) or (index_exists(game_matrix, down, left) is True and game_matrix[down][left] == char_against):
                    if (row + col) == len(game_matrix):
                        arb_row, arb_col = len(game_matrix), 0
                    elif (row + col) > 7:
                        arb_row, arb_col = len(game_matrix), (col - (len(game_matrix) - row))
                    elif (row + col) < 7:
                        arb_row, arb_col = (row + col), 0
                
                    diag_row = diag2_getter(game_matrix, arb_row, arb_col)
                    diag_row = row_finder(diag_row, char_for, char_against)
                    diag_row.reverse()
                    diag_row = row_finder(diag_row, char_for, char_against)
                    diag_row.reverse()
                    game_matrix = diag2_putter(game_matrix, diag_row, arb_row, arb_col) 

    for i in range(len(game_matrix)):
        game_hashmap[i] = game_matrix[i]
    
    return printer(game_hashmap), game_hashmap

def validity_checker(game_hashmap, dy, dx, rowcol):
    
    if dy > rowcol - 1  or dx > rowcol - 1:
        return 0
    else:
        row = game_hashmap[dy]
        if row[dx] == constant_chars(6):
            return 1
        
        else:
            return 0
def does_move_exist(game_hashmap):
    for row in game_hashmap.keys():
        if constant_chars(6) in game_hashmap[row]:
            return True
    return False

def row_mover(row, char_for, char_against, start_index):
    for index in range(len(row), start_index + 1):
        if row[index]  == char_for:
            end_index = index
        elif row[index] == char_against:
            continue
        elif row[index] == constant_chars(1):
            return False, row

    for index in range(end_index, start_index):
        row[index] == char_for

    return True, row
def move(game_hashmap, row, col, char_for, char_against):
    game_matrix = [row for row in game_hashmap.values()]

    # checking and placing rightwards of the piece
    right = col + 1
    left = col - 1
    up = row + 1
    down = row - 1

    # row straight direction: 1
    if index_exists(game_matrix, row, right) is True and game_matrix[row][right] == char_against:
        
        move_valid, game_matrix[row] = row_mover(game_matrix[row], char_for, char_against, col)
        if move_valid is True:
            for i in range(len(game_matrix)):
                game_hashmap[i] = game_matrix[i]
            return game_hashmap
    
    # row reversed direction: 2
    if index_exists(game_matrix, row, left) is True and game_matrix[row][left] == char_against:
        
        changed_row = game_matrix[row]
        changed_row.reverse()
        move_valid, changed_row = row_mover(changed_row, char_for, char_against, col)
        
        if move_valid is True:
            changed_row.reverse()
            game_matrix[row] = changed_row
            for i in range(len(game_matrix)):
                game_hashmap[i] = game_matrix[i]
            return game_hashmap

    # column straight direction: 3
    if index_exists(game_matrix, up, col) is True and game_matrix[up][col] == char_against:
        
        column_lst = [game_matrix[col_extraction][col] for col_extraction in range(len(game_matrix))]
        move_valid, column_lst = row_mover(column_lst, char_for, char_against, row)
        if move_valid is True:
            for column_lst_col in range(len(game_matrix)):
                game_matrix[column_lst_col][col] = column_lst[column_lst_col]
            for i in range(len(game_matrix)):
                game_hashmap[i] = game_matrix[i]
            return game_hashmap
    
    # column reversed direction: 4
    if index_exists(game_matrix, down, col) is True and game_matrix[down][col] == char_against:
        
        column_lst = [game_matrix[col_extraction][col] for col_extraction in range(len(game_matrix))]
        column_lst.reverse()
        move_valid, column_lst = row_mover(column_lst, char_for, char_against, row)
        if move_valid is True:
            column_lst.reverse()
            for column_lst_col in range(len(game_matrix)):
                game_matrix[column_lst_col][col] = column_lst[column_lst_col]
            for i in range(len(game_matrix)):
                game_hashmap[i] = game_matrix[i]
            return game_hashmap

    #diagonally upwards straight direction: 5
    if index_exists(game_matrix, up, left) is True and game_matrix[up][left] == char_against:
        
        if row == col:
            arb_row, arb_col = 0, 0
        elif row > col:
            arb_row = row - col
            arb_col = col
        elif row < col: 
            arb_col = col - row
            arb_row = row
        
        diag_row = diag_getter(game_matrix, arb_row, arb_col)
        move_valid, diag_row = row_mover(diag_row, char_for, char_against, col)  # I belive both row and col would work
        if move_valid is True:
            game_matrix = diag_putter(game_matrix, diag_row, arb_row, arb_col)
            for i in range(len(game_matrix)):
                game_hashmap[i] = game_matrix[i]
            
            return game_hashmap

    # diagonally upwards reversed direction: 6 
    if index_exists(game_matrix, down, right) is True and game_matrix[down][right] == char_against:
        if row == col:
            arb_row, arb_col = 0, 0
        elif row > col:
            arb_row = row - col
            arb_col = col
        elif row < col: 
            arb_col = col - row
            arb_row = row

        diag_row = diag_getter(game_matrix, arb_row, arb_col)
        diag_row.reverse()
        diag_row = row_mover(diag_row, char_for, char_against, col)
        if move_valid is True:
            diag_row.reverse()
            game_matrix = diag_putter(game_matrix, diag_row, arb_row, arb_col)
            for i in range(len(game_matrix)):
                game_hashmap[i] = game_matrix[i]
            
            return game_hashmap
    
    # diagonally upwards straight direction: 7
    if index_exists(game_matrix, up, right) is True and game_matrix[up][right] == char_against:
        
        if (row + col) == len(game_matrix):
            arb_row, arb_col = len(game_matrix), 0
        elif (row + col) > 7:
            arb_row, arb_col = len(game_matrix), (col - (len(game_matrix) - row))
        elif (row + col) < 7:
            arb_row, arb_col = (row + col), 0
        
        diag_row = diag2_getter(game_matrix, arb_row, arb_col)
        move_valid, diag_row = row_mover(diag_row, char_for, char_against, col)  # I belive both row and col would work
        if move_valid is True:
            game_matrix = diag2_putter(game_matrix, diag_row, arb_row, arb_col)
            for i in range(len(game_matrix)):
                game_hashmap[i] = game_matrix[i]
            
            return game_hashmap

    # diagonally upwards reversed direction: 8
    if index_exists(game_matrix, down, left) is True and game_matrix[down][left] == char_against:
        
        if (row + col) == len(game_matrix):
            arb_row, arb_col = len(game_matrix), 0
        elif (row + col) > 7:
            arb_row, arb_col = len(game_matrix), (col - (len(game_matrix) - row))
        elif (row + col) < 7:
            arb_row, arb_col = (row + col), 0

        diag_row = diag2_getter(game_matrix, arb_row, arb_col)
        diag_row.reverse()
        move_valid, diag_row = row_mover(diag_row, char_for, char_against, col)
        if move_valid is True:
            diag_row.reverse()
            game_matrix = diag2_putter(game_matrix, diag_row, arb_row, arb_col)
            for i in range(len(game_matrix)):
                game_hashmap[i] = game_matrix[i]
            
            return game_hashmap


"""game initialization"""
rowcol = int(input('What grid would you like your game to be: '))
game_hashmap = starting_board(rowcol)

"""Game Loop"""
gameend = False
while gameend == False:


    # moveset for X
    board_print, game_hashmap = move_finder(game_hashmap, constant_chars(2), constant_chars(3))
    print(board_print)
    dmeX = does_move_exist(game_hashmap)
    if dmeX is True:
        #move validity for if the move is within the board
        moveX_validity = 0
        while moveX_validity == 0:
            print('X turn: ')
            dymove_X = int(input('Enter row: ')) - 1
            dxmove_X = int(input('Enter column: ')) - 1
            moveX_validity += validity_checker(game_hashmap, dymove_X, dxmove_X, rowcol) # checks if move is in bounds and if its on the potential moves checker positions
            if moveX_validity == 0:
                print('Invalid move')    
        game_hashmap = xmove(dxmove_X, dymove_X, game_hashmap)
        game_hashmap = move(game_hashmap, dymove_X, dxmove_X, constant_chars(2), constant_chars(3))
    elif dmeX is False:
        print('No moves can be made')
    

    # moveset for O
    board_print, game_hashmap = move_finder(game_hashmap, constant_chars(3), constant_chars(2))
    print(board_print)
    dmeO = does_move_exist(game_hashmap)
    if dmeO is True:
        #move validity for if the move is within the board
        moveO_validity = 0
        while moveO_validity == 0:  # move input code for O
            print('O turn: ')
            dymove_O = int(input('Enter row: ')) - 1
            dxmove_O = int(input('Enter column: ')) - 1
            moveO_validity += validity_checker(game_hashmap, dymove_O, dxmove_O, rowcol) # checks if move is in bounds and if its on the potential moves checker positions
            if moveO_validity == 0:
                print('Invalid move')   
        game_hashmap = omove(dxmove_O, dymove_O, game_hashmap)
    elif dmeO is False:
        print('no moves can be made')


    # endgame code for counting who wins
    if dmeO is False and dmeX is False:
        scoreX = score_counterX(game_hashmap)
        scoreO = score_counterO(game_hashmap)

        if scoreX == scoreO:
            print('Its a tie')
        elif scoreX > scoreO:
            print('X wins!')
        elif scoreO < scoreX:
            print('O wins!')
        
        print('GAME OVER')
        gameend = True

