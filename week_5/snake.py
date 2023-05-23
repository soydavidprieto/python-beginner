import math
import random
from time import sleep


class Board:
    def __init__(self, width, height, border='*'):
        self.width = width
        self.height = height
        self.boarder = border
        self.board = self.init_board()
    @staticmethod
    def colored(symbol: str) -> str:
        if symbol == '*':
            return f'{Color.WARNING}{symbol}{Color.ENDC}'
        elif symbol == '@':
            return f'{Color.FAIL}{symbol}{Color.ENDC}'
        elif symbol == 'o':
            return f'{Color.OKGREEN}{symbol}{Color.ENDC}'
        elif symbol == '%':
            return f'{Color.PINK}{symbol}{Color.ENDC}'
        elif symbol == '^':
            return f'{Color.PINK}{symbol}{Color.ENDC}'
        else:
            return symbol

    @staticmethod
    def distance(p1: tuple, p2: tuple):
        p1_i, p1_j = p1
        p2_i, p2_j = p2
        return math.sqrt((p2_i - p1_i) ** 2 + (p2_j - p1_j) ** 2)

    def init_board(self):
        board = []

        # for i in range(self.height):
        #     row = [''] * self.width
        #     board.append(row)

        # ['*', '*', '*', '*']
        # ['*', ' ', ' ', '*']
        # ['*', ' ', ' ', '*']
        # ['*', '*', '*', '*']

        for i in range(self.height):
            if i in {0, self.height - 1}:
                row = [Board.colored(self.boarder)] * self.width
                board.append(row)
            else:
                row = []
                for j in range(self.width):
                    if j in {0, self.width - 1}:
                        row.append(Board.colored(self.boarder))
                    else:
                        row.append(' ')
                board.append(row)
        return board

    def show(self):
        for row in self.board:
            # print(row)
            print(' '.join(row))


class Snake:
    def __init__(self, symbol='o', position=(1, 1)):
        self.symbol = symbol
        self.body = [position]

    def eat(self, position: tuple):
        self.body.append(position)

    def move(self, position: tuple):
        self.body.append(position)
        self.body.pop(0)

    def choices(self):
        possible_move = set()
        i, j = self.body[-1]
        if (i, j + 1) not in self.body:
            possible_move.add((i, j + 1))
        if (i, j - 1) not in self.body:
            possible_move.add((i, j - 1))
        if (i + 1, j) not in self.body:
            possible_move.add((i + 1, j))
        if (i - 1, j) not in self.body:
            possible_move.add((i - 1, j))
        return possible_move


class Apple:
    def __init__(self, symbol='$', position=(2, 2)):
        self.position = position
        self.symbol = symbol


class Game:
    def __init__(self, width=20, height=20):
        self.width = width
        self.height = height
        self.board = Board(self.width, self.height)
        self.snake = Snake()
        self.apple = Apple()

    def init_apple(self):
        last_position = self.apple.position
        empty_idx = []
        for ind_x, x in enumerate(self.board.board):
            for idx_y, y in enumerate(x):
                if y == " ":
                    empty_idx.append((ind_x, idx_y))
        if not empty_idx:
            raise GameOverError('No places for apple!')
        next_apple_id = random.randrange(len(empty_idx))
        next_apple = empty_idx[next_apple_id]
        self.apple = Apple(position=next_apple)
        # return next_apple

    def play(self):
        #game_cycles = 20
        try:
            self.render()
            while True:
                snake_i, snake_j = self.snake.body[-1]
                next_move = None
                valid_board = []
                valid_choice = []
                shortest_way = {}
                for inx_i, i in enumerate(self.board.board):
                    for inx_j, j in enumerate(i):
                        if j == "*":
                            continue
                        else:
                            valid_board.append((inx_i, inx_j))
                for valid_c in self.snake.choices():
                    if valid_c in valid_board:
                        valid_choice.append(valid_c)
                for move in valid_choice:
                    shortest_way.update({move: Board.distance(move, self.apple.position)})
                next_move = min(shortest_way, key=shortest_way.get)
                if next_move is None:  # there is no possible move for snake
                    self.snake.move((snake_i + 1, snake_j + 1))  # just do one move forward for snake
                    self.render()  # render last move
                    GameOverError('No moves for snake!')  # end the game (snake does not have next valid move)
                if next_move == self.apple.position:
                    self.snake.eat(self.apple.position)
                    self.init_apple()
                    self.render()
                    continue  # go to next game cycle
                self.snake.move(next_move)
                self.render()
                #game_cycles -= 1
        except GameOverError:
            print('Game Over!')

    def clear(self):
        # for i in range(len(self.board.board)):
        #     board_item = self.board.board[i]
        #     for j in range(len(board_item)):
        #         if self.board.board[i][j] == self.snake.symbol:
        #             self.board.board[i][j] = ' '
        self.board = Board(self.width, self.height)

    def render(self):
        self.clear()
        # the easiest way to place snake's body on the board
        i, j = self.snake.body[0]
        self.board.board[i][j] = self.snake.symbol
        for (x, y) in self.snake.body:
            if (x, y) == self.snake.body[-1]:
                self.board.board[x][y] = Board.colored("%")
            elif (x, y) == self.snake.body[0]:
                self.board.board[x][y] = Board.colored("^")
            else:
                self.board.board[x][y] = Board.colored("o")
        a, b = self.apple.position
        self.board.board[a][b] = Board.colored("@")
        self.board.show()
        sleep(2)


class GameOverError(Exception):
    pass
class Color:
    """
    ANSI Colors for terminal
    """
    HEADER: str = '\033[95m'
    OKBLUE: str = '\033[94m'
    OKCYAN: str = '\033[96m'
    OKGREEN: str = '\033[92m'
    WARNING: str = '\033[93m'
    FAIL: str = '\033[91m'
    ENDC: str = '\033[0m'
    BOLD: str = '\033[1m'
    UNDERLINE: str = '\033[4m'
    PINK: str = '\033[38;5;206m'

if __name__ == '__main__':
    game = Game()
    game.play()
    game.play()
