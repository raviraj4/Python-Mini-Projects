import random
import os
import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    

def display_board(board):
    '''Displaying the board'''
    
    clear_terminal()
    print("___________")
    print("   |   |   ")
    print(" "+ board[7]+" | "+board[8]+" | "+board[9]+" ")
    print("___|___|___")
    print("   |   |   ")
    print(" "+board[4]+" | "+board[5]+" | "+board[6]+" ")
    print("___|___|___")
    print("   |   |   ")
    print(" "+board[1]+" | "+board[2]+" | "+board[3]+" ")
    print("___|___|___")


def ask_input():
    '''Output is in the form of tuple 
    Output = (player 1 marker, player 2 marker)'''

    print("What symbol do you want? [X or O]")
    user_input = "wrong"
    choice_list = ["X","O"]

    while user_input not in choice_list :
        user_input = input("player 1: ").upper()
        if user_input not in choice_list:
            print("invalid input! try again.")
        else:
            pass
    player1 = user_input
    if(player1 == 'X'):
        return ('X','O')
    else:
        return ('O','X')


def place_marker(board, marker, position):
    '''place marker: takes board, marker, position as arguments
    IT MARKS THE MARKER ON THE POSITION'''
    # now we have a blank board, a marker either X or O, and a position
    board[position] = marker
    

def win_check(board, mark):
    '''CHECKS FOR A WIN CASE'''
    # win??
    # all rows, check if they share the same marker
    if (board[1]== board[2]== board[3]==mark) or (board[4]== board[5]== board[6]==mark) or (board[7]== board[8]== board[9]==mark):
        return True
    # all columns, check if they share the same marker
    elif (board[7]== board[4]== board[1]==mark) or (board[8]== board[5]== board[2]==mark) or (board[9]== board[6]== board[3]==mark):
        return True
        
    # 2 diagonals columns, check if they share the same marker
    elif (board[7]== board[5]== board[3]==mark) or (board[9] == board[5] == board[1]==mark):
        return True
    else:
        return False

    
def choose_first():
    '''randomly selecting players turn'''
    flip= random.randint(0,1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    '''returns true if position is blank'''
    return board[position] == ' '

def full_board_check(board):
    '''returns true is board is full'''
    for i in [1,2,3,4,5,6,7,8,9]:
        if space_check(board,i):
            return False
        
    return True 
       
def player_choice(board):
    '''returns the position of the player'''
    position = 0
    X = True
    range_list = [1,2,3,4,5,6,7,8,9]
    while X:
        position = int(input("enter position (1-9): "))
        if(position not in range_list):
            print("Invalid position. Choose a position between 1 and 9.")
        elif(board[position]!=' '):
            print("Position is already occupied. Choose another position.")
        else:
            X = False
        
    return position

def replay():
    '''returns True if Y 
    (i.e. if user wants to replay) '''
    
    choice = str(input("Wanna play again? (Y,N): "))

    # clear_terminal()
    return choice.upper() == 'Y'
    

    




