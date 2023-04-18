from Piece import Piece


class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)

    def char(self):
        return 'B'

    # Метод, который определяет, может ли Слон переместиться с позиции
    def can_move(self, board, row, col, row1, col1):
        # нельзя пойти в ту же клетку
        if row == row1 and col == col1:
            return False

        # Нельзя ходить не по диагонали
        if abs(row - row1) != abs(col - col1):
            return False

        # Нельзя перепрыгивать через другие фигуры
        r_step = 1 if row1 > row else -1
        c_step = 1 if col1 > col else -1
        r, c = row + r_step, col + c_step
        while r != row1 and c != col1:
            if board.get_piece(r, c) is not None:
                return False
            r += r_step
            c += c_step

        return True

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)
