from time import sleep


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
    def __init__(self, symbol: str = 'o', position: tuple = (1, 1)) -> None:
        self.symbol = symbol
        self.body = [position]

    def eat(self, position: tuple):
        self.body.append(position)

    def move(self, position: tuple):
        self.body.append(position)
        self.body.pop(0)


class Game:
    def __init__(self, width: int = 20, height: int = 20) -> None:
        self.width = width
        self.height = height
        self.board = Board(self.width, self.height)
        self.snake = Snake()

    def render(self):
        self.clear()
        for position in self.snake.body:
            i, j = position
            self.board.board[i][j] = self.snake.symbol
        self.board.show()

    def clear(self):
        self.board = Board(self.width, self.height)

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

        apple = (2, 4)
        self.snake.move(apple)
        self.render()
        sleep(2)

        apple = (3, 4)
        self.snake.move(apple)
        self.render()
        sleep(2)


if __name__ == '__main__':
    game = Game()
    game.play()
