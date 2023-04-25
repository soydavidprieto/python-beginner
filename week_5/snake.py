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
        self.body.pop(-1)


class Game:
    def __init__(self):
        self.board = Board(width=10, height=10)
        self.snake = Snake()

    def render(self):
        # the easiest way to place snake's body on the board
        i, j = self.snake.body[0]
        self.board.board[i][j] = self.snake.symbol
        self.board.show()
        x_coord = range(1, 10)
        y_coord = range(1, 10)
        apple_lst = []
        #while True:
        for x, y in zip(x_coord, y_coord):
            apple_lst.append(x)
            apple_lst.append(y)
            apple = tuple(apple_lst)
            self.snake.eat(apple)
            apple_lst.pop(0)
            apple_lst.pop(0)


                # apple = (2, 2)
                # self.snake.eat(apple)
                #
                # apple = (2, 3)
                # self.snake.eat(apple)

        self.board.show()


if __name__ == '__main__':
    game = Game()
    game.render()
