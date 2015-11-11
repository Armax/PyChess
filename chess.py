#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Coded by @Arm4x 24/3/2015
#
# Chess.py

import socket, threading, os, validate

class king:
    kingcount = 0
    def __init__(self, name, color):
        self.name = name
        self.color = color
        if(self.color=="white"):
            self.symbol = "♔"
        if(self.color=="black"):
            self.symbol = "♚"
        king.kingcount += 1
    
    def printpiece(self):
        if(self.color=="white"):
            print symbol
        if(self.color=="black"):
            print symbol

    def getPosition(self):
        return self.position
    
    def setPosition(self,a,b):
        if(self.color=="white"):
            chessboard[a][b] = self.symbol
        if(self.color=="black"):
            chessboard[a][b] = self.symbol

class tower:
    towercount = 0
    def __init__(self, name, color):
        self.name = name
        self.color = color
        tower.towercount += 1
    
    def printpiece(self):
        if(self.color=="white"):
            print "♖"
        if(self.color=="black"):
            print "♜"

    def getPosition(self):
        return self.position
    
    def setPosition(self,a,b):
        if(self.color=="white"):
            chessboard[a][b] = "♖"
        if(self.color=="black"):
            chessboard[a][b] = "♜"

class knight:
    knightcount = 0
    def __init__(self, name, color):
        self.name = name
        self.color = color
        knight.knightcount += 1
    
    def printpiece(self):
        if(self.color=="white"):
            print "♘"
        if(self.color=="black"):
            print "♞"

    def getPosition(self):
        return self.position
    
    def setPosition(self,a,b):
        if(self.color=="white"):
            chessboard[a][b] = "♘"
        if(self.color=="black"):
            chessboard[a][b] = "♞"

class bishop:
    bishopcount = 0
    def __init__(self, name, color):
        self.name = name
        self.color = color
        bishop.bishopcount += 1
    
    def printpiece(self):
        if(self.color=="white"):
            print "♗"
        if(self.color=="black"):
            print "♝"

    def getPosition(self):
        return self.position
    
    def setPosition(self,a,b):
        if(self.color=="white"):
            chessboard[a][b] = "♗"
        if(self.color=="black"):
            chessboard[a][b] = "♝"

class queen:
    queencount = 0
    def __init__(self, name, color):
        self.name = name
        self.color = color
        queen.queencount += 1
    
    def printpiece(self):
        if(self.color=="white"):
            print "♗"
        if(self.color=="black"):
            print "♝"

    def getPosition(self):
        return self.position
    
    def setPosition(self,a,b):
        if(self.color=="white"):
            chessboard[a][b] = "♕"
        if(self.color=="black"):
            chessboard[a][b] = "♛"

class pawn:
    pawncount = 0
    def __init__(self, name, color):
        self.name = name
        self.color = color
        pawn.pawncount += 1
    
    def printpiece(self):
        if(self.color=="white"):
            print "♙"
        if(self.color=="black"):
            print "♟"

    def getPosition(self):
        return self.position
    
    def setPosition(self,a,b):
        if(self.color=="white"):
            chessboard[a][b] = "♙"
        if(self.color=="black"):
            chessboard[a][b] = "♟"



def displayChessboard():
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                     for row in chessboard]))
def numStr(a):
    if(a=="a"):
        return 1
    if(a=="b"):
        return 2
    if(a=="c"):
        return 3
    if(a=="d"):
        return 4
    if(a=="e"):
        return 5
    if(a=="f"):
        return 6
    if(a=="g"):
        return 7
    if(a=="h"):
        return 8

def turn(cturn):
    if(cturn==0):
        print "White turn"
    if(cturn==1):
        print "Black turn"

def skipTurn(cturn):
    if(cturn==0):
        return 1
    if(cturn==1):
        return 0

