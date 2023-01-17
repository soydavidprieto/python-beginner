import os
import random
from time import sleep


LOGO = """
  ██████  ███▄    █  ▄▄▄       ██ ▄█▀▓█████ 
▒██    ▒  ██ ▀█   █ ▒████▄     ██▄█▒ ▓█   ▀ 
░ ▓██▄   ▓██  ▀█ ██▒▒██  ▀█▄  ▓███▄░ ▒███   
  ▒   ██▒▓██▒  ▐▌██▒░██▄▄▄▄██ ▓██ █▄ ▒▓█  ▄ 
▒██████▒▒▒██░   ▓██░ ▓█   ▓██▒▒██▒ █▄░▒████▒
▒ ▒▓▒ ▒ ░░ ▒░   ▒ ▒  ▒▒   ▓▒█░▒ ▒▒ ▓▒░░ ▒░ ░
░ ░▒  ░ ░░ ░░   ░ ▒░  ▒   ▒▒ ░░ ░▒ ▒░ ░ ░  ░
░  ░  ░     ░   ░ ░   ░   ▒   ░ ░░ ░    ░   
      ░           ░       ░  ░░  ░      ░  ░
"""


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
    def __init__(self, width: int = 40, height: int = 20, border: str = '*') -> None:
        self.board = self.init_board(width, height, border)

    @staticmethod
    def init_board(width: int, height: int, border: str):
        board = []
        for i in range(height):
            if i in {0, height - 1}:
                board.append([border] * width)
            else:
                board.append([])
                for j in range(width):
                    if j in {0, width - 1}:
                        board[i].append(border)
                    else:
                        board[i].append(' ')
        return board

    def show(self):
        for row in self.board:
            symbols = [self.colored(s) for s in row]
            print(' '.join(symbols))

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
        return abs(pow((p2_i - p1_i) ** 2 + (p2_j - p1_j) ** 2, 0.5))


class Snake:
    def __init__(self, symbol: str = 'o', position: tuple = (1, 1),
                 head_symbol: str = '%', tail_symbol: str = '^') -> None:
        self.symbol = symbol
        self.body = [position]
        self.head_symbol = head_symbol
        self.tail_symbol = tail_symbol

    def eat(self, position: tuple):
        assert position, f'Snake needs something to eat!'
        self.body.append(position)

    def move(self, position: tuple):
        assert position, f'Snake needs somewhere to move!'
        self.body.append(position)
        self.body.pop(0)

    def choices(self):
        # next possible positions
        i, j = self.body[-1]
        options = {(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)}
        positions = {p for p in options if p not in self.body}
        if not positions:
            raise GameOverError('Snake can\'t move further!')
        return positions


class Apple:
    def __init__(self, symbol: str = '@', position: tuple = (2, 2)):
        self.position = position
        self.symbol = symbol


class GameOverError(Exception):
    pass


class Game:
    def __init__(self, width: int = 5, height: int = 5) -> None:
        self.width = width
        self.height = height
        self.board = Board(self.width, self.height)
        self.snake = Snake()
        self.apple = Apple()
        self.seconds_played = 0

    def render(self):
        self.clear()

        # render apple
        i, j = self.apple.position
        self.board.board[i][j] = self.apple.symbol

        # render snake
        # -- render snake head
        i, j = self.snake.body[-1]
        self.board.board[i][j] = self.snake.head_symbol

        # -- render snake tail
        if len(self.snake.body) > 1:
            i, j = self.snake.body[0]
            self.board.board[i][j] = self.snake.tail_symbol

        # -- render snake body
        if len(self.snake.body) > 2:
            for position in self.snake.body[1:-1]:
                i, j = position
                self.board.board[i][j] = self.snake.symbol

        self.board.show()

        self.seconds_played += 1
        print(f'{Color.HEADER}Snake size: {len(self.snake.body)}{Color.ENDC}')
        print(f'{Color.UNDERLINE}Time played: {self.seconds_played}s{Color.ENDC}')
        sleep(1)

    def clear(self):
        self.board = Board(self.width, self.height)
        # clear console
        if os.name == 'nt':
            # windows
            os.system('cls')
        else:
            os.system('clear')

    def init_apple(self):
        last_position = self.apple.position
        positions = []
        for i in range(1, self.height - 1):
            for j in range(1, self.width - 1):
                if (i, j) not in self.snake.body:
                    if (i, j) != last_position:
                        positions.append((i, j))

        if not positions:
            raise GameOverError('No places for apple!')

        position = random.choices(positions)[0]
        self.apple = Apple(position=position)

    def play(self):
        try:
            self.render()
            while True:
                next_move = None
                for possible_move in self.snake.choices():
                    if possible_move == self.apple.position:
                        next_move = self.apple.position
                        break

                    i, j = possible_move
                    if i in {0, self.height - 1} or j in {0, self.width - 1}:
                        # border
                        continue

                    if next_move is None:
                        next_move = possible_move
                        continue

                    d1 = self.board.distance(next_move, self.apple.position)
                    d2 = self.board.distance(possible_move, self.apple.position)
                    if d2 < d1:
                        next_move = possible_move

                if next_move is None:
                    self.render()
                    raise GameOverError('No moves for snake!')

                if next_move == self.apple.position:
                    self.snake.eat(self.apple.position)
                    self.render()
                    self.init_apple()
                    self.render()
                    continue

                self.snake.move(next_move)
                self.render()

        except GameOverError as e:
            print('Game Over!')
            print(e)


if __name__ == '__main__':
    # TODO: run via terminal for proper rendering
    print(f'{Color.OKGREEN}{LOGO}{Color.ENDC}')
    sleep(3)
    game = Game(width=15, height=15)
    game.play()

    # TODO:
    # 1. Shortest Path (Strategy) (Right now, it's shortest move (Tactic),
    #    which leads to fail if there is no move after it)
    # 2. Accept Input Move
