class Board:
    def __init__(self):
        """
        Initialize the board with the correct positions for the checkers.
        """
        # Initialize the board with pieces in their starting positions
        self.board = self.generate_initial_board()
        self.current_player = "black"  # 'black' starts the game
        self.winner = None

    def generate_initial_board(self):
        """
        Generates the initial doc
        """
        # Generate the initial Checkers board
        board = [[None for _ in range(8)] for _ in range(8)]

        # Place black pieces
        for row in range(3):
            for col in range(0 if row % 2 == 0 else 1, 8, 2):
                board[row][col] = "b"

        # Place white pieces
        for row in range(5, 8):
            for col in range(0 if row % 2 == 0 else 1, 8, 2):
                board[row][col] = "w"

        return board

    def display_board(self):
        """_summary_"""
        # Display the current state of the board
        for row in self.board:
            pretty_row = ["_" if value is None else value for value in row]

            print(" ".join(map(str, pretty_row)))
        print()

    def get_piece_at(self, position):
        """
        Return the piece at the given position.
        Position is a tuple of (row, column), with the top-left of the board being (0, 0).
        Use 'b' to represent a black piece, 'w' to represent a white piece,
        'bK' to represent a black king, and 'wK' to represent a white king.
        """
        row, col = position
        return self.board[row][col]

    def is_valid_move(self, start, end):
        """_summary_
        Check if the move is valid or not
        Args:
            start (_type_): _description_
            end (_type_): _description_

        Returns:
            _type_: _description_
        """
        start_row, start_col = start
        end_row, end_col = end

        # Check if the start and end positions are within the board bounds
        if not (
            0 <= start_row < 8
            and 0 <= start_col < 8
            and 0 <= end_row < 8
            and 0 <= end_col < 8
        ):
            return False

        # Check if the piece at the start position belongs to the current player
        if self.current_player == "black" and self.board[start_row][start_col] not in [
            "b",
            "bK",
        ]:
            return False
        elif self.current_player == "white" and self.board[start_row][
            start_col
        ] not in ["w", "wK"]:
            return False

        # Check if the end position is empty
        if self.board[end_row][end_col] != None:
            return False

        # Calculate the row and column differences for movement
        row_diff = end_row - start_row
        col_diff = end_col - start_col

        # Implement rules for regular piece movement
        if abs(row_diff) == 1 and abs(col_diff) == 1:
            # Regular piece can move diagonally forward one space
            if self.can_capture_opponent():
                return False

            if self.get_piece_at(start) == "b" and (row_diff < 0 or col_diff < 0):
                return False

            if self.get_piece_at(start) == "w" and (row_diff > 0 or col_diff > 0):
                return False

            return True

        # Implement rules for regular piece capture
        if abs(row_diff) == 2 and abs(col_diff) == 2:
            # Check if there is an opponent's piece diagonally in front
            if self.get_piece_at(start) == "b" and (row_diff < 0 or col_diff < 0):
                return False

            if self.get_piece_at(start) == "w" and (row_diff > 0 or col_diff > 0):
                return False

            mid_row = (start_row + end_row) // 2
            mid_col = (start_col + end_col) // 2
            if self.current_player == "black" and self.board[mid_row][mid_col] in [
                "w",
                "wK",
            ]:
                return True
            elif self.current_player == "white" and self.board[mid_row][mid_col] in [
                "b",
                "bK",
            ]:
                return True

        # Implement rules for king piece movement and capture
        if (
            self.board[start_row][start_col].endswith("K")
            and abs(row_diff) == abs(col_diff)
            and abs(row_diff) == 1
        ):
            if self.can_capture_opponent():
                return False

            # King piece can move diagonally in any direction
            return True
        elif (
            self.board[start_row][start_col].endswith("K")
            and abs(row_diff) == abs(col_diff) == 2
        ):
            # King piece can capture opponent's piece diagonally
            mid_row = (start_row + end_row) // 2
            mid_col = (start_col + end_col) // 2
            if self.current_player == "black" and self.board[mid_row][mid_col] in [
                "w",
                "wK",
            ]:
                return True
            elif self.current_player == "white" and self.board[mid_row][mid_col] in [
                "b",
                "bK",
            ]:
                return True

        return False

    def can_capture_opponent(self):
        """
        Check if the current player can capture any piece of the opponent.
        Returns True if a capturing move is possible, False otherwise.
        """
        current_player_piece = "b" if self.current_player == "black" else "w"
        opponent_piece = "w" if current_player_piece == "b" else "b"

        for row in range(8):
            for col in range(8):
                if self.board[row][col] == current_player_piece:
                    # Check capturing moves for regular pieces
                    if self.current_player == "black" and self.can_capture_forward(
                        row, col, opponent_piece
                    ):
                        return True
                    elif self.current_player == "white" and self.can_capture_backward(
                        row, col, opponent_piece
                    ):
                        return True
                    # Check capturing moves for king pieces
                    elif self.board[row][col] == current_player_piece + "K" and (
                        self.can_capture_backward(row, col, opponent_piece)
                        or self.can_capture_forward(row, col, opponent_piece)
                    ):
                        return True

        return False

    def can_capture_forward(self, row, col, opponent_piece):
        """
        Check if a regular piece at the given position can capture an opponent's piece diagonally forward.
        """
        # Check if there is an opponent's piece diagonally forward and an empty space behind it
        if (
            row + 1 < 8
            and col + 1 < 8
            and self.board[row + 1][col + 1] == opponent_piece
            and row + 2 < 8
            and col + 2 < 8
            and self.board[row + 2][col + 2] == None
        ):
            return True
        elif (
            row + 1 < 8
            and col - 1 >= 0
            and self.board[row + 1][col - 1] == opponent_piece
            and row + 2 < 8
            and col - 2 >= 0
            and self.board[row + 2][col - 2] == None
        ):
            return True
        else:
            return False

    def can_capture_backward(self, row, col, opponent_piece):
        """
        Check if a king piece at the given position can capture an opponent's piece diagonally backward.
        """
        # Check if there is an opponent's piece diagonally backward and an empty space behind it
        if (
            row - 1 >= 0
            and col + 1 < 8
            and self.board[row - 1][col + 1] == opponent_piece
            and row - 2 >= 0
            and col + 2 < 8
            and self.board[row - 2][col + 2] == None
        ):
            return True
        elif (
            row - 1 >= 0
            and col - 1 >= 0
            and self.board[row - 1][col - 1] == opponent_piece
            and row - 2 >= 0
            and col - 2 >= 0
            and self.board[row - 2][col - 2] == None
        ):
            return True
        else:
            return False

    def handle_king_promotion(self, end):
        """_summary_

        Args:
            end (_type_): _description_
        """
        end_row, end_col = end
        piece = self.board[end_row][end_col]

        # Check if the piece reaches the last row on the opponent's side
        if (piece == "b" and end_row == 7) or (piece == "w" and end_row == 0):
            # Promote the piece to a king
            self.board[end_row][end_col] = piece + "K"

    def switch_player(self):
        """_summary_"""
        # Switch the turn to the next player
        self.current_player = "white" if self.current_player == "black" else "black"

    def handle_winner(self):
        """_summary_
        The function `handle_winner` checks the number of black and white pieces on the board and
        updates the `winner` attribute based on the piece count.
        """
        # Check if there is a winner (optional, for bonus points)
        black_pieces = 0
        white_pieces = 0

        # Count the number of black and white pieces on the board
        for row in self.board:
            for piece in row:
                if piece == "b" or piece == "bK":
                    black_pieces += 1
                elif piece == "w" or piece == "wK":
                    white_pieces += 1

        # Update the winner attribute based on the piece count
        if black_pieces == 0:
            self.winner = "white"
        elif white_pieces == 0:
            self.winner = "black"

    def move(self, from_position, to_position):
        """
        Move a checker from the given position to another position.
        Ensure that the move is valid according to the rules of checkers.
        If the move is not valid, raise a ValueError with the message 'Invalid move'.
        If a piece becomes a king as a result of this move, represent it as such.
        If a piece jumps over an opponent's piece, remove the jumped piece from the board.
        from_position and to_position are tuples of (row, column), with the top-left of the board being (0, 0).
        """
        # Move a piece from the start position to the end position
        if self.is_valid_move(from_position, to_position):
            start_row, start_col = from_position
            end_row, end_col = to_position
            self.board[end_row][end_col] = self.board[start_row][start_col]
            self.board[start_row][start_col] = None
            self.handle_king_promotion(to_position)
            self.handle_winner()
            self.switch_player()
        else:
            raise ValueError
