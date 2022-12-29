from time import sleep
import os
import random
import math


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


class Board:

    @staticmethod
    def colored(symbol: str) -> str:
        if symbol == '<':
            return f'{Color.WARNING}{Color.BOLD}{symbol}{Color.ENDC}'
        elif symbol == '>':
            return f'{Color.WARNING}{Color.BOLD}{symbol}{Color.ENDC}'
        elif symbol == '^':
            return f'{Color.WARNING}{Color.BOLD}{symbol}{Color.ENDC}'
        elif symbol == '$':
            return f'{Color.FAIL}{symbol}{Color.ENDC}'
        elif symbol == 'o':
            return f'{Color.OKGREEN}{symbol}{Color.ENDC}'
        elif symbol == '&':
            return f'{Color.PINK}{symbol}{Color.ENDC}'
        elif symbol == '@':
            return f'{Color.PINK}{symbol}{Color.ENDC}'
        elif symbol == 'Game over!':
            return f'{Color.OKBLUE}{Color.BOLD}{symbol}{Color.ENDC}'
        else:
            return symbol

    @staticmethod
    def distance(p1: tuple, p2: tuple):
        p1_i, p1_j = p1
        p2_i, p2_j = p2
        d = math.sqrt((p2_i - p1_i) ** 2 + (p2_j - p1_j) ** 2)
        return d

    def __init__(self, width, height, top_border="<", bottom_border=">", vert_border="^"):
        self.snake = Snake()
        self.top_boarders = top_border
        self.bottom_boarders = bottom_border
        self.vert_boarders = vert_border
        self.width = width
        self.height = height
        self.board = self.init_board()

    def init_board(self):
        new_board = []
        for i in range(self.height):
            if i == 0:
                row = [self.colored(symbol=self.top_boarders)] * self.width
                new_board.append(row)
            elif i in {self.height - 1}:
                row = [self.colored(symbol=self.bottom_boarders)] * self.width
                new_board.append(row)
            else:
                row = []
                for j in range(self.width):
                    if j in {0, self.width - 1}:
                        row.append(self.colored(symbol=self.vert_boarders))
                    else:
                        row.append(" ")
                new_board.append(row)
        return new_board

    def show(self):
        for row in self.board:
            print(' '.join(row))


class Snake:
    def __init__(self, symbol="o", position=(1, 1)):
        self.symbol = symbol
        self.body = [position]

    def eat(self, position: tuple):
        self.body.append(position)

    def move(self, position: tuple):
        self.body.append(position)
        self.body.pop(0)

    def choices(self):
        next_positions = [
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1)
        ]
        result = []
        for next_position in next_positions:
            new_positions = self.body[-1][0] + next_position[0], self.body[-1][1] + next_position[1]
            result.append(new_positions)
        return result


class Apple:
    def __init__(self, symbol='$', position=(2, 2)):
        self.position = position
        self.symbol = symbol


class GameOverError(Exception):
    pass


class Game:
    def __init__(self, width, height):
        self.symbol = "o"
        self.width = width
        self.height = height
        self.board = Board(self.width, self.height)
        self.snake = Snake()
        self.apple = Apple()

    def init_apple(self):
        last_pos = self.apple.position
        self.board = Board(self.width, self.height)
        positions = []
        for x in range(self.height):
            for y in range(self.width):
                z = (item for item in self.snake.body)
                if (x, y) != last_pos and (x, y) not in z:
                    if self.board.board[x][y] == ' ':
                        positions.append((x, y))

        if positions:
            position = random.choices(positions)[0]
            self.apple = Apple(position=position, symbol="$")
            return self.apple.position
        else:
            raise GameOverError('No places for apple!')

    def play(self):

        try:
            self.render()
            while True:
                i, j = self.snake.body[-1]
                possible_moves = self.snake.choices()
                next_moves = []
                for move in possible_moves:
                    if move in self.snake.body:
                        continue
                    if move[0] != 0 and move[1] != 0 and move[0] != (self.height-1) and move[1] != (self.width-1):
                        next_moves.append(move)
                distances = []
                for move in next_moves:
                    dist = self.board.distance(move, self.apple.position)
                    distances.append(dist)
                res = dict(zip(next_moves, distances))
                try:
                    next_move = min(res, key=res.get)
                except ValueError:
                    print(self.board.colored(symbol='Game over!'))
                    break
                if next_move == self.apple.position:
                    self.snake.eat(self.apple.position)
                    self.init_apple()
                    self.render()
                    continue
                else:
                    self.snake.move(next_move)
                    self.render()
        except GameOverError:
            print(self.board.colored(symbol='Game over!'))

    def clear(self):
        self.board = Board(self.width, self.height)
        if os.name == 'posix':
            os.system('clear')
        else:
            os.system('cls')

    def render(self):
        self.clear()
        i, j = self.apple.position
        self.board.board[i][j] = self.board.colored(symbol=self.apple.symbol)
        for i, j in self.snake.body:
            self.board.board[i][j] = self.board.colored(symbol=self.snake.symbol)
            if (i, j) == self.snake.body[-1]:
                self.board.board[i][j] = self.board.colored(symbol="@")
            elif (i, j) == self.snake.body[0]:
                self.board.board[i][j] = self.board.colored(symbol="&")
        self.board.show()
        sleep(1)


if __name__ == '__main__':
    game = Game(10, 10)
    game.play()
