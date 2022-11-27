# Code by Faraihan Rafi Adityawarman
# NRP 5025211074


# funtion to get minor as a value computed 
# from the determinant of a square matrix 
# which is obtained after crossing out a row and a column
def minor(matrix, i, j):
    return [row[: j] + row[j+1:] for row in (matrix[: i] + matrix[i+1:])]
 
#function to get determinant
def determinant(matrix):
 
    # this function is used if the matrix is 2x2
    if(len(matrix) == 2):
        det = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
        
        return det
    # else, use the other function to find the determinant
 
    # set the determinant to zero
    det = 0
    
    for checkedcolumn in range(len(matrix)):
        sign = (-1) ** (checkedcolumn) # ** = exponent (x**y, x to the power of y)
        sub_det = determinant(minor(matrix, 0, checkedcolumn))
        det += (sign * matrix[0][checkedcolumn] * sub_det)
 
    return det

def main() :
    # Inputting the row and column
    column = row = int(input("input the size of matrix \n(example : 2 = [2][2]; 3 = [3][3]) : " ))
    
    # Initialize the matrix
    matrix = []
    
    # Inputting and scanning the matrix
    for i in range(row):
        temp = []
        for j in range(column):
            temp.append(int(input()))
        matrix.append(temp)
    
    # Printing the inputted matrix
    print()
    print(row, "x", column, "matrix :" + "\n")
    for i in range(row):
        for j in range(column):
            print(matrix[i][j], end = " ")
        print()
    print()
    
    # find the Determinant by using matrixDeterminant function
    matrixDeterminant = determinant(matrix)
    print("Determinant value of matrix : " + str(matrixDeterminant))
    
    # Transpose the matrix
    
    # We can use this function, but it's way more complicated
    # transposeMatrix = []
    # for i in range(len(matrix[0])):
    #     for j in range(len(matrix)):
    #         transposeMatrix[j][i] = matrix[i][j]
            
    # So we use this function to do the transposeMatrix
    transposeMatrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
     
    print()
    print(row, "x", column, "transposed matrix :" + "\n")
    for i in range(row):
        for j in range(column):
            print(transposeMatrix[i][j], end = " ")
        print()
    print()
    
    
    
if __name__ == "__main__":
    main()
    