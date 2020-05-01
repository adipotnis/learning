# write your code here
def checkshow(stringentry):
    def diag_check(matrix):
        winner_string = matrix[1][1]
        if matrix[0][0] == matrix[1][1] == matrix[2][2] != "_":
            return True, winner_string
        elif matrix[0][2] == matrix[1][1] == matrix[2][0] != "_":
            return True, winner_string
        else:
            return False, ''

    def row_check(matrix, test_for="_"):

        for row in matrix:
            if (row[0] == row[1] == row[2] != "_") and (row[1] != test_for):
                return True, row[1]
        return False, ""

    def column_check(matrix, test_for="_"):
        for column in range(3):
            if (matrix[0][column] == matrix[1][column] == matrix[2][column] != '_') and (matrix[1][column] != test_for) :
                return True, matrix[1][column]
        return False, ""


    def imposs_check(string_entry):
        x_count = 0
        o_count = 0
        for value in string_entry:
            if value == "X":
                x_count += 1
            elif value == 'O':
                o_count += 1

        return not ((abs(x_count-o_count) == 1) or (abs(x_count-o_count) == 0))





    def game_finish(string_entry):
        if "_" not in string_entry:
            return True
        else:
            return False




    print("Enter cells: > ")
    string_entry = stringentry
    count_char = 3
    game_matrix = [ [ 0 for row_ in range(3) ] for column_ in range(3) ]
    print("---------")  #start
    for row in range(3):
        line_string = ""
        for column in range(3):
            line_string += " " + "".join(string_entry[3*row + column])
            game_matrix[row][column] = string_entry[3*row + column]
        print("|" + line_string + " |")



    print("---------")  #end

    # Impossibility checker
    if imposs_check(string_entry):
        print("Impossible")
    #impossible type 2
    elif (row_check(game_matrix, 'X')[0] and row_check(game_matrix, 'O')[0]) or (column_check(game_matrix, 'X')[0] and column_check(game_matrix, 'O')[0]):
        print("Impossible")


    # win/draw/unfinished

    elif row_check(game_matrix)[0] or column_check(game_matrix)[0] or diag_check(game_matrix)[0]:
        winner = row_check(game_matrix)[1] + column_check(game_matrix)[1] + diag_check(game_matrix)[1]
        print("{} wins".format(winner))
        return True

    elif game_finish(string_entry):
        print("Draw")
        return True

    #else:
        #print("Game not finished"
    return False
    #--------------------------------------------------------------------



string_entry = "_" * 9
checkshow(string_entry)
turn = "X"
while True:
    while True:
        print("Enter the coordinates: > ")
        posin_entry = input()
        col_row = posin_entry.split()
        #check if number
        if (col_row[0] in "0123456789") and (col_row[1] in "0123456789"):
            col_row = [int(num) for num in col_row]
            #check if 1 to 3
            if col_row[0] in range(1,4) and col_row[1] in range(1,4):
                checkempty = col_row[0] -1 + 3 * (3 - col_row[1])
                if string_entry[checkempty]  != '_':
                    print("This cell is occupied! Choose another one!")
                    continue
                else:
                    break


            else:
                print("Coordinates should be from 1 to 3!")
                continue
        else:
            print("You should enter numbers!")


    #modify str
    modified_str = list(string_entry)

    modified_str[checkempty] = turn
    string_entry = "".join(modified_str)
    if turn == "X":
        turn = "O"
    else:
        turn = "X"
    if checkshow(string_entry):
        break