def initchess():
    print "[i] Initializing white chess..."
    #### Initializing white chess ####
    whitetower1 = tower("whitetower1","white")
    whitetower1.setPosition(8,1)
    whiteknight1 = knight("whiteknight1","white")
    whiteknight1.setPosition(8,2)
    whitebishop1 = bishop("whitebishop1","white")
    whitebishop1.setPosition(8,3)
    whitequeen = queen("whitequeen","white")
    whitequeen.setPosition(8,4)
    whiteking = king("whiteking","white")
    whiteking.setPosition(8,5)
    whitebishop2 = bishop("whitebishop1","white")
    whitebishop2.setPosition(8,6)
    whiteknight2 = knight("whiteknight1","white")
    whiteknight2.setPosition(8,7)
    whitetower2 = tower("whitetower2","white")
    whitetower2.setPosition(8,8)
    whitepawn1 = pawn("whitepawn1","white")
    whitepawn1.setPosition(7,1)
    whitepawn2 = pawn("whitepawn2","white")
    whitepawn2.setPosition(7,2)
    whitepawn3 = pawn("whitepawn3","white")
    whitepawn3.setPosition(7,3)
    whitepawn4 = pawn("whitepawn4","white")
    whitepawn4.setPosition(7,4)
    whitepawn5 = pawn("whitepawn5","white")
    whitepawn5.setPosition(7,5)
    whitepawn6 = pawn("whitepawn6","white")
    whitepawn6.setPosition(7,6)
    whitepawn7 = pawn("whitepawn7","white")
    whitepawn7.setPosition(7,7)
    whitepawn8 = pawn("whitepawn8","white")
    whitepawn8.setPosition(7,8)
    print "[i] Initializing black chess..."
    #### Initializing black chess ####
    blacktower1 = tower("blacktower1","black")
    blacktower1.setPosition(1,1)
    blackknight1 = knight("blackknight1","black")
    blackknight1.setPosition(1,2)
    blackbishop1 = bishop("blackbishop1","black")
    blackbishop1.setPosition(1,3)
    blackqueen = queen("blackqueen","black")
    blackqueen.setPosition(1,4)
    blackking = king("blackking","black")
    blackking.setPosition(1,5)
    blackbishop2 = bishop("blackbishop1","black")
    blackbishop2.setPosition(1,6)
    blackknight2 = knight("blackknight1","black")
    blackknight2.setPosition(1,7)
    blacktower2 = tower("blacktower2","black")
    blacktower2.setPosition(1,8)
    blackpawn1 = pawn("blackpawn1","black")
    blackpawn1.setPosition(2,1)
    blackpawn2 = pawn("blackpawn2","black")
    blackpawn2.setPosition(2,2)
    blackpawn3 = pawn("blackpawn3","black")
    blackpawn3.setPosition(2,3)
    blackpawn4 = pawn("blackpawn4","black")
    blackpawn4.setPosition(2,4)
    blackpawn5 = pawn("blackpawn5","black")
    blackpawn5.setPosition(2,5)
    blackpawn6 = pawn("blackpawn6","black")
    blackpawn6.setPosition(2,6)
    blackpawn7 = pawn("blackpawn7","black")
    blackpawn7.setPosition(2,7)
    blackpawn8 = pawn("blackpawn8","black")
    blackpawn8.setPosition(2,8)
    #### other settings ####
    chessboard[0][0] = "."
    chessboard[0][1] = "a b c d e f g h" #kinda bugged when printing in line
    chessboard[0][2] = ""
    chessboard[0][3] = ""
    chessboard[0][4] = ""
    chessboard[0][5] = ""
    chessboard[0][6] = ""
    chessboard[0][7] = ""
    chessboard[0][8] = ""
    chessboard[1][0] = "1"
    chessboard[2][0] = "2"
    chessboard[3][0] = "3"
    chessboard[4][0] = "4"
    chessboard[5][0] = "5"
    chessboard[6][0] = "6"
    chessboard[7][0] = "7"
    chessboard[8][0] = "8"

print "Welcome to PyChess - Coded by @Arm4x follow me on twitter :D"
print
print "[i] Initializing chessboard..."
chessboard = [["☐" for x in range(9)] for x in range(9)]
initchess()
displayChessboard()
cturn = 0

while True:
    turn(cturn)
    firstmove = raw_input("first pos: ").split(",")
    firstmove[1] = numStr(firstmove[1])
    secondmove = raw_input("second pos: ").split(",")
    secondmove[1] = numStr(secondmove[1])
    ches = chessboard[int(firstmove[0])][firstmove[1]]
    enches = chessboard[int(secondmove[0])][secondmove[1]]
    os.system("clear")
    valx = validate.validateMove(int(firstmove[0]),firstmove[1],int(secondmove[0]),secondmove[1],ches,enches,cturn,chessboard)
    if(valx == 1):
        chessboard[int(firstmove[0])][firstmove[1]] = "☐"
        chessboard[int(secondmove[0])][secondmove[1]] = ches
        displayChessboard()
        cturn = skipTurn(cturn)
    else:
        displayChessboard()
        if(valx==16):
            print "[!] You can't go on your chess"
        elif(valx==18):
            print "[!] You can't move enemy chess"
        else:
            print "[!] Invalid move!"
