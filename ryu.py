'''
    Name: Ryu
    Desc: a sudoku solveable generating algorithm
    Autors: Jeroen R. & Levi N.

'''

#imports of the needed libaries
import random
import time
import numpy as np #to manage the matrix

#setting up the variables
width = 9
height = 9

#constrcution of the (empty) sudoku matrix
def generateEmptyField():
    '''
    Alternative generation method makes matrix filled with 0 based on pumpy library
    np.zeros(width,height)
    '''
    '''
    found a more optimized way | old way:
    field = [[None]*width for i in range(height)]
    '''
    field = [[None]*width for _ in range(height)]
    for i in range(height):
        for j in range(width):
            field[i][j] = j



#test function to see matrix
def printField():
    print(np.matrix(field))


'''
    The "Main" state
'''
generateEmptyField()
printField()
