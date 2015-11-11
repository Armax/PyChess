#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Coded by @Arm4x 24/3/2015
#
# validate.py
#
# a & b = first position
# c & d = second position
# f & g = first and second chess
# h = turn


print "[i] Validate lib 1.0 loaded!"

def validateMove(a,b,c,d,f,g,h,chessboard):
    #Checking if the player is going on his chess
    if(h==0):
        if(g=="♔"):
            return 16 #SCELTO DA IANNACCONE
        if(g=="♖"):
            return 16
        if(g=="♘"):
            return 16
        if(g=="♗"):
            return 16
        if(g=="♗"):
            return 16
        if(g=="♙"):
            return 16
    if(h==1):
        if(g=="♚"):
            return 16
        if(g=="♜"):
            return 16
        if(g=="♞"):
            return 16
        if(g=="♝"):
            return 16
        if(g=="♝"):
            return 16
        if(g=="♟"):
            return 16
    #Checking if the player is trying to move enemy chess
    if(h==1):
        if(f=="♔"):
            return 18
        if(f=="♖"):
            return 18
        if(f=="♘"):
            return 18
        if(f=="♗"):
            return 18
        if(f=="♗"):
            return 18
        if(f=="♙"):
            return 18
    if(h==0):
        if(f=="♚"):
            return 18
        if(f=="♜"):
            return 18
        if(f=="♞"):
            return 18
        if(f=="♝"):
            return 18
        if(f=="♝"):
            return 18
        if(f=="♟"):
            return 18

    #KING
    if(f=="♔" or f=="♚"):
        if(a==c+1 and b==d):
            return 1
        if(a==c and b==d+1):
            return 1
        if(a==c and b==d-1):
            return 1
        if(a==c-1 and b==d):
            return 1
        if(a==c+1 and b==d+1):
            return 1
        if(a==c+1 and b==d-1):
            return 1
        if(a==c-1 and b==d+1):
            return 1
        if(a==c-1 and b==d-1):
            return 1
    #KNIGHT
    if(f=="♘" or f=="♞"):
        if(a==c+1 and b==d+2):
            return 1
        if(a==c+2 and b==d+1):
            return 1
        if(a==c+2 and b==d-1):
            return 1
        if(a==c+1 and b==d-2):
            return 1
        if(a==c-1 and b==d-2):
            return 1
        if(a==c-2 and b==d-1):
            return 1
        if(a==c-2 and b==d+1):
            return 1
        if(a==c-1 and b==d+2):
            return 1
    #TOWER
    if(f=="♖" or f=="♜"):
        if(a==c):
            x=1
            dist = abs(b-d)
            while(x!=dist):
                if(d>b):
                    if(chessboard[a][b+x] != "☐"):
                        return 0
                if(d<b):
                    if(chessboard[a][b-x] != "☐"):
                        return 0
                x = x+1
            return 1
        if(b==d):
            x=1
            dist = abs(a-c)
            while(x!=dist):
                if(c>a):
                    if(chessboard[b][a+x] != "☐"):
                        return 0
                if(c<a):
                    if(chessboard[b][a-x] != "☐"):
                        return 0
                x = x+1
            return 1
    #BISHOP
    if(f=="♗" or f=="♝"):
        if(abs(a-c) == abs(b-d)):
            x=1
            if(a>c and b<d):
                dist = abs(a-c)
                while(x!=dist):
                    if(chessboard[a-x][b+x] != "☐"):
                        return 0
                    x=x+1
                return 1
            if(a>c and b>d):
                dist = abs(a-c)
                while(x!=dist):
                    if(chessboard[a-x][b-x] != "☐"):
                        return 0
                    x=x+1
                return 1
            if(a<c and b>d):
                dist = abs(a-c)
                while(x!=dist):
                    if(chessboard[a+x][b-x] != "☐"):
                        return 0
                    x=x+1
                return 1
            if(a<c and b<d):
                dist = abs(a-c)
                while(x!=dist):
                    if(chessboard[a+x][b+x] != "☐"):
                        return 0
                    x=x+1
                return 1
    #QUEEN
    if(f=="♕" or f=="♛"):
        if(a==c):
            x=1
            dist = abs(b-d)
            while(x!=dist):
                if(d>b):
                    if(chessboard[a][b+x] != "☐"):
                        return 0
                if(d<b):
                    if(chessboard[a][b-x] != "☐"):
                        return 0
                x = x+1
            return 1
        if(b==d):
            x=1
            dist = abs(a-c)
            while(x!=dist):
                if(c>a):
                    if(chessboard[b][a+x] != "☐"):
                        return 0
                if(c<a):
                    if(chessboard[b][a-x] != "☐"):
                        return 0
                x = x+1
            return 1
        if(abs(a-c) == abs(b-d)):
            x=1
            if(a>c and b<d):
                dist = abs(a-c)
                while(x!=dist):
                    if(chessboard[a-x][b+x] != "☐"):
                        return 0
                    x=x+1
                return 1
            if(a>c and b>d):
                dist = abs(a-c)
                while(x!=dist):
                    if(chessboard[a-x][b-x] != "☐"):
                        return 0
                    x=x+1
                return 1
            if(a<c and b>d):
                dist = abs(a-c)
                while(x!=dist):
                    if(chessboard[a+x][b-x] != "☐"):
                        return 0
                    x=x+1
                return 1
            if(a<c and b<d):
                dist = abs(a-c)
                while(x!=dist):
                    if(chessboard[a+x][b+x] != "☐"):
                        return 0
                    x=x+1
                return 1
    #PAWN
    if(f=="♙" or f=="♟"):
        if(f=="♙"):
            if(a==c+1 and b==d):
                if(chessboard[c][d]=="☐"):
                    return 1
            if(a==c+2 and b==d and a==7):
                if(chessboard[c][d]=="☐"):
                    return 1
        if(f=="♟"):
            if(a==c-1 and b==d):
                if(chessboard[c][d]=="☐"):
                    return 1
            if(a==c-2 and b==d and a==2):
                if(chessboard[c][d]=="☐"):
                    return 1

    return 0
