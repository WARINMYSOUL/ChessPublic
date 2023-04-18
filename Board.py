from Rook import Rook
from Pawn import Pawn
from Knight import Knight
from King import King
from Queen import Queen
from Bishop import Bishop

WHITE = 1
BLACK = 2


def correct_coords(row, col):
    '''Функция проверяет, что координаты (row, col) лежат
    внутри доски'''
    return 0 <= row < 8 and 0 <= col < 8


def opponent(color):
    if color == WHITE:
        return BLACK
    else:
        return WHITE


class Board:
    def __init__(self):
        # Заполняем поле шахматами
        #    +----+----+----+----+----+----+----+----+
        # 8  | bR | bN | bB | bQ | bK | bB | bN | bR |
        #    +----+----+----+----+----+----+----+----+
        # 7  | bP | bP | bP | bP | bP | bP | bP | bP |
        #    +----+----+----+----+----+----+----+----+
        # 6  |    |    |    |    |    |    |    |    |
        #    +----+----+----+----+----+----+----+----+
        # 5  |    |    |    |    |    |    |    |    |
        #    +----+----+----+----+----+----+----+----+
        # 4  |    |    |    |    |    |    |    |    |
        #    +----+----+----+----+----+----+----+----+
        # 3  |    |    |    |    |    |    |    |    |
        #    +----+----+----+----+----+----+----+----+
        # 2  | wP | wP | wP | wP | wP | wP | wP | wP |
        #    +----+----+----+----+----+----+----+----+
        # 1  | wR | wN | wB | wQ | wK | wB | wN | wR |
        #    +----+----+----+----+----+----+----+----+
        #       A    B    C    D    E    F    G    H

        self.color = WHITE
        self.field = [[None] * 8 for row in range(8)]

        self.field[0] = [
            Rook(WHITE), Knight(WHITE), Bishop(WHITE), Queen(WHITE),
            King(WHITE), Bishop(WHITE), Knight(WHITE), Rook(WHITE)
        ]
        self.field[1] = [
            Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE),
            Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE)
        ]
        self.field[6] = [
            Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK),
            Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK)
        ]
        self.field[7] = [
            Rook(BLACK), Knight(BLACK), Bishop(BLACK), Queen(BLACK),
            King(BLACK), Bishop(BLACK), Knight(BLACK), Rook(BLACK)
        ]

    # Текущий цвет шахматы
    def current_player_color(self):
        return self.color

    def cell(self, row, col):
        '''Возвращает строку из двух символов. Если в клетке (row, col)
        находится фигура, символы цвета и фигуры. Если клетка пуста,
        то два пробела.'''
        piece = self.field[row][col]
        if piece is None:
            return '  '
        color = piece.get_color()
        c = 'w' if color == WHITE else 'b'
        return c + piece.char()

    # Получение местоположения
    def get_piece(self, row, col):
        if correct_coords(row, col):
            return self.field[row][col]

    def move_piece(self, row, col, row1, col1):
        ''' Переместить фигуру из точки (row, col) в точку (row1, col1).
        Если перемещение возможно, метод выполнит его и вернёт True.
        Если нет --- вернёт False '''

        if not correct_coords(row, col) or not correct_coords(row1, col1):
            return False
        if row == row1 and col == col1:
            return False  # нельзя пойти в ту же клетку
        piece = self.field[row][col]
        if piece is None:
            return False
        if piece.get_color() != self.color:
            return False

        if self.field[row1][col1] is None:
            if not piece.can_move(self, row, col, row1, col1):
                return False
        else:
            if not piece.can_attack(self, row, col, row1, col1):
                return False

        self.field[row][col] = None  # Снять фигуру.
        self.field[row1][col1] = piece  # Поставить на новое место.
        self.color = opponent(self.color)  # поменять цвет
        return True

    # Может или не может атаковать
    def is_under_attack(self, row, col, color):
        # Проходим по всем клеткам
        for i in range(8):
            for j in range(8):
                piece = self.field[i][j]
                # Если фигура на клетке существует и её цвет не совпадает вызывается can_attack
                if piece is not None and piece.get_color() != color:
                    if piece.can_attack(self, row, col, i, j):
                        # Может атаковать фигуру нужного цвета на клетке
                        return True
        # не может атаковать фигуру нужного цвета на клетке
        return False

    # Рокировка слева
    def castling0(self):
        # Содержит координаты ладьи и короля до и после рокировки
        cor = ((0, 0), (0, 4)) if self.color == WHITE else ((7, 0), (7, 4))

        r, k = cor
        # Проверка: есть ли на доске король и ладья, которые необходимы для рокировки
        if self.field[k[0]][k[1]] is None or self.field[r[0]][r[1]] is None:
            return False

        # Получение объектов фигур короля и ладьи
        fig_k = self.get_piece(k[0], k[1])
        fig_r = self.get_piece(r[0], r[1])

        # Проверяем их типы
        if fig_k.char() != 'K' or fig_r.char() != 'R':
            return False
        # Проверка: двигалась ли каждая из фигур до этого?
        if not (fig_k.can_move and fig_r.can_move):
            return False
        # Проверка: цвет каждой из фигур соответствует текущему ходу?
        if fig_k.get_color() != fig_r.get_color():
            return False

        # Проверка: можно ли осуществить рокировку?
        if fig_r.can_move(self, r[0], r[1], k[0], k[1]):
            self.field[r[0]][r[1]] = None
            self.field[k[0]][k[1]] = None
            fig_r.has_moved = False
            fig_k.has_moved = False
            self.field[r[0]][3] = fig_r
            self.field[k[0]][2] = fig_k
        else:
            return False
        # Меняем текущий цвет
        self.color = opponent(self.color)
        return True

    # Рокировка справа
    def castling7(self):
        # Содержит координаты ладьи и короля до и после рокировки
        cor = ((0, 7), (0, 4)) if self.color == WHITE else ((7, 7), (7, 4))

        r, k = cor
        # Проверка: есть ли на доске король и ладья, которые необходимы для рокировки
        if self.field[k[0]][k[1]] is None or self.field[r[0]][r[1]] is None:
            return False

        # Получение объектов фигур короля и ладьи
        fig_k = self.get_piece(k[0], k[1])
        fig_r = self.get_piece(r[0], r[1])

        # Проверяем их типы
        if fig_k.char() != 'K' or fig_r.char() != 'R':
            return False
        # Проверка: двигалась ли каждая из фигур до этого?
        if not (fig_k.can_move and fig_r.can_move):
            return False
        # Проверка: цвет каждой из фигур соответствует текущему ходу?
        if fig_k.get_color() != fig_r.get_color():
            return False

        # Проверка: можно ли осуществить рокировку?
        if fig_r.can_move(self, r[0], r[1], k[0], k[1]):
            self.field[r[0]][r[1]] = None
            self.field[k[0]][k[1]] = None
            fig_r.has_moved = False
            fig_k.has_moved = False
            self.field[r[0]][5] = fig_r
            self.field[k[0]][6] = fig_k
        else:
            return False
        # Меняем текущий цвет
        self.color = opponent(self.color)
        return True

    # Превращение пешки в другую фигуру шахмат
    def promotion(self, row, col, row2, col2, char):
        pwn = Pawn
        # Проверяет, что фигура на позиции
        if not isinstance(self.field[row][col], pwn):
            return False
        # Позиция либо пуста, либо занята фигурой, которую можно атаковать пешкой
        if self.field[row2][col2] is not None:
            if not self.field[row][col].can_attack(self, row, col, row2, col2):
                return False
        else:
            if not self.field[row][col].can_move(self, row, col, row2, col2):
                return False
        # Заменяет пешку на выбранную фигуру на новой позиции
        # Если проверки не проходят, возвращает False.
        p = self.field[row][col]
        self.field[row][col] = None
        if char == 'Q':
            self.field[row2][col2] = Queen(p.color)
        elif char == 'R':
            self.field[row2][col2] = Rook(p.color)
        elif char == 'B':
            self.field[row2][col2] = Bishop(p.color)
        elif char == 'N':
            self.field[row2][col2] = Knight(p.color)
        # Меняет ход
        self.color = opponent(self.color)
        return True
