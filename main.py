import copy, pygame as pg, time
from math import pi
from turtle import width

def flip(row, col):
    global player
    fliped = False
    drdc = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for dr, dc in drdc:
        for i in range(1, 8):
            if not -1 < row + dr*i < 8 or not -1 < col + dc*i < 8:
                break
            if board[row + dr*i][col + dc*i] == player:
                for j in range(1, i):
                    board[row + dr*j][col + dc*j] = 'grey'
                    fliped = True
                break
            elif board[row + dr*i][col + dc*i] == ' ':
                break

    if fliped:
        board[row][col] = player

        for i in range(0, 255, 3):
            display(i if player == 'O' else 255-i)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'grey':
                    board[i][j] = player
                       
        player = 'X' if player == 'O' else 'O'

def display(grey_color = None):

    window.fill((0, 220, 0))

    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if col == 'X':
                pg.draw.circle(window, (1, 0, 0), ((j + 1/2)*piece_size, (i + 1/2)*piece_size), piece_size*.45)
            if col == 'O':
                pg.draw.circle(window, (255, 255, 255), ((j + 1/2)*piece_size, (i + 1/2)*piece_size), piece_size*.45)
            if col == 'grey':
                pg.draw.circle(window, (grey_color, grey_color, grey_color), ((j + 1/2)*piece_size, (i + 1/2)*piece_size), piece_size*.45)

    for i in range(0, max(width, height), piece_size):
        pg.draw.line(window, (150, 255, 100), (0, i), (width, i), 2)
        pg.draw.line(window, (150, 255, 100), (i, 0), (i, height), 2)

    if player == 'X':
        pg.draw.circle(window, (1, 0, 0), (mx, my), piece_size*.4)
    else:
        pg.draw.circle(window, (255, 255, 255), (mx, my), piece_size*.4)
    pg.display.update()


board = [[' ' for i in range(8)]for i in range(8)]
board[3][3], board[4][4] = 'X', 'X'
board[3][4], board[4][3] = 'O', 'O'

player = 'X'
piece_size = 80
width, height = piece_size*8, piece_size*8
window = pg.display.set_mode((width, height))
pg.init()

while True:
    mx, my = pg.mouse.get_pos()

    for event in pg.event.get():
        if event.type == pg.QUIT:

            pg.quit()
            break
        elif event.type == pg.MOUSEBUTTONDOWN:

            row = my//piece_size
            col = mx//piece_size

            if not (0 <= row < 8) or not (0 <= col < 8) or board[row][col] != ' ':
                print('Invalid move. Try again.')
                continue

            flip(row, col)

    display()
    