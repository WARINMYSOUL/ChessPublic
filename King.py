from Piece import Piece


class King(Piece):
    # Метод, который определяет, может ли Король переместиться с позиции
    def can_move(self, board, row, col, row1, col1):
        # Проверяем, что новая клетка находится на доске
        if row1 < 0 or row1 > 7 or col1 < 0 or col1 > 7:
            return False

        # Проверяем, что король не ходит на ту же клетку
        if row == row1 and col == col1:
            return False

        # Проверяем, что король не перемещается на большее расстояние, чем одна клетка
        if abs(row - row1) > 1 or abs(col - col1) > 1:
            return False

        # Проверяем, что на новой клетке нет своих фигур
        if board[row1][col1] != None and board[row1][col1].color == self.color:
            return False

        # Король может ходить на любую свободную клетку, поэтому возвращаем True
        return True

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(self, board, row, col, row1, col1)

    def char(self):
        return 'K'
