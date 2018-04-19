import matplotlib.pyplot as plt
import numpy as np

def matrix_io_input(name):
    numRow = input("Input Number of Rows for Matrix " + str(name) + ": ")
    numCol = input("Input Number of Columns for Matrix "+ str(name) + ": ")

    matrix = []
    print "Input Data for Matrix", name
    for i in range(numRow):
        row = ""
        while (len(row) != 2*numCol-1):
            row = raw_input("Input a row: ")
            if (len(row) == 2*numCol-1):
                matrix.append(map(int, row.split()))
            else:
                print "Input a row of the correct length."
    return matrix

def matrix_input(filename):
    with open(filename) as f:
        read_data = f.read()
        
    read_data = map(int, read_data.split())

    numRow = read_data.pop(0)
    numCol = read_data.pop(0)
    matrix = []
    for i in range(numRow):
        row = []
        for j in range(numCol):
            row.append(read_data.pop(0))
        matrix.append(row)
    return matrix
            
def graph_matrix (matrix):
    for column in range(np.asarray(matrix).shape[1]-1):
        x = [matrix[0][column], matrix[0][column+1]]
        y = [matrix[1][column], matrix[1][column+1]]
        plt.plot(x,y)

    x = [matrix[0][0], matrix[0][len(matrix[0])-1]]
    y = [matrix[1][0], matrix[1][len(matrix[0])-1]]
    plt.plot(x,y)

    #find bounds for graph, make it always fit nicely in a square plot
    max_val = 0
    for row in matrix:
        for val in row:
            if max_val < val:
                max_val = val

    axes = plt.gca()
    _, y_max = axes.get_ylim()
    _, x_max = axes.get_xlim()

    if max_val > y_max or max_val > x_max:
        plt.ylim(-max_val, max_val)
        plt.xlim(-max_val, max_val)


    

def matrix_mult (transMatrix, matrix):
    mRow = len(matrix)
    mCol = len(matrix[0])
    transRow = len(transMatrix)
    transCol = len(transMatrix[0])

    assert transCol == mRow #make sure its okay to multiple the two matricies
    
    new_matrix = [[None]* mCol for _ in range(transRow)]

    for rowNum in range(mRow):
        for colNum in range(mCol):
            total_sum = 0
            for idx in range(transRow):
                total_sum += transMatrix[rowNum][idx]*matrix[idx][colNum]
            new_matrix[rowNum][colNum] = total_sum

    return new_matrix
            
# matrxiM = matrix_io_input("M") #for inputing manually

matrix = matrix_input("matrix.txt") #for inputing by file
transMatrix = matrix_input("transformationMatrix.txt")

print "matrix:", matrix
print "transformation Matrix:", transMatrix

graph_matrix (matrix)

transMatrix = matrix_mult(transMatrix, matrix)

graph_matrix(transMatrix)
graph_matrix(matrix)

plt.show()