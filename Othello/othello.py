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

def printer(matrix):
    printer_job = ''
    for i in range(len(matrix)):
        for j in matrix[i]:
            printer_job += str(j)
            printer_job += '  '
        printer_job += constant_chars(4)
    return printer_job

def starting_board(func_rowcol):
    #prints the starting board
    if func_rowcol % 2 == 1:  #eliminates attempts to make an odd board grid
        return 'The board grid size has to be an even number!'

    #calls the constant chars function to get the apropriate characters. This part of the function also finds the first 4 positions in the matrix where the black and the while disks have to be placed at
    game_matrix = [[constant_chars(1)] * func_rowcol] * func_rowcol
    pos = func_rowcol//2

    row3 = game_matrix[pos-1]
    row4 = game_matrix[pos]
    row3[pos-1] = constant_chars(2)
    row3[pos] = constant_chars(3)
    print(row3)
    row4[pos-1] = constant_chars(3)
    row4[pos] = constant_chars(2)
    print(row4)
    game_matrix[[pos]] = row4
    game_matrix[pos-1] = row3
    print(game_matrix)

    #game_matrix[pos -1][pos -1] == constant_chars(2)  # 3,3
    #game_matrix[pos][pos] = constant_chars(2)  # 4,4
    #game_matrix[pos -1][pos] == constant_chars(3)  # 3,4
    #game_matrix[pos][pos -1] == constant_chars(3)  # 4,3

    return printer(game_matrix)  # the function sends all its information to the printer function in order to print make the board suited to be printed


"""Starting Game Loop"""
rowcol = int(input('What grid would you like your game to be: '))
print(starting_board(rowcol))

#gameend = False
#while gameend == False:

