from time import sleep
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
    def _init_(self, width, height, border=(Color.WARNING + '*' + Color.ENDC)):
        self.width = width
        self.height = height
        self.border = border
        self.board = self.init_board()

    def init_board(self):
        board = []

        # for i in range(self.height):
        #     row = [''] * self.width
        #     board.append(row)

        # ['', '', '', '']
        # ['', ' ', ' ', '']
        # ['', ' ', ' ', '']
        # ['', '', '', '']

        for i in range(self.height):
            if i in {0, self.height - 1}:
                row = [self.border] * self.width
                board.append(row)
            else:
                row = []
                for j in range(self.width):
                    if j in {0, self.width - 1}:
                        row.append(self.border)
                    else:
                        row.append(' ')
                board.append(row)
        return board

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

    def show(self):
        for row in self.board:
            print(' '.join(row))

    def clear_board(self):
        self.board = self.init_board()

    @staticmethod
    def distance(p1: tuple, p2: tuple):
        p1_i, p1_j = p1
        p2_i, p2_j = p2
        return math.sqrt(math.pow(p2_i - p1_i, 2) +
                         math.pow(p2_j - p1_j, 2) * 1.0)


class Snake:
    def _init_(self, head=(Color.PINK + '%' + Color.ENDC), symbol=(Color.OKGREEN + 'o' + Color.ENDC), tail=(Color.PINK + '^' + Color.ENDC), position=(1, 1)):
        self.symbol = symbol
        self.body = [position]
        self.head = head
        self.tail = tail

    def eat(self, position: tuple):
        self.body.append(position)

    def move(self, position: tuple):
        self.body.append(position)
        self.body.pop(0)

    def choices(self):
        i, j = self.body[-1]
        choice = []
        if ((i + 1), j) not in self.body and i < (game.width - 2):
            choice.append((i + 1, j))
        if (i, (j + 1)) not in self.body and j < (game.height - 2):
            choice.append((i, j + 1))
        if ((i - 1), j) not in self.body and i > 1:
            choice.append((i - 1, j))
        if (i, (j - 1)) not in self.body and j > 1:
            choice.append((i, j - 1))
        return choice


class Apple:
    def _init_(self, symbol=(Color.FAIL + '$' + Color.ENDC), position=(2, 2)):
        self.position = position
        self.symbol = symbol

    def show(self, position: tuple):
        self.position = position


class GameOverError(Exception):
    pass


class Game:
    def _init_(self, width=7, height=7):
        self.width = width
        self.height = height
        self.board = Board(self.width, self.height)
        self.snake = Snake()
        self.apple = Apple()

    def init_apple(self):
        last_position = self.apple.position
        possible_positions = []
        for new_i in range(1, (self.width - 1)):
            for new_j in range(1, (self.height - 1)):
                new_position = (new_i, new_j)
                if new_position == last_position or new_position in self.snake.body:
                    continue
                else:
                    possible_positions.append(new_position)
        if len(possible_positions) == 0:
            raise GameOverError('No places for apple!')
        else:
            position = random.choice(possible_positions)
            self.apple = Apple(position=position)
            self.board.show()

    def play(self):
        try:
            self.render()  # initial render of board, snake and apple
            while True:  # start our game
                snake_i, snake_j = self.snake.body[-1]  # remember last position of snake's head

                # TODO: find next possible position (next_move) for snake to move
                possible_positions = self.snake.choices()
                if len(possible_positions) == 0:
                    next_position = None
                else:
                    # next_move = random.choice(possible_positions)
                    actual_distance = Board.distance(self.apple.position, self.snake.body[-1])
                    for x in range(len(possible_positions)):
                        next_distance = Board.distance(self.apple.position, possible_positions[x])
                        if next_distance < actual_distance and possible_positions[x] not in self.snake.body:
                            next_position = possible_positions[x]
                        else:
                            if next_distance < actual_distance and possible_positions[x] in self.snake.body:
                                next_position = random.choice(possible_positions)
                            else:
                                continue
                next_move = next_position

                if next_move is None:  # there is no possible move for snake
                    self.snake.move((snake_i + 1, snake_j + 1))  # just do one move forward for snake
                    self.render()  # render last move
                    raise GameOverError('No moves for snake!')  # end the game (snake does not have next valid move)
                if next_move == self.apple.position:
                    # TODO: eat apple, render this action, init new apple and render it on board
                    self.snake.eat(self.apple.position)
                    # self.render()
                    self.init_apple()
                    self.render()
                    continue  # go to next game cycle
                # if game is not over, and snake did not eat the apple in current game cycle, then it means it can simply move on next valid position:
                self.snake.move(next_move)
                self.render()
        except GameOverError:
            print('Game Over!')

    def clear(self):
        self.board.clear_board()

    def render(self):
        self.clear()
        i, j = self.apple.position
        self.board.board[i][j] = self.apple.symbol
        i, j = self.snake.body[-1]
        self.board.board[i][j] = self.snake.head
        if len(self.snake.body) > 1:
            i, j = self.snake.body[0]
            self.board.board[i][j] = self.snake.tail
        for (x, y) in self.snake.body[1:-1]:
            self.board.board[x][y] = self.snake.symbol
        self.board.show()
        sleep(1)


if _name_ == '_main_':
    game = Game()
    game.play()