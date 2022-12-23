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
            print(' '.join(row))


class Snake:
    def __init__(self, body: str = 'o', position: tuple = (1, 1)) -> None:
        self.body = body
        self.position = position


class Game:
    def __init__(self) -> None:
        self.board = Board(20, 20)
        self.snake = Snake()

    def render(self):
        i, j = self.snake.position
        self.board.board[i][j] = self.snake.body[0]
        self.board.show()


if __name__ == '__main__':
    game = Game()
    game.render()
