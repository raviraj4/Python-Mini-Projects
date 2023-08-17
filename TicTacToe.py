from ttt_func import * 

print('tic tac toe game: \n')
print('___________________\n')
print("instructions: \n")
print("1. the game has two players. X and O \n")
print("2. use the numpad to play the game.\n")
print("3. lastly, enjoy the game.\n")

while True:
    board1 = [' ']*10
    # board created
    player1_mark, player2_mark = ask_input()
    print("______________\nPlayer 1 is: X \n______________\nPlayer 2 is: O \n")
    # player marks set
    turn = choose_first()
    print(turn, " will go first! ")
    
    Y = True 
    game_on = True
    while Y:
        ready = input("are you ready? Y or N: ").upper()
        if ready == 'Y'or ready == 'y':
            game_on = True
            Y = False
        elif ready == 'N' or ready == 'n':
            Y = False
            game_on = False
        else:
            print("invalid, enter y or n.")


    while game_on:
        if turn == "Player 1":
            # player 1: 
            # display board
            display_board(board1)
            # ask for choice
            choice = player_choice(board1)
            # place the marker 
            place_marker(board1, player1_mark, choice)
            # win check
            if win_check(board1, player1_mark):
                print("hey we have reached an end: \n")
                display_board(board1)
                print("Player 1 has won")
                game_on = False
                replay()
            else: 
                # check for tie
                display_board(board1)
                if full_board_check(board1) == True:
                    print("hey we have reached an end: \n")
                    print("there was a tie!")
                    game_on = False
                    replay()
                else:
                    turn = "Player 2"
                    
    
        else: 
            # player 2: 
            # display board
            display_board(board1)
            # ask for choice
            choice = player_choice(board1)
            # place the marker 
            place_marker(board1, player2_mark, choice)
            # win check
            if win_check(board1, player2_mark):
                display_board(board1)
                print("hey we have reached an end: \n")
                print("Player 2 has won")
                game_on = False
                replay()
            else: 
                # check for tie
                display_board(board1)
                if full_board_check(board1) == True:
                    print("hey we have reached an end: \n")
                    print("there was a tie!")
                    game_on = False
                    replay()
                else:
                    turn = "Player 1"
   
    if not replay():
        break
