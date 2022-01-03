# In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

# You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.

# The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

# If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

 

# Example 1:
# Input: mat = [[1,2],[3,4]], r = 1, c = 4
# Output: [[1,2,3,4]]

# Example 2:
# Input: mat = [[1,2],[3,4]], r = 2, c = 4
# Output: [[1,2],[3,4]]


def reshape1(mat, r, c):
    n = len(mat[0])
    if r * c == len(mat) * n:
        new_mat = []
        total_count = 0
        for _ in range(r):
            temp_list = []
            for _ in range(c):
                row = total_count // n
                col = total_count - row * n
                temp_list.append(mat[row][col])
                total_count += 1
            new_mat.append(temp_list)
        return new_mat 
    else:
        return mat

# import numpy as np
# def reshape2(mat, r, c):
#     try:
#         return np.reshape(mat, (r, c))
#     except ValueError as e:
#         return mat

def reshape3(mat, r, c):
    if r * c == len(mat) * len(mat[0]):
        x , y = 0 , 0 
        matrix = [[0] * c for _ in range(r)]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                matrix[x][y] = mat[i][j]
                y += 1
                if y % c == 0:
                    x += 1
                    y = 0
                    
        return matrix
    else:
        return mat
    


