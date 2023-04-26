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
    def __init__(self, body='o', position=(1, 1)):
        self.body = body
        self.position = position


class Game:
    def __init__(self):
        self.board = Board(width=4, height=4)
        self.snake = Snake()

    def render(self):
        ...


if __name__ == '__main__':
    b = Board(width=4, height=4)

    # lst = b.init_board()
    #
    # for cur_row in lst:
    #     print(cur_row)

    b.show()
