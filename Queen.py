from Piece import Piece


def correct_coords(row, col):
    '''Функция проверяет, что координаты (row, col) лежат
    внутри доски'''
    return 0 <= row < 8 and 0 <= col < 8


class Queen(Piece):
    # Метод, который определяет, может ли Ферзь переместиться с позиции
    def can_move(self, board, row, col, row1, col1):
        # Проверка: может ли фигура, находящаяся в заданной позиции на шахматной доске?
        if not correct_coords(row1, col1):
            return False

        # Проверка: может ли фигура, переместиться на заданную позицию?
        piece1 = board.get_piece(row1, col1)
        if not (piece1 is None) and piece1.get_color() == self.color:
            return False

        # Проверка: новые координаты находятся внутри границ доски?
        if row == row1 or col == col1:
            step = 1 if (row1 >= row) else -1
            # Проверка: на новой позиции либо нет фигуры, либо есть фигура, принадлежащая противоположному цвету
            for r in range(row + step, row1, step):
                if not (board.get_piece(r, col) is None):
                    return False
            step = 1 if (col1 >= col) else -1
            for c in range(col + step, col1, step):
                if not (board.get_piece(row, c) is None):
                    return False
            return True

        # Проверка: является ли перемещение по горизонтали?
        if row - col == row1 - col1:
            step = 1 if (row1 >= row) else -1
            # Проверяет, что между начальной и конечной позицией нет других фигур
            for r in range(row + step, row1, step):
                c = col - row + r
                # Если перемещение происходит по диагонали:
                # Проверяет, что на диагонали между начальной и конечной позицией нет других фигур
                if not (board.get_piece(r, c) is None):
                    return False
            return True

        # Проверка: является ли перемещение вертикали?
        if row + col == row1 + col1:
            step = 1 if (row1 >= row) else -1
            # Проверяет, что между начальной и конечной позицией нет других фигур
            for r in range(row + step, row1, step):
                c = row + col - r
                # Если перемещение происходит по диагонали:
                # Проверяет, что на диагонали между начальной и конечной позицией нет других фигур
                if not (board.get_piece(r, c) is None):
                    return False
            return True
        return False

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(self, board, row, col, row1, col1)

    def char(self):
        return 'Q'
