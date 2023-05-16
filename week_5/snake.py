import random
from time import sleep


class Board:
    def __init__(self, width, height, border='*'):
        self.width = width
        self.height = height
        self.boarder = border
        self.board = self.init_board()

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
                row = [self.boarder] * self.width
                board.append(row)
            else:
                row = []
                for j in range(self.width):
                    if j in {0, self.width - 1}:
                        row.append(self.boarder)
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
    def __init__(self, symbol='$', position=(5, 5)):
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
        game_cycles = 5
        try:
            self.render()
            while game_cycles > 0:
                snake_i, snake_j = self.snake.body[-1]
                next_move = None
                for i, j in self.snake.choices():
                    if i != self.board.board:



                next_move = random.choice(list(self.snake.choices()))
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
                game_cycles -= 1
        except GameOverError:
            print('Game Over!')
        apple = (1, 1)
        self.snake.move(apple)
        self.render()
        sleep(1)

        apple = (2, 2)
        self.snake.move(apple)
        self.render()
        sleep(1)

        apple = (2, 3)
        self.snake.move(apple)
        self.render()
        sleep(1)

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
            self.board.board[x][y] = self.snake.symbol
        a, b = self.apple.position
        self.board.board[a][b] = self.apple.symbol
        self.board.show()
        sleep(2)


class GameOverError(Exception):
    pass


if __name__ == '__main__':
    game = Game()
    game.play()
    print(game.snake.choices())
    print(game.init_apple())
