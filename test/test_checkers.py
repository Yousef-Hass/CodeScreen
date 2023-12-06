import pytest
from src.board import Board

class TestBoard:
    def setup(self):
        self.board = Board()

    def test_initialization(self):
        assert self.board.get_piece_at((0, 0)) == 'b'
        assert self.board.get_piece_at((0, 1)) is None
        assert self.board.get_piece_at((7, 7)) == 'w'
        assert self.board.get_piece_at((7, 6)) is None

    def test_move(self):
        self.board.move((2, 2), (3, 3))  # added valid move for black
        with pytest.raises(ValueError):
            self.board.move((0, 1), (1, 0))  # moving from an empty position

        with pytest.raises(ValueError):
            self.board.move((0, 0), (0, 2))  # moving to a non-diagonal position

        with pytest.raises(ValueError):
            self.board.move((0, 0), (2, 2))  # jumping without capturing

        self.board.move((5, 1), (4, 0))  # valid move
        assert self.board.get_piece_at((5, 1)) is None
        assert self.board.get_piece_at((4, 0)) == 'w'

    def test_capture(self):
        # Arrange the board in a way that allows for a capture
        self.board.move((2, 2), (3, 3))
        self.board.move((5, 1), (4, 0))
        self.board.move((2, 0), (3, 1))

        with pytest.raises(ValueError):
            self.board.move((5, 7), (4, 6))  # Forced capture test

        self.board.move((4, 0), (2, 2))  # white captures black
        assert self.board.get_piece_at((3, 1)) is None  # captured piece is removed
        assert self.board.get_piece_at((4, 0)) is None
        assert self.board.get_piece_at((2, 2)) == 'w'

    def test_becoming_king(self):
        # Arrange the board in a way that allows for a piece to become a king
        self.board.move((2, 6), (3, 7))  # valid move for black
        self.board.move((5, 5), (4, 4))  # valid move for white

        self.board.move((2, 4), (3, 3))  # valid move for black
        self.board.move((6, 4), (5, 5))  # valid move for white

        self.board.move((2, 0), (3, 1))  # valid move for black
        self.board.move((7, 3), (6, 4))  # valid move for white

        self.board.move((3, 1), (4, 0))  # valid move for black
        self.board.move((5, 5), (4, 6))  # valid move for white

        self.board.move((3, 7), (5, 5))  # black double jump
        self.board.move((5, 5), (7, 3))  

        assert self.board.get_piece_at((7, 3)) == 'bK'
