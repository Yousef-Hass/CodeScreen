class Board:
    def __init__(self):
        """
        Initialize the board with the correct positions for the checkers.
        """
        pass

    def get_piece_at(self, position):
        """
        Return the piece at the given position.
        Position is a tuple of (row, column), with the top-left of the board being (0, 0).
        Use 'b' to represent a black piece, 'w' to represent a white piece,
        'bK' to represent a black king, and 'wK' to represent a white king.
        """
        pass

    def move(self, from_position, to_position):
        """
        Move a checker from the given position to another position.
        Ensure that the move is valid according to the rules of checkers.
        If the move is not valid, raise a ValueError with the message 'Invalid move'.
        If a piece becomes a king as a result of this move, represent it as such.
        If a piece jumps over an opponent's piece, remove the jumped piece from the board.
        from_position and to_position are tuples of (row, column), with the top-left of the board being (0, 0).
        """
        pass