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
        self.board.board[apple[0]][apple[1]] = self.snake.symbol

        apple = (2, 2)
        self.snake.eat(apple)
        self.board.board[apple[0]][apple[1]] = self.snake.symbol

        apple = (2, 3)
        self.snake.eat(apple)
        self.board.board[apple[0]][apple[1]] = self.snake.symbol

        self.board.show()


if __name__ == '__main__':
    b = Board(width=4, height=4)

    # lst = b.init_board()
    #
    # for cur_row in lst:
    #     print(cur_row)

    b.show()
    s = Snake()
    print(s.body)
    s.eat((1, 2))
    print(s.body)

    s.move((1, 3))
    print(s.body)
    game = Game()
    game.render()