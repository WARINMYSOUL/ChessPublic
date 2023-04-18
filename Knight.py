from Piece import Piece


class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.color = color

    # Метод, который определяет, может ли Конь переместиться с позиции
    def can_move(self, board, row, col, row1, col1):
        # Конь двигается буквой Г (2 вертикально, 1 горизонтально)
        if abs(row - row1) == 2 and abs(col - col1) == 1:
            return True
        # Конь двигается буквой Г (1 вертикально, 2 горизонтально)
        if abs(row - row1) == 1 and abs(col - col1) == 2:
            return True

        return False

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)

    def char(self):
        return 'N'
