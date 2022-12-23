import os
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

    def choices(self):
        # next possible positions
        i, j = self.body[-1]
        positions = {(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)}
        return {p for p in positions if p not in self.body}


class Apple:
    def __init__(self, symbol: str = '$', position: tuple = (2, 2)):
        self.position = position
        self.symbol = symbol


class GameOverError(Exception):
    pass


class Game:
    def __init__(self, width: int = 20, height: int = 20) -> None:
        self.width = width
        self.height = height
        self.board = Board(self.width, self.height)
        self.snake = Snake()
        self.apple = Apple()

    def render(self):
        self.clear()

        # render apple
        i, j = self.apple.position
        self.board.board[i][j] = self.apple.symbol

        # render snake
        for position in self.snake.body:
            i, j = position
            self.board.board[i][j] = self.snake.symbol

        self.board.show()
        sleep(2)

    def clear(self):
        self.board = Board(self.width, self.height)
        # clear console
        if os.name == 'nt':
            # windows
            os.system('cls')
        else:
            os.system('clear')

    def init_apple(self):
        last_position = self.apple.position if self.apple else None
        for i in range(1, self.height - 1):
            for j in range(1, self.width - 1):
                if (i, j) not in self.snake.body:
                    self.apple = Apple(position=(i, j))
                    break
        if last_position is None:
            return
        if last_position == self.apple.position:
            raise GameOverError('No places for apple!')

    def play(self):
        game_cycles = 5
        try:
            self.render()
            while game_cycles > 0:
                snake_i, snake_j = self.snake.body[-1]

                next_move = None
                for possible_move in self.snake.choices():
                    if possible_move == self.apple.position:
                        next_move = self.apple.position
                        break

                    i, j = possible_move
                    if i == 0 or j in {0, self.width - 1}:
                        # border
                        continue

                    next_move = possible_move
                    break

                if next_move is None:
                    self.snake.move((snake_i + 1, snake_j + 1))
                    self.render()
                    GameOverError('No moves for snake!')

                if next_move == self.apple.position:
                    self.snake.eat(self.apple.position)
                    self.render()
                    self.init_apple()
                    self.render()
                    continue

                self.snake.move(next_move)
                self.render()
                game_cycles -= 1

        except GameOverError:
            print('Game Over!')


if __name__ == '__main__':
    # TODO: run via terminal for proper rendering
    game = Game()
    game.play()
