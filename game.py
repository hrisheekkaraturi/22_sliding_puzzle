import time
from puzzle import Puzzle


class SlidingPuzzle:
    def __init__(self):
        self.size = self.choose_size()
        self.puzzle = Puzzle(self.size)
        self.moves = 0
        self.started = time.monotonic()
        self.finished = False

    def choose_size(self):
        print("Choose puzzle size:")
        print("3 - 3x3")
        print("4 - 4x4")
        print("5 - 5x5")

        while True:
            choice = input("Size (3/4/5): ").strip()
            if choice in {"3", "4", "5"}:
                return int(choice)
            print("Please enter 3, 4, or 5.")

    def display(self):
        print()
        for row in self.puzzle.board:
            print(" ".join(f"{x or ' ':>2}" for x in row))
        elapsed = int(time.monotonic() - self.started)
        print("Moves:", self.moves, " Time:", elapsed, "s")

    def run(self):
        print()
        print("Sliding Puzzle — W/A/S/D moves the tile into the blank. Q quits.")

        while True:
            self.display()

            if self.puzzle.solved():
                self.finished = True
                print("Solved!")
                print(
                    f"Completed in {self.moves} moves and "
                    f"{int(time.monotonic() - self.started)} seconds."
                )
                return

            key = input("> ").strip().lower()

            if key == "q":
                print("Quit.")
                return

            if key not in {"w", "a", "s", "d"}:
                print("Use W/A/S/D.")
                continue

            if self.finished:
                print("Puzzle is already complete.")
                continue

            if self.puzzle.move(key):
                self.moves += 1
                print("Tile moved.")
            else:
                print("That move is not possible.")
