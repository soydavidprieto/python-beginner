from time import sleep

class Board:
    def __init__(self, width, height, border='*'):
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

    def show(self):
        for row in self.board:
            # print(row)
            print(' '.join(row))

    def clear_board(self):
        self.board = self.init_board()


class Snake:
    def __init__(self, symbol='o', position=(1, 1)):
        self.symbol = symbol
        self.body = [position]


    def eat(self, position: tuple):
        self.body.append(position)


    def move(self, position: tuple):
        # by means append to the body next position and
        # pop from the body the position at 0 index at the same time.
        self.body.append(position)
        self.body.pop(0)

    def choices(self, x=1, y=1):
        # TODO: this method should return set of next possible positions
        # where snake can move based on it's current position.
        # Note: if next possible position is already in snake body, filter it out.
        self.x = x
        self.y = y
        choice=[]
        if ((self.x+1), self.y) not in self.body and ((self.x+1), self.y) != '*':
            choice.append((self.x+1, self.y))
        if (self.x, (self.y+1)) not in self.body and (self.x, (self.y+1)) != '*':
            choice.append((self.x, self.y+1))
        if ((self.x - 1), self.y) not in self.body and ((self.x - 1), self.y) != '*':
            choice.append((self.x - 1, self.y))
        if (self.x, (self.y-1)) not in self.body and (self.x, (self.y-1)) != '*':
            choice.append((self.x, self.y-1))
        return choice


class Game:
    def __init__(self, width=20, height=20):
        self.width = width
        self.height = height
        self.board = Board(self.width, self.height)
        self.snake = Snake()

    def play(self):
        apple = (1, 2)
        self.snake.eat(apple)
        self.render()
        sleep(2)

        apple = (2, 2)
        self.snake.eat(apple)
        self.render()
        sleep(2)

        apple = (2, 3)
        self.snake.eat(apple)
        self.render()
        sleep(2)

        apple = (3, 3)
        self.snake.move(apple)
        self.render()
        sleep(2)

        apple = (4, 3)
        self.snake.move(apple)
        self.render()
        sleep(2)

    def clear(self):
        self.board.clear_board()

    def render(self):
        self.clear()
        i, j = self.snake.body[0]
        self.board.board[i][j] = self.snake.symbol
        for (x, y) in self.snake.body:
            self.board.board[x][y] = self.snake.symbol
        self.board.show()


# if __name__ == '__main__':
#     game = Game()
#     game.play()

s = Snake()
print(s.choices())  # {(2, 1), (1, 2), (0, 1), (1, 0)}

