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
        del(self.body[0])
        self.body.append(position)


class Game:
    def __init__(self):
        self.board = Board(width=20, height=20)
        self.snake = Snake()

    def render(self):
        # the easiest way to place snake's body on the board
        i, j = self.snake.body[0]
        self.board.board[i][j] = self.snake.symbol

        apple = (1, 2)
        self.snake.eat(apple)
        apple = (2, 2)
        self.snake.eat(apple)
        apple = (2, 3)
        self.snake.eat(apple)

        for i, j in self.snake.body:
            self.board.board[i][j] = self.snake.symbol

        self.board.show()


if __name__ == '__main__':
    b = Board(width=4, height=4)
    game = Game()
    game.render()
