from main import (
    WHITE, BLACK
)
from Rook import Rook
from Pawn import Pawn
from Knight import Knight
from King import King
from Queen import Queen
from Bishop import Bishop
from Board import Board


# ----------------------------------------------------------------------------------

# Задания 1-4 (ABCD. Классы фигур)
# Пример 1

board = Board()
board.field = [([None] * 8) for i in range(8)]
board.field[0][3] = Queen(WHITE)
queen = board.get_piece(0, 3)

for row in range(7, -1, -1):
    for col in range(8):
        if queen.can_move(board, 0, 3, row, col):
            print('x', end='')
        else:
            cell = board.cell(row, col)[1]
            cell = cell if cell != ' ' else '-'
            print(cell, end='')
    print()

# Пример 2

# row0 = 4
# col0 = 5
#
# board = Board()
# board.field = [([None] * 8) for i in range(8)]
# board.field[row0][col0] = Bishop(BLACK)
# bishop = board.get_piece(row0, col0)
#
# for row in range(7, -1, -1):
#     for col in range(8):
#         if bishop.can_move(board, row0, col0, row, col):
#             print('x', end='')
#         else:
#             cell = board.cell(row, col)[1]
#             cell = cell if cell != ' ' else '-'
#             print(cell, end='')
#     print()

# Пример 3

# row0 = 2
# col0 = 2
#
# knight = Knight(WHITE)
# board = Board()
#
# for row in range(7, -1, -1):
#     for col in range(8):
#         if row == row0 and col == col0:
#             print(knight.char(), end='')
#         elif knight.can_move(board, row0, col0, row, col):
#             print('x', end='')
#         else:
#             print('-', end='')
#     print()

# ----------------------------------------------------------------------------------
# Задание 5 (E. Поля под боем)
# Пример 1

# board = Board()
#
# board.field = [([None] * 8) for i in range(8)]
# board.field[0][0] = Rook(WHITE)
# board.field[1][2] = Bishop(WHITE)
# coords = ((0, 0), (1, 2))
#
# for row in range(7, -1, -1):
#     for col in range(8):
#         if (row, col) in coords:
#             print('W', end='')
#         elif board.is_under_attack(row, col, BLACK):
#             print('x', end='')
#         else:
#             print('-', end='')
#     print()

# Пример 2

# board = Board()
#
# board.field = [([None] * 8) for i in range(8)]
# board.field[0][5] = Rook(WHITE)
# board.field[1][2] = Bishop(WHITE)
# board.field[7][6] = Knight(WHITE)
# coords = ((0, 5), (1, 2), (7, 6))
#
# for row in range(7, -1, -1):
#     for col in range(8):
#         if (row, col) in coords:
#             print('W', end='')
#         elif board.is_under_attack(row, col, BLACK):
#             print('x', end='')
#         else:
#             print('-', end='')
#     print()

# Пример 3

# board = Board()
#
# board.field = [([None] * 8) for i in range(8)]
# board.field[0][5] = Rook(WHITE)
# board.field[1][2] = Bishop(WHITE)
# board.field[7][6] = Knight(BLACK)
# w_coords = ((0, 5), (1, 2))
# b_coords = ((7, 6),)
#
# print('Write:')
# for row in range(7, -1, -1):
#     for col in range(8):
#         if (row, col) in w_coords:
#             print('W', end='')
#         elif board.is_under_attack(row, col, BLACK):
#             print('x', end='')
#         else:
#             print('-', end='')
#     print()
# print()
#
# print('Black:')
# for row in range(7, -1, -1):
#     for col in range(8):
#         if (row, col) in b_coords:
#             print('B', end='')
#         elif board.is_under_attack(row, col, WHITE):
#             print('x', end='')
#         else:
#             print('-', end='')
#     print()

# ----------------------------------------------------------------------------------
# Задание 6 (F. Рокировка)
# Пример 1

