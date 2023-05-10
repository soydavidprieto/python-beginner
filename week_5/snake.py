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
        global new_positon
        try:
            last_position = self.apple.position
            if self.snake.body[-1] == last_position:
                self.snake.eat(self.apple.position)
                for (i, j) in self.board.board:
                    if (i, j) not in self.snake.body:
                        new_i = random.randrange(1, 20)
                        new_j = random.randrange(1, 20)
                        new_positon = new_positon[new_i][new_j]
            return new_positon
        except GameOverError:
            print("There is no free space for apple, the game ended")

    def play(self):
        apple = (1, 2)
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

        apple = (2, 4)
        self.snake.move(apple)
        self.render()
        sleep(1)

        apple = (2, 5)
        self.snake.move(apple)
        self.render()
        sleep(1)

        apple = (3, 5)
        self.snake.move(apple)
        self.render()
        sleep(1)

        apple = (4, 5)
        self.snake.move(apple)
        self.render()
        sleep(1)

        apple = (5, 5)
        self.snake.move(apple)
        self.render()
        sleep(1)

        apple = (6, 5)
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
