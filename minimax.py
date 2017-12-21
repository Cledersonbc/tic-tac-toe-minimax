#!/usr/bin/env python3
from math import inf as infinity
from random import choice
import platform
import time
from os import system

"""
An implementation of Minimax AI Algorithm in Tic Tac Toe,
using Python.
This software is available under GPL license.
Author: Clederson Cruz
Year: 2017
"""

board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]

h_choice = ''  # X or O
c_choice = ''  # X or O
HUMAN = -1
COMP = +1


def evaluate(state):
    """
    Function to heuristic evaluation of state.
    :param state: the state of the current board
    :return: +1 if the computer wins; -1 if the human wins; 0 draw
    """
    if game_over(state, COMP):
        score = +1
    elif game_over(state, HUMAN):
        score = -1
    else:
        score = 0

    return score


def game_over(state, player):
    """
    This function tests if a specific player wins. Possibilities:
    * Three rows    [X X X] or [O O O]
    * Three cols    [X X X] or [O O O]
    * Two diagonals [X X X] or [O O O]
    :param state: the state of the current board
    :param player: a human or a computer
    :return: True if the player wins
    """
    win_state = [
        [state[0][0], state[0][1], state[0][2]],
        [state[1][0], state[1][1], state[1][2]],
        [state[2][0], state[2][1], state[2][2]],
        [state[0][0], state[1][0], state[2][0]],
        [state[0][1], state[1][1], state[2][1]],
        [state[0][2], state[1][2], state[2][2]],
        [state[0][0], state[1][1], state[2][2]],
        [state[2][0], state[1][1], state[0][2]],
    ]
    if [player, player, player] in win_state:
        return True
    else:
        return False


def game_over_all(state):
    """
    This function test if the human or computer wins
    :param state: the state of the current board
    :return: True if the human or computer wins
    """
    return game_over(state, HUMAN) or game_over(state, COMP)


def empty_cells(state):
    """
    Each empty cell will be added into cells' list
    :param state: the state of the current board
    :return: a list of empty cells
    """
    cells = []

    for x, row in enumerate(state):
        for y, cell in enumerate(row):
            if cell == 0:
                cells.append([x, y])
    return cells


def valid_move(x, y):
    """
    A move is valid if the chosen cell is empty
    :param x: X coordinate
    :param y: Y coordinate
    :return: True if the board[x][y] is empty
    """
    if [x, y] in empty_cells(board):
        return True
    else:
        return False


def set_move(x, y, player):
    """
    Set the move on board, if the coordinates are valid
    :param x: X coordinate
    :param y: Y coordinate
    :param player: the current player
    """
    if valid_move(x, y):
        board[x][y] = player
        return True
    else:
        return False


def minimax(state, depth, player):
    """
    AI function that choice the best move
    :param state: current state of the board
    :param depth: node index in the tree (0 <= depth <= 9),
    but never nine in this case (see iaturn() function)
    :param player: an human or a computer
    :return: a list with [the best row, best col, best score]
    """
    if player == COMP:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    if depth == 0 or game_over_all(state):
        score = evaluate(state)
        return [-1, -1, score]

    for cell in empty_cells(state):
        x, y = cell[0], cell[1]
        state[x][y] = player
        score = minimax(state, depth - 1, -player)
        state[x][y] = 0
        score[0], score[1] = x, y

        if player == COMP:
            if score[2] > best[2]:
                best = score  # max value
        else:
            if score[2] < best[2]:
                best = score  # min value

    return best


def clean():
    """
    Clears the console
    """
    osname = platform.system().lower()
    if 'windows' in osname:
        system('cls')
    else:
        system('clear')


def render(state):
    """
    Print the board on console
    :param state: current state of the board
    """
    print('----------------')
    for row in state:
        print('\n----------------')
        for cell in row:
            if cell == +1:
                print('|', c_choice, '|', end='')
            elif cell == -1:
                print('|', h_choice, '|', end='')
            else:
                print('|', ' ', '|', end='')
    print('\n----------------')


def iaturn():
    """
    It calls the minimax function if the depth < 9,
    else it choices a random coordinate.
    :return:
    """
    clean()
    print('Computer turn [{}]'.format(c_choice))
    render(board)

    if len(empty_cells(board)) == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
    else:
        move = minimax(board, len(empty_cells(board)), COMP)
        x, y = move[0], move[1]

    set_move(x, y, COMP)
    time.sleep(1)


def main():
    """
    Main function that calls all functions
    """
    clean()
    global h_choice, c_choice
    first = ''  # if human is the first

    # Dictionary of valid moves
    moves = {
        7: [0, 0], 8: [0, 1], 9: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        1: [2, 0], 2: [2, 1], 3: [2, 2],
    }

    # Human chooses X or O to play
    while h_choice != 'O' and h_choice != 'X':
        try:
            print('')
            h_choice = input('Choose X or O\nChosen: ').upper()
        except KeyboardInterrupt:
            print('Bye')
            exit()
        except:
            print('Bad choice')

    # Setting computer's choice
    if h_choice == 'X':
        c_choice = 'O'
    else:
        c_choice = 'X'

    clean()
    # Human may starts first
    while first != 'Y' and first != 'N':
        try:
            first = input('First to start?[y/n]: ').upper()
        except KeyboardInterrupt:
            print('Bye')
            exit()
        except:
            print('Bad choice')

    # If not, computer starts first
    if first == 'N':
        iaturn()

    # Main loop of this game
    while not game_over_all(board) and len(empty_cells(board)) > 0:
        clean()
        print('Human turn [{}]'.format(h_choice))
        render(board)
        move = 0
        while move < 1 or move > 9:
            try:
                move = int(input('Use numpad (1..9): '))
                coord = moves[move]
                try_move = set_move(coord[0], coord[1], HUMAN)

                if try_move == False:
                    print('Bad move')
                    move = 0
            except KeyboardInterrupt:
                print('Bye')
                exit()
            except:
                print('Bad choice')

        # AI turn
        iaturn()

    # Game over message
    if game_over(board, HUMAN):
        clean()
        print('Human turn [{}]'.format(h_choice))
        print('YOU WIN!')
    elif game_over(board, COMP):
        clean()
        print('Computer turn [{}]'.format(c_choice))
        render(board)
        print('YOU LOSE!')
    else:
        clean()
        render(board)
        print('DRAW!')

    exit()


if __name__ == '__main__':
    main()
