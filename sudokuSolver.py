#!/usr/bin/env python3
import sys
original_stdout = sys.stdout

def loadPuzzle():
    """
Koden börjar med en funktion som laddar puzzlet från csv fil till py koden som ska lösa puzzlet.
Och detta gjordes genom att använda funktionen sys.argv som gör det möjligt för oss att skriva in filnamnet utanför
koden som gör det lättare för att puzzel fil som ska lösas.
fileHandle = open(filnamn[1], "r") Eftersom vi använde funktionen sys.arg och när vi skriver fil namnet
i terminalen då kommer vi få tillbaks en lista med båda sudokuSolver.py och sudoku.csv samtidigt och vi
behöver pega på en av de som är [1] i det fallet så att filen läser in den.
puzzle = fileHandle.readlines() #Gör att man kan läsa alla rader från filen.
for line in range(len(puzzle)): #är en for loop som är lika lång som puzzlet
if loopen är för att den ska inte fortsätta läsa efter sista raden och den gör att den splitar där vi har “,”.
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
Här ska vi hitta dem tomma kollumer och rader och de är märkta med 0 i sudoku filen och varje 0 som
hittas ska märkas med sin placering med (i, j) i är för rad och j är för kolumnen.
koden körs många gånger tills den har lika många gånger som antal siffror i listan och sen avslutar den.
    """
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j) #row, column
    return None


def valid(board, num, pos):
    """
Här ska vi hitta platsen som behöver att lägga till en siffra till och vi kollar att den inte har
något liknande nummer i rad, kolumn och 3x3 boxen.

Detta gör att man kollar rad och om den har samma nummer vi kollar längden på raden och ifall 
den har samma nummer eller det är en plats som vi har lagt nummer till så retunerar vi false.

 for i in range(len(board[0])):
        if board[row][i] == num and column != i:
            return False

Detta gör i princip samma sak att man kollar kommunen och om den har samma nummer. 
Vi kollar längden på kommunen och ifall den har samma nummer eller det är en plats som vi har lagt nummer till så returnerar vi false.

   for i in range(len(board)):
        if board[i][column] == num and row != i:
            return False
Detta gör i princip samma sak att man kollar boxen och om den har samma nummer. 
Vi kollar på box ifall den har samma nummer eller det är en plats som vi har lagt nummer till så returnerar vi false.
Men detta görs på lite annorlunda sätt och detta är genom att kolla vilken box vi är på och detta görs genom att dela 3 på raden och ta resultatet och behandla det som en plats för en box i sudokun, detta görs med rader och kolum och då för vi ett nummer som är till exempel (0,2) då är det boxen som ligger högst upp i mitten. efter vi har fått platsen till boxen då gör vi den.  
  for i in range(startRowBox*3, (startRowBox*3)+3):
        for j in range(startColumnBox*3, (startColumnBox*3)+3):
Den gör att vi har platsen förr nummrerna som ligger i boxen.

            if board[i][j] == num and row != i and column != j:
Det gör att om boxen har samma nummer då ska den retunera false.

startRowBox = row//3 
    startColumnBox= column//3
    for i in range(startRowBox*3, (startRowBox*3)+3):
        for j in range(startColumnBox*3, (startColumnBox*3)+3):
            if board[i][j] == num and row != i and column != j:
                return False
    return True

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

def printBoard(board):    """
Vi skriver ut sudokun här och skickar den till terminalen, vi skriver ut den lösta koden 
om findEmpty är klar då är vi klara med sudokun, annars skriver vi sudokun utan lösning och
detta används när vi anropade på funktionerna för att skriva ut sudoku innan lösning efter det
nropar vi funktionen som löser sudokun därefter anropar vi samma funktion igen som skriver ut den 
lösta koden eftersom sudokun är löst.
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
Vi skriver ut texten och lägger det till solved.csv
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
Här löser vi sudokun.
om vi inte hittar find eller find returnerar none i förra funktionen då returnerar vi True som betyder att vi är klara

annars har find en plats till en siffra som behöver ersättas med en siffra.
Vi hittar den lediga platsen som vi har hittat i förra funktionen.

  for i in range(1,10):
        if valid(board, i, find):
            board[row][col] = i
Detta gör att vi ska lägga till en siffra mellan 1 - 9
och om vi hittar en plats i sudokun som har 0 då ska vi skriva in i som provar sig fram till rätt siffra.
nu om vi har hitta en siffra som passar in och när vi har gått vidare till nästa plats som har en nolla och
vi inte hittar något siffra som passar in då behöver vi gå bak och hitta ett annat siffra som passar in i
boxen och om vi inte hittar något då backar vi och provar ett annat lösning och detta  görs genom:
 if solve(board):
                return True

            board[row][col] = 0
    return False
Detta gör om vi hittar en lösning till platsen returnerar vi True annars går vi tillbaks till förra siffra och gör det till 0 som gör att denna plats behöver hitta en ny lösning som är inte samma som förra lösning eller som siffror som finns i rad, kolumn eller box. 
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

board = loadPuzzle()   #Hämtar data från puzzwel filen till board
printBoard(board)      #Skriver ut sudokun innan lösning
solve(board)           #löser sudokun
printBoard(board)      #Skriver ut sudoku efter lösning
printsolved(board)     #Skickar den klara sudokun till Solved.csv filen
