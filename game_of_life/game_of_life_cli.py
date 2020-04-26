
def create_matrix(rows, columns):
    x = [["O" for i in range(rows)] for j in range(columns)]
    return x

def output_matrix_cli(matrix):
    for row in matrix:
        for column in row:
            print(str(column), end = " ")
        print()

CELL = "1"
EMPTY = "0"

def calculate_number_of_neighbours(matrix, x, y):

    rows = len(matrix)-1
    cols = len(matrix[0])-1

    neighbours = 0

    '''
    covering sides:
    '''
    if x == 0 and cols > y > 0:
        # upper side
        if matrix[x][y-1] == CELL: neighbours += 1
        if matrix[x+1][y] == CELL: neighbours += 1
        if matrix[x][y+1] == CELL: neighbours += 1
        if matrix[x+1][y-1] == CELL: neighbours += 1
        if matrix[x+1][y+1] == CELL: neighbours += 1
    elif y == 0 and rows > x > 0:
        # left side
        if matrix[x-1][y] == CELL: neighbours += 1
        if matrix[x-1][y+1] == CELL: neighbours += 1
        if matrix[x][y+1] == CELL: neighbours += 1
        if matrix[x+1][y+1] == CELL: neighbours += 1
        if matrix[x+1][y] == CELL: neighbours += 1
    elif y == cols and rows > x > 0:
        # right side
        if matrix[x+1][y] == CELL: neighbours += 1
        if matrix[x+1][y-1] == CELL: neighbours += 1
        if matrix[x+1][y] == CELL: neighbours += 1
        if matrix[x-1][y-1] == CELL: neighbours += 1
        if matrix[x-1][y] == CELL: neighbours += 1
    elif x == rows and cols > y > 0:
        # bottom side
        if matrix[x][y-1] == CELL: neighbours += 1
        if matrix[x-1][y-1] == CELL: neighbours += 1
        if matrix[x-1][y] == CELL: neighbours += 1
        if matrix[x-1][y+1] == CELL: neighbours += 1
        if matrix[x][y+1] == CELL: neighbours += 1
    elif x == 0 and y == 0:
        #left upper corner
        if matrix[x + 1][y] == CELL: neighbours += 1
        if matrix[x][y + 1] == CELL: neighbours += 1
        if matrix[x + 1][y + 1] == CELL: neighbours += 1
    elif x == 0 and y == cols:
        #right upper corner
        if matrix[x + 1][y] == CELL: neighbours += 1
        if matrix[x][y - 1] == CELL: neighbours += 1
        if matrix[x + 1][y - 1] == CELL: neighbours += 1
    elif x == rows and y == 0:
        #left bottom corner
        if matrix[x - 1][y] == CELL: neighbours += 1
        if matrix[x][y + 1] == CELL: neighbours += 1
        if matrix[x - 1][y + 1] == CELL: neighbours += 1
    elif x == rows and y == cols:
        #right bottom corner
        if matrix[x - 1][y] == CELL: neighbours += 1
        if matrix[x][y - 1] == CELL: neighbours += 1
        if matrix[x - 1][y - 1] == CELL: neighbours += 1
    else:
        if matrix[x - 1][y] == CELL: neighbours += 1
        if matrix[x + 1][y] == CELL: neighbours += 1
        if matrix[x][y + 1] == CELL: neighbours += 1
        if matrix[x][y - 1] == CELL: neighbours += 1
        if matrix[x - 1][y - 1] == CELL: neighbours += 1
        if matrix[x + 1][y + 1] == CELL: neighbours += 1
        if matrix[x - 1][y + 1] == CELL: neighbours += 1
        if matrix[x + 1][y - 1] == CELL: neighbours += 1

    return neighbours

def calculate_next_state_matrix(previous_state_matrix):

    rows = len(previous_state_matrix)
    cols = len(previous_state_matrix[0])

    next_matrix = create_matrix(rows, cols)

    for x in range(len(previous_state_matrix)):
        for y in range(len(previous_state_matrix[x])):
            if calculate_number_of_neighbours(previous_state_matrix, x, y) == 2 :
                next_matrix[x][y] = CELL
            if calculate_number_of_neighbours(previous_state_matrix, x, y) == 3:
                next_matrix[x][y] = CELL
            if calculate_number_of_neighbours(previous_state_matrix, x, y)  > 3:
                next_matrix[x][y] = EMPTY

    return next_matrix

def main():

    matrix = create_matrix(10, 10)

    matrix[2][2] = CELL
    matrix[2][3] = CELL
    matrix[2][4] = CELL
    matrix[3][4] = CELL
    matrix[3][2] = CELL
    matrix[4][4] = CELL
    matrix[4][2] = CELL
    matrix[4][3] = CELL

    neighbours = 0;

    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            calculate_number_of_neighbours(matrix, x, y)

    output_matrix_cli(matrix)


    print (calculate_number_of_neighbours(matrix, 3,3))

    for x in range(10):
        output_matrix_cli(calculate_next_state_matrix(matrix))
        print("\n")

if __name__ == "__main__":
    main()


