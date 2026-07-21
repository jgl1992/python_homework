# ------------------------------------------------------------
# Task I: logger_decorator
# ------------------------------------------------------------
import logging

logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        function_name = func.__name__
        positional_parameters = list(args) if args else "none"
        keyword_parameters = dict(kwargs) if kwargs else "none"

        result = func(*args, **kwargs)

        log_message = (
            f"function: {function_name}\n"
            f"positional parameters: {positional_parameters}\n"
            f"keyword parameters: {keyword_parameters}\n"
            f"return: {result}\n"
            "----------------"
        )

        logger.log(logging.INFO, log_message)
        return result
    return wrapper


@logger_decorator
def func_hello():
    print("Hello, World!")


@logger_decorator
def func_args_true(*args):
    return True


@logger_decorator
def func_kwargs_dec(**kwargs):
    return logger_decorator


# ------------------------------------------------------------
# Task II: uppercase_decorator
# ------------------------------------------------------------
def uppercase_decorator(func):
    def wrapper():
        result = func()
        return str(result).upper()
    return wrapper


@uppercase_decorator
def return_string():
    return "not a number"


def return_int():
    return 5


# ------------------------------------------------------------
# Task III: List Comprehensions
# ------------------------------------------------------------
employeeList = ['a', 'b', 'a']

employee_names = [
    letter
    for index, letter in enumerate(employeeList)
    if letter != 'a' or index in (0, len(employeeList) - 1)
]

print("Employee names:", employee_names)

names = ["Eve", "Adam", "Edward", "Bob"]
names_start_e = [name for name in names if name.lower().startswith("e")]
print("Names starting with E:", names_start_e)


# ------------------------------------------------------------
# Task IV: Hangman Closure (simple version)
# ------------------------------------------------------------
def hangman_closure(secret_word):
    guessed = set()

    def guess(letter):
        guessed.add(letter)
        return "".join(c if c in guessed else "_" for c in secret_word)

    return guess


# ------------------------------------------------------------
# Task V: Point and Vector classes
# ------------------------------------------------------------
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def distance(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5


class Vector(Point):
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)


v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2
print(v3)
print(v3.distance(v1))


# ------------------------------------------------------------
# Task VI: TicTacToe
# ------------------------------------------------------------
class TictactoeException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class Board:
    valid_moves = [
        "upper left", "upper center", "upper right",
        "middle left", "middle center", "middle right",
        "lower left", "lower center", "lower right"
    ]

    def __init__(self):
        self.board_array = [[" " for _ in range(3)] for _ in range(3)]
        self.turn = "X"
        self.last_move = None

    def __str__(self):
        rows = [" | ".join(row) for row in self.board_array]
        return "\n---------\n".join(rows)

    def move(self, move_string):
        if move_string not in Board.valid_moves:
            raise TictactoeException("That's not a valid move.")

        index = Board.valid_moves.index(move_string)
        row = index // 3
        col = index % 3

        if self.board_array[row][col] != " ":
            raise TictactoeException("That spot is taken.")

        self.board_array[row][col] = self.turn
        self.last_move = (row, col)

        self.turn = "O" if self.turn == "X" else "X"

    def whats_next(self):
        board = self.board_array

        # Rows
        for row in board:
            if row[0] == row[1] == row[2] != " ":
                return (True, f"{row[0]} has won")

        # Columns
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] != " ":
                return (True, f"{board[0][col]} has won")

        # Diagonals
        if board[0][0] == board[1][1] == board[2][2] != " ":
            return (True, f"{board[0][0]} has won")

        if board[0][2] == board[1][1] == board[2][0] != " ":
            return (True, f"{board[0][2]} has won")

        # Cat's game
        full = all(board[r][c] != " " for r in range(3) for c in range(3))
        if full:
            return (True, "Cat's Game")

        return (False, f"{self.turn}'s turn")


# ------------------------------------------------------------
# Main Execution
# ------------------------------------------------------------
if __name__ == "__main__":
    func_hello()
    func_args_true(0, 1, 2, "test", True)
    func_kwargs_dec(a=0, b=1, user="Sapphire")

    print("The test has been done; check ./decorator.log")
