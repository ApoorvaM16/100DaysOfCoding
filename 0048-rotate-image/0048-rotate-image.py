class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """
        We can rotate an array by:
        1. findig Transpose of a matrix
        2. Reversing every row of a matrix
        """
        
#         finding the transpose
        n = len(matrix)
        for i in range(n):
            for j in range(i):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        
        # reversing the matrix row
        for i in matrix:
            i.reverse()
            
            
            
# from typing import List
# def rotate(matrix: List[List[int]]) -> None:
#     n = len(matrix)
#     # transposing the matrix
#     for i in range(n):
#         for j in range(i):
#             matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
#     # reversing each row of the matrix
#     for i in range(n):
#         matrix[i].reverse()





