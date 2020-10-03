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
    field = [[None]*width for i in range(height)]

# fill the field with random numbers
'''
    dont forget to set seed on currrent time before random
'''
