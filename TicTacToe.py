'''
A simple Tic Tac Toe game
'''

from random import *


def wincheck(player_choice, board):
    win = 0
    if (board[6] == player_choice and board[7] == player_choice and board[8] == player_choice) or \
            (board[3] == player_choice and board[4] == player_choice and board[5] == player_choice) or \
            (board[0] == player_choice and board[1] == player_choice and board[2] == player_choice) or \
            (board[6] == player_choice and board[3] == player_choice and board[0] == player_choice) or \
            (board[7] == player_choice and board[4] == player_choice and board[1] == player_choice) or \
            (board[8] == player_choice and board[5] == player_choice and board[2] == player_choice) or \
            (board[6] == player_choice and board[4] == player_choice and board[2] == player_choice) or \
            (board[0] == player_choice and board[4] == player_choice and board[8] == player_choice):
        win = 1
    return win


def draw_check(board):
    draw = 1
    for i in range(0, 9):
        if board[i] == ' ':
            draw = 0
            break
    return draw


def player_placeholder(player_to_play, Player_Choice, Board):
    while True:
        position_choice = int(raw_input(player_to_play + ' please select the position:'))
        if position_choice < 1 or position_choice > 9 or Board[position_choice-1] != ' ':
            print("Please enter valid position on the board")
            continue
        else:
            break
    Board[position_choice-1] = Player_Choice
    return Board


def update_board(board):
    print " %s | %s | %s " % (board[6], board[7], board[8])
    print "- - - - - - "
    print " %s | %s | %s " % (board[3], board[4], board[5])
    print "- - - - - - "
    print " %s | %s | %s " % (board[0], board[1], board[2])
    print "- - - - - - "
    return board


def player_choice():
    random_choice = randint(0, 1)
    if random_choice == 1:
        while True:
            player_1_choice = raw_input("Player 1 please select input choice(either 'X' or 'O'):")
            if player_1_choice == 'X' or player_1_choice == 'O':
                break
        if player_1_choice == 'X':
            player_2_choice = 'O'
        else:
            player_2_choice = 'X'
    else:
        while True:
            player_2_choice = raw_input("Player 2 please select input choice(either 'X' or 'O'):")
            if player_2_choice == 'X' or player_2_choice == 'O':
                break
        if player_2_choice == 'X':
            player_1_choice = 'O'
        else:
            player_1_choice = 'X'
    return player_1_choice, player_2_choice


# main function

print("Welcome to the Tic Tac Toe!!!!")
Play_Choice = 'Y'
while Play_Choice[0] == 'Y' or Play_Choice[0] == 'y':
    Player_1_Choice, Player_2_Choice = player_choice()
    print "Player 1 sign : %s" % Player_1_Choice
    print "Player 2 sign : %s" % Player_2_Choice
    Board = [' ']*9
    Board = update_board(Board)
    player_to_play = 'Player_1'
    while True:
        if player_to_play == 'Player_1':
            Board = player_placeholder(player_to_play, Player_1_Choice, Board)
            update_board(Board)
            if draw_check(Board):
                print("Game Drawn!!!")
                break
            if wincheck(Player_1_Choice, Board):
                print("Player one won the game!!!")
                break
            player_to_play = 'Player_2'
        if player_to_play == 'Player_2':
            Board = player_placeholder(player_to_play, Player_2_Choice, Board)
            update_board(Board)
            if draw_check(Board):
                print("Game Drawn!!!")
                break
            if wincheck(Player_2_Choice, Board):
                print("Player two won the game!!!")
                break
            player_to_play = 'Player_1'
    Play_Choice = raw_input('DO you want to play again?(Yes/No)?:')