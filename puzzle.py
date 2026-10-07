import random


class Puzzle:
    def __init__(self, size=4, scramble_moves=None):
        if size not in (3, 4, 5):
            raise ValueError("Size must be 3, 4, or 5.")
        self.size = size
        self.board = self.make_board()
        self.scramble(self.size * self.size * 20 if scramble_moves is None else scramble_moves)

    def make_board(self):
        tiles = list(range(1, self.size * self.size)) + [0]
        return [tiles[r * self.size:(r + 1) * self.size]
                for r in range(self.size)]

    def blank_pos(self):
        for r in range(self.size):
            for c in range(self.size):
                if self.board[r][c] == 0:
                    return r, c
        return None

    def move(self, direction):
        directions = {
            "w": (-1, 0),
            "s": (1, 0),
            "a": (0, -1),
            "d": (0, 1),
        }
        if direction not in directions:
            return False

        r, c = self.blank_pos()
        dr, dc = directions[direction]
        nr, nc = r + dr, c + dc

        if not (0 <= nr < self.size and 0 <= nc < self.size):
            return False

        self.board[r][c], self.board[nr][nc] = (
            self.board[nr][nc], self.board[r][c]
        )
        return True

    def scramble(self, moves):
        """Scramble by making only legal moves from the solved board."""
        previous = None
        opposite = {"w": "s", "s": "w", "a": "d", "d": "a"}
        directions = {
            "w": (-1, 0),
            "s": (1, 0),
            "a": (0, -1),
            "d": (0, 1),
        }

        for _ in range(moves):
            r, c = self.blank_pos()
            possible = []

            for direction, (dr, dc) in directions.items():
                nr, nc = r + dr, c + dc
                if 0 <= nr < self.size and 0 <= nc < self.size:
                    if direction != opposite.get(previous):
                        possible.append(direction)

            direction = random.choice(possible)
            self.move(direction)
            previous = direction

    def solved(self):
        return sum(self.board, []) == list(range(1, self.size * self.size)) + [0]
