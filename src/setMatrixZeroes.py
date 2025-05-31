# https://leetcode.com/problems/set-matrix-zeroes/

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        firstColZero = False
        firstRowZero = False

        row = len(matrix)
        col = len(matrix[0])

        for i in range(row):
            if matrix[i][0] == 0:
                firstRowZero = True

        for i in range(col):
            if matrix[0][i] == 0:
                firstColZero = True

        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if firstRowZero :

            for i in range(row):
                matrix[i][0] = 0



        if firstColZero :

            for i in range(col):
                map[map]
                matrix[0][i] = 0


