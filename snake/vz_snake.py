import random
import time


class Board:
    def __init__(self, width, height, border='*'):
        self.width = width
        self.height = height
        self.boarder = border
        self.board = self.init_board()

    def init_board(self):
        board = []
        for i in range(self.height):
            row = ['*' if i == 0 or i == self.height-1 or j == 0 or j == self.width-1 else ' ' for j in range(self.width)]
            board.append(row)
        return board

    def show(self):
        for row in self.board:
            print(' '.join(row))


class Snake:

    def __init__(self, width, height, body='o', position=(1, 1)):
        self.body = body
        self.position = position
        self.snake_pos = [self.position]
        self.width = width
        self.height = height

    def move(self):
        x, y = self.snake_pos[-1]
        ax, ay = self.apple.position
        if ax > x and (x + 1, y) not in self.snake_pos:
            x += 1
        elif ax < x and (x - 1, y) not in self.snake_pos:
            x -= 1
        elif ay > y and (x, y + 1) not in self.snake_pos:
            y += 1
        elif ay < y and (x, y - 1) not in self.snake_pos:
            y -= 1
        if x < 1:  # if the snake is going off the top edge
            x = self.height - 2
        elif x >= self.height - 1:  # if the snake is going off the bottom edge
            x = 1
        if y < 1:  # if the snake is going off the left edge
            y = self.width - 2
        elif y >= self.width - 1:  # if the snake is going off the right edge
            y = 1
        if (x, y) not in self.snake_pos:
            self.snake_pos.append((x, y))
            if self.board[x][y] != self.apple.symbol:
                self.snake_pos.pop(0)
            else:
                self.generate_apple()

    def generate_apple(self):
        while True:
            apple_x, apple_y = random.randint(1, self.height - 2), random.randint(1, self.width - 2)
            if (apple_x, apple_y) not in self.snake_pos:
                break
        self.board[apple_x][apple_y] = self.apple.symbol
        self.apple.position = (apple_x, apple_y)


class Apple:
    def __init__(self, symbol='$', position=(2, 2), width=20, height=20):
        self.position = position
        self.symbol = symbol
        self.width = width
        self.height = height


class Game:
    def __init__(self, width=20, height=20):
        self.board = Board(width, height)
        self.snake = Snake(width=width, height=height)
        self.apple = Apple()
        self.snake.board = self.board.board
        self.snake.apple = self.apple
        self.board.board[self.apple.position[0]][self.apple.position[1]] = self.apple.symbol

    def render(self):
        self.snake.move()
        for i in range(self.board.height):
            for j in range(self.board.width):
                self.board.board[i][j] = ' '
        for pos in self.snake.snake_pos:
            self.board.board[pos[0]][pos[1]] = self.snake.body
        self.board.board[self.apple.position[0]][self.apple.position[1]] = self.apple.symbol
        self.board.show()
        time.sleep(1)


if __name__ == '__main__':
    game = Game(width=10, height=10)
    while True:
        game.render()