# board = Board()
# board.field = [([None] * 8) for i in range(8)]
# board.field[0][0] = Rook(WHITE)
# board.field[0][4] = King(WHITE)
# board.field[0][7] = Rook(WHITE)
#
# board.field[7][0] = Rook(BLACK)
# board.field[7][4] = King(BLACK)
# board.field[7][7] = Rook(BLACK)
#
# print('before:')
# for row in range(7, -1, -1):
#     for col in range(8):
#         char = board.cell(row, col)[1]
#         print(char.replace(' ', '-'), end='')
#     print()
# print()
#
# print("Рокировка")
# print(board.castling0())
# print(board.castling7())
#
# for row in range(7, -1, -1):
#     for col in range(8):
#         char = board.cell(row, col)[1]
#         print(char.replace(' ', '-'), end='')
#     print()

# Пример 2

# board = Board()
# board.field = [([None] * 8) for i in range(8)]
# board.field[0][0] = Knight(WHITE)
# board.field[0][4] = King(WHITE)
# board.field[0][7] = Knight(WHITE)
#
# board.field[7][0] = Knight(BLACK)
# board.field[7][4] = King(BLACK)
# board.field[7][7] = Knight(BLACK)
#
# print('before')
# for row in range(7, -1, -1):
#     for col in range(8):
#         char = board.cell(row, col)[1]
#         print(char.replace(' ', '-'), end='')
#     print()
# print()
#
# print("Вместо ладей кони")
# print(board.castling0())
# print(board.castling7())
#
# for row in range(7, -1, -1):
#     for col in range(8):
#         char = board.cell(row, col)[1]
#         print(char.replace(' ', '-'), end='')
#     print()

# Пример 3

# board = Board()
# board.field = [([None] * 8) for i in range(8)]
# board.field[0][0] = Rook(WHITE)
# board.field[0][4] = King(WHITE)
# board.field[0][7] = Rook(WHITE)
#
# board.field[7][0] = Rook(BLACK)
# board.field[7][4] = King(BLACK)
# board.field[7][7] = Rook(BLACK)
#
# print('before')
# for row in range(7, -1, -1):
#     for col in range(8):
#         char = board.cell(row, col)[1]
#         print(char.replace(' ', '-'), end='')
#     print()
# print()
#
# print("Сдвиги ладей")
# board.move_piece(0, 0, 0, 1)
# board.move_piece(7, 0, 7, 1)
# print(board.castling0())
# print(board.castling7())
#
# for row in range(7, -1, -1):
#     for col in range(8):
#         char = board.cell(row, col)[1]
#         print(char.replace(' ', '-'), end='')
#     print()
# print()
#
# print(board.castling0())
# print(board.castling7())
#
# for row in range(7, -1, -1):
#     for col in range(8):
#         char = board.cell(row, col)[1]
#         print(char.replace(' ', '-'), end='')
#     print()

# ----------------------------------------------------------------------------------
# Задание 7 (G. Превращение пешки)
# Пример 1

# board = Board()
# board.field = [([None] * 8) for i in range(8)]
# board.field[6][5] = Pawn(WHITE)
#
# print('before:')
# for row in range(7, -1, -1):
#     for col in range(8):
#         char = board.cell(row, col)[1]
#         print(char.replace(' ','-'), end='')
#     print()
# print()
#
# board.promotion(6, 5, 7, 5,'Q')
#
# print('after:')
# for row in range(7, -1, -1):
#     for col in range(8):
#         char = board.cell(row, col)[1]
#         print(char.replace(' ','-'), end='')
#     print()

# Пример 2

# board = Board()
# board.field = [([None] * 8) for i in range(8)]
# board.field[6][3] = Pawn(WHITE)
# board.field[7][4] = Rook(BLACK)
#
# print('before:')
# for row in range(7, -1, -1):
#     for col in range(8):
#         char = board.cell(row, col)[1]
#         print(char.replace(' ', '-'), end='')
#     print()
# print()
#
# board.promotion(6, 3, 7, 4, 'N')
#
# print('after:')
# for row in range(7, -1, -1):
#     for col in range(8):
#         char = board.cell(row, col)[1]
#         print(char.replace(' ', '-'), end='')
#     print()
