#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
original_stdout = sys.stdout

def loadPuzzle():
    """
    A method to read a file having puzzle in it. The puzzle should have nine lines
     of nine numbers each between 0-9 seprated by commas.
     
    Arguments:
    None
    
    Output:
    A list variable board
    """
    filnamn = sys.argv
    board = []
    fileHandle = open(filnamn[1], "r")
    puzzle = fileHandle.readlines()
    for line in range(len(puzzle)):
        if line != len(puzzle) - 1:
            puzzle[line] = puzzle[line][:-1]
            board.append(list(map(int,puzzle[line].split(","))))
        else:
            board.append(list(map(int,puzzle[line].split(","))))
    fileHandle.close()
    return board
def findEmpty(board):
    """
    A method to find the next empty cell of the puzzle.
    Iterates from left to right and top to bottom
    
    Arguments:
    board - a list of nine sub lists with 9 numbers in each sub list
    
    Output:
    A tuple (i, j) which is index of row, column
    """
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j) #row, column
    return None
def valid(board, num, pos):
    """
    A method to find if a number num is valid or not
    
    Arguments:
    board - a list of nine sub lists with 9 numbers in each sub list
    num - a number between 1 to 9 both inclusive
    pos - a tuple (i, j) representing row, column
    
    Output:
    True if the number is valid in position pos of puzzle else False.
    """
    row = pos[0]
    column = pos[1]
    #checking rows
    for i in range(len(board[0])):
        if board[row][i] == num and column != i:
            return False
    #checking columns
    for i in range(len(board)):
        if board[i][column] == num and row != i:
            return False
    
    #checking box
    startRowBox = row//3 
    startColumnBox= column//3
    for i in range(startRowBox*3, (startRowBox*3)+3):
        for j in range(startColumnBox*3, (startColumnBox*3)+3):
            if board[i][j] == num and row != i and column != j:
                return False
    return True

def printBoard(board):
    """
    A method to print the sudoku puzzle in a visually appealing format

    Arguments:
    board - a list of nine sub lists with 9 numbers in each sub list

    Output:
    Prints a nine x nine puzzle represented as a sudoku puzzle. Returns None.
    """
    if not findEmpty(board):
        print("Finished puzzle")
    else:
        print("Unsolved puzzle")
    for i in range(len(board)):
        if i%3 == 0:
            print("-------------------")

        for j in range(len(board[0])):
            if j%3 == 0:
                print("\b|", end ="")

            print(str(board[i][j])+" ", end="")
        print("\b|")
    print("-------------------")


def printsolved(board):
    """
    A method to print the sudoku puzzle in a visually appealing format

    Arguments:
    board - a list of nine sub lists with 9 numbers in each sub list

    Output:
    Prints a nine x nine puzzle represented as a sudoku puzzle. Returns None.
    """

    with open('solved.csv', 'w') as f:
        sys.stdout = f
        if not findEmpty(board):
            print("Finished puzzle")
        else:
            print("Unsolved puzzle")
        for i in range(len(board)):
            if i%3 == 0:
                print("-------------------")

            for j in range(len(board[0])):
                if j%3 == 0:
                    print("\b|", end ="")

                print(str(board[i][j])+" ", end="")
            print("\b|")
        print("-------------------")
        sys.stdout = original_stdout

def solve(board):
    """
    A method to solve the sudoku puzzle using the other functions defined.
    We use a simple recursion and backtracking method.

    Arguments:
    board - a list of nine sub lists with 9 numbers in each sub list

    Output:
    Returns True once the puzzle is successfully solved else False
    """
    find = findEmpty(board)
    
    if not find:
        return True
    else:
        row, col = find
    
    for i in range(1,10):
        if valid(board, i, find):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0
    return False

board = loadPuzzle()   #loading the board from puzzle file     
#printBoard(board)      #printing the board before solving the puzzle
solve(board)           #solving the puzzle
#printBoard(board)      #printing the puzzle after solving
printsolved(board)
